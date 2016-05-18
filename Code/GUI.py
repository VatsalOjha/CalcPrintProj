import easygui as eg
from easygui import *
def AxisRevScreen():
	msg ="""Choose something
		"""
	title = "3D Printer Thing. Choose Axis:"
	AxisChoice = ["Y-axis", "X-axis"]
	achoice = choicebox(msg, title, AxisChoice)
	return achoice
def BoundsScreen():
	msg= "Choose the bounds"
	title = "Choose Bounds"
	fieldNames = ["First Bound", "Final Bound"]
	fieldValues = []
	fieldValues = multenterbox(msg, title, fieldNames)
	return fieldValues