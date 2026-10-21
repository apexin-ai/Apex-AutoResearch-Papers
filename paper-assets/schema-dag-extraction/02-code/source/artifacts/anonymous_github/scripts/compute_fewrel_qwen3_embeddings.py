#!/usr/bin/env python3
"""Compute Qwen3-32B mean-pooled embeddings for FewRel 80 relation types."""
import torch, json, os
os.chdir(".")

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch.nn.functional as F

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

# Load FewRel relation types
with open("configs/fewrel_relation_types.json") as f:
    rel_types = json.load(f)

type_names = sorted(rel_types.keys())
print(f"Computing embeddings for {len(type_names)} relation types...", flush=True)

embeddings = {}
for i, pid in enumerate(type_names):
    name = rel_types[pid]
    text = f"Relation type: {name} ({pid})"
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to("cuda:0")
    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)
        hidden = outputs.hidden_states[-1]
        mask = inputs["attention_mask"].unsqueeze(-1)
        emb = (hidden * mask).sum(dim=1) / mask.sum(dim=1)
        emb = emb.squeeze().cpu()
    embeddings[pid] = emb
    if (i+1) % 20 == 0:
        print(f"  {i+1}/{len(type_names)}", flush=True)

print(f"All {len(type_names)} done. dim={emb.shape[0]}, dtype={emb.dtype}", flush=True)

# Save embeddings
torch.save(embeddings, "artifacts/fewrel_qwen3_embeddings.pt")
print("Saved artifacts/fewrel_qwen3_embeddings.pt", flush=True)

# Compute similarity matrix
E = torch.stack([embeddings[n] for n in type_names]).float()
E_norm = F.normalize(E, dim=1)
sim = E_norm @ E_norm.T
torch.save({"similarity_matrix": sim, "type_names": type_names, "relation_labels": {pid: rel_types[pid] for pid in type_names}}, "artifacts/fewrel_qwen3_sim_matrix.pt")

mask_tri = torch.triu(torch.ones_like(sim), diagonal=1).bool()
vals = sim[mask_tri]
print(f"SimMatrix shape: {sim.shape}")
print(f"BCS stats: mean={vals.mean():.4f}, std={vals.std():.4f}, min={vals.min():.4f}, max={vals.max():.4f}")
print("Saved artifacts/fewrel_qwen3_sim_matrix.pt", flush=True)
