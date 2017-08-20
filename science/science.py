from pulp import import *
f = LpProblem('lptest',LpMinimize)

x = LpVariable('x',lowBound=0)
y = LpVariable('y',lowBound=0)
z = LpVariable('z',lowBound=0)

f += 3.05*x + 4.05*y + 6.1*z >= 7.9
f.solve(GLPK())

for v in f.variables():
        print v.name, "=",v.varValue

