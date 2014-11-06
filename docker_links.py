import re
from urlparse import urlparse


def parse_links(env):
    links = {}

    for envkey in env.keys():
        m = re.match("([A-Z0-9_]+)_PORT_\d+_([A-Z0-9]+)", envkey)
        if m is None:
            continue

        key = m.group(0)
        alias = m.group(1)
        proto = m.group(2).lower()
        name = env["%s_NAME" % alias]
        url = env[key]
        url_parts = urlparse(url)
        default_url = env["%s_PORT" % alias]
        alias = alias.lower()

        if alias not in links:
            links[alias] = {}

        if default_url == url:
            links[alias].update({
                "port": url_parts.port,
                "hostname": url_parts.hostname,
                "url": url,
                "proto": proto,
                "name": name
            })

        if proto not in links[alias]:
            links[alias][proto] = {}

        links[alias][proto][url_parts.port] = {
            "hostname": url_parts.hostname,
            "url": url
        }

    return links
