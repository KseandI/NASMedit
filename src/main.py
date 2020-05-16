import sys
import os
from subprocess import PIPE, run
#import re
import PyQt5
from UI import Ui_MainWindow
import difflib
#import syntax

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

class Window(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.code = ""
        self.filePath = ""
        self.fileName = ""
        self.fileOp = ""
        self.userEdit = True
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnOpenCode.clicked.connect(self.openCodeDiag)
        self.ui.btnSaveCode.clicked.connect(self.saveCodeDiag)
        self.ui.codeEditor.textChanged.connect(self.textChanged)
        self.ui.btnRunCode.clicked.connect(self.runCode)
        self.ui.btnCompileCode.clicked.connect(self.compileCode)
    
    def textChanged(self):
        if self.userEdit:
            self.userEdit = False
            self.updateCode()
            return
        cursor = self.ui.codeEditor.textCursor()
        pos = cursor.position()
        for _i,s in enumerate(difflib.ndiff(self.code, self.ui.codeEditor.toPlainText())):
            if s[0] == "+": # if edited
                try:     # \/  if (added enter) and (tab is first element of last line)
                    if s[-1] == "\n" and "\t" == self.code.split("\n")[-1][0]: # auto-tab
                        self.userEdit = True
                        self.ui.codeEditor.setPlainText(self.code)
                        txt = ""
                        self.userEdit = True
                        self.ui.codeEditor.setPlainText(self.ui.codeEditor.toPlainText()[:pos-1]+"\n\t"+self.ui.codeEditor.toPlainText()[pos-1:])
                        pos+=1
                        for _i in range(len(self.code.split("\n")[-2].split("\t"))-2):
                            txt += "\t"
                            pos+=1
                        self.userEdit = True
                        self.ui.codeEditor.setPlainText(self.ui.codeEditor.toPlainText()+txt)
                        self.userEdit = True                                   # auto-tab
                except IndexError:
                    print("error")
                    pass
        self.updateCode() # code << textEditor
        text = self.highlightText(self.code)
        self.userEdit = True
        self.ui.codeEditor.clear()
        self.userEdit = True
        for i in text.split("\n"):
            self.userEdit = True
            self.ui.codeEditor.appendHtml("<pre>"+i+"</pre>")
        cursor.setPosition(pos)
        self.ui.codeEditor.setTextCursor(cursor)
    
    def updateWorkPath(self, path: str) -> None:
        _fpath = path.split("/")
        fpath = ""
        for i in _fpath:
            if i != _fpath[-1]:
                fpath += i+"/"
        os.chdir(fpath)
        self.filePath = path
        self.fileName = _fpath[-1].split(".")[0]
        self.fileOp = _fpath[-1].split(".")[-1]
    
    def updateCode(self):
        self.code = self.ui.codeEditor.toPlainText()
        
    
    def openCodeDiag(self):
        self.userEdit = True
        fname = PyQt5.QtWidgets.QFileDialog.getOpenFileName(
            self, # IDK
            'Open file', # window title
            os.getcwd(), # open up directory
            "Asm Files (*.asm);;All Files (*);;Text Files (*.txt)" # filters
        )[0]
        if fname: # if user open file
            self.updateWorkPath(fname)
            f = open(fname, 'r')
            with f:
                data = f.read()
                self.ui.codeEditor.setPlainText(data)
    
    def saveCodeDiag(self):
        fname = PyQt5.QtWidgets.QFileDialog.getSaveFileName(
            self, # IDK
            'Open file', # window title
            os.getcwd(), # open up directory
            "Asm Files (*.asm);;All Files (*);;Text Files (*.txt)" # filters
        )[0]
        if fname:
            self.saveCode(fname)
    
    def saveCode(self, path):
        self.updateWorkPath(path)
        self.updateCode()
        with open(path, 'w') as file:
            file.write(self.code+"\n")
    
    def keyPressEvent(self, e):
            if e.modifiers() == PyQt5.QtCore.Qt.ControlModifier:
                if e.key() == PyQt5.QtCore.Qt.Key_S:
                    if self.filePath == "":
                        self.saveCodeDiag()
                    else:
                        self.saveCode(self.filePath)
            else:
                super(Window, self).keyPressEvent(e)
    
    def compileCode(self):
        print(out("nasm -f elf "+self.fileName+"."+self.fileOp))
        print(out("ld -m elf_i386 "+self.fileName+".o -o "+self.fileName))

    def runCode(self):
        if self.fileName == "":
            self.saveCodeDiag()
        if self.fileName == "":
            return
        if not self.fileName in str(out("ls")).split("\n"):
            self.compileCode()
        print(out("./"+self.fileName))
    
    #def highlightText(self, txt: str) -> str:  # use regex to find text
    #    text = txt
    #    for i in syntax.NASMsyntax.keys():
    #        for j in syntax.NASMsyntax[i]:
    #            word = re.search(j, text)
    #            if not word is None:
    #                pass#print("Word: "+word.group()+"\npos: "+str(word.start()))
    #    return text
        

if __name__ == '__main__':
    os.chdir(os.path.expanduser("~"))
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    
    sys.exit(app.exec())

# TODO: syntax highlighting