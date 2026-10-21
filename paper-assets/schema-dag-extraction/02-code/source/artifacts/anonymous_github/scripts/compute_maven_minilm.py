#!/usr/bin/env python3
"""Compute MiniLM embeddings and cosine similarity matrix for MAVEN event types."""
import os
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_DISABLE_XET"] = "1"

import json
import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer

MODEL_PATH = "~/.cache/huggingface/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/c9745ed1d9f207416be6d2e6f8de32d1f16199bf"
TYPES_FILE = "./configs/maven_event_types.json"
EMB_OUT = "./artifacts/maven_minilm_embeddings.pt"
SIM_OUT = "./artifacts/maven_minilm_sim_matrix.pt"

with open(TYPES_FILE) as f:
    type_defs = json.load(f)

type_keys = sorted(type_defs.keys())
type_display_names = [type_defs[k] for k in type_keys]
print(f"Types: {len(type_keys)}")

model = SentenceTransformer(MODEL_PATH)
embeddings_np = model.encode(type_display_names, show_progress_bar=False)
embeddings_tensor = torch.tensor(embeddings_np, dtype=torch.float32)
print(f"Embeddings shape: {embeddings_tensor.shape}")

normed = F.normalize(embeddings_tensor, dim=1)
sim_matrix = normed @ normed.T
print(f"Sim matrix shape: {sim_matrix.shape}")

mask = torch.triu(torch.ones_like(sim_matrix, dtype=torch.bool), diagonal=1)
upper = sim_matrix[mask]
print(f"Sim stats - mean: {upper.mean():.4f}, std: {upper.std():.4f}, min: {upper.min():.4f}, max: {upper.max():.4f}")

emb_dict = {name: embeddings_tensor[i] for i, name in enumerate(type_keys)}
torch.save(emb_dict, EMB_OUT)
print(f"Saved embeddings to {EMB_OUT}")

sim_data = {"similarity_matrix": sim_matrix, "type_names": type_keys}
torch.save(sim_data, SIM_OUT)
print(f"Saved sim matrix to {SIM_OUT}")

loaded = torch.load(SIM_OUT, map_location="cpu", weights_only=True)
print(f"Validation: keys={list(loaded.keys())}, shape={loaded['similarity_matrix'].shape}, n_types={len(loaded['type_names'])}")
print("DONE")
