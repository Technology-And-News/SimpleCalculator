import webbrowser
import globalPluginHandler
import wx
import gui
from keyboardHandler import KeyboardInputGesture
from scriptHandler import script
import addonHandler
addonHandler.initTranslation()

showDialog = None
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(
description= _("open semple calculator dialog"),
category= _("SimpleCalculator"),
gesture="kb:nvda+alt+s")
	def script_start (self, gesture):
		global showDialog
		if not showDialog:
			showDialog= mainDialog(gui.mainFrame)
			showDialog.Raise()
		else:
			showDialog.Raise()

class mainDialog(wx.Dialog):
	def __init__(self, parent):
		super(mainDialog, self).__init__(parent, title = _("Simple calculator"))
		wx.StaticText(self, -1, _("Arithmetic operation"))
		self.number1= wx.TextCtrl(self, -1)
		r= wx.Button(self, -1, _("&get result"))
		r.Bind(wx.EVT_BUTTON, self.onr)
		r.SetDefault()
		wx.StaticText(self, -1, _("result"))
		self.re= wx.TextCtrl(self, -1,style=wx.TE_MULTILINE+wx.HSCROLL+wx.TE_READONLY)
		self.Bind(wx.EVT_CHAR_HOOK, self.OnHook)
		help=wx.Button(self,-1, _("&Help"))
		self.Bind(wx.EVT_BUTTON, self.onLanguagec,help)

		self.Show()
	def OnHook(self,event):
		k=event.GetKeyCode()
		if k==wx.WXK_ESCAPE:
			self.Destroy()
		event.Skip()
	def onLanguagec(self, event):
		h= wx.Menu()
		NUA= h.Append(-1, _("Simple calculator on GitHub "))
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("https://github.com/Technology-And-News/SimpleCalculator/"), NUA)
		con= wx.Menu()
		Anas= wx.Menu()
		telegram= Anas.Append(-1, "telegram")
		twitter= Anas.Append(-1, "twitter")
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("https://t.me/mesteranasm"), telegram)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("https://twitter.com/mesteranasm"), twitter)
		Mohammed= wx.Menu()
		telegram1= Mohammed.Append(-1, "telegram")
		twitter1= Mohammed.Append(-1, "twitter")
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("https://t.me/mohamedtechnology"), telegram1)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("https://twitter.com/mohamedtechnolo"), twitter1)
		Tan= wx.Menu()
		telegram2= Tan.Append(-1, "telegram")
		youtube= Tan.Append(-1, "GitHub")
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("https://t.me/tanprojects"), telegram2)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("https://github.com/Technology-And-News/"), youtube)
		con.AppendSubMenu(Anas, _("&Mester Anas"))
		con.AppendSubMenu(Mohammed, _("&Mohammed technology"))
		con.AppendSubMenu(Tan, _("&Technology and news"))
		don= h.Append(-1, _("&donate"))
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open("https://www.paypal.me/AMohammed231"), don)
		h.AppendSubMenu(con, _("&Contact us"))
		self.PopupMenu(h)

	def onr(self, event):
		self.re.Value=""
		try:
			num1=eval(self.number1.Value)
			self.re.Value=str(num1)
			iiii=str(num1)
			wx.MessageBox(iiii)
		except:
			wx.MessageBox(_("can't make this operation"),_("error"))

