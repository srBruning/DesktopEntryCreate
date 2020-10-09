import gi
from gi.repository import Gtk
from util import *
gi.require_version("Gtk", "3.0")

class AppWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self)
		self.connect("destroy", Gtk.main_quit)
		self.set_title("Add menu")
		self.vbox = Gtk.VBox()
		self.lstTxt = [] 
		self.bfFileName= self.creat_field("File Name","", False)
		self.lbStatus = Gtk.Label("")
		btn = Gtk.Button("salvar")

		for param in defeultDesktopEntryParams():
			self.creat_field(param[0], param[1])


		btn.connect('clicked', self._save)
		self.vbox.pack_start(btn, True, False,10)
		self.vbox.pack_start(self.lbStatus, True, False,10)
		self.add(self.vbox)


	def _save(self, ev):
		fName = _getText(self.bfFileName)
		if len(fName)<2 :
			self.lbStatus.set_text("Nome do arquivo invalido")
			return

		self.lbStatus.set_text("")
		
		params =[]
		for linha in self.lstTxt:
			params.append([linha[0], _getText(linha[1])])

		saveDesktopEntry(fName, params)

		self.lbStatus.set_text("sucesso")

	def creat_field(self, label, value, indAdd=True):
		buffer1 = Gtk.TextBuffer()
		buffer1.set_text(value)
		txt = Gtk.TextView(buffer=buffer1)
		txt.set_size_request(500, 25)
		lbl = Gtk.Label(label)
		lbl.set_size_request(100, 25)
		hbox = Gtk.HBox()
		hbox.pack_start(lbl, True, False, 50);
		hbox.pack_end(txt, True, True, 0)

		self.vbox.pack_start(hbox, True, False, 5)
		self.lstTxt.append([label,buffer1])
		return buffer1

def _getText(txtBuffer):
	start_iter = txtBuffer.get_start_iter()
	end_iter = txtBuffer.get_end_iter()
	return  txtBuffer.get_text(start_iter, end_iter, True)  


if __name__ == '__main__':
	window = AppWindow()
	window.show_all()
	Gtk.main()
