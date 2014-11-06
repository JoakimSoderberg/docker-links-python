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
	"DB_REDIS_PORT_6379_TCP_PROTO": "tcp",
	"DB_REDIS_PORT_6379_UDP": "udp://172.17.0.2:6379",
	"DB_REDIS_PORT_6379_UDP_ADDR": "172.17.0.2",
	"DB_REDIS_PORT_6379_UDP_PORT": "6379",
	"DB_REDIS_PORT_6379_UDP_PROTO": "udp"
};

class DockerLinkTests(unittest.TestCase):
	
	def test_parse_links(self):
		l = docker_links.parse_links(TEST_ENV)

		self.assertEqual(l["db"]["hostname"], TEST_ENV["DB_PORT_6379_TCP_ADDR"])
		self.assertEqual(l["db"]["port"], int(TEST_ENV["DB_PORT_6379_TCP_PORT"]))
		self.assertEqual(l["db"]["proto"], TEST_ENV["DB_PORT_6500_TCP_PROTO"])
		
		print "%s" % json.dumps(l, indent=2, sort_keys=True)

if __name__ == '__main__':
    unittest.main()
