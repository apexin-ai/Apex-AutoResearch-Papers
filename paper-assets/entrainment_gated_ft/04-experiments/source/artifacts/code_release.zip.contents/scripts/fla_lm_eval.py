"""Wrapper: register fla model types with transformers and patch compatibility, then run lm_eval CLI."""
from transformers import AutoConfig, AutoModelForCausalLM

from fla.models.gla import GLAConfig, GLAForCausalLM
from fla.models.delta_net import DeltaNetConfig, DeltaNetForCausalLM
from fla.models.hgrn import HGRNConfig, HGRNForCausalLM
from fla.models.gated_deltanet import GatedDeltaNetConfig, GatedDeltaNetForCausalLM
from fla.models.hgrn2 import HGRN2Config, HGRN2ForCausalLM
from fla.models.retnet import RetNetConfig, RetNetForCausalLM

for model_type, config_cls, model_cls in [
    ("gla", GLAConfig, GLAForCausalLM),
    ("delta_net", DeltaNetConfig, DeltaNetForCausalLM),
    ("hgrn", HGRNConfig, HGRNForCausalLM),
    ("gated_deltanet", GatedDeltaNetConfig, GatedDeltaNetForCausalLM),
    ("hgrn2", HGRN2Config, HGRN2ForCausalLM),
    ("retnet", RetNetConfig, RetNetForCausalLM),
]:
    AutoConfig.register(model_type, config_cls)
    AutoModelForCausalLM.register(config_cls, model_cls)

# Patch: fla 0.5.0 uses list for _tied_weights_keys, transformers 5.x expects dict
import transformers.modeling_utils as _mu
_orig_get_expanded = _mu.PreTrainedModel.get_expanded_tied_weights_keys

def _patched_get_expanded(self, all_submodels=False):
    tied = getattr(self, "_tied_weights_keys", None)
    if isinstance(tied, list):
        # Convert list to dict format: key -> source via _get_tied_param_mapping
        if tied and hasattr(self, "get_input_embeddings") and hasattr(self, "get_output_embeddings"):
            ie = self.get_input_embeddings()
            oe = self.get_output_embeddings()
            if ie is not None and oe is not None and ie.weight.data_ptr() == oe.weight.data_ptr():
                # Find param names
                ie_name = oe_name = None
                for name, param in self.named_parameters():
                    if param.data_ptr() == ie.weight.data_ptr():
                        if "embed" in name:
                            ie_name = name
                        elif "lm_head" in name or "output" in name:
                            oe_name = name
                if ie_name and oe_name:
                    self._tied_weights_keys = {oe_name: ie_name}
                else:
                    self._tied_weights_keys = {}
            else:
                self._tied_weights_keys = {}
        else:
            self._tied_weights_keys = {}
    return _orig_get_expanded(self, all_submodels=all_submodels)

_mu.PreTrainedModel.get_expanded_tied_weights_keys = _patched_get_expanded

from lm_eval.__main__ import cli_evaluate
cli_evaluate()
