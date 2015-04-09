from Queue import PriorityQueue
from graphStorage import GraphStorage
from graphBuilder import GraphBuilder

import collections
import functools

class DegreeGraph(object):
	def __init__(self, filename, rebuild = False):
		self.storage = GraphStorage()
		if rebuild:
			self.storage.flush()
		if len(self.storage) == 0:
			self.fill_db(GraphBuilder(filename))

	def fill_db(self, graphBuilder):
		graph, names = graphBuilder.build()
		self.storage.add_nodes(0,0)

	def get_links(self, node):
		return self.storage.get('links', node)

	def get_name(self, node):
		return self.storage.get('name', node)

	def get_id(self, node):
		return self.storage.get('id', node)

	def connect(self, start, stop):
		visited = set()
		unvisited = PriorityQueue()
		unvisited.put((1, start, [start]))
		
		while not unvisited.empty():
			cost, position, path = unvisited.get()
			
			if position == stop: 
				return map(self.get_name, path)

			for node in (i for i in self.get_links(position)):
				if node not in visited and (not self.storage.is_leaf(node) or node == stop):
					node_cost = cost + 1
					node_path = path + [node]
					unvisited.put((node_cost, node, node_path))
					visited.add(node)
	def __len__(self):
		return self.graph.vcount()

g = DegreeGraph('links.txt', True)
# start = '3'
# stop = '9'
# print start, stop
# print g.connect(start, stop)
# layout = g.graph.layout("kk")
# igraph.plot(g.graph, layout = layout)