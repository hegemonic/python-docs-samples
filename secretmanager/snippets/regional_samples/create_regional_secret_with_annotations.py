#!/usr/bin/env python

# Copyright 2024 Google LLC
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
"""
command line application and sample code for creating a new secret with
annotations.
"""

# [START secretmanager_create_regional_secret_with_annotations]
import argparse
import typing

# Import the Secret Manager client library.
from google.cloud import secretmanager_v1


def create_regional_secret_with_annotations(
    project_id: str,
    location_id: str,
    secret_id: str,
    annotations: typing.Dict[str, str],
) -> secretmanager_v1.Secret:
    """
    Create a new secret with the given name. A secret is a logical wrapper
    around a collection of secret versions. Secret versions hold the actual
    secret material.
    """

    # Endpoint to call the regional secret manager sever
    api_endpoint = f"secretmanager.{location_id}.rep.googleapis.com"

    # Create the Secret Manager client.
    client = secretmanager_v1.SecretManagerServiceClient(
        client_options={"api_endpoint": api_endpoint},
    )

    # Build the resource name of the parent project.
    parent = f"projects/{project_id}/locations/{location_id}"

    # Create the secret.
    response = client.create_secret(
        request={
            "parent": parent,
            "secret_id": secret_id,
            "secret": {"annotations": annotations},
        }
    )

    # Print the new secret name.
    print(f"Created secret: {response.name}")

    return response


# [END secretmanager_create_regional_secret_with_annotations]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("project_id", help="id of the GCP project")
    parser.add_argument(
        "location_id", help="id of the location where secret is to be created"
    )
    parser.add_argument("secret_id", help="id of the secret to create")
    parser.add_argument("annotation_key", help="key of the annotation you want to add")
    parser.add_argument(
        "annotation_value", help="value of the annotation you want to add"
    )
    args = parser.parse_args()

    annotations = {args.annotation_key, args.annotation_value}
    create_regional_secret_with_annotations(
        args.project_id, args.location_id, args.secret_id, annotations
    )
