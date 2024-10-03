# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import snippets_create_client_v2

def test_create_client_with_endpoint():
    clients = snippets_create_client_v2.create_client_with_endpoint("securitycenter.me-central2.rep.googleapis.com")
    assert len(clients.keys()) == 2
    assert "securitycenter.googleapis.com" in clients.keys()
    assert "securitycenter.me-central2.rep.googleapis.com" in clients.keys()
