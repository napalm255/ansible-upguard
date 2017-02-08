.. _upguard_node:


upguard_node - Manage UpGuard Node
++++++++++++++++++++++++++++++++++

.. versionadded:: 2.3


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* T
* h
* i
* s
*  
* m
* o
* d
* u
* l
* e
*  
* w
* i
* l
* l
*  
* m
* a
* n
* a
* g
* e
*  
* a
* n
*  
* U
* p
* G
* u
* a
* r
* d
*  
* n
* o
* d
* e
* .
*  
* I
* t
*  
* c
* a
* n
*  
* c
* r
* e
* a
* t
* e
* ,
*  
* u
* p
* d
* a
* t
* e
*  
* a
* n
* d
*  
* d
* e
* l
* e
* t
* e
*  
* a
*  
* n
* o
* d
* e
* .
*  
* A
* d
* d
*  
* t
* h
* e
*  
* n
* o
* d
* e
*  
* t
* o
*  
* a
*  
* n
* o
* d
* e
*  
* g
* r
* o
* u
* p
* .
*  
* C
* r
* e
* a
* t
* e
*  
* j
* o
* b
*  
* t
* o
*  
* s
* c
* a
* n
*  
* t
* h
* e
*  
* n
* o
* d
* e
* .
* 





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
        <td><div>Properties of the node.</div><div>See <a href='https://support.upguard.com/upguard/nodes-api-v2.html#create'>https://support.upguard.com/upguard/nodes-api-v2.html#create</a>.</div></td></tr>
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
        <td><div>Create or delete node.</div><div>When <em>state</em> is set to <code>present</code> facts will be gathered.</div></td></tr>
            <tr>
    <td>url<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The url of the Upguard Management Console. Port is optional. i.e.  https://upguard.example.com[:8443]
    </div></td></tr>
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
        <td align=center> present </td>
        <td align=center> dict </td>
        <td align=center> "node": {
    "created_at": "2017-01-26T22:37:12.866-05:00",
    "created_by": 8,
    "environment_id": 7,
    "id": 1117
    }
 </td>
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
