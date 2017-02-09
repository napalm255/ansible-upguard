.. _upguard_node:


upguard_node - Manage UpGuard Node
++++++++++++++++++++++++++++++++++

.. versionadded:: 2.3


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage UpGuard node.
* CRUD supported.
* Add node to node group.
* Create job to scan node.
* Check mode supported.


Requirements (on host that executes module)
-------------------------------------------

  * requests


Options
-------

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
            <tr>
    <td>gather_facts<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>True</li><li>False</li></ul></td>
        <td><div>Return node and group details.</div></td></tr>
            <tr>
    <td>groups<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>list</li></ul></td>
        <td><div>List of group ids and/or group names in which to add the node.</div></td></tr>
            <tr>
    <td>name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The name of the node.</div></td></tr>
            <tr>
    <td>node_type<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>SV</td>
        <td><ul><li>SV: Server</li><li>DT: Desktop</li><li>SW: Network Switch</li><li>FW: Firewall</li><li>RT: Router</li><li>PH: Smart Phone</li><li>RB: Robot</li><li>SS: SAN Storage</li><li>WS: Website</li></ul></td>
        <td><div>The node type. Use two letter code.</div></td></tr>
            <tr>
    <td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The password of the Upguard Management Console.</div></td></tr>
            <tr>
    <td>properties<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>dict</li></ul></td>
        <td><div>Properties of the node.</div><div>See <a href='https://support.upguard.com/upguard/nodes-api-v2.html#create'>https://support.upguard.com/upguard/nodes-api-v2.html#create</a>.</div><div>Invalid or misspelled properties will be ignored.</div><div>Property values are not validated.</div></td></tr>
            <tr>
    <td>scan<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>True</li><li>False</li></ul></td>
        <td><div>Create a job to scan the node.</div></td></tr>
            <tr>
    <td>scan_label<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>ansible initiated</td>
        <td><ul></ul></td>
        <td><div>Assign a label to the scan job.</div></td></tr>
            <tr>
    <td>scan_timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>120</td>
        <td><ul></ul></td>
        <td><div>Timeout in seconds to wait for the scan job.</div><div>The task will fail if the timeout is reached.</div></td></tr>
            <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>Create or delete node.</div><div>When <code>state=present</code> facts will be gathered.</div></td></tr>
            <tr>
    <td>url<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The url of the Upguard Management Console. Port is optional.</div><div>i.e.  https://upguard.example.com[:8443]</div></td></tr>
            <tr>
    <td>username<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The username of the Upguard Management Console.</div></td></tr>
            <tr>
    <td>validate_certs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
        <td><ul><li>True</li><li>False</li></ul></td>
        <td><div>Allows connection when SSL certificates are not valid.</div><div>Set to false when certificates are not trusted.</div></td></tr>
        </table>
    </br>



Examples
--------

 ::

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
    
    # create/update, add to groups and scan node
    - upguard_node:
        url: "https://upguard.example.com"
        username: "upguard_user"
        password: "upguard_pass"
        name: "node_name"
        node_type: "SV"
        state: "present"
        scan: true
        groups:
          - 100
          - GroupName
    
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
    

Return Values
-------------

Common return values are documented here :doc:`common_return_values`, the following are the fields unique to this module:

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">name</th>
    <th class="head">description</th>
    <th class="head">returned</th>
    <th class="head">type</th>
    <th class="head">sample</th>
    </tr>

        <tr>
        <td> node </td>
        <td> node details </td>
        <td align=center> either state is present or gather_facts is true </td>
        <td align=center> dict </td>
        <td align=center> {'connect_mode': 'f', 'primary_node_group_id': None, 'environment_id': 7, 'operating_system_id': None, 'discovery_type': None, 'medium_password': None, 'updated_at': '2017-02-08T18:07:19.502-05:00', 'node_type': 'SV', 'id': 1120, 'description': None, 'uuid': '686ddbc5-0f6a-4641-af41-5e99f62fe2ac', 'created_by': 8, 'medium_ssl_privkey': None, 'last_scan_id': None, 'mac_address': None, 'short_description': '', 'medium_group': None, 'medium_info': {}, 'status': 1, 'medium_port': 22, 'updated_by': 8, 'medium_username': None, 'alternate_password': None, 'medium_ssl_cert': None, 'online': False, 'scan_options': None, 'last_vuln_scan_at': None, 'ip_address': None, 'info': None, 'organisation_id': 4, 'medium_type': 3, 'name': 'SOME_NODE_NAME', 'operating_system_family_id': None, 'external_id': None, 'created_at': '2017-02-08T02:16:31.962-05:00', 'medium_connection_fail_count': 0, 'last_scan_status': None, 'public': False, 'url': None, 'connection_manager_group_id': None, 'medium_hostname': None} </td>
    </tr>
            <tr>
        <td> groups </td>
        <td> group details </td>
        <td align=center> groups are defined and either state is present or gather_facts is true </td>
        <td align=center> dict </td>
        <td align=center> {'102': {'status': 1, 'organisation_id': 4, 'description': None, 'node_rules': None, 'search_query': None, 'created_at': '2017-02-08T00:57:47.817-05:00', 'updated_at': '2017-02-08T00:57:47.817-05:00', 'name': 'SOME_GROUP_NAME', 'diff_notify': False, 'scan_options': '{"scan_directory_options":[]}', 'external_id': None, 'id': 102, 'owner_id': None}} </td>
    </tr>
            <tr>
        <td> scan </td>
        <td> scan job details </td>
        <td align=center> scan is true </td>
        <td align=center> dict </td>
        <td align=center> {'status': -1, 'organisation_id': 4, 'source_name': 'SOME_NODE_NAME', 'updated_by': 8, 'created_at': '2017-02-08T23:46:30.143-05:00', 'updated_at': '2017-02-08T23:46:37.133-05:00', 'created_by': 8, 'scheduled_job_id': None, 'source_type': 11, 'diff_stats': None, 'source_id': 1117, 'stats': None, 'upload_node_id': 1117, 'id': 780} </td>
    </tr>
        
    </table>
    </br></br>




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support
~~~~~~~

This module is community maintained without core committer oversight.

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/developing_test_pr` and :doc:`dev_guide/developing_modules`.
