

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
conn = sqlite3.connect('fcdb.db')
cur = conn.cursor()

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(773, 691)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.horizontalLayout = QtWidgets.QHBoxLayout()
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(22)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.horizontalLayout.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.verticalLayout_2.addLayout(self.horizontalLayout)
                self.line = QtWidgets.QFrame(self.centralwidget)
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.verticalLayout_2.addWidget(self.line)
                self.verticalLayout = QtWidgets.QVBoxLayout()
                self.verticalLayout.setObjectName("verticalLayout")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.label_bat = QtWidgets.QLabel(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_bat.setFont(font)
                self.label_bat.setObjectName("label_bat")
                self.horizontalLayout_2.addWidget(self.label_bat)
                self.le_bat = QtWidgets.QLineEdit(self.centralwidget)
                self.le_bat.setEnabled(True)
                self.le_bat.setDragEnabled(False)
                self.le_bat.setReadOnly(True)
                self.le_bat.setObjectName("le_bat")
                self.horizontalLayout_2.addWidget(self.le_bat)
                self.label_bow = QtWidgets.QLabel(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_bow.setFont(font)
                self.label_bow.setObjectName("label_bow")
                self.horizontalLayout_2.addWidget(self.label_bow)
                self.le_bow = QtWidgets.QLineEdit(self.centralwidget)
                self.le_bow.setReadOnly(True)
                self.le_bow.setObjectName("le_bow")
                self.horizontalLayout_2.addWidget(self.le_bow)
                self.label_ar = QtWidgets.QLabel(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_ar.setFont(font)
                self.label_ar.setObjectName("label_ar")
                self.horizontalLayout_2.addWidget(self.label_ar)
                self.le_ar = QtWidgets.QLineEdit(self.centralwidget)
                self.le_ar.setReadOnly(True)
                self.le_ar.setObjectName("le_ar")
                self.horizontalLayout_2.addWidget(self.le_ar)
                self.label_wk = QtWidgets.QLabel(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_wk.setFont(font)
                self.label_wk.setObjectName("label_wk")
                self.horizontalLayout_2.addWidget(self.label_wk)
                self.le_wk = QtWidgets.QLineEdit(self.centralwidget)
                self.le_wk.setReadOnly(True)
                self.le_wk.setObjectName("le_wk")
                self.horizontalLayout_2.addWidget(self.le_wk)
                self.verticalLayout.addLayout(self.horizontalLayout_2)
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.label_available = QtWidgets.QLabel(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_available.setFont(font)
                self.label_available.setObjectName("label_available")
                self.horizontalLayout_4.addWidget(self.label_available)
                self.le_available = QtWidgets.QLineEdit(self.centralwidget)
                self.le_available.setReadOnly(True)
                self.le_available.setObjectName("le_available")
                self.horizontalLayout_4.addWidget(self.le_available)
                spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_4.addItem(spacerItem)
                spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_4.addItem(spacerItem1)
                spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_4.addItem(spacerItem2)
                spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_4.addItem(spacerItem3)
                self.label_used = QtWidgets.QLabel(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_used.setFont(font)
                self.label_used.setObjectName("label_used")
                self.horizontalLayout_4.addWidget(self.label_used)
                self.le_used = QtWidgets.QLineEdit(self.centralwidget)
                self.le_used.setReadOnly(True)
                self.le_used.setObjectName("le_used")
                self.horizontalLayout_4.addWidget(self.le_used)
                self.verticalLayout.addLayout(self.horizontalLayout_4)
                self.verticalLayout_2.addLayout(self.verticalLayout)
                self.line_2 = QtWidgets.QFrame(self.centralwidget)
                self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_2.setObjectName("line_2")
                self.verticalLayout_2.addWidget(self.line_2)
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.rb_bat = QtWidgets.QRadioButton(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.rb_bat.setFont(font)
                self.rb_bat.setObjectName("rb_bat")
                self.horizontalLayout_5.addWidget(self.rb_bat)
                self.rb_bow = QtWidgets.QRadioButton(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.rb_bow.setFont(font)
                self.rb_bow.setObjectName("rb_bow")
                self.horizontalLayout_5.addWidget(self.rb_bow)
                self.rb_ar = QtWidgets.QRadioButton(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.rb_ar.setFont(font)
                self.rb_ar.setObjectName("rb_ar")
                self.horizontalLayout_5.addWidget(self.rb_ar)
                self.rb_wk = QtWidgets.QRadioButton(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.rb_wk.setFont(font)
                self.rb_wk.setObjectName("rb_wk")
                self.horizontalLayout_5.addWidget(self.rb_wk)
                spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_5.addItem(spacerItem4)
                spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_5.addItem(spacerItem5)
                self.label_tn = QtWidgets.QLabel(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_tn.setFont(font)
                self.label_tn.setObjectName("label_tn")
                self.horizontalLayout_5.addWidget(self.label_tn)
                self.le_tn = QtWidgets.QLineEdit(self.centralwidget)
                self.le_tn.setReadOnly(True)
                self.le_tn.setObjectName("le_tn")
                self.horizontalLayout_5.addWidget(self.le_tn)
                self.verticalLayout_2.addLayout(self.horizontalLayout_5)
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.listWidget_1 = QtWidgets.QListWidget(self.centralwidget)
                self.listWidget_1.setObjectName("listWidget_1")
                self.horizontalLayout_6.addWidget(self.listWidget_1)
                spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_6.addItem(spacerItem6)
                self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
                self.listWidget_2.setObjectName("listWidget_2")
                self.horizontalLayout_6.addWidget(self.listWidget_2)
                self.verticalLayout_2.addLayout(self.horizontalLayout_6)
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 21))
                self.menubar.setObjectName("menubar")
                self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.menuManage_Teams.setFont(font)
                self.menuManage_Teams.setObjectName("menuManage_Teams")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.actionNEW_Team = QtWidgets.QAction(MainWindow)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.actionNEW_Team.setFont(font)
                self.actionNEW_Team.setObjectName("actionNEW_Team")
                self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
                self.actionOPEN_Team.setObjectName("actionOPEN_Team")
                self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
                self.actionSAVE_Team.setObjectName("actionSAVE_Team")
                self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
                self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
                self.menuManage_Teams.addAction(self.actionNEW_Team)
                self.menuManage_Teams.addSeparator()
                self.menuManage_Teams.addAction(self.actionOPEN_Team)
                self.menuManage_Teams.addSeparator()
                self.menuManage_Teams.addAction(self.actionSAVE_Team)
                self.menuManage_Teams.addSeparator()
                self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
                self.menubar.addAction(self.menuManage_Teams.menuAction())
                
                self.rb_bat.toggled.connect(self.ctg)
                self.rb_bow.toggled.connect(self.ctg)
                self.rb_ar.toggled.connect(self.ctg)
                self.rb_wk.toggled.connect(self.ctg) 

                self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu)
                
        
                self.bat=0
                self.bwl=0
                self.ar=0
                self.wk=0
                self.avl=1000
                self.used=0

                self.listWidget_1.itemDoubleClicked.connect(self.removelist1)
                self.listWidget_2.itemDoubleClicked.connect(self.removelist2)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_4.setText(_translate("MainWindow", "YOUR SELECTIONS"))
                self.label_bat.setText(_translate("MainWindow", "Batsmen (BAT)"))
                self.label_bow.setText(_translate("MainWindow", "Bowlers (BOW) "))
                self.label_ar.setText(_translate("MainWindow", "All Rounders (AR) "))
                self.label_wk.setText(_translate("MainWindow", "Wicket Keepers (WK) "))
                self.label_available.setText(_translate("MainWindow", "Points Available "))
                self.label_used.setText(_translate("MainWindow", "Points Used"))
                self.rb_bat.setText(_translate("MainWindow", "BAT"))
                self.rb_bow.setText(_translate("MainWindow", "BOW"))
                self.rb_ar.setText(_translate("MainWindow", "AR"))
                self.rb_wk.setText(_translate("MainWindow", "WK"))
                self.label_tn.setText(_translate("MainWindow", "Team Name"))
                self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
                self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
                self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
                self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
                self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        
        def menu(self, action):
                txt= (action.text())
                if txt =='NEW Team':
                        self.bat=0
                        self.bwl=0
                        self.ar=0
                        self.wk=0
                        self.avl=1000
                        self.used=0
                        self.listWidget_1.clear()
                        self.listWidget_2.clear()
                        text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter name of team:")
                        if ok:
                                self.le_tn.setText(str(text))

                        self.show()
                if txt =='OPEN Team':
                        self.bat=0
                        self.bwl=0
                        self.ar=0
                        self.wk=0
                        self.avl=1000
                        self.used=0
                        self.listWidget_1.clear()
                        self.listWidget_2.clear()
                        self.show()
                        self.openteam()
			
                if txt =='SAVE Team':
                        count=self.listWidget_2.count()
                        selected=""
                        for i in range(count):
                                selected+=self.listWidget_2.item(i).text()
                                if i<count:
                                                selected+=","
                        self.saveteam(self.le_tn.text(),selected,self.used)
            
                if txt=='EVALUATE Team':
                                from eval import Ui_Form
                                Dialog = QtWidgets.QDialog()
                                ui = Ui_Form()
                                ui.setupUi(Dialog)
                                ret=Dialog.exec()
        def show(self):
                self.le_bat.setText(str(self.bat))
                self.le_bow.setText(str(self.bwl))
                self.le_wk.setText(str(self.wk))
                self.le_ar.setText(str(self.ar))
                self.le_available.setText(str(self.avl))
                self.le_used.setText(str(self.used))	
	
        def criteria(self,ctgr,item):
                msg=''
                if ctgr=="BAT" and self.bat>=5:msg="Batsmen not more than 5"
                if ctgr=="BWL" and self.bwl>=5:msg="bowlers not more than 5"
                if ctgr=="AR" and self.ar>=3:msg="Allrounders not more than 3"
                if ctgr=="WK" and self.wk>=1:msg="Wicketkeepers not more than 1"
                if msg!='':
                        self.showdlg(msg)
                        return False
        
                if self.avl<=0:
                        msg="You Have Exhausted your Points"
                        self.showdlg(msg)
                        return False
        
                if ctgr=="BAT":self.bat+=1
                if ctgr=="BWL":self.bwl+=1
                if ctgr=="AR":self.ar+=1
                if ctgr=="WK":self.wk+=1

        
                sql="SELECT value from stats where player='"+item.text()+"'"
                cur=conn.execute(sql)
                row=cur.fetchone()
                self.avl-=int(row[0])
                self.used+=int(row[0])
                return True
			
	
        def ctg(self):
                ctgr=''
                if self.rb_bat.isChecked()==True:ctgr='BAT'
                if self.rb_bow.isChecked()==True:ctgr='BWL'
                if self.rb_ar.isChecked()==True:ctgr='AR'
                if self.rb_wk.isChecked()==True:ctgr='WK'
       	
                self.fillList(ctgr)
		
		
        def fillList(self,ctgr):
                if self.le_tn.text()=='':
                        self.showdlg("Enter name of team")
                        return
        
                self.listWidget_1.clear()
                sql="SELECT player from stats where ctg='"+ctgr+"';"
                cur=conn.execute(sql)
                for row in cur:
                        selected=[]
                        for i in range(self.listWidget_2.count()):
                                selected.append(self.listWidget_2.item(i).text())
                        if row[0] not in selected:self.listWidget_1.addItem(row[0])


        def removelist1(self,item):
        
                ctgr=''
                if self.rb_bat.isChecked()==True:ctgr='BAT'
                if self.rb_bow.isChecked()==True:ctgr='BWL'
                if self.rb_ar.isChecked()==True:ctgr='AR'
                if self.rb_wk.isChecked()==True:ctgr='WK'
                ret=self.criteria(ctgr,item)
        
                if ret==True:
                        self.listWidget_1.takeItem(self.listWidget_1.row(item))
                        self.listWidget_2.addItem(item.text())
                        self.show()
	
        def removelist2(self,item):
                self.listWidget_2.takeItem(self.listWidget_2.row(item))
        
                cursor = conn.execute("SELECT player,value, ctg from stats where player='"+item.text()+"'")
                row=cursor.fetchone()
                self.avl=self.avl+int(row[1])
                self.used=self.used-int(row[1])
                ctgr=row[2]
                if ctgr=="BAT":
                        self.bat-=1
                        if self.rb_bat.isChecked()==True:self.listWidget_1.addItem(item.text())
                if ctgr=="BWL":
                        self.bwl-=1
                        if self.rb_bow.isChecked()==True:self.listWidget_1.addItem(item.text())
                if ctgr=="AR":
                        self.ar-=1
                        if self.rb_ar.isChecked()==True:self.listWidget_1.addItem(item.text())
                if ctgr=="WK":
                        self.wk-=1
                        if self.rb_wk.isChecked()==True:self.listWidget_1.addItem(item.text())
                self.show()



        def openteam(self):
            
       
                sql="select name from teams;"
                
                cur=conn.execute(sql)
               
                teams=[]
              
                for row in cur:
                        teams.append(row[0])
        
                team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Dream","Choose A Team",teams,0,False)
                if ok and team:
                        self.le_tn.setText(team)
        
                sql1="SELECT players,value from teams where name='"+team+"';"
                cur=conn.execute(sql1)
                row=cur.fetchone()
                selected=row[0].split(',')
               
                self.listWidget_2.addItems(selected)
                
                self.used=row[1]
        
                self.avl=1000-row[1]
                count=self.listWidget_2.count()

               

                for i in range(count-1):
                        ply=self.listWidget_2.item(i).text()
                        
                        sql="select ctg from stats where player='"+ply+"';"
            
                        cur=conn.execute(sql)
            
                        row=cur.fetchone()
 
                        ctgr=row[0]
                        #print("ej")
                        if ctgr=="BAT":self.bat+=1
                        if ctgr=="BWL":self.bwl+=1
                        if ctgr=="AR":self.ar+=1
                        if ctgr=="WK":self.wk+=1  

                
                self.show()
                
        
		
	

        def saveteam(self,nm,ply,val):
                
        
                if self.bat+self.bwl+self.ar+self.wk!=11:
                        self.showdlg("Insufficient players")
                        return
        
                
                sql="INSERT INTO teams (name,players,value) VALUES ('"+nm+"','"+ply+"','"+str(val)+"');"
                
                try:
                       
                        cur=conn.execute(sql)
                      
                        self.showdlg("Team Saved Succesfully")
                        conn.commit()
                except:
                        self.showdlg("Error in Operation")
                        conn.rollback()   
        
        
        def showdlg(self,msg):
               
                Dialog=QtWidgets.QMessageBox()
                Dialog.setText(msg)
                Dialog.setWindowTitle("Dream Team selector")
                ret=Dialog.exec()

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
