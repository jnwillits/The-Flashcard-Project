# !/usr/bin/env python

"""
The Flashcard Project
Copyright (c) 2019 (MIT License) Jeffrey Neil Willits   @jnwillits

Use this to build a flash card learning deck. Edit the cards as you learn. The Next (green arrow) button can be set to either randomly or sequentially display the cards. Click Archive, if you do not want to see a card again and you do not want to delete it from the database. See the README file in the 
project's GitHub repository for more information.
"""

import pickle
import yaml
import os
import sys
from pathlib import Path
from random import choice, randrange

import wx

import theflashcardprojectgui as fp
import fphelp


card_file = 'cards'
tags = set()
exclude_tags = set()


def add_zeros(card):
    """ This adds leading zeros to the card number display. """
    return str(['000' if card < 100 else '00'][0]) + str(card)[-5:]


def get_cards_total(cards):
    deleted_total = len(
        list(filter(lambda k: cards[k][0] == 'deleted', cards)))
    return len(cards) - deleted_total


def get_status_total(cards, status):
    return len(list(filter(lambda k: cards[k][0] == status, cards)))


def set_card(card, status):
    # The set stores card tags.
    return {card: [status, '', '', set()], }


def reset(cards):
    for key in cards:
        if cards[key][0] == 'archived':
            cards[key][0] = 'active'
    return cards


def find_sequential_next_card(active_keys, last_card):
    """ Find the next sequential dictionary key for cards not deleted. """
    new_card = int()
    active_keys.sort()
    if last_card == active_keys[-1]:
        new_card = min(active_keys)
    elif last_card in active_keys:
        new_card = active_keys[active_keys.index(last_card) + 1]
    else:
        new_card = next(filter(lambda e: e > last_card, active_keys), None)
        if new_card is None:
            new_card = min(active_keys)
    return new_card


def find_active_keys(cards):
    inactive_status = ['deleted', 'archived']
    active_keys = list(
        filter(lambda key: cards[key][0] not in inactive_status, cards))
    # Remove keys with excluded tags.
    for key in active_keys:
        if not cards[key][3].isdisjoint(exclude_tags):
            active_keys.remove(key)
    return active_keys


def choose_card(cards, random_view, last_card):
    """ Select an active card key for the next card to view. """
    active_keys = find_active_keys(cards)
    if len(active_keys) == 1:
        cards = reset(cards)
        active_keys = find_active_keys(cards)
    else:
        # Assure the previous card is not immediately shown again.
        if last_card in active_keys:
            active_keys.remove(last_card)
    if random_view:
        card = choice(active_keys)
    else:
        card = find_sequential_next_card(active_keys, last_card)
    return card, cards


def read():
    card_path = ''
    if os.path.exists(card_file):
        card_path = Path.cwd() / card_file
    if os.path.isfile(card_path):
        with open(card_path, 'rb') as f:
            cards = pickle.load(f)
    else:
        cards = set_card(1, 'active')
    return cards


def write_db(cards):
    global card_file
    card_file = card_file.rstrip('.db')
    with open(card_file + '.db', 'wb') as f:
        pickle.dump(cards, f)


class EditTags(fp.Dialog_edit_tags):
    def __init__(self, parent):
        fp.Dialog_edit_tags.__init__(self, parent)

        self.card = getattr(frame, 'card')
        self.staticText_card_label.SetLabel(f'Card: {add_zeros(self.card)}')

    def on_button_close(self, event):
        global tags
        cards = getattr(frame, 'cards')
        tags_entry = set()
        # Unwanted spaces are removed from the tag entries.
        tags_entry_dirty = (self.textCtrl_edit_tags.GetValue()).split(',')
        for i in range(0, len(tags_entry_dirty)):
            tags_entry.add(tags_entry_dirty[i].strip())
        tags = tags.union(tags_entry)
        cards[self.card][3] = tags_entry
        setattr(frame, 'cards', cards)
        setattr(frame, 'update_ui', True)
        self.Close()


class DeleteTags(fp.Dialog_delete_tags):
    def __init__(self, parent):
        fp.Dialog_delete_tags.__init__(self, parent)

        self.tags_temp = sorted(list(tags))
        self.listBox_delete_tags.Set(self.tags_temp)

    def on_button_delete_tag(self, event):
        """ Choose tags to delete from all cards that have them attached. """
        global tags
        cards = getattr(frame, 'cards')
        deleted_tags = set()
        deleted_tags_indexes = self.listBox_delete_tags.GetSelections()
        for i in range(0, len(deleted_tags_indexes)):
            deleted_tags.add(self.tags_temp[deleted_tags_indexes[i]])
        tags = tags.difference(deleted_tags)
        # Remove the deleted tags from the tag sets in cards.
        for key in cards:
            cards[key][3] = cards[key][3].difference(deleted_tags)
        setattr(frame, 'cards', cards)
        setattr(frame, 'update_ui', True)
        self.Close()


class ExcludeTags(fp.Dialog_exclude_tags):
    def __init__(self, parent):
        fp.Dialog_exclude_tags.__init__(self, parent)

        self.tags_temp = sorted(list(tags))
        self.listBox_exclude_tags.Set(self.tags_temp)

    def on_button_exclude_tag(self, event):
        """ Choose tags to exclude. Cards with excluded tags will not be shown. """
        global exclude_tags
        exclude_tags = set()
        exclude_tags_indexes = self.listBox_exclude_tags.GetSelections()
        for i in range(0, len(exclude_tags_indexes)):
            exclude_tags.add(self.tags_temp[exclude_tags_indexes[i]])
        setattr(frame, 'update_ui', True)
        self.Close()


class CardAppearance(fp.Dialog_font_size):
    def __init__(self, parent):
        fp.Dialog_font_size.__init__(self, parent)

    def on_button_close(self, event):
        font_size = self.spinCtrl_font_size.GetValue()
        setattr(frame, 'font_size', int(font_size))
        setattr(frame, 'update_ui', True)
        self.Close()


class SequenceSetup(fp.Dialog_view_order):
    def __init__(self, parent):
        fp.Dialog_view_order.__init__(self, parent)

    def on_check_random(self, event):
        setattr(frame, 'random_view', True)
        self.checkBox_sequential.SetValue(False)

    def on_check_sequential(self, event):
        setattr(frame, 'random_view', False)
        self.checkBox_random.SetValue(False)
        setattr(frame, 'card', 0)

    def on_button_sequence_set(self, event):
        self.Close()
        frame.next_card()


class HelpAbout(fp.Dialog_about):
    def __init__(self, parent):
        fp.Dialog_about.__init__(self, parent)

        self.font_size = 9
        font = wx.Font(self.font_size, wx.MODERN, wx.NORMAL, wx.BOLD)
        self.richText_about.SetFont(font)
        self.richText_about.AppendText(fphelp.about_text)

    def on_button_about_close(self, event):
        self.Close()


class HelpUsage(fp.Dialog_usage):
    def __init__(self, parent):
        fp.Dialog_usage.__init__(self, parent)

        self.font_size = 9
        font = wx.Font(self.font_size, wx.MODERN, wx.NORMAL, wx.BOLD)
        self.richText_usage.SetFont(font)
        self.richText_usage.AppendText(fphelp.usage_text)

    def on_button_usage_close(self, event):
        self.Close()


class Interface(fp.MainFrame):
    def __init__(self, parent):
        fp.MainFrame.__init__(self, parent)

        self.path = 'fpicon_64.bmp'
        self.icon = wx.Icon(self.path, wx.BITMAP_TYPE_BMP)
        self.SetIcon(self.icon)
        self.card = 1
        self.last_card = int()
        self.update_ui = True
        self.cards = set_card(1, 'active')
        self.cards_total = 1
        self.random_view = True
        self.font_size = 14
        self.cards = read()

    def on_update_ui(self, event):
        if self.update_ui:
            self.richText_front.Clear()
            self.richText_back.Clear()

            # pointSize, family, style, weight (BOLD)
            font = wx.Font(self.font_size, wx.MODERN, wx.NORMAL, wx.BOLD)
            self.richText_front.SetFont(font)
            self.richText_back.SetFont(font)

            try:
                self.richText_front.AppendText(self.cards[self.card][1])
            except KeyError:
                3, 6

            separator = '  ' + '\u2022' + '  '
            tags_label = separator.join(list(self.cards[self.card][3]))
            self.staticText_tags_label.SetLabel(tags_label)

            crds_tot = get_cards_total(self.cards)
            stat_tot = get_status_total(self.cards, 'active')
            arch = get_status_total(self.cards, 'archived')
            crd = add_zeros(self.card)
            self.staticText_stats.SetLabel(
                f'Cards: {crds_tot}        Studying: {stat_tot}        Archived: {arch}        Current: {crd}')

            if card_file != '':
                self.statusBar.SetLabel(f' Card deck: {card_file}')
            self.update_ui = False

    def next_card(self):
        self.last_card = self.card
        self.card, self.cards = choose_card(
            self.cards, self.random_view, self.last_card)
        self.update_ui = True

    def on_button_archive(self, event):
        self.cards[self.card][0] = 'archived'
        self.next_card()

    def on_button_answer(self, event):
        self.richText_back.Clear()
        self.richText_back.AppendText(self.cards[self.card][2])

    def on_button_next(self, event):
        self.next_card()

    def on_menu_reset(self, event):
        self.cards = reset(self.cards)
        self.next_card()

    def on_button_add(self, event):
        # Switch to an available card key.
        deleted = list(
            filter(lambda k: self.cards[k][0] == 'deleted', self.cards))
        if len(deleted) > 0:
            self.card = min(deleted)
        else:
            self.card = len(self.cards) + 1
        (self.cards).update(set_card(self.card, 'active'))
        self.update_ui = True

    def on_button_delete(self, event):
        """ Blank the card, but keep the key in the dictionary. """
        if get_cards_total(self.cards) == 1:
            wx.MessageBox('There are no more cards to delete.')
        else:
            self.cards[self.card][0] = 'deleted'
        self.next_card()

    def on_button_save(self, event):
        self.cards[self.card][1] = self.richText_front.GetValue()
        # If no answer is displayed, only save the unedited answer.
        if len(self.richText_back.GetValue()) > 1:
            self.cards[self.card][2] = self.richText_back.GetValue()
        self.cards_total = get_cards_total(self.cards)
        write_db(self.cards)
        setattr(frame, 'update_ui', True)
        if len(self.cards[self.card][3]) > 0:
            wx.MessageBox(f'Card {str(self.card)} is saved.')
        else:
            wx.MessageBox(
                f'Card {str(self.card)} is saved. Consider adding tags.')

    def on_menu_new_file(self, event):
        global card_file
        global tags
        with wx.FileDialog(self, "New file...", wildcard="DB files (*.db)|*.db", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.card = 1
            card_file = fileDialog.GetPath()
            self.cards = set_card(1, 'active')
            self.update_ui = True

    def on_menu_save_as(self, event):
        global card_file
        with wx.FileDialog(self, "Save the card file...", wildcard="DB files (*.db)|*.db", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            card_file = fileDialog.GetPath()
            write_db(self.cards)
            self.next_card()

    def on_menu_open(self, event):
        global card_file
        global tags
        with wx.FileDialog(self, "Open a card file...", wildcard="DB files (*.db)|*.db",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            card_file = fileDialog.GetPath()
            try:
                self.cards = read()
                # Populate the tags set.
                for key in self.cards:
                    tags = tags.union(self.cards[key][3])
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)
            self.next_card()

    def export(self, f_type, exten):
        with wx.FileDialog(self, f'Save the cards to a {f_type} file.',      wildcard=f'{f_type} files (*.{exten})|*.{exten}', style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w') as f:
                    eval(f'{exten}.dump(self.cards, f)')
            except IOError:
                wx.LogError(
                    "Cannot save current data in file '%s'." % pathname)

    def import_and_merge_yaml(self):
        global tags
        with wx.FileDialog(self, "Import and merge a YAML card file...", wildcard="YAML files (*.yaml)|*.yaml",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            card_file = fileDialog.GetPath()
            try:
                cards_temp = self.cards
                card_path = ''
                if os.path.exists(card_file):
                    card_path = Path.cwd() / card_file
                if os.path.isfile(card_path):
                    with open(card_path, 'r') as f:
                        imported_cards = yaml.load(f, Loader=yaml.SafeLoader)
                else:
                    cards = set_card(1, 'active')
                # Imported card keys must be changed so they do not match.
                card_values = []
                imported_card_values = []
                for i in range(len(cards_temp)):
                    card_values.append(cards_temp[i + 1])
                for i in range(len(imported_cards)):
                    imported_card_values.append(imported_cards[i + 1])
                card_values.extend(imported_card_values)
                cards_temp = {}
                for i in range(len(card_values)):
                    cards_temp.update({i + 1: card_values[i]})
                self.cards = cards_temp
                # Populate the tags set.
                for key in self.cards:
                    tags = tags.union(self.cards[key][3])
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)
            self.next_card()

    def on_menu_export_yaml(self, event):
        self.export('YAML', 'yaml')

    def on_menu_import_yaml(self, event):
        self.import_and_merge_yaml()

    def on_menu_view(self, event):
        dlg = SequenceSetup(None)
        dlg.Show(True)

    def on_menu_appearance(self, event):
        dlg = CardAppearance(None)
        dlg.Show(True)

    def on_menu_edit_tags(self, event):
        dlg = EditTags(None)
        dlg.Show(True)

    def on_menu_delete_tags(self, event):
        dlg = DeleteTags(None)
        dlg.Show(True)

    def on_menu_exclude_tags(self, event):
        dlg = ExcludeTags(None)
        dlg.Show(True)

    def on_menu_quit(self, event):
        self.Close()
        sys.exit()

    def on_menu_about(self, event):
        dlg = HelpAbout(None)
        dlg.Show(True)

    def on_menu_usage(self, event):
        dlg = HelpUsage(None)
        dlg.Show(True)

    def on_close(self, event):
        self.Close()
        sys.exit()


if __name__ == '__main__':
    app = wx.App(False)
    frame = Interface(None)
    frame.Show(True)
    app.MainLoop()
