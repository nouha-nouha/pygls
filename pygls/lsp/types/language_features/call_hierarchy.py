############################################################################
# Original work Copyright 2017 Palantir Technologies, Inc.                 #
# Original work licensed under the MIT License.                            #
# See ThirdPartyNotices.txt in the project root for license information.   #
# All modifications Copyright (c) Open Law Library. All rights reserved.   #
#                                                                          #
# Licensed under the Apache License, Version 2.0 (the "License")           #
# you may not use this file except in compliance with the License.         #
# You may obtain a copy of the License at                                  #
#                                                                          #
#     http: // www.apache.org/licenses/LICENSE-2.0                         #
#                                                                          #
# Unless required by applicable law or agreed to in writing, software      #
# distributed under the License is distributed on an "AS IS" BASIS,        #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
# See the License for the specific language governing permissions and      #
# limitations under the License.                                           #
############################################################################
"""This module contains Language Server Protocol types
https://microsoft.github.io/language-server-protocol/specification

-- Language Features - Call Hierarchy --

Class attributes are named with camel-case notation because client is expecting
that.
"""
from typing import Any, List, Optional

from pygls.lsp.types.basic_structures import (Model, PartialResultParams, Range,
                                              StaticRegistrationOptions,
                                              TextDocumentPositionParams,
                                              TextDocumentRegistrationOptions,
                                              WorkDoneProgressOptions, WorkDoneProgressParams)
from pygls.lsp.types.language_features.document_symbol import SymbolKind, SymbolTag


class CallHierarchyClientCapabilities(Model):
    dynamic_registration: Optional[bool] = False


class CallHierarchyOptions(WorkDoneProgressOptions):
    pass


class CallHierarchyRegistrationOptions(TextDocumentRegistrationOptions, CallHierarchyOptions, StaticRegistrationOptions):
    pass


class CallHierarchyPrepareParams(TextDocumentPositionParams, WorkDoneProgressParams):
    pass


class CallHierarchyItem(Model):
    name: str
    kind: SymbolKind
    uri: str
    range: Range
    selection_range: Range
    tags: Optional[List[SymbolTag]] = None
    detail: Optional[str] = None
    data: Optional[Any] = None


class CallHierarchyIncomingCallsParams(WorkDoneProgressParams, PartialResultParams):
    item: CallHierarchyItem


class CallHierarchyIncomingCall(Model):
    from_: CallHierarchyItem
    from_ranges: List[Range]


class CallHierarchyOutgoingCallsParams(WorkDoneProgressParams, PartialResultParams):
    item: CallHierarchyItem


class CallHierarchyOutgoingCall(Model):
    to: CallHierarchyItem
    from_ranges: List[Range]
