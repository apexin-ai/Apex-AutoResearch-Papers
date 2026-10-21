#!/usr/bin/env python3
"""Compute Qwen3-32B mean-pooled embeddings for MAVEN 168 event types."""
import torch, json, sys, os
os.chdir(".")

from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "~/.cache/huggingface/qwen3-32b-fp8/"
print("Loading tokenizer...", flush=True)
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
print("Loading model...", flush=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path, device_map="cuda:0",
    torch_dtype=torch.bfloat16, trust_remote_code=True
)
model.eval()
print("Model loaded.", flush=True)

# Get MAVEN types
import pandas as pd
df = pd.read_parquet("data/maven_parquet/valid.parquet")
types = set()
for ents in df['entities']:
    if ents is None:
        continue
    lst = json.loads(ents) if isinstance(ents, str) else ents
    if lst is None:
        continue
    for e in lst:
        types.add(e['type'])
type_names = sorted(types)
print(f"Computing embeddings for {len(type_names)} types...", flush=True)

embeddings = {}
for i, name in enumerate(type_names):
    inputs = tokenizer(name, return_tensors="pt", padding=True, truncation=True).to("cuda:0")
    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)
        hidden = outputs.hidden_states[-1]
        mask = inputs["attention_mask"].unsqueeze(-1)
        emb = (hidden * mask).sum(dim=1) / mask.sum(dim=1)
        emb = emb.squeeze().cpu()
    embeddings[name] = emb
    if (i+1) % 20 == 0:
        print(f"  {i+1}/{len(type_names)}", flush=True)

print(f"All {len(type_names)} done. dim={emb.shape[0]}, dtype={emb.dtype}", flush=True)

# Save embeddings (keep bfloat16 to match Few-NERD)
torch.save(embeddings, "artifacts/maven_type_embeddings_qwen3.pt")
print(f"Saved embeddings to artifacts/maven_type_embeddings_qwen3.pt", flush=True)

# Compute BCS matrix
import torch.nn.functional as F
E = torch.stack([embeddings[n] for n in type_names]).float()
E_norm = F.normalize(E, dim=1)
sim = E_norm @ E_norm.T
mask_tri = torch.triu(torch.ones_like(sim), diagonal=1).bool()
vals = sim[mask_tri]
print(f"BCS stats: mean={vals.mean():.4f}, std={vals.std():.4f}, min={vals.min():.4f}, max={vals.max():.4f}")
torch.save({"similarity_matrix": sim, "type_names": type_names}, "artifacts/maven_bcs_matrix_qwen3.pt")
print("Saved BCS matrix to artifacts/maven_bcs_matrix_qwen3.pt")
