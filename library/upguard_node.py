#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) 2016, Brad Gibson <napalm255@gmail.com>
#
# This file is a 3rd Party module for Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

"""Ansible Upguard Module."""
from __future__ import absolute_import, unicode_literals

DOCUMENTATION = '''
---
module: upguard_node
author: "Brad Gibson"
version_added: "2.2"
short_description: Manage UpGuard Node
requires: [ requests==2.13.0 ]
description:
    - Manage UpGuard Nodes. Create, Update, Delete and Scan Nodes with UpGuard.
options:
    url:
        required: true
        description:
            - The url of the Upguard Management Console. i.e.  https://upguard.example.com
    port:
        required: false
        default: 443
        description:
            - The port to connect to Upguard Management Console.
    username:
        required: true
        description:
            - The username of the Upguard Management Console.
    password:
        required: true
        description:
            - The password of the Upguard Management Console.
    name:
        required: true
        description:
            - The name of the node.
    node_type:
        required: true
        choices:
            - "SV: Server"
            - "DT: Desktop"
            - "SW: Network Switch"
            - "FW: Firewall"
            - "RT: Router"
            - "PH: Smart Phone"
            - "RB: Robot"
            - "SS: SAN Storage"
            - "WS: Website"
        description:
            - The node type. Use two letter code.
    gather_facts:
        required: false
        default: false
        choices:
            - true
            - false
        description:
            - Return node details.
    state:
        required: false
        choices:
            - present
            - absent
        description:
            - Create or delete node.
    properties:
        required: false
        choices:
            - dict
        description:
            - Properties of the node. See https://support.upguard.com/upguard/nodes-api-v2.html#create.
    scan:
        required: false
        default: false
        choices:
            - true
            - false
        description:
            - Scan node.
    validate_certs:
        required: false
        default: true
        choices:
            - true
            - false
        description:
            - Allows connection when SSL certificates are not valid. Set to false when certificates are not trusted.
'''

EXAMPLES = '''
# create/update node
- upguard_node:
    url: "https://upguard.example.com"
    username: "upguard_user"
    password: "upguard_pass"
    name: "node_name"
    node_type: "SV"
    state: "present"

# delete node
- upguard_node:
    url: "https://upguard.example.com"
    username: "upguard_user"
    password: "upguard_pass"
    name: "node_name"
    node_type: "SV"
    state: "absent"

# create/update and scan node
- upguard_node:
    url: "https://upguard.example.com"
    username: "upguard_user"
    password: "upguard_pass"
    name: "node_name"
    node_type: "SV"
    state: "present"
    scan: true

# scan node
- upguard_node:
    url: "https://upguard.example.com"
    username: "upguard_user"
    password: "upguard_pass"
    name: "node_name"
    node_type: "SV"
    scan: true

# gather facts
- upguard_node:
    url: "https://upguard.example.com"
    username: "upguard_user"
    password: "upguard_pass"
    name: "node_name"
    node_type: "SV"
    gather_facts: true
  register: results

'''

REQUIREMENTS = dict()
try:
    import time
    import operator
    import sys
    import json
    # pylint: disable = redefined-builtin, redefined-variable-type
    # pylint: disable = invalid-name, undefined-variable
    if sys.version_info[0] == 2:
        # Python 2
        # strings and ints
        text_type = unicode  # noqa
        string_types = (str, unicode)  # noqa
        integer_types = (int, long)  # noqa
        # lazy iterators
        range = xrange  # noqa
        from itertools import izip as zip  # noqa
        iteritems = operator.methodcaller('iteritems')  # noqa
        iterkeys = operator.methodcaller('iterkeys')  # noqa
        itervalues = operator.methodcaller('itervalues')  # noqa
    else:
        # Python 3
        # strings and ints
        text_type = str  # noqa
        string_types = (str,)  # noqa
        integer_types = (int,)  # noqa
        # lazy iterators
        zip = zip  # noqa
        range = range  # noqa
        iteritems = operator.methodcaller('items')  # noqa
        iterkeys = operator.methodcaller('keys')  # noqa
        itervalues = operator.methodcaller('values')  # noqa
except ImportError:
    pass

try:
    from ansible.module_utils.basic import AnsibleModule  # noqa
    REQUIREMENTS['ansible'] = True
except ImportError:
    REQUIREMENTS['ansible'] = False

try:
    import requests
    REQUIREMENTS['requests'] = True
except ImportError:
    REQUIREMENTS['requests'] = False


class UpguardNode(object):
    """Upguard Class."""

    def __init__(self, module):
        """Init."""
        self.module = module
        # turn module params into arg
        self.arg = lambda: None
        for arg in self.module.params:
            setattr(self.arg, arg, self.module.params[arg])
        # set defaults
        self.arg.name = self.arg.name.upper()
        # redact password for security
        if 'password' in module.params:
            module.params['password'] = 'REDACTED'
        # strip trailing slash and append api version
        self.arg.url = self.arg.url.rstrip('/') + '/api/v2'
        # define default results
        self.results = {'changed': False,
                        'failed': False,
                        'args': module.params}
        # define medium types mapping
        self.medium_types = {'AGENT': 1, 'SSH': 3, 'TELNET': 5, 'HTTPS': 6,
                             'WINRM': 7, 'SERVICE': 8, 'WEB': 9}
        # define node types mapping
        self.node_types = {'SV': 'Server', 'DT': 'Desktop',
                           'SW': 'Network Switch', 'FW': 'Firewall',
                           'RT': 'Router', 'PH': 'Smart Phone',
                           'RB': 'Robot', 'SS': 'SAN Storage', 'WS': 'Website'}
        # define nodes status codes mapping
        self.status_codes = {0: 'PENDING', 1: 'PROCESSING', 2: 'SUCCESS',
                             3: 'ASSIGNED', 5: 'ACTIONED', 9: 'FAILURE',
                             10: 'OFFLINE', 20: 'CANCELLED', 55: 'TIMEOUT',
                             88: 'ERROR', 99: 'EXCEPTION'}

    def __enter__(self):
        """Initiate connection."""
        return self

    def __exit__(self, type, value, traceback):
        """Disconnect."""
        # pylint: disable=redefined-builtin
        return

    def _connect(self, url=None, data=None, method='get'):
        """Connect and return request."""
        req = getattr(requests, str(method.lower()))
        url = self.arg.url + str(url)
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}
        auth = (self.arg.username, self.arg.password)
        verify = bool(self.arg.validate_certs)
        try:
            response = req(url, headers=headers, auth=auth, json=data,
                           verify=verify)
        except requests.exceptions.RequestException as ex:
            self.module.fail_json(msg=str(ex))

        return response

    @property
    def node_id(self):
        """Return node id."""
        try:
            url = '/nodes/lookup.json?name=' + str(self.arg.name)
            response = self._connect(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as ex:
            self.module.fail_json(msg=str(ex))

        content = {}
        if response.content:
            content = json.loads(response.content)

        node_id = None
        if 'node_id' in content:
            node_id = content['node_id']

        return node_id

    @property
    def node(self):
        """Return node."""
        node_id = self.node_id
        content = {}
        if node_id is not None:
            try:
                response = self._connect('/nodes/%s.json' % (node_id))
            except requests.exceptions.HTTPError as ex:
                self.module.fail_json(msg=str(ex))
            if response.content:
                content = json.loads(response.content)
        self.results['node'] = content
        return self.results['node']

    @property
    def exists(self):
        """Node exists."""
        node_exists = True
        try:
            url = '/nodes/lookup.json?name=' + str(self.arg.name)
            response = self._connect(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as ex:
            err = str(ex)
            if '404' in err:
                node_exists = False
            else:
                self.module.fail_json(msg=str(ex))
        self.results['node_exists'] = node_exists
        return node_exists

    @property
    def matches(self):
        """Match node to properties."""
        node_matches = True
        # define properties to match
        properties = {'name': self.arg.name,
                      'node_type': self.arg.node_type}
        properties.update(self.arg.properties)

        content = self.node
        # match properties
        for key, value in iteritems(properties):
            if key in content and value != content[key]:
                node_matches = False

        self.results['node_matches'] = node_matches
        return self.results['node_matches']

    def create(self):
        """Create node."""
        # define properties to set
        properties = {'name': self.arg.name,
                      'node_type': self.arg.node_type}
        properties.update(self.arg.properties)
        try:
            response = self._connect('/nodes.json', method='post',
                                     data={'node': properties})
            response.raise_for_status()
        except requests.exceptions.HTTPError as ex:
            self.module.fail_json(msg=str(ex))

        content = {}
        if response.content:
            content = json.loads(response.content)

        return content

    def update(self):
        """Update node."""
        updated = False
        node_id = self.node_id
        # define properties to set
        properties = {'node_type': self.arg.node_type}
        properties.update(self.arg.properties)
        try:
            url = '/nodes/%s.json' % (node_id)
            response = self._connect(url, method='put',
                                     data={'node': properties})
            response.raise_for_status()
            if response.status_code == 204:
                updated = True
        except requests.exceptions.HTTPError as ex:
            self.module.fail_json(msg=str(ex))

        self.results['updated'] = updated
        return self.results['updated']

    def delete(self):
        """Delete node."""
        deleted = False
        node_id = self.node_id
        try:
            url = '/nodes/%s.json' % (node_id)
            response = self._connect(url, method='delete')
            response.raise_for_status()
            if response.status_code == 204:
                deleted = True
        except requests.exceptions.HTTPError as ex:
            self.module.fail_json(msg=str(ex))

        self.results['deleted'] = deleted
        return self.results['deleted']

    def present(self):
        """Set state to present."""
        node_changed = False
        # create
        if not self.exists:
            self.results['created'] = self.create()
            node_changed = True
        # update
        elif self.exists and not self.matches:
            self.update()
            node_changed = True
        # validate
        if not self.exists or not self.matches:
            self.module.fail_json(msg="error validating state is present")
        return node_changed

    def absent(self):
        """Set state to absent."""
        node_changed = False
        # delete
        if self.exists:
            self.results['deleted'] = self.delete()
            node_changed = True
        # validate
        if self.exists:
            self.module.fail_json(msg="error validating state is absent")
        return node_changed

    def gather_facts(self):
        """Gather facts."""
        facts = False
        if self.exists:
            facts = bool(self.node)
        return facts

    def job(self, job_id):
        """Return job."""
        try:
            url = '/jobs/%s.json' % (job_id)
            response = self._connect(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as ex:
            self.module.fail_json(msg=str(ex))

        content = {}
        if response.content:
            content = json.loads(response.content)

        return content

    def scan(self, label='ansible initiated', sleep=60):
        """Scan node."""
        node_id = self.node_id
        try:
            url = '/nodes/%s/start_scan.json?label=%s' % (node_id, label)
            response = self._connect(url, method='post')
            response.raise_for_status()
        except requests.exceptions.HTTPError as ex:
            self.module.fail_json(msg=str(ex))

        content = {}
        if response.content:
            content = json.loads(response.content)

        if 'job_id' not in content:
            self.module.fail_json(msg='failed to create scan job')
        job_id = content['job_id']

        job = None
        for pause in range(sleep):
            job = self.job(job_id)
            status = job['status']
            if status == 2:
                break
            elif status == -1 or status > 2:
                self.module.fail_json(msg='scan failed')
            elif status < 2:
                time.sleep(pause)

        return job


def main():
    """Main."""
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(type='str', required=True),
            port=dict(type='int', default=443, required=False),
            username=dict(type='str', required=True),
            password=dict(type='str', required=True),
            gather_facts=dict(type='bool', default=False, required=False),
            name=dict(type='str', required=True),
            node_type=dict(type='str', default='Server', required=False),
            state=dict(type='str', default=None, required=False),
            properties=dict(type='dict', default=None, required=False),
            scan=dict(type='bool', default=False),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True
    )

    # check dependencies
    for requirement in REQUIREMENTS:
        if not requirement:
            module.fail_json(msg='%s not installed.' % (requirement))

    # check mode
    if module.check_mode:
        with UpguardNode(module) as upguard:
            if not upguard.exists or not upguard.matches:
                upguard.results['changed'] = True
            module.exit_json(**upguard.results)

    # gather facts
    if module.params['gather_facts']:
        with UpguardNode(module) as upguard:
            upguard.results['gather_facts'] = upguard.gather_facts()
            module.exit_json(**upguard.results)

    # process
    with UpguardNode(module) as upguard:
        state = module.params['state']
        scan = module.params['scan']
        # absent
        if 'absent' in state:
            upguard.results['changed'] = upguard.absent()
            module.exit_json(**upguard.results)
        # present
        if 'present' in state:
            upguard.results['changed'] = upguard.present()
        # scan
        if scan:
            upguard.results['scan'] = upguard.scan()
        module.exit_json(**upguard.results)

    # if no results, fail
    module.exit_json(**{'failed': True, 'msg': 'nothing to do'})


if __name__ == '__main__':
    main()
