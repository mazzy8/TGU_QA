from graphviz import Graph
import os


os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
g = Graph(filename='bug_life_cycle.gv', format='png')

g.attr('node', shape='diamond')
g.node('1', 'Reproduced?')
g.node('2', 'Test passed?')

g.attr('node', shape='box')
g.node('3', 'New bug')
g.node('4', 'Close')

g.attr('node', shape='ellipse')
g.node('5', 'Approved')
g.node('6', 'Not approved')
g.node('7', 'Active')
g.node('8', 'Fix')
g.node('9', 'Reopen')
g.node('10', 'Check')

g.edge('3', '1', label='accept for \n verification')
g.edge('1', '5', label='true')
g.edge('1', '6', label='false')
g.edge('6', '4')
g.edge('5', '7', label='take to \n work')
g.edge('7', '8')
g.edge('8', '2', label='take for \n testing')
g.edge('2', '9', label='false')
g.edge('9', '7')
g.edge('2', '10', label='true')
g.edge('10', '4')

g.attr(label=r'bug life cycle')
g.attr(fontsize='20')

g.view()
