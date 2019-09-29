# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"The Flashcard Project", pos = wx.DefaultPosition, size = wx.Size( 1250,625 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer37 = wx.BoxSizer( wx.VERTICAL )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.staticText_card_num = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Question", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_card_num.Wrap( -1 )

		self.staticText_card_num.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		gSizer4.Add( self.staticText_card_num, 0, wx.LEFT|wx.TOP|wx.ALIGN_BOTTOM, 6 )

		self.m_staticText22 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Answer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		gSizer4.Add( self.m_staticText22, 0, wx.ALIGN_BOTTOM|wx.LEFT|wx.TOP, 6 )


		bSizer37.Add( gSizer4, 0, wx.EXPAND, 1 )

		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )

		self.richText_front = wx.richtext.RichTextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.richText_front.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer38.Add( self.richText_front, 1, wx.EXPAND |wx.ALL, 5 )

		self.richText_back = wx.richtext.RichTextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer38.Add( self.richText_back, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer37.Add( bSizer38, 1, wx.EXPAND, 5 )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		self.staticText_tags = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Tags:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_tags.Wrap( -1 )

		self.staticText_tags.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer30.Add( self.staticText_tags, 0, wx.ALL, 5 )

		self.staticText_tags_label = wx.StaticText( self.m_panel7, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_tags_label.Wrap( -1 )

		self.staticText_tags_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer30.Add( self.staticText_tags_label, 0, wx.ALL, 5 )


		bSizer37.Add( bSizer30, 0, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.button_add = wx.Button( self.m_panel7, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.button_add, 0, wx.ALL, 5 )

		self.button_save = wx.Button( self.m_panel7, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.button_save, 0, wx.ALL, 5 )

		self.button_delete = wx.Button( self.m_panel7, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.button_delete, 0, wx.ALL, 5 )


		bSizer44.Add( bSizer6, 1, wx.EXPAND, 5 )


		gSizer5.Add( bSizer44, 1, wx.EXPAND|wx.ALIGN_RIGHT, 5 )

		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )

		self.button_archive = wx.Button( self.m_panel7, wx.ID_ANY, u"Archive", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_archive.SetMinSize( wx.Size( 100,-1 ) )

		bSizer45.Add( self.button_archive, 0, wx.ALL, 5 )

		self.button_answer = wx.Button( self.m_panel7, wx.ID_ANY, u"Answer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_answer.SetMinSize( wx.Size( 100,-1 ) )

		bSizer45.Add( self.button_answer, 0, wx.ALL, 5 )

		self.button_next = wx.BitmapButton( self.m_panel7, wx.ID_FORWARD, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.button_next.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_FORWARD, wx.ART_BUTTON ) )
		self.button_next.SetMinSize( wx.Size( 100,-1 ) )

		bSizer45.Add( self.button_next, 0, wx.ALL, 5 )


		gSizer5.Add( bSizer45, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		bSizer37.Add( gSizer5, 0, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.staticText_stats = wx.StaticText( self.m_panel7, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_stats.Wrap( -1 )

		self.staticText_stats.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer18.Add( self.staticText_stats, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer18, 1, wx.EXPAND, 5 )


		bSizer37.Add( bSizer16, 0, wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer37 )
		self.m_panel7.Layout()
		bSizer37.Fit( self.m_panel7 )
		bSizer36.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer36 )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.STB_DEFAULT_STYLE, wx.ID_ANY )
		self.statusBar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.menu_new = wx.MenuItem( self.menu_file, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_new )

		self.menu_open = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_open )

		self.menu_save_as = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Save As", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_save_as )

		self.menu_file.AppendSeparator()

		self.menuItem_import_yaml = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Import YAML", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menuItem_import_yaml )

		self.menuItem_export_YAML = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Export YAML", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menuItem_export_YAML )

		self.menu_file.AppendSeparator()

		self.menuItem_quit = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menuItem_quit )

		self.m_menubar1.Append( self.menu_file, u"File" )

		self.menu_tags = wx.Menu()
		self.menuItem_edit_tags = wx.MenuItem( self.menu_tags, wx.ID_ANY, u"Edit", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_tags.Append( self.menuItem_edit_tags )

		self.menuItem_delete_tags = wx.MenuItem( self.menu_tags, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_tags.Append( self.menuItem_delete_tags )

		self.menuItem_exclude_tags = wx.MenuItem( self.menu_tags, wx.ID_ANY, u"Exclude", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_tags.Append( self.menuItem_exclude_tags )

		self.m_menubar1.Append( self.menu_tags, u"Tags" )

		self.menu_setup = wx.Menu()
		self.menu_reset = wx.MenuItem( self.menu_setup, wx.ID_ANY, u"Reset", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_setup.Append( self.menu_reset )

		self.menu_view = wx.MenuItem( self.menu_setup, wx.ID_ANY, u"Viewing Order", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_setup.Append( self.menu_view )

		self.menu_appearance = wx.MenuItem( self.menu_setup, wx.ID_ANY, u"Font Size", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_setup.Append( self.menu_appearance )

		self.m_menubar1.Append( self.menu_setup, u"Setup" )

		self.menu_help = wx.Menu()
		self.menuItem_usage = wx.MenuItem( self.menu_help, wx.ID_ANY, u"Usage", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_help.Append( self.menuItem_usage )

		self.menuItem_about = wx.MenuItem( self.menu_help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_help.Append( self.menuItem_about )

		self.m_menubar1.Append( self.menu_help, u"Help" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.m_panel7.Bind( wx.EVT_UPDATE_UI, self.on_update_ui )
		self.button_add.Bind( wx.EVT_BUTTON, self.on_button_add )
		self.button_save.Bind( wx.EVT_BUTTON, self.on_button_save )
		self.button_delete.Bind( wx.EVT_BUTTON, self.on_button_delete )
		self.button_archive.Bind( wx.EVT_BUTTON, self.on_button_archive )
		self.button_answer.Bind( wx.EVT_BUTTON, self.on_button_answer )
		self.button_next.Bind( wx.EVT_BUTTON, self.on_button_next )
		self.Bind( wx.EVT_MENU, self.on_menu_new_file, id = self.menu_new.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_open, id = self.menu_open.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_save_as, id = self.menu_save_as.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_import_yaml, id = self.menuItem_import_yaml.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_export_yaml, id = self.menuItem_export_YAML.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_quit, id = self.menuItem_quit.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_edit_tags, id = self.menuItem_edit_tags.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_delete_tags, id = self.menuItem_delete_tags.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_exclude_tags, id = self.menuItem_exclude_tags.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_reset, id = self.menu_reset.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_view, id = self.menu_view.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_appearance, id = self.menu_appearance.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_usage, id = self.menuItem_usage.GetId() )
		self.Bind( wx.EVT_MENU, self.on_menu_about, id = self.menuItem_about.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_close( self, event ):
		event.Skip()

	def on_update_ui( self, event ):
		event.Skip()

	def on_button_add( self, event ):
		event.Skip()

	def on_button_save( self, event ):
		event.Skip()

	def on_button_delete( self, event ):
		event.Skip()

	def on_button_archive( self, event ):
		event.Skip()

	def on_button_answer( self, event ):
		event.Skip()

	def on_button_next( self, event ):
		event.Skip()

	def on_menu_new_file( self, event ):
		event.Skip()

	def on_menu_open( self, event ):
		event.Skip()

	def on_menu_save_as( self, event ):
		event.Skip()

	def on_menu_import_yaml( self, event ):
		event.Skip()

	def on_menu_export_yaml( self, event ):
		event.Skip()

	def on_menu_quit( self, event ):
		event.Skip()

	def on_menu_edit_tags( self, event ):
		event.Skip()

	def on_menu_delete_tags( self, event ):
		event.Skip()

	def on_menu_exclude_tags( self, event ):
		event.Skip()

	def on_menu_reset( self, event ):
		event.Skip()

	def on_menu_view( self, event ):
		event.Skip()

	def on_menu_appearance( self, event ):
		event.Skip()

	def on_menu_usage( self, event ):
		event.Skip()

	def on_menu_about( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_usage
###########################################################################

class Dialog_usage ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Using this software...", pos = wx.DefaultPosition, size = wx.Size( 717,701 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		bSizer301 = wx.BoxSizer( wx.VERTICAL )

		bSizer301.SetMinSize( wx.Size( -1,20 ) )
		self.staticText_usage = wx.StaticText( self.m_panel2, wx.ID_ANY, u"The Flashcard Project", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_usage.Wrap( -1 )

		self.staticText_usage.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer301.Add( self.staticText_usage, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 25 )


		bSizer27.Add( bSizer301, 0, wx.EXPAND, 5 )

		bSizer3011 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( bSizer3011, 0, wx.ALIGN_CENTER_HORIZONTAL, 15 )

		bSizer302 = wx.BoxSizer( wx.VERTICAL )

		bSizer302.SetMinSize( wx.Size( -1,20 ) )
		self.staticText_usage = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Version 1.0\nCopyright(c) 2019 Jeffrey Neil Willits", wx.DefaultPosition, wx.Size( -1,100 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.staticText_usage.Wrap( -1 )

		self.staticText_usage.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.staticText_usage.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.staticText_usage.SetMinSize( wx.Size( -1,100 ) )

		bSizer302.Add( self.staticText_usage, 0, wx.ALIGN_CENTER_HORIZONTAL, 15 )


		bSizer27.Add( bSizer302, 0, wx.EXPAND, 0 )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.richText_usage = wx.richtext.RichTextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.richText_usage.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer40.Add( self.richText_usage, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer27.Add( bSizer40, 1, wx.EXPAND, 5 )


		bSizer5.Add( bSizer27, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.button_usage_close = wx.Button( self.m_panel2, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.button_usage_close, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		bSizer4.Add( self.m_panel2, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_usage_close.Bind( wx.EVT_BUTTON, self.on_button_usage_close )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_button_usage_close( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_about
###########################################################################

class Dialog_about ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About this software...", pos = wx.DefaultPosition, size = wx.Size( 717,701 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		bSizer301 = wx.BoxSizer( wx.VERTICAL )

		bSizer301.SetMinSize( wx.Size( -1,20 ) )
		self.staticText_about = wx.StaticText( self.m_panel2, wx.ID_ANY, u"The Flashcard Project", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_about.Wrap( -1 )

		self.staticText_about.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer301.Add( self.staticText_about, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 25 )


		bSizer27.Add( bSizer301, 0, wx.EXPAND, 5 )

		bSizer3011 = wx.BoxSizer( wx.VERTICAL )

		bSizer3011.SetMinSize( wx.Size( -1,20 ) )

		bSizer27.Add( bSizer3011, 0, wx.EXPAND, 5 )

		bSizer302 = wx.BoxSizer( wx.VERTICAL )

		bSizer302.SetMinSize( wx.Size( -1,20 ) )
		self.staticText_about = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Version 1.0\nCopyright(c) 2019 Jeffrey Neil Willits", wx.DefaultPosition, wx.Size( -1,100 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.staticText_about.Wrap( -1 )

		self.staticText_about.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.staticText_about.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.staticText_about.SetMinSize( wx.Size( -1,100 ) )

		bSizer302.Add( self.staticText_about, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )


		bSizer27.Add( bSizer302, 0, wx.EXPAND, 0 )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.richText_about = wx.richtext.RichTextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.richText_about.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer40.Add( self.richText_about, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer27.Add( bSizer40, 1, wx.EXPAND, 5 )


		bSizer5.Add( bSizer27, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.button_about_close = wx.Button( self.m_panel2, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.button_about_close, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		bSizer4.Add( self.m_panel2, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_about_close.Bind( wx.EVT_BUTTON, self.on_button_about_close )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_button_about_close( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_exclude_tags
###########################################################################

class Dialog_exclude_tags ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Exclude tags...", pos = wx.DefaultPosition, size = wx.Size( 411,303 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.panel_delete_tags = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		listBox_exclude_tagsChoices = [ u"tags" ]
		self.listBox_exclude_tags = wx.ListBox( self.panel_delete_tags, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBox_exclude_tagsChoices, wx.LB_MULTIPLE )
		bSizer24.Add( self.listBox_exclude_tags, 1, wx.ALL|wx.EXPAND, 5 )

		self.button_exclude_tag = wx.Button( self.panel_delete_tags, wx.ID_ANY, u"Exclude", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.button_exclude_tag, 0, wx.ALL, 5 )


		self.panel_delete_tags.SetSizer( bSizer24 )
		self.panel_delete_tags.Layout()
		bSizer24.Fit( self.panel_delete_tags )
		bSizer7.Add( self.panel_delete_tags, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_exclude_tag.Bind( wx.EVT_BUTTON, self.on_button_exclude_tag )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_button_exclude_tag( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_delete_tags
###########################################################################

class Dialog_delete_tags ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Delete tags...", pos = wx.DefaultPosition, size = wx.Size( 411,303 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.panel_delete_tags = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		listBox_delete_tagsChoices = [ u"tags" ]
		self.listBox_delete_tags = wx.ListBox( self.panel_delete_tags, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBox_delete_tagsChoices, wx.LB_MULTIPLE )
		bSizer24.Add( self.listBox_delete_tags, 1, wx.ALL|wx.EXPAND, 5 )

		self.button_delete_tag = wx.Button( self.panel_delete_tags, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.button_delete_tag, 0, wx.ALL, 5 )


		self.panel_delete_tags.SetSizer( bSizer24 )
		self.panel_delete_tags.Layout()
		bSizer24.Fit( self.panel_delete_tags )
		bSizer7.Add( self.panel_delete_tags, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_delete_tag.Bind( wx.EVT_BUTTON, self.on_button_delete_tag )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_button_delete_tag( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_font_size
###########################################################################

class Dialog_font_size ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Card text size...", pos = wx.DefaultPosition, size = wx.Size( 218,144 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )

		self.staticText_font_size1 = wx.StaticText( self, wx.ID_ANY, u"Font Point Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_font_size1.Wrap( -1 )

		bSizer241.Add( self.staticText_font_size1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

		self.spinCtrl_font_size = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 9, 28, 14 )
		bSizer241.Add( self.spinCtrl_font_size, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer7.Add( bSizer241, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 10 )

		self.button_font_size = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.button_font_size, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_font_size.Bind( wx.EVT_BUTTON, self.on_button_close )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_button_close( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_edit_tags
###########################################################################

class Dialog_edit_tags ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit tags...", pos = wx.DefaultPosition, size = wx.Size( 600,200 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Enter tags separated with a comma.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer26.Add( self.m_staticText9, 0, wx.ALL, 22 )


		bSizer7.Add( bSizer26, 1, wx.EXPAND, 5 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.staticText_edit_tags = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Tags:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_edit_tags.Wrap( -1 )

		bSizer24.Add( self.staticText_edit_tags, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )

		self.textCtrl_edit_tags = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer24.Add( self.textCtrl_edit_tags, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0 )


		self.m_panel2.SetSizer( bSizer24 )
		self.m_panel2.Layout()
		bSizer24.Fit( self.m_panel2 )
		bSizer7.Add( self.m_panel2, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.staticText_card_label = wx.StaticText( self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_card_label.Wrap( -1 )

		gSizer3.Add( self.staticText_card_label, 0, wx.ALL, 22 )

		self.button_font_size = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.button_font_size, 0, wx.ALL|wx.ALIGN_RIGHT, 15 )


		bSizer7.Add( gSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_font_size.Bind( wx.EVT_BUTTON, self.on_button_close )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_button_close( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_view_order
###########################################################################

class Dialog_view_order ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"View cards...", pos = wx.DefaultPosition, size = wx.Size( 145,168 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.checkBox_random = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"Randomly", wx.DefaultPosition, wx.DefaultSize, wx.CHK_2STATE )
		self.checkBox_random.SetValue(True)
		bSizer24.Add( self.checkBox_random, 1, wx.ALL, 10 )

		self.checkBox_sequential = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"Sequentially", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.checkBox_sequential, 1, wx.ALL, 10 )


		self.m_panel2.SetSizer( bSizer24 )
		self.m_panel2.Layout()
		bSizer24.Fit( self.m_panel2 )
		bSizer7.Add( self.m_panel2, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer37 = wx.BoxSizer( wx.VERTICAL )

		self.button_set = wx.Button( self, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.button_set, 0, wx.ALL|wx.ALIGN_RIGHT, 10 )


		bSizer7.Add( bSizer37, 1, wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.checkBox_random.Bind( wx.EVT_CHECKBOX, self.on_check_random )
		self.checkBox_sequential.Bind( wx.EVT_CHECKBOX, self.on_check_sequential )
		self.button_set.Bind( wx.EVT_BUTTON, self.on_button_sequence_set )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_check_random( self, event ):
		event.Skip()

	def on_check_sequential( self, event ):
		event.Skip()

	def on_button_sequence_set( self, event ):
		event.Skip()


