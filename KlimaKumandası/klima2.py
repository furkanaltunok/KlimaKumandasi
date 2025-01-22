from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from klima import *

class KlimaKumandasi(QMainWindow):
    def __init__(self, durum="KAPALI", derece=dereceSayi, mod="SOĞUTMA", fan="DÜŞÜK", turboMod = "KAPALI",swing = "HAREKETLİ"):
        self.durum = durum
        self.derece =  derece
        self.mod = mod
        self.fan = fan
        self.turboMod = turboMod
        self.swing = swing

        
        super().__init__()
        self.qtTasarim = Ui_mainWindow()
        self.qtTasarim.setupUi(self)
        self.setFixedSize(353,340) #Pencere boyutu ayarlama engellendi
        self.qtTasarim.powerButon.setIcon(QIcon("powerIcon.png")) # power butonuna ikon eklendi
        self.qtTasarim.dereceButon1.clicked.connect(self.dereceArttir)
        self.qtTasarim.dereceButon2.clicked.connect(self.dereceAzalt)
        self.qtTasarim.fanButon.clicked.connect(self.fanDegis)
        self.qtTasarim.modeButon.clicked.connect(self.modDegis)
        self.qtTasarim.turboButon.clicked.connect(self.turboAcKapa)
        self.qtTasarim.swingButon.clicked.connect(self.swingDegis)
        self.qtTasarim.powerButon.clicked.connect(self.acKapa)
        self.qtTasarim.cutButon.clicked.connect(self.shortCut)
        if(self.durum == "KAPALI"):
            self.qtTasarim.cutButon.setDisabled(True)
            self.qtTasarim.dereceButon1.setDisabled(True)
            self.qtTasarim.dereceButon2.setDisabled(True)
            self.qtTasarim.dereceLabel.setDisabled(True)
            self.qtTasarim.fanButon.setDisabled(True)
            self.qtTasarim.fanLabel.setDisabled(True)
            self.qtTasarim.fanLabel2.setDisabled(True)
            self.qtTasarim.modeButon.setDisabled(True)
            self.qtTasarim.modLabel.setDisabled(True)
            self.qtTasarim.modLabel2.setDisabled(True)
            self.qtTasarim.swingButon.setDisabled(True)
            self.qtTasarim.swingLabel.setDisabled(True)
            self.qtTasarim.swingLabel2.setDisabled(True)
            self.qtTasarim.turboButon.setDisabled(True)
            return
       
    def dereceArttir(self):
        self.qtTasarim.klimaLabel.clear()
        if(self.derece != 30):
            self.derece+=1
            self.qtTasarim.dereceLabel.setText(str(self.derece))
            return

    def dereceAzalt(self):
        self.qtTasarim.klimaLabel.clear()
        if(self.derece != 17):
            self.derece-=1
            self.qtTasarim.dereceLabel.setText(str(self.derece))
            return

    def modDegis(self):
        self.qtTasarim.klimaLabel.clear()
        if(self.mod == "SOĞUTMA"):
            self.mod = "ISITMA"
            self.qtTasarim.modLabel2.setText(self.mod)
            return
        if(self.mod == "ISITMA"):
            self.mod = "SOĞUTMA"
            self.qtTasarim.modLabel2.setText(self.mod)
            return

    def fanDegis (self):
        self.qtTasarim.klimaLabel.clear()
        if(self.turboMod == "AÇIK"):
            self.qtTasarim.klimaLabel.setText(("Turbo mod açık olduğunda fan ayarları değiştirilemez."))
            return
        if(self.fan == "DÜŞÜK"):
            self.fan = "ORTA"
            self.qtTasarim.fanLabel2.setText(self.fan)
            return
        if(self.fan == "ORTA"):
            self.fan = "YÜKSEK"
            self.qtTasarim.fanLabel2.setText(self.fan)
            return
        if(self.fan == "YÜKSEK"):
            self.fan = "DÜŞÜK"
            self.qtTasarim.fanLabel2.setText(self.fan)
            return

    def turboAcKapa(self):
        self.qtTasarim.klimaLabel.clear()
        if(self.turboMod == "KAPALI"):
            self.turboMod = "AÇIK"
            self.qtTasarim.fanLabel2.setText("TURBO")
            return
        else:
            self.turboMod = "KAPALI"
            self.qtTasarim.fanLabel2.setText(self.fan)
            return
        
    def swingDegis(self):
        self.qtTasarim.klimaLabel.clear()
        if(self.swing == "HAREKETLİ"):
            self.swing = "SABİT"
            self.qtTasarim.swingLabel2.setText(self.swing)
            return
        if(self.swing == "SABİT"):
            self.swing = "HAREKETLİ"
            self.qtTasarim.swingLabel2.setText(self.swing)
            return

    
    def acKapa(self):
        self.qtTasarim.klimaLabel.clear()
        if(self.durum == "KAPALI"):
            self.durum = "AÇIK"
            self.qtTasarim.cutButon.setDisabled(False)
            self.qtTasarim.dereceButon1.setDisabled(False)
            self.qtTasarim.dereceButon2.setDisabled(False)
            self.qtTasarim.dereceLabel.setDisabled(False)
            self.qtTasarim.fanButon.setDisabled(False)
            self.qtTasarim.fanLabel.setDisabled(False)
            self.qtTasarim.fanLabel2.setDisabled(False)
            self.qtTasarim.modeButon.setDisabled(False)
            self.qtTasarim.modLabel.setDisabled(False)
            self.qtTasarim.modLabel2.setDisabled(False)
            self.qtTasarim.swingButon.setDisabled(False)
            self.qtTasarim.swingLabel.setDisabled(False)
            self.qtTasarim.swingLabel2.setDisabled(False)
            self.qtTasarim.turboButon.setDisabled(False)
            return
        if(self.durum == "AÇIK"):
            self.durum = "KAPALI"
            self.qtTasarim.cutButon.setDisabled(True)
            self.qtTasarim.dereceButon1.setDisabled(True)
            self.qtTasarim.dereceButon2.setDisabled(True)
            self.qtTasarim.dereceLabel.setDisabled(True)
            self.qtTasarim.fanButon.setDisabled(True)
            self.qtTasarim.fanLabel.setDisabled(True)
            self.qtTasarim.fanLabel2.setDisabled(True)
            self.qtTasarim.modeButon.setDisabled(True)
            self.qtTasarim.modLabel.setDisabled(True)
            self.qtTasarim.modLabel2.setDisabled(True)
            self.qtTasarim.swingButon.setDisabled(True)
            self.qtTasarim.swingLabel.setDisabled(True)
            self.qtTasarim.swingLabel2.setDisabled(True)
            self.qtTasarim.turboButon.setDisabled(True)
            return
    
    def shortCut(self):
        self.qtTasarim.klimaLabel.clear()
        self.qtTasarim.fanLabel2.setText("DÜŞÜK")
        self.qtTasarim.swingLabel2.setText("HAREKETLİ")
        self.qtTasarim.dereceLabel.setText(str(24))
        self.qtTasarim.modLabel2.setText("SOĞUTMA")
        self.turboMod = "KAPALI"
        return

        
        
        

uygulama = QApplication([])
pencere = KlimaKumandasi()
pencere.show()
uygulama.exec_()