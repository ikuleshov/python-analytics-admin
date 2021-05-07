#!/usr/bin/env python

# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Analytics Admin API sample application which prints the Google
Analytics accounts available to the current user.

See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts/list
for more information.
"""
# [START analyticsadmin_accounts_list]
from google.analytics.admin import AnalyticsAdminServiceClient

from accounts_get import print_account


def run_sample():
    """Runs the sample."""
    list_accounts()


def list_accounts():
    """Lists the Google Analytics accounts available to the current user."""
    client = AnalyticsAdminServiceClient()
    results = client.list_accounts()

    print("Result:")
    for account in results:
        print_account(account)


# [END analyticsadmin_accounts_list]


if __name__ == "__main__":
    run_sample()