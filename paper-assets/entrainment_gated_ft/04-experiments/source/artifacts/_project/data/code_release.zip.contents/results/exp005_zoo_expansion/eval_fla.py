import json
import sys
import os
import torch

arch_name = sys.argv[3]
model_path = sys.argv[1]
output_dir = sys.argv[2]

print(f"EVAL {arch_name} START")
os.makedirs(output_dir, exist_ok=True)

# Load model directly with fla, bypassing AutoModel
arch_map = {
    'GLA': ('fla.models.gla', 'GLAForCausalLM'),
    'DeltaNet': ('fla.models.delta_net', 'DeltaNetForCausalLM'),
    'HGRN': ('fla.models.hgrn', 'HGRNForCausalLM'),
}

import importlib
mod_name, cls_name = arch_map[arch_name]
mod = importlib.import_module(mod_name)
ModelClass = getattr(mod, cls_name)

# Patch _tied_weights_keys to empty dict to avoid transformers 5.x compat issues
ModelClass._tied_weights_keys = {}

model = ModelClass.from_pretrained(model_path, torch_dtype=torch.float32)
model = model.to('cuda:0')

# Manually tie lm_head to embeddings if needed
if hasattr(model, 'lm_head') and hasattr(model, 'model') and hasattr(model.model, 'embeddings'):
    model.lm_head.weight = model.model.embeddings.weight

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

import lm_eval
from lm_eval.models.huggingface import HFLM

lm = HFLM(pretrained=model, tokenizer=tokenizer, batch_size='auto')

results = lm_eval.simple_evaluate(
    model=lm,
    tasks=['lambada_openai', 'arc_easy'],
    log_samples=True,
)

with open(os.path.join(output_dir, 'results.json'), 'w') as f:
    json.dump(results['results'], f, indent=2, default=str)

for task, res in results['results'].items():
    metrics = {k: v for k, v in res.items() if isinstance(v, (int, float))}
    print(f"  {task}: {metrics}")

print(f"EVAL {arch_name} DONE")
