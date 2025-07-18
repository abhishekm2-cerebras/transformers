# Copyright 2022 EleutherAI and The HuggingFace Inc. team. All rights reserved.
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
from typing import TYPE_CHECKING

from ...utils import (
    OptionalDependencyNotAvailable,
    _LazyModule,
    is_flax_available,
    is_sentencepiece_available,
    is_tokenizers_available,
    is_torch_available,
)


_import_structure = {
    "configuration_jais_plus": ["JaisPlusConfig"],
}

try:
    if not is_sentencepiece_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["tokenization_jais_plus"] = ["JaisPlusTokenizer"]

try:
    if not is_tokenizers_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["tokenization_jais_plus_fast"] = ["JaisPlusTokenizerFast"]

try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_jais_plus"] = [
        "JaisPlusForCausalLM",
        "JaisPlusModel",
        "JaisPlusPreTrainedModel",
        "JaisPlusForSequenceClassification",
        "JaisPlusForQuestionAnswering",
        "JaisPlusForTokenClassification",
    ]

try:
    if not is_flax_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_flax_jais_plus"] = ["FlaxJaisPlusForCausalLM", "FlaxJaisPlusModel", "FlaxJaisPlusPreTrainedModel"]


if TYPE_CHECKING:
    from .configuration_jais_plus import JaisPlusConfig

    try:
        if not is_sentencepiece_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .tokenization_jais_plus import JaisPlusTokenizer

    try:
        if not is_tokenizers_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .tokenization_jais_plus_fast import JaisPlusTokenizerFast

    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_jais_plus import (
            JaisPlusForCausalLM,
            JaisPlusForQuestionAnswering,
            JaisPlusForSequenceClassification,
            JaisPlusForTokenClassification,
            JaisPlusModel,
            JaisPlusPreTrainedModel,
        )

    try:
        if not is_flax_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_flax_jais_plus import FlaxJaisPlusForCausalLM, FlaxJaisPlusModel, FlaxJaisPlusPreTrainedModel


else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)
