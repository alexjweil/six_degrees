from redis import StrictRedis
import linecache

class GraphStorage(object):
	def __init__(self, link_file = 'links.txt', host = 'localhost', port = 6379):
		self.db = StrictRedis(host, port)
		self.link_file = link_file

	def add_nodes(self, graphDict, nameDict):
		pipe = self.db.pipeline()
		with open(self.link_file) as link_file:
			for _ in xrange(1):
				for _ in xrange(570607):
					node, links = self.create_link(next(link_file))
					name = linecache.getline('titles.txt', node)
					pipe.rpush('links-{0}'.format(node), *links)
					pipe.append('name-{0}'.format(node), name)
					pipe.append('id-{0}'.format(name), node)
				pipe.execute()

	def create_link(self, link):
		start, targets = link.rstrip('\n').split(': ')
		return int(start), map(int, targets.split())

	def get(self, kind, value):
		key = '{0}-{1}'.format(kind, value)
		if kind in ('name', 'id'):
			return self.db.get(key)
		elif kind == 'links':
			return self.db.lrange(key, 0, -1)
		raise ValueError

	def is_leaf(self, value):
		return self.db.sismember('leaves', value)

	def flush(self):
		self.db.flushall()

	def __len__(self):
		return self.db.dbsize()

# 5706070