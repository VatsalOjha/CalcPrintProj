import sys
import numpy as np
import sympy as sm
from sympy.solvers import solve
from sympy import Symbol, Function
import GUI as gui
import math
GCodeFile = open('C:\\3D Printer Calculus Project\\docs\\Sample.txt', 'w+')
x = Symbol('x')
f = Function('f')(x)
f = 0.5*x
xVals = []
yVals = []
zVals = []
SideArray = []
TotalVolume = 0
AxisChoice = gui.AxisRevScreen()
if AxisChoice == "X-axis":
	Bounds = gui.BoundsScreen()
	FirstBound = int(Bounds[0])
	FinalBound = int(Bounds[1])
	xInitialVal = FirstBound
	yInitialVal = f.subs(x, FirstBound)
	zInitialVal = 0
	xVals.append(xInitialVal)
	yVals.append(yInitialVal)
	zVals.append(zInitialVal)
	FinalBound1 = int(FinalBound * 10)
	FirstBound1 = int(FirstBound * 10)
	for t in range (FirstBound1, FinalBound1):
	### This for loop generates the x coordinates ###
		if t % 2 == 0:
			xVal = t/10.0
			for i in range (1,37):
				###This for loop generates the y and z coordinates for each x coordinate when the graph is spun around###
				newYVal = f.subs(x, xVal) * np.cos((3.14159265359*i)/18)
				newZVal = f.subs(x, xVal) * np.sin((3.14159265359*i)/18)
				yVals.append(newYVal)
				zVals.append(newZVal)
				xVals.append(xVal)
#####################################################################################################################################
				###Test Stuff to make sure my points are actually correct###
				DeltaY = yVals[len(yVals) - 1] - yVals[len(yVals) - 2]
				DeltaZ = zVals[len(zVals) - 1] - zVals[len(zVals) - 2]
				Side = math.sqrt(DeltaY * DeltaY + DeltaZ * DeltaZ)
				Area = f.subs(x, xVal) * (np.sin((0.4722222222)*(3.14159265359))) * (Side/2)
				Volume = Area * 0.2
				TotalVolume = TotalVolume + Volume
				###End Test###
#####################################################################################################################################
				SideArray.append(Side)
				if i == 36:
					for i in range (1,37):
						newInnerYVal = (f.subs(x, xVal) - 0.2) * np.cos((3.14159265359*i)/18)
						newInnerZVal = (f.subs(x, xVal) - 0.2) * np.sin((3.14159265359*i)/18)
						yVals.append(newInnerYVal)
						zVals.append(newInnerZVal)
						xVals.append(xVal)
						DeltaY = yVals[len(yVals) - 1] - yVals[len(yVals) - 2]
						DeltaZ = zVals[len(zVals) - 1] - zVals[len(zVals) - 2]
						Side = math.sqrt(DeltaY * DeltaY + DeltaZ * DeltaZ)
						SideArray.append(Side)
						if i == 36:
							for i in range (1,37):
								newInnerMostYVal = (f.subs(x, xVal) - 0.4) * np.cos((3.14159265359*i)/18)
								newInnerMostZVal = (f.subs(x, xVal) - 0.4) * np.sin((3.14159265359*i)/18)
								yVals.append(newInnerMostYVal)
								zVals.append(newInnerMostZVal)
								xVals.append(xVal)
								DeltaY = yVals[len(yVals) - 1] - yVals[len(yVals) - 2]
								DeltaZ = zVals[len(zVals) - 1] - zVals[len(zVals) - 2]
								Side = math.sqrt(DeltaY * DeltaY + DeltaZ * DeltaZ)
								SideArray.append(Side)
								if i == 36:
									for i in range (1,37):
										newInnerInnerMostYVal = (f.subs(x, xVal) - 0.6) * np.cos((3.14159265359*i)/18)
										newInnerInnerMostZVal = (f.subs(x, xVal) - 0.6) * np.sin((3.14159265359*i)/18)
										yVals.append(newInnerInnerMostYVal)
										zVals.append(newInnerInnerMostZVal)
										xVals.append(xVal)
										DeltaY = yVals[len(yVals) - 1] - yVals[len(yVals) - 2]
										DeltaZ = zVals[len(zVals) - 1] - zVals[len(zVals) - 2]
										Side = math.sqrt(DeltaY * DeltaY + DeltaZ * DeltaZ)
										SideArray.append(Side)
										if i == 36:
											for i in range (1,37):
												newInnerInnerInnerMostYVal = (f.subs(x, xVal) - 0.8) * np.cos((3.14159265359*i)/18)
												newInnerInnerInnerMostZVal = (f.subs(x, xVal) - 0.8) * np.sin((3.14159265359*i)/18)
												yVals.append(newInnerInnerInnerMostYVal)
												zVals.append(newInnerInnerInnerMostZVal)
												xVals.append(xVal)
												DeltaY = yVals[len(yVals) - 1] - yVals[len(yVals) - 2]
												DeltaZ = zVals[len(zVals) - 1] - zVals[len(zVals) - 2]
												Side = math.sqrt(DeltaY * DeltaY + DeltaZ * DeltaZ)
												SideArray.append(Side)

	if yVals[len(yVals) - 1] < yVals[0]:
		for i in range (1,len(yVals)):
			GCodeLine1 = 'G1 X%1.4f' %(zVals[i-1] + 100)
			GCodeLine2 = ' Y%1.4f' %(yVals[i-1] + 100)
			GCodeLine3 = ' Z%1.4f F1500' %xVals[i-1]
			GCodeLine4 = ' E%1.4f' %(SideArray[i-1]/2.25)
			GCodeFile.write(GCodeLine1)
			GCodeFile.write(GCodeLine2)
			GCodeFile.write(GCodeLine3)
			GCodeFile.write(GCodeLine4)
			GCodeFile.write("\n")
	else:
		for i in range (1,len(yVals)):
			GCodeLine1 = 'G1 X%1.4f' %(zVals[len(zVals)-(i+1)] + 100)
			GCodeLine2 = ' Y%1.4f' %(yVals[len(yVals)-(i+1)] + 100)
			GCodeLine3 = ' Z%1.4f F1000' %(xVals[i-1])
			GCodeLine4 = ' E%1.4f' %(SideArray[i-1]/2.25)
			GCodeFile.write(GCodeLine1)
			GCodeFile.write(GCodeLine2)
			GCodeFile.write(GCodeLine3)
			GCodeFile.write(GCodeLine4)
			GCodeFile.write("\n")

if AxisChoice == "Y-axis":
	Bounds = gui.BoundsScreen()
	FirstBound = int(Bounds[0])
	FinalBound = int(Bounds[1])
	yInitialVal = FirstBound
	xInitialVal = solve(f - FirstBound, x)[0]
	zInitialVal = 0
	xVals.append(xInitialVal)
	yVals.append(yInitialVal)
	zVals.append(zInitialVal)
	FinalBound1 = int(FinalBound * 10)
	FirstBound1 = int(FirstBound * 10)
	for t in range (FirstBound1, FinalBound1):
	### This for loop generates the x coordinates ###
		if t % 2 == 0:
			yVal = (t)/10.0
			print t
			if t < 0:
				if t == FirstBound1:
					ZAdjustment = yVal
			for i in range (1,37):
				###This for loop generates the y and z coordinates for each x coordinate when the graph is spun around###
				newXVal = solve(f - yVal, x)[0] * np.cos((3.14159265359*i)/18)
				newZVal = solve(f - yVal, x)[0] * np.sin((3.14159265359*i)/18)
				xVals.append(newXVal)
				zVals.append(newZVal) 
				yVals.append(yVal)

#####################################################################################################################################
				###Test Stuff to make sure my points are actually correct###
				DeltaX = xVals[len(xVals) - 1] - xVals[len(xVals) - 2]
				DeltaZ = zVals[len(zVals) - 1] - zVals[len(zVals) - 2]
				Side = math.sqrt(DeltaX * DeltaX + DeltaZ * DeltaZ)
				Area = solve(f - yVal, x)[0] * (np.sin((0.4722222222)*(3.14159265359))) * (Side/2)
				Volume = Area * 0.2
				TotalVolume = TotalVolume + Volume

				###End Test###
#####################################################################################################################################
				SideArray.append(Side)
				if i == 36:
					for i in range (1,37):
						newInnerXVal = (solve(f - yVal, x)[0] - 0.2) * np.cos((3.14159265359*i)/18)
						newInnerZVal = (solve(f - yVal, x)[0] - 0.2) * np.sin((3.14159265359*i)/18)
						xVals.append(newInnerXVal)
						zVals.append(newInnerZVal)
						yVals.append(yVal)
						DeltaX = xVals[len(xVals) - 1] - xVals[len(xVals) - 2]
						DeltaZ = zVals[len(zVals) - 1] - zVals[len(zVals) - 2]
						Side = math.sqrt(DeltaX * DeltaX + DeltaZ * DeltaZ)
						SideArray.append(Side)
						if i == 36:
							for i in range (1,37):
								newInnerMostXVal = (solve(f - yVal, x)[0] - 0.4) * np.cos((3.14159265359*i)/18)
								newInnerMostZVal = (solve(f - yVal, x)[0] - 0.4) * np.sin((3.14159265359*i)/18)
								xVals.append(newInnerMostXVal)
								zVals.append(newInnerMostZVal)
								yVals.append(yVal)
								DeltaX = xVals[len(xVals) - 1] - xVals[len(xVals) - 2]
								DeltaZ = zVals[len(zVals) - 1] - zVals[len(zVals) - 2]
								Side = math.sqrt(DeltaX * DeltaX + DeltaZ * DeltaZ)
								SideArray.append(Side)
								if i == 36:
									for i in range (1,37):
										newInnerInnerMostXVal = (solve(f - yVal, x)[0] - 0.6) * np.cos((3.14159265359*i)/18)
										newInnerInnerMostZVal = (solve(f - yVal, x)[0] - 0.6) * np.sin((3.14159265359*i)/18)
										xVals.append(newInnerInnerMostXVal)
										zVals.append(newInnerInnerMostZVal)
										yVals.append(yVal)
										DeltaX = xVals[len(xVals) - 1] - xVals[len(xVals) - 2]
										DeltaZ = zVals[len(zVals) - 1] - zVals[len(zVals) - 2]
										Side = math.sqrt(DeltaX * DeltaX + DeltaZ * DeltaZ)
										SideArray.append(Side)
										if i == 36:
											for i in range (1,37):
												newInnerInnerInnerMostXVal = (solve(f - yVal, x)[0] - 0.8) * np.cos((3.14159265359*i)/18)
												newInnerInnerInnerMostZVal = (solve(f - yVal, x)[0] - 0.8) * np.sin((3.14159265359*i)/18)
												xVals.append(newInnerInnerInnerMostXVal)
												zVals.append(newInnerInnerInnerMostZVal)
												yVals.append(yVal)
												DeltaX = xVals[len(xVals) - 1] - xVals[len(xVals) - 2]
												DeltaZ = zVals[len(zVals) - 1] - zVals[len(zVals) - 2]
												Side = math.sqrt(DeltaX * DeltaX + DeltaZ * DeltaZ)
												SideArray.append(Side)

	if xVals[len(xVals) - 1] < xVals[0]:
		for i in range (1,len(xVals)):
			GCodeLine1 = 'G1 X%1.4f' %(zVals[i-1] + 100)
			GCodeLine2 = ' Y%1.4f' %(xVals[i-1] + 100)
			GCodeLine3 = ' Z%1.4f F1000' %(yVals[i-1]-ZAdjustment)
			GCodeLine4 = ' E%1.4f' %(SideArray[i-1]/225)
			GCodeFile.write(GCodeLine1)
			GCodeFile.write(GCodeLine2)
			GCodeFile.write(GCodeLine3)
			GCodeFile.write(GCodeLine4)
			GCodeFile.write("\n")
	else:
		for i in range (1,len(xVals)):
			GCodeLine1 = 'G1 X%1.4f' %(zVals[len(zVals)-(i+1)] + 100)
			GCodeLine2 = ' Y%1.4f' %(xVals[len(xVals)-(i+1)] + 100)
			GCodeLine3 = ' Z%1.4f F150' %(yVals[len(yVals)-(i+1)]-ZAdjustment)
			GCodeLine4 = ' E%1.4f' %(SideArray[i-1]/225)
			GCodeFile.write(GCodeLine1)
			GCodeFile.write(GCodeLine2)
			GCodeFile.write(GCodeLine3)
			GCodeFile.write(GCodeLine4)
			GCodeFile.write("\n")

print TotalVolume