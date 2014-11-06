import unittest
import docker_links
import json

TEST_ENV = {
	"DB_NAME": "romantic_lumiere/db",
	"DB_PORT": "tcp://172.17.0.5:6379",
	"DB_PORT_6379_TCP": "tcp://172.17.0.5:6379",
	"DB_PORT_6379_TCP_ADDR": "172.17.0.5",
	"DB_PORT_6379_TCP_PORT": "6379",
	"DB_PORT_6379_TCP_PROTO": "tcp",
	"DB_PORT_6500_TCP": "tcp://172.17.0.5:6500",
	"DB_PORT_6500_TCP_ADDR": "172.17.0.5",
	"DB_PORT_6500_TCP_PORT": "6500",
	"DB_PORT_6500_TCP_PROTO": "tcp",
	"DB_REDIS_NAME": "romantic_lumiere/db_redis",
	"DB_REDIS_PORT": "tcp://172.17.0.2:6379",
	"DB_REDIS_PORT_6379_TCP": "tcp://172.17.0.2:6379",
	"DB_REDIS_PORT_6379_TCP_ADDR": "172.17.0.2",
	"DB_REDIS_PORT_6379_TCP_PORT": "6379",
	"DB_REDIS_PORT_6379_TCP_PROTO": "tcp"
};

class DockerLinkTests(unittest.TestCase):
	
	def test_parse_links(self):
		l = docker_links.parse_links(TEST_ENV)

		self.assertEqual(l["db"]["port"], 6379)
		
		print "%s" % json.dumps(l, indent=4)

if __name__ == '__main__':
    unittest.main()
