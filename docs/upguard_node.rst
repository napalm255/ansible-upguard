.. _upguard_node:


upguard_node - Manage UpGuard Node
++++++++++++++++++++++++++++++++++

.. versionadded:: 2.2


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage UpGuard node.
* Create, update and delete node.
* Add node to node groups.
* Scan node.




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
        <td><div>Return node details.</div></td></tr>
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
    <td></td>
        <td><ul><li>SV: Server</li><li>DT: Desktop</li><li>SW: Network Switch</li><li>FW: Firewall</li><li>RT: Router</li><li>PH: Smart Phone</li><li>RB: Robot</li><li>SS: SAN Storage</li><li>WS: Website</li></ul></td>
        <td><div>The node type. Use two letter code.</div></td></tr>
            <tr>
    <td>password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The password of the Upguard Management Console.</div></td></tr>
            <tr>
    <td>port<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>443</td>
        <td><ul></ul></td>
        <td><div>The port to connect to Upguard Management Console.</div></td></tr>
            <tr>
    <td>properties<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>dict</li></ul></td>
        <td><div>Properties of the node.</div><div>See https://support.upguard.com/upguard/nodes-api-v2.html#create.</div></td></tr>
            <tr>
    <td>scan<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>True</li><li>False</li></ul></td>
        <td><div>Scan node.</div></td></tr>
            <tr>
    <td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>Create or delete node.</div></td></tr>
            <tr>
    <td>url<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The url of the Upguard Management Console.</div><div>i.e.  https://upguard.example.com</div></td></tr>
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
    





Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support
~~~~~~~

This module is community maintained without core committer oversight.

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/developing_test_pr` and :doc:`dev_guide/developing_modules`.
