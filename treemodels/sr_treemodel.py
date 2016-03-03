from PySide import QtGui

import sys
import yaml

from treemodel_pyside_example import NamesModel


class NameElement(object): # your internal structure
    def __init__(self, name, subelements):
        # todo - accept name as single constructor argument
        self.name = name
        self.subelements = subelements if isinstance(subelements, list) else [subelements]

    @classmethod
    def generateFromDict(cls, input):
        # todo - handle dict with multiple keys
        sibling_elements = []
        if isinstance(input, dict):
            #for key, values in input.items():
            return ([cls(key, cls.generateFromDict(val)) for key,val in input.items()])
            return sibling_elements
        elif isinstance(input, list):
            return ([cls("list", cls.generateFromDict(val)) for val in input])
            return sibling_elements
        else:
            return cls(input, [])
        # todo - handle input as list

    @classmethod
    def generateFromNestedList(cls, input):
        raise NotImplementedError

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setLayout(QtGui.QFormLayout(self))
        self.treeview = QtGui.QTreeView(self)

        objects = yaml.load(open("objects.yml", "rU"))
        self.els_from_yml = NameElement.generateFromDict(objects)

        self.model_from_yml = NamesModel(self.els_from_yml, headers=["Parameter", "Value"])

        self.treeview.setModel(self.model_from_yml)
        self.layout().addRow(self.treeview)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()