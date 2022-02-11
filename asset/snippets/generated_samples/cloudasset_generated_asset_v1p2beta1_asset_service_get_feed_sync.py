# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for GetFeed
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-asset


# [START cloudasset_generated_asset_v1p2beta1_AssetService_GetFeed_sync]
from google.cloud import asset_v1p2beta1


def sample_get_feed():
    # Create a client
    client = asset_v1p2beta1.AssetServiceClient()

    # Initialize request argument(s)
    request = asset_v1p2beta1.GetFeedRequest(
        name="name_value",
    )

    # Make the request
    response = client.get_feed(request=request)

    # Handle the response
    print(response)

# [END cloudasset_generated_asset_v1p2beta1_AssetService_GetFeed_sync]