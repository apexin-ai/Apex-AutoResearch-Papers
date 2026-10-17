#!/bin/bash
# Compute Qwen3-32B embeddings for FewRel 80 relations + similarity matrix.
# GPU required (~2min on A6000/4090). Do not run on CPU.
set -e

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/schema-dag-extraction

MODEL_PATH="/root/autodl-tmp/.hf_cache/qwen3-32b-fp8"
TYPES_FILE="configs/fewrel_relation_types.json"
EMB_OUTPUT="artifacts/fewrel_qwen3_embeddings.pt"
SIM_OUTPUT="artifacts/fewrel_qwen3_sim_matrix.pt"

echo "=== Step 1: Compute Qwen3 embeddings for 80 FewRel relations ==="
python3 src/compute_type_embeddings.py \
    --types "$TYPES_FILE" \
    --model "$MODEL_PATH" \
    --output "$EMB_OUTPUT" \
    --batch-size 8 \
    --dtype bfloat16

echo "=== Step 2: Compute cosine similarity matrix ==="
python3 -c "
import torch
import torch.nn.functional as F

data = torch.load('$EMB_OUTPUT', map_location='cpu', weights_only=True)
type_names = sorted(data.keys())
embeddings = torch.stack([data[name] for name in type_names]).float()
normed = F.normalize(embeddings, dim=1)
sim_matrix = normed @ normed.T

torch.save({'sim_matrix': sim_matrix, 'type_names': type_names}, '$SIM_OUTPUT')
print(f'Saved sim_matrix {sim_matrix.shape} with {len(type_names)} types to $SIM_OUTPUT')

upper = sim_matrix[torch.triu(torch.ones_like(sim_matrix, dtype=torch.bool), diagonal=1)]
print(f'Similarity stats: mean={upper.mean():.4f}, std={upper.std():.4f}, '
      f'min={upper.min():.4f}, max={upper.max():.4f}')
"

echo "=== Done ==="
echo "Embeddings: $EMB_OUTPUT"
echo "Sim matrix: $SIM_OUTPUT"
