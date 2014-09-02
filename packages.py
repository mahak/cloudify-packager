# flake8: NOQA
########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from user_definitions import *

# TODO: add support for "skip_get" and "skip_pack" flags.
VARIABLES = {
    "logstash": {

    },
    "manager_server_path": "{0}/manager/cloudify-manager-{1}/rest-service/manager_rest/".format(VIRTUALENVS_PATH, MANAGER_BRANCH),
    "gunicorn_user": "root",
    "manager_rest_port": "8100",
    "manager_file_server_dir": "{0}/manager/resources".format(VIRTUALENVS_PATH),
    "gunicorn_conf_path": "{0}/manager/config/conf/guni.conf".format(VIRTUALENVS_PATH),
    "unicorn_user": "root",
    "kibana_run_dir": "/opt/kibana3",
    "kibana_port": "3000",
    "nginx_rest_and_ui_port": "80",
    "nginx_file_server_port": "53229",
    "nginx_file_server_dir": "{0}/manager/resources".format(VIRTUALENVS_PATH),
    "rabbitmq_port": "5672"
    "elasticsearch_port": "9200"
    "langohr_jar": "{0}/riemann/langohr/langohr.jar".format(COMPONENT_PACKAGES_PATH),
    "manager_config": "{0}/manager/cloudify-manager-{1}/plugins/riemann-controller/riemann_controller/resources/manager.config".format(VIRTUALENVS_PATH, MANAGER_BRANCH)
    "celery_init_path": "/etc/init/celeryd-cloudify-management.conf",
    "celery_run_dir": "{0}/celery".format(VIRTUALENVS_PATH),
    "ui_log_file": "/var/log/cloudify-ui/cosmo-ui.log",
    "ui_user": "root",
    "ui_run_dir": "/opt/cloudify-ui",
    "ui_port": "9001",
    "celery_work_dir": "{0}/celery/cloudify.management__worker".format(VIRTUALENVS_PATH),
    "celery_workers_autoscale": "5,2"
    "logstash_jar": "logstash.jar",
    "logstash_log_file": "/var/log/logstash.out",
    "logstash_conf_path": "/etc/logstash.conf",
    "logstash_run_dir": "/opt/logstash",
    "logstash_user": "root",
    "logstash_events_queue": "cloudify-events",
    "logstash_logs_queue": "cloudify-logs",
    "logstash_test_tcp_port": "9999",
    "logstash_events_index": "cloudify_events",
    "elasticsearch_run_dir": "/opt/elasticsearch",
    "elasticsearch_user": "root",
}
PACKAGES = {
    "cloudify-core": {
        "name": "cloudify-core",
        "version": "3.0.0",
        "depends": [
            'cloudify-components'
        ],
        "package_path": "/cloudify",
        "sources_path": CORE_PACKAGES_PATH,
        "src_package_type": "dir",
        "dst_package_type": ["deb"],
        "bootstrap_script_in_pkg": "{0}/cloudify-core-bootstrap.sh".format(SCRIPTS_PATH),
        "bootstrap_template": "cloudify-core-bootstrap.template",
        "bootstrap_log": "/var/log/cloudify-core-bootstrap.log",
        "overwrite_package": False,
    },
    "cloudify-components": {
        "name": "cloudify-components",
        "version": "3.0.0",
        "package_path": "/cloudify",
        "sources_path": COMPONENT_PACKAGES_PATH,
        "src_package_type": "dir",
        "dst_package_type": ["deb"],
        "bootstrap_script_in_pkg": "{0}/cloudify-components-bootstrap.sh".format(SCRIPTS_PATH),
        "bootstrap_template": "cloudify-components-bootstrap.template",
        "bootstrap_log": "/var/log/cloudify-bootstrap.log",
        "overwrite_package": False,
        "bootstrap_params": {
            "req_free_mem": "10000",
            "req_free_disk": "5",
            "req_cpu_cores": "1",
            "req_arch": "x86_64",
            "req_os": "precise",
        },
        "config_templates": {
            "template_file_nginx": {
                "template": "{0}/nginx/conf/default.conf.template".format(CONFIGS_PATH),
                "output_file": "default.conf",
                "config_dir": "config/nginx",
                "dst_dir": "/etc/nginx/conf.d",
            },
            "template_file_nginx_init": {
                "template": "{0}/nginx/init/nginx.conf.template".format(CONFIGS_PATH),
                "config_dir": "config/nginx",
                "output_file": "nginx.conf",
                "dst_dir": "/etc/init",
            },
            "template_file_riemann": {
                "template": "{0}/riemann/init/riemann.conf.template".format(CONFIGS_PATH),
                "config_dir": "config/riemann/init",
                "dst_dir": "/etc/init/riemann.conf",
            },
            "template_file_rabbitmq": {
                "template": "{0}/rabbitmq/init/rabbitmq-server.conf.template".format(CONFIGS_PATH),
                "config_dir": "config/rabbitmq",
                "dst_dir": "/etc/init/rabbitmq-server.conf",
            },
        }
    },
    "cloudify-ui": {
        "name": "cloudify-ui",
        "version": "1.0.0",
        "depends": [
            'nodejs'
        ],
        "package_path": "/cloudify",
        "sources_path": "{0}/cloudify-ui".format(PACKAGES_PATH),
        "src_package_type": "dir",
        "dst_package_type": ["deb"],
        "bootstrap_script": "{0}/cloudify-ui-bootstrap.sh".format(SCRIPTS_PATH),
        "bootstrap_template": "cloudify-ui-bootstrap.template",
        "bootstrap_log": "/var/log/cloudify-bootstrap.log",
        "config_templates": {
            "template_file_init": {
                "template": "{0}/cloudify-ui/init/cloudify-ui.conf.template".format(CONFIGS_PATH),
                "output_file": "cloudify-ui.conf",
                "config_dir": "config/init",
                "dst_dir": "/etc/init",
            },
        }
    },
    "cloudify-ubuntu-agent": {
        "name": "cloudify-ubuntu-agent",
        "version": "3.0.0",
        "package_path": "/cloudify",
        "sources_path": "{0}/Ubuntu-agent".format(AGENT_PACKAGES_PATH),
        "src_package_type": "dir",
        "dst_package_types": ["deb", "rpm"],
        "bootstrap_script": "{0}/agent-ubuntu-bootstrap.sh".format(SCRIPTS_PATH),
        "bootstrap_template": "agent-ubuntu-bootstrap.template",
        "bootstrap_params": {
            "file_server_path": "{0}/manager/resources".format(VIRTUALENVS_PATH),
            "dst_agent_location": "packages/agents",
            "dst_template_location": "packages/templates",
            "dst_script_location": "packages/scripts"
        },
        "bootstrap_log": "/var/log/cloudify3-bootstrap.log",
        # TODO: CREATE INIT AND DEFAULTS FILES FROM TEMPLATES!
        "config_templates": {
            "config_dir": {
                "files": "{0}/ubuntu-agent".format(CONFIGS_PATH),
                "config_dir": "config",
                "dst_dir": "{0}/manager/resources/packages/agents/templates/".format(VIRTUALENVS_PATH),
            },
        },
    },
    "cloudify-windows-agent": {
        "name": "cloudify-windows-agent",
        "version": "3.0.0",
        "package_path": "/cloudify",
        "sources_path": "{0}/windows-agent".format(AGENT_PACKAGES_PATH),
        "src_package_type": "dir",
        "dst_package_types": ["deb"],
        "bootstrap_script": "{0}/agent-windows-bootstrap.sh".format(SCRIPTS_PATH),
        "bootstrap_template": "agent-windows-bootstrap.template",
        "bootstrap_params": {
            "file_server_path": "{0}/manager/resources".format(VIRTUALENVS_PATH),
            "dst_agent_location": "packages/agents",
        },
        "bootstrap_log": "/var/log/cloudify3-bootstrap.log",
    },
    "Ubuntu-agent": {
        "name": "Ubuntu-agent",
        "version": "3.0.0",
        "source_urls": [
            "https://github.com/cloudify-cosmo/cloudify-manager/archive/{0}.tar.gz".format(MANAGER_BRANCH),
        ],
        "package_path": "{0}/Ubuntu-agent".format(AGENT_PACKAGES_PATH),
        "sources_path": "/Ubuntu-agent/env",
        "modules": ['billiard==2.7.3.28', 'celery==3.0.24', 'pika',
                    'https://github.com/cloudify-cosmo/cloudify-rest-client/archive/{0}.tar.gz'.format(REST_CLIENT_BRANCH),
                    'https://github.com/cloudify-cosmo/cloudify-plugins-common/archive/{0}.tar.gz'.format(PLUGINS_COMMON_BRANCH),
                    '/Ubuntu-agent/env/cloudify-manager-{0}/plugins/agent-installer/'.format(MANAGER_BRANCH),
                    '/Ubuntu-agent/env/cloudify-manager-{0}/plugins/plugin-installer/'.format(MANAGER_BRANCH),
                    '/Ubuntu-agent/env/cloudify-manager-{0}/plugins/windows-agent-installer/'.format(MANAGER_BRANCH),
                    '/Ubuntu-agent/env/cloudify-manager-{0}/plugins/windows-plugin-installer/'.format(MANAGER_BRANCH),
        ],
        "src_package_type": "dir",
        "dst_package_types": ["tar.gz"],
    },
    "manager": {
        "name": "manager",
        "version": "3.0.0",
        "source_urls": [
            "https://github.com/cloudify-cosmo/cloudify-manager/archive/{0}.tar.gz".format(MANAGER_BRANCH),
        ],
        "package_path": "{0}/manager/".format(CORE_PACKAGES_PATH),
        "sources_path": "{0}/manager".format(VIRTUALENVS_PATH),
        "modules": [
            'https://github.com/cloudify-cosmo/cloudify-dsl-parser/archive/{0}.tar.gz'.format(DSL_PARSER_BRANCH),
            '{0}/manager/cloudify-manager-{1}/rest-service/'.format(VIRTUALENVS_PATH, MANAGER_BRANCH),
        ],
        "resources_path": "{0}/manager/cloudify-manager-{1}/resources/rest-service/cloudify/".format(VIRTUALENVS_PATH, MANAGER_BRANCH),
        "file_server_dir": "{0}/manager/resources".format(VIRTUALENVS_PATH),
        "src_package_type": "dir",
        "dst_package_type": ["deb"],
        "bootstrap_script": "{0}/manager-bootstrap.sh".format(SCRIPTS_PATH),
        "bootstrap_template": "manager-bootstrap.template",
        "bootstrap_params": {
            "resources_dir_src": "cosmo-manager-*/orchestrator/src/main/resources/cloudify/",
            "resources_dir_dst": "filesrv",
            "alias_file_src": "cosmo-manager-*/orchestrator/src/main/resources/org/CloudifySource/cosmo/dsl/alias-mappings.yaml",
            "alias_file_dst": "filesrv/cloudify",
        },
        "config_templates": {
            "#__template_file_init_gunicorn": {
                "template": "{0}/manager/init/manager.conf.template".format(CONFIGS_PATH),
                "output_file": "manager.conf",
                "config_dir": "config/init",
                "dst_dir": "/etc/init",
            },
            "template_file_conf": {
                "template": "{0}/manager/conf/guni.conf.template".format(CONFIGS_PATH),
                "output_file": "guni.conf",
                "config_dir": "config/conf",
                # "dst_dir": "/opt/manager/config/conf",
            },
            "template_dir_init": {
                "templates": "{0}/manager/init".format(CONFIGS_PATH),
                "config_dir": "config/init",
                "dst_dir": "/etc/init",
            },
        }
    },
    "celery": {
        "name": "celery",
        "version": "0.0.1",
        "source_urls": [
            "https://github.com/cloudify-cosmo/cloudify-manager/archive/{0}.tar.gz".format(MANAGER_BRANCH),
        ],
        "package_path": "{0}/celery/".format(CORE_PACKAGES_PATH),
        "sources_path": "{0}/celery/cloudify.management__worker/env".format(VIRTUALENVS_PATH),
        "modules": [
            'billiard==2.7.3.28', 'celery==3.0.24', 'pika',
            'https://github.com/cloudify-cosmo/cloudify-rest-client/archive/{0}.tar.gz'.format(REST_CLIENT_BRANCH),
            'https://github.com/cloudify-cosmo/cloudify-plugins-common/archive/{0}.tar.gz'.format(PLUGINS_COMMON_BRANCH),
            '{0}/celery/cloudify.management__worker/env/cloudify-manager-{1}/plugins/agent-installer/'.format(VIRTUALENVS_PATH, MANAGER_BRANCH),
            '{0}/celery/cloudify.management__worker/env/cloudify-manager-{1}/plugins/plugin-installer/'.format(VIRTUALENVS_PATH, MANAGER_BRANCH),
            '{0}/celery/cloudify.management__worker/env/cloudify-manager-{1}/plugins/riemann-controller/'.format(VIRTUALENVS_PATH, MANAGER_BRANCH),
            '{0}/celery/cloudify.management__worker/env/cloudify-manager-{1}/workflows/'.format(VIRTUALENVS_PATH, MANAGER_BRANCH),
        ],
        "src_package_type": "dir",
        "dst_package_type": ["deb"],
        "bootstrap_script": "{0}/celery-bootstrap.sh".format(SCRIPTS_PATH),
        "bootstrap_template": "celery-bootstrap.template",
        "config_templates": {
            "template_file_init": {
                "template": "{0}/celery/init/celeryd-cloudify-management.conf.template".format(CONFIGS_PATH),
                "output_file": "celeryd-cloudify-management.conf",
                "config_dir": "config/init",
                "dst_dir": "/etc/init",
            },
        }
    },
    "logstash": {
        "name": "logstash",
        "version": "1.3.2",
        "source_urls": [
            "https://download.elasticsearch.org/logstash/logstash/logstash-1.3.2-flatjar.jar",
        ],
        "depends": [
            'openjdk-7-jdk'
        ],
        "package_path": "{0}/logstash/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/logstash".format(PACKAGES_PATH),
        "src_package_type": "dir",
        "dst_package_type": ["deb"],
        "bootstrap_script": "{0}/logstash-bootstrap.sh".format(SCRIPTS_PATH),
        "bootstrap_template": "logstash-bootstrap.template",
        "config_templates": {
            "template_file_init": {
                "template": "{0}/logstash/init/logstash.conf.template".format(CONFIGS_PATH),
                "output_file": "logstash.conf",
                "config_dir": "config/init",
                "dst_dir": "/etc/init",
            },
            "template_file_conf": {
                "template": "{0}/logstash/conf/logstash.conf.template".format(CONFIGS_PATH),
                "output_file": "logstash.conf",
                "config_dir": "config/conf",
                "dst_dir": "/etc",
            },
        }
    },
    "elasticsearch": {
        "name": "elasticsearch",
        "version": "1.0.1",
        "source_urls": [
            "https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.0.1.tar.gz",
        ],
        "depends": [
            'openjdk-7-jdk'
        ],
        "package_path": "{0}/elasticsearch/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/elasticsearch".format(PACKAGES_PATH),
        "src_package_type": "dir",
        "dst_package_type": ["deb"],
        "bootstrap_script": "{0}/elasticsearch-bootstrap.sh".format(SCRIPTS_PATH),
        "bootstrap_template": "elasticsearch-bootstrap.template",
        "config_templates": {
            "template_file_init": {
                "template": "{0}/elasticsearch/init/elasticsearch.conf.template".format(CONFIGS_PATH),
                "output_file": "elasticsearch.conf",
                "config_dir": "config/init",
                "dst_dir": "/etc/init",
            },
            "template_file_conf": {
                "template": "{0}/elasticsearch/init/elasticsearch.conf.template".format(CONFIGS_PATH),
                "output_file": "elasticsearch.conf",
                "config_dir": "config/conf",
                "dst_dir": "/etc/init",
            },
        }
    },
    "kibana3": {
        "name": "kibana3",
        "version": "3.0.0milestone4",
        "source_urls": [
            "https://download.elasticsearch.org/kibana/kibana/kibana-3.0.0milestone4.tar.gz",
        ],
        "depends": [
            'openjdk-7-jdk',
            'logstash',
            'elasticsearch'
        ],
        "package_path": "{0}/kibana3/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/kibana3".format(PACKAGES_PATH),
        "src_package_type": "dir",
        "dst_package_type": ["deb"],
        "bootstrap_script": "{0}/kibana-bootstrap.sh".format(SCRIPTS_PATH),
        "bootstrap_template": "kibana-bootstrap.template",
    },
    "nginx": {
        "name": "nginx",
        "version": "1.5.8",
        "reqs": [
            "nginx"
        ],
        "source_repos": [
            "deb http://nginx.org/packages/mainline/ubuntu/ precise nginx",
            "deb-src http://nginx.org/packages/mainline/ubuntu/ precise nginx",
        ],
        "source_keys": ["http://nginx.org/keys/nginx_signing.key"],
        # "key_files": ["{0}/nginx/nginx_signing.key".format(PACKAGES_PATH)],
        "package_path": "{0}/nginx/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/nginx".format(PACKAGES_PATH),
        "dst_package_type": ["deb"],
    },
    "rabbitmq-server": {
        "name": "rabbitmq-server",
        "version": "0.0.1",
        "source_urls": [
            "http://www.rabbitmq.com/releases/rabbitmq-server/v3.2.4/rabbitmq-server_3.2.4-1_all.deb",
        ],
        "reqs": [
            "erlang-nox",
        ],
        "package_path": "{0}/rabbitmq-server/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/rabbitmq-server".format(PACKAGES_PATH),
        "dst_package_type": ["deb"]
    },
    "langohr": {
        "name": "langohr",
        "version": "2.11.0",
        "source_urls": [
            "https://s3-eu-west-1.amazonaws.com/gigaspaces-repository-eu/langohr/2.11.0/langohr.jar"
        ],
        "package_path": "{0}/riemann/langohr".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/langohr".format(PACKAGES_PATH),
        "src_package_type": "dir",
        "dst_package_type": ["deb"],
    },
    "riemann": {
        "name": "riemann",
        "version": "0.2.6",
        "source_urls": [
            "http://aphyr.com/riemann/riemann_0.2.6_all.deb",
        ],
        "depends": [
            'langohr'
            'openjdk-7-jdk'
        ],
        "package_path": "{0}/riemann/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/riemann".format(PACKAGES_PATH),
        "dst_package_type": ["deb"]
    },
    "nodejs": {
        "name": "nodejs",
        "version": "0.0.1",
        "reqs": [
            "nodejs"
        ],
        "source_ppas": ["ppa:chris-lea/node.js"],
        "package_path": "{0}/nodejs/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/nodejs".format(PACKAGES_PATH),
        "dst_package_type": ["deb"],
        "prereqs": ['python-software-properties', 'g++', 'make']
    },
    "openjdk-7-jdk": {
        "name": "openjdk-7-jdk",
        "version": "0.0.1",
        "reqs": [
            "openjdk-7-jdk"
        ],
        "package_path": "{0}/openjdk-7-jdk/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/openjdk-7-jdk".format(PACKAGES_PATH),
        "dst_package_type": ["deb"],
    },
    "virtualenv": {
        "name": "virtualenv",
        "version": "1.11.4",
        "package_path": "{0}/virtualenv/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/virtualenv".format(PACKAGES_PATH),
        "modules": [
            'virtualenv==1.11.4'
        ],
        "src_package_type": "dir",
        "dst_package_type": ["deb"],
        "bootstrap_script": "{0}/virtualenv-bootstrap.sh".format(SCRIPTS_PATH),
        "bootstrap_template": "virtualenv-bootstrap.template"
    },
    "curl": {
        "name": "curl",
        "version": "0.0.1",
        "reqs": [
            "curl",
            "libcurl3",
        ],
        "package_path": "{0}/curl/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/curl".format(PACKAGES_PATH),
        "dst_package_type": ["deb"],
    },
    "make": {
        "name": "make",
        "version": "0.0.1",
        "reqs": [
            "make"
        ],
        "package_path": "{0}/make/".format(COMPONENT_PACKAGES_PATH),
        "sources_path": "{0}/make".format(PACKAGES_PATH),
        "dst_package_type": ["deb"],
    },
}