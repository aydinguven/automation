from awxkit import api, config, utils, cli
from awxkit.api import ApiV2, job_templates
from awxkit.api.resources import resources

USERNAME = "admin"
PASSWORD = ""
BASEURL = "https://0.0.0.0"
LIMIT = "vm1,vm2,vm3,vm4"
TEMPLATE = "Template Name on Controller"


config.base_url = BASEURL
config.credentials = utils.PseudoNamespace({'default': {'username': USERNAME, 'password': PASSWORD}})
# Loads the credentials to a session
awx = ApiV2()
session_connection = awx.load_session().get()

# Initialize the session
session_connection.get(resources)

# Find the template by it's name
template_by_name = awx.job_templates.get(name=TEMPLATE).results[0]

template_by_name.limit = LIMIT
launch = template_by_name.launch()
