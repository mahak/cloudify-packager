# flake8: NOQA

# user configuration (OPTIONAL)
MAIN_BRANCH = 'master'  # branch to use when retrieving resources
MANAGER_BRANCH = MAIN_BRANCH
REST_CLIENT_BRANCH = MAIN_BRANCH
PLUGINS_COMMON_BRANCH = MAIN_BRANCH
DSL_PARSER_BRANCH = MAIN_BRANCH

PACKAGES_PATH = "/packages"  # temporary directory to which items are downloaded and in which packages are created.
VIRTUALENVS_PATH = "/opt"  # directory for cosmo modules and virtual environments
CLOUDIFY_LOGS_PATH = "/var/log/cloudify"  # directory for cloudify logs
AGENT_VIRTUALENVS_PATH = "/env"  # final directory to put the created packages in.
COMPONENT_PACKAGES_PATH = "/cloudify-components"  # where to put 3rd party components packages
CORE_PACKAGES_PATH = "/cloudify-core"  # where to put code package
UI_PACKAGE_PATH = "/agents"  # where to put the ui package
AGENT_PACKAGES_PATH = "/agents"  # where to put agent packages
SCRIPTS_PATH = "package-scripts"  # directory for bootstrap/download/removal/package scripts - if applicable
CONFIGS_PATH = "package-configuration"  # directory for configuration files and templates - if applicable
