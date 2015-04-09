import linecache

class GraphBuilder(object):
	def __init__(self, link_file):
		self.link_file = link_file

	def create_link(self, link):
		return start, targets.split()

	def build_graph(self):
		return dict(self.create_link(link) for link in open(self.link_file))

	def build_names(self, graph_dict):
		getline = linecache.getline
		return {node : getline('titles.txt', int(node)).rstrip('\n') for node in graph_dict}

	def build(self):
		graph = self.build_graph()
		names = self.build_names(graph)
		return graph, names