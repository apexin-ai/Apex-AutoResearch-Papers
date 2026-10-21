import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import json
import torch
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Load type definitions
with open('./configs/few_nerd_types.json') as f:
    types = json.load(f)
print(f"Loaded {len(types)} types")

type_names = sorted(types.keys())

# Load model on CPU
print("Loading intfloat/e5-large-v2 on CPU...")
try:
    model = SentenceTransformer('intfloat/e5-large-v2', device='cpu')
except Exception as e:
    print(f"e5-large-v2 failed: {e}, trying all-MiniLM-L6-v2...")
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device='cpu')

model_name = model[0].auto_model.config._name_or_path
print(f"Model: {model_name}")

# Version A: name + definition
texts_a = [f"Entity type: {name}. Definition: {types[name]}." for name in type_names]
print("Encoding Version A (name+definition)...")
embeddings_a = model.encode(texts_a, normalize_embeddings=True, show_progress_bar=True)

# Version B: name only
texts_b = [f"Entity type: {name}." for name in type_names]
print("Encoding Version B (name only)...")
embeddings_b = model.encode(texts_b, normalize_embeddings=True, show_progress_bar=True)

# Compute similarity matrices
sim_matrix_a = cosine_similarity(embeddings_a)
np.fill_diagonal(sim_matrix_a, 0)
upper_tri_a = sim_matrix_a[np.triu_indices_from(sim_matrix_a, k=1)]

sim_matrix_b = cosine_similarity(embeddings_b)
np.fill_diagonal(sim_matrix_b, 0)
upper_tri_b = sim_matrix_b[np.triu_indices_from(sim_matrix_b, k=1)]

print(f"\n=== BCS Distribution ===")
print(f"Version A (name+def): min={upper_tri_a.min():.4f}, max={upper_tri_a.max():.4f}, mean={upper_tri_a.mean():.4f}, std={upper_tri_a.std():.4f}")
print(f"Version B (name only): min={upper_tri_b.min():.4f}, max={upper_tri_b.max():.4f}, mean={upper_tri_b.mean():.4f}, std={upper_tri_b.std():.4f}")

# Compare with Qwen3
qwen_data = torch.load('./data/type_embeddings.pt', weights_only=True)
qwen_sim = None
if 'similarity_matrix' in qwen_data:
    qwen_sim = qwen_data['similarity_matrix'].numpy()
elif 'embeddings' in qwen_data:
    qwen_emb = qwen_data['embeddings'].numpy()
    qwen_sim = cosine_similarity(qwen_emb)
else:
    keys = list(qwen_data.keys())
    print(f"Qwen data keys: {keys}")
    for k in keys:
        if isinstance(qwen_data[k], torch.Tensor) and qwen_data[k].dim() == 2:
            qwen_emb = qwen_data[k].float().numpy()
            qwen_sim = cosine_similarity(qwen_emb)
            break

if qwen_sim is not None:
    np.fill_diagonal(qwen_sim, 0)
    upper_tri_qwen = qwen_sim[np.triu_indices_from(qwen_sim, k=1)]
    print(f"Qwen3 (mean-pool):    min={upper_tri_qwen.min():.4f}, max={upper_tri_qwen.max():.4f}, mean={upper_tri_qwen.mean():.4f}, std={upper_tri_qwen.std():.4f}")

    print(f"\n=== Comparison Table ===")
    print(f"{'Method':<25} {'Min':>8} {'Max':>8} {'Mean':>8} {'Std':>8} {'Range':>8}")
    print(f"{'-'*25} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*8}")
    for label, tri in [
        ("Qwen3 mean-pool", upper_tri_qwen),
        ("E5 name+definition", upper_tri_a),
        ("E5 name-only", upper_tri_b),
    ]:
        print(f"{label:<25} {tri.min():>8.4f} {tri.max():>8.4f} {tri.mean():>8.4f} {tri.std():>8.4f} {tri.max()-tri.min():>8.4f}")
else:
    print("WARNING: Could not load Qwen3 similarity data")

# Heatmaps
for version, sim_matrix, label in [
    ('a_name_def', sim_matrix_a, 'E5-large-v2 (name+definition)'),
    ('b_name_only', sim_matrix_b, 'E5-large-v2 (name only)'),
]:
    fig, ax = plt.subplots(figsize=(20, 18))
    sns.heatmap(sim_matrix, xticklabels=type_names, yticklabels=type_names,
                cmap='RdYlBu_r', vmin=-0.1, vmax=1.0, ax=ax,
                square=True, linewidths=0.1)
    ax.set_title(f'Pairwise Cosine Similarity - {label}', fontsize=14)
    plt.xticks(rotation=90, fontsize=5)
    plt.yticks(fontsize=5)
    plt.tight_layout()
    path = f'./data/heatmap_e5_{version}.pdf'
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'Saved: {path}')

# Save embeddings
torch.save({
    'type_names': type_names,
    'embeddings_a': torch.tensor(embeddings_a),
    'embeddings_b': torch.tensor(embeddings_b),
    'sim_matrix_a': torch.tensor(sim_matrix_a),
    'sim_matrix_b': torch.tensor(sim_matrix_b),
    'model_name': model_name,
}, './data/type_embeddings_e5.pt')
print('Saved: ./data/type_embeddings_e5.pt')

print("\nDONE")
