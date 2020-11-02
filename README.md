#pre-reqs

* install wsl2: https://docs.microsoft.com/en-us/windows/wsl/install-win10
* install docker: https://docs.docker.com/docker-for-windows/install/
* install git: https://desktop.github.com/

#instructions

* git clone
* cd connection-dev-spike
* docker-compose up
* get container id: docker ps(look for image odoo:12)
* docker exec -it <container id> bash
* enter: odoo --stop-after-init --test-enable -d test -i connection_test_spike --test-tags connection_test_spike

ouput will contain something like:

2020-11-02 21:39:40,993 1517 INFO test odoo.modules.loading: loading 10 modules... 
2020-11-02 21:39:41,082 1517 WARNING test odoo.models: The model connection_dev_spike.connection_binding has no _description 
2020-11-02 21:39:41,114 1517 INFO test odoo.modules.registry: module connection_dev_spike: creating or updating database tables 
2020-11-02 21:39:41,181 1517 INFO test odoo.modules.loading: loading connection_dev_spike/views/views.xml 
2020-11-02 21:39:41,189 1517 INFO test odoo.modules.loading: loading connection_dev_spike/views/templates.xml 
2020-11-02 21:39:41,194 1517 INFO test odoo.modules.loading: Module connection_dev_spike: loading demo 
2020-11-02 21:39:41,195 1517 INFO test odoo.modules.loading: loading connection_dev_spike/demo/demo.xml 
2020-11-02 21:39:41,248 1517 INFO test odoo.modules.module: odoo.addons.connection_dev_spike.tests.test_connection_binding running tests. 
2020-11-02 21:39:41,249 1517 INFO test odoo.addons.connection_dev_spike.tests.test_connection_binding: test_connection_binding (odoo.addons.connection_dev_spike.tests.test_connection_binding.TestConnection) 
2020-11-02 21:39:41,249 1517 INFO test odoo.addons.connection_dev_spike.tests.test_connection_binding: ` check if connection works 
2020-11-02 21:39:41,299 1517 INFO test odoo.addons.connection_dev_spike.tests.test_connection_binding: Ran 1 test in 0.050s 
2020-11-02 21:39:41,299 1517 INFO test odoo.addons.connection_dev_spike.tests.test_connection_binding: OK 
2020-11-02 21:39:41,352 1517 WARNING test odoo.models: The model connection_dev_spike.connection_binding has no _description