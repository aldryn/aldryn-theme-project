#!/usr/bin/env python
import sys
import os
from django.core.management import ManagementUtility

try:
    config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'newrelic.ini')
    environment = os.environ['USER']

    import newrelic.agent
    newrelic.agent.initialize(config_file, environment)

except ImportError:
    sys.stderr.write("Couldn't import new relic, skipping New Relic initialization")  # not installed

except KeyError:
    sys.stderr.write("Could not get username from environment, skipping New Relic initialization")  # not on a standard server setup

except newrelic.api.exceptions.ConfigurationError:
    sys.stderr.write("Could not load newrelic.ini configuration file, skipping New Relic initialization")  # config file not found

if __name__ == "__main__":
    utility = ManagementUtility(None)
    utility.execute()
