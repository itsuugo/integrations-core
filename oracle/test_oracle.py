# (C) Datadog, Inc. 2010-2016
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

# stdlib
import logging

# 3p
from nose.plugins.attrib import attr

# project
from tests.checks.common import AgentCheckTest

logging.basicConfig()

"""
Using the "system" user as permission granting not available
for default "system" user

Set up Oracle instant client:
http://jasonstitt.com/cx_oracle_on_os_x

Set:
export ORACLE_HOME=/opt/oracle/instantclient_12_1/
export DYLD_LIBRARY_PATH="$ORACLE_HOME:$DYLD_LIBRARY_PATH"
"""

CONFIG = {
    'init_config': {},
    'instances': [{
        'server': 'localhost:1521',
        'user': 'system',
        'password': 'oracle',
        'service_name': 'xe',
    }]
}

SERVICE_CHECK_NAME = 'oracle.can_connect'
METRICS = [
    'oracle.buffer_cachehit_ratio',
    'oracle.cursor_cachehit_ratio',
    'oracle.library_cachehit_ratio',
    'oracle.shared_pool_free',
    'oracle.physical_reads',
    'oracle.physical_writes',
    'oracle.enqueue_timeouts',
    'oracle.gc_cr_receive_time',
    'oracle.cache_blocks_corrupt',
    'oracle.cache_blocks_lost',
    'oracle.logons',
    'oracle.active_sessions',
    'oracle.long_table_scans',
    'oracle.service_response_time',
    'oracle.user_rollbacks',
    'oracle.sorts_per_user_call',
    'oracle.rows_per_sort',
    'oracle.disk_sorts',
    'oracle.memroy_sorts_ratio',
    'oracle.database_wait_time_ratio',
    'oracle.enqueue_timeouts',
    'oracle.session_limit_usage',
    'oracle.session_count',
    'oracle.temp_space_used',
]

@attr(requires='oracle')
class TestOracle(AgentCheckTest):
    """Basic Test for oracle integration."""
    CHECK_NAME = 'oracle'

    def testOracle(self):
        self.run_check_twice(CONFIG)

        for m in METRICS:
            self.assertMetric(m, at_least=1)

        self.assertServiceCheck(SERVICE_CHECK_NAME)
        self.coverage_report()