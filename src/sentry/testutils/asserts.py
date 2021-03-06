"""
sentry.testutils.asserts
~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""


def assert_date_resembles(one, two):
    # this is mostly intended to handle discrepencies between mysql/postgres
    assert one.replace(microsecond=0) == two.replace(microsecond=0)
