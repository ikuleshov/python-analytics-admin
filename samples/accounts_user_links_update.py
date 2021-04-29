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

"""Google Analytics Admin API sample application which updates the account
user link.

See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts.userLinks/update
for more information.
"""
# [START analyticsadmin_accounts_user_links_update]
from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics.admin_v1alpha.types import UserLink

from accounts_user_links_get import print_user_link


def run_sample():
    """Runs the sample."""

    # !!! ATTENTION !!!
    #  Running this sample may change/delete your Google Analytics account
    #  configuration. Make sure to not use the Google Analytics property ID from
    #  your production environment below.

    # TODO(developer): Replace this variable with your Google Analytics
    #  account ID (e.g. "123456") before running the sample.
    account_id = "YOUR-GA-ACCOUNT-ID"

    # TODO(developer): Replace this variable with your Google Analytics
    #  account user link ID (e.g. "123456") before running the sample.
    account_user_link_id = "YOUR-ACCOUNT-USER-LINK-ID"

    update_account_user_link(account_id, account_user_link_id)


def update_account_user_link(account_id, account_user_link_id):
    """Updates the account user link."""
    client = AnalyticsAdminServiceClient()
    # This call updates the email address and direct roles of the user link.
    # The user link to update is specified in the `name` field of the `UserLink`
    # instance.
    user_link = client.update_user_link(
        user_link=UserLink(
            name=f"accounts/{account_id}/userLinks/{account_user_link_id}",
            direct_roles=["predefinedRoles/collaborate"],
        ),
    )

    print("Result:")
    print_user_link(user_link)


# [END analyticsadmin_accounts_user_links_update]


if __name__ == "__main__":
    run_sample()
