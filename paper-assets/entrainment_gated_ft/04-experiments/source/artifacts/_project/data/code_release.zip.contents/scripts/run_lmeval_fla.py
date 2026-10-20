#!/usr/bin/env python3
import functools
from transformers import AutoModelForCausalLM, AutoConfig

try:
    from fla.models.gated_deltanet import GatedDeltaNetConfig, GatedDeltaNetForCausalLM
    AutoConfig.register('gated_deltanet', GatedDeltaNetConfig)
    AutoModelForCausalLM.register(GatedDeltaNetConfig, GatedDeltaNetForCausalLM)
except (ImportError, ValueError):
    pass
try:
    from fla.models.hgrn2 import HGRN2Config, HGRN2ForCausalLM
    AutoConfig.register('hgrn2', HGRN2Config)
    AutoModelForCausalLM.register(HGRN2Config, HGRN2ForCausalLM)
except (ImportError, ValueError):
    pass
try:
    from fla.models.retnet import RetNetConfig, RetNetForCausalLM
    AutoConfig.register('retnet', RetNetConfig)
    AutoModelForCausalLM.register(RetNetConfig, RetNetForCausalLM)
except (ImportError, ValueError):
    pass

_orig = AutoModelForCausalLM.from_pretrained

@functools.wraps(_orig)
def _patched(*a, **kw):
    m = _orig(*a, **kw)
    cfg = getattr(m, 'config', None)
    if cfg and getattr(cfg, 'tie_word_embeddings', False):
        if hasattr(m, 'lm_head') and hasattr(m, 'model'):
            emb = getattr(m.model, 'embeddings', None) or getattr(m.model, 'embed_tokens', None)
            if emb is not None:
                m.lm_head.weight = emb.weight
                print(f"Weight tying: applied for {type(m).__name__}")
    else:
        print(f"Weight tying: SKIPPED (tie_word_embeddings={getattr(cfg, 'tie_word_embeddings', 'N/A')})")
    return m

AutoModelForCausalLM.from_pretrained = _patched

from lm_eval.__main__ import cli_evaluate
cli_evaluate()
