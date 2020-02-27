


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(443, 455)
                self.verticalLayout = QtWidgets.QVBoxLayout(Form)
                self.verticalLayout.setObjectName("verticalLayout")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.label_title = QtWidgets.QLabel(Form)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_title.setFont(font)
                self.label_title.setObjectName("label_title")
                self.horizontalLayout_3.addWidget(self.label_title, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.verticalLayout.addLayout(self.horizontalLayout_3)
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.label_explain = QtWidgets.QLabel(Form)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(9)
                font.setItalic(True)
                self.label_explain.setFont(font)
                self.label_explain.setObjectName("label_explain")
                self.horizontalLayout_2.addWidget(self.label_explain, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.verticalLayout.addLayout(self.horizontalLayout_2)
                self.line = QtWidgets.QFrame(Form)
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.verticalLayout.addWidget(self.line)
                self.horizontalLayout = QtWidgets.QHBoxLayout()
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.label_ct = QtWidgets.QLabel(Form)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_ct.setFont(font)
                self.label_ct.setObjectName("label_ct")
                self.horizontalLayout.addWidget(self.label_ct, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.cb_ct = QtWidgets.QComboBox(Form)
                self.cb_ct.setObjectName("cb_ct")
                self.horizontalLayout.addWidget(self.cb_ct)
                import sqlite3
                conn = sqlite3.connect('fcdb.db')
                self.horizontalLayout.addWidget(self.cb_ct)
                sql="select name from teams"
                cur=conn.execute(sql)
                teams=[]
                for row in cur:
                        self.cb_ct.addItem(row[0])        
                conn.close()
                self.label_cm = QtWidgets.QLabel(Form)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_cm.setFont(font)
                self.label_cm.setObjectName("label_cm")
                self.horizontalLayout.addWidget(self.label_cm, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.cb_cm = QtWidgets.QComboBox(Form)
                self.cb_cm.setObjectName("cb_cm")
                self.cb_cm.addItem("")
                self.cb_cm.addItem("")
                self.cb_cm.addItem("")
                self.horizontalLayout.addWidget(self.cb_cm)
                self.verticalLayout.addLayout(self.horizontalLayout)
                self.line_2 = QtWidgets.QFrame(Form)
                self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_2.setObjectName("line_2")
                self.verticalLayout.addWidget(self.line_2)
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.label_pname = QtWidgets.QLabel(Form)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_pname.setFont(font)
                self.label_pname.setObjectName("label_pname")
                self.horizontalLayout_4.addWidget(self.label_pname, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.label_sname = QtWidgets.QLabel(Form)
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_sname.setFont(font)
                self.label_sname.setObjectName("label_sname")
                self.horizontalLayout_4.addWidget(self.label_sname, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.verticalLayout.addLayout(self.horizontalLayout_4)
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.lw_players = QtWidgets.QListWidget(Form)
                self.lw_players.setObjectName("lw_players")
                self.horizontalLayout_5.addWidget(self.lw_players)
                spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_5.addItem(spacerItem)
                self.lw_scores = QtWidgets.QListWidget(Form)
                self.lw_scores.setObjectName("lw_scores")
                self.horizontalLayout_5.addWidget(self.lw_scores)
                self.verticalLayout.addLayout(self.horizontalLayout_5)
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.pb_score = QtWidgets.QPushButton(Form)
                self.pb_score.setMinimumSize(QtCore.QSize(75, 0))
                font = QtGui.QFont()
                font.setFamily("Cambria")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.pb_score.setFont(font)
                self.pb_score.setObjectName("pb_score")
                self.pb_score.clicked.connect(self.calculate)
                self.horizontalLayout_6.addWidget(self.pb_score, 0, QtCore.Qt.AlignLeft)
                spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_6.addItem(spacerItem1)
                self.le_score = QtWidgets.QLineEdit(Form)
                self.le_score.setObjectName("le_score")
                self.horizontalLayout_6.addWidget(self.le_score)
                self.verticalLayout.addLayout(self.horizontalLayout_6)

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)
        
        def calculate(self):
                import sqlite3
                conn = sqlite3.connect('fcdb.db')
                team=self.cb_ct.currentText()
                self.lw_players.clear()
                sql1="select players, value from teams where name='"+team+"'"
                cur=conn.execute(sql1)
                row=cur.fetchone()
                selected=row[0].split(',')
                self.lw_players.addItems(selected)
                teamttl=0
                self.lw_scores.clear()
                match=self.cb_cm.currentText()
                for i in range(0,self.lw_players.count()-1):
                        ttl, batscore, bowlscore, fieldscore=0,0,0,0
                        nm=self.lw_players.item(i).text()
                        cursor=conn.execute("select * from "+match+" where player='"+nm+"'")
                        row=cursor.fetchone()
                        batscore=int(row[1]/2)
                        if batscore>=50: batscore+=5
                        if batscore>=100: batscore+=10
                        if row[1]>0:
                                sr=row[1]/row[2]
                                if sr>=80 and sr<100: batscore+=2
                                if sr>=100:batscore+=4
                        batscore=batscore+row[3]
                        batscore=batscore+2*row[4]
                        bowlscore=row[8]*10
                        if row[8]>=3: bowlscore=bowlscore+5
                        if row[8]>=5: bowlscore=bowlscore=bowlscore+10
                        if row[7]>0:
                                er=6*row[7]/row[5]
                                if er<=2: bowlscore=bowlscore+10
                                if er>2 and er<=3.5: bowlscore=bowlscore+7
                                if er>3.5 and er<=4.5: bowlscore=bowlscore+4
                        fieldscore=(row[9]+row[10]+row[11])*10            
                        ttl=batscore+bowlscore+fieldscore
                        self.lw_scores.addItem(str(ttl))
                        teamttl=teamttl+ttl
                self.le_score.setText(str(teamttl))
               
                
        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.label_title.setText(_translate("Form", "Performance Evaluator"))
                self.label_explain.setText(_translate("Form", "Evaluate the Performace of Your Fantasy Team"))
                self.label_ct.setText(_translate("Form", "Choose Team"))
                self.label_cm.setText(_translate("Form", "Choose Match"))
                self.cb_cm.setItemText(0, _translate("Form", "match"))
                self.cb_cm.setItemText(1, _translate("Form", "match2"))
                self.cb_cm.setItemText(2, _translate("Form", "match3"))
                self.label_pname.setText(_translate("Form", "Players"))
                self.label_sname.setText(_translate("Form", "Scores"))
                self.pb_score.setText(_translate("Form", "Calculate Score"))


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
