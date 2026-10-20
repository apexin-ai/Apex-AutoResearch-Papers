import sys

def patch_tied_weights(model_cls, source_key):
    twk = getattr(model_cls, '_tied_weights_keys', None)
    if isinstance(twk, list):
        model_cls._tied_weights_keys = {k: source_key for k in twk}

from transformers import AutoConfig, AutoModelForCausalLM

model_registry = {
    'delta_net': ('fla.models.delta_net', 'DeltaNetConfig', 'DeltaNetForCausalLM', 'model.embeddings.weight'),
    'hgrn': ('fla.models.hgrn', 'HGRNConfig', 'HGRNForCausalLM', 'model.embeddings.weight'),
    'hgrn2': ('fla.models.hgrn2', 'HGRN2Config', 'HGRN2ForCausalLM', 'model.embeddings.weight'),
    'gated_deltanet': ('fla.models.gated_deltanet', 'GatedDeltaNetConfig', 'GatedDeltaNetForCausalLM', 'model.embeddings.weight'),
    'retnet': ('fla.models.retnet', 'RetNetConfig', 'RetNetForCausalLM', 'model.embeddings.weight'),
    'gla': ('fla.models.gla', 'GLAConfig', 'GLAForCausalLM', 'model.embeddings.weight'),
    'rwkv6': ('fla.models.rwkv6', 'RWKV6Config', 'RWKV6ForCausalLM', 'model.embeddings.weight'),
}

for model_type, (module_path, config_name, model_name, embed_key) in model_registry.items():
    try:
        mod = __import__(module_path, fromlist=[config_name, model_name])
        config_cls = getattr(mod, config_name)
        model_cls = getattr(mod, model_name)
        patch_tied_weights(model_cls, embed_key)
        try:
            AutoConfig.register(model_type, config_cls)
            AutoModelForCausalLM.register(config_cls, model_cls)
        except ValueError:
            pass
    except (ImportError, AttributeError) as e:
        print(f'Warning: could not register {model_type}: {e}', file=sys.stderr)

if __name__ == '__main__':
    from lm_eval.__main__ import cli_evaluate
    cli_evaluate()
