Semantic Ablation Multi-Model Results

Location: cqa1-22115:/root/autodl-tmp/gen-depth-contamination/artifacts/semantic_ablation_multi_model.json

## Pythia-1.4B (retrain-chain data)
| Pair | 15D AUC | 17D AUC | Diff |
|------|---------|---------|------|
| 0v1 | 0.9859 | 0.9865 | +0.0006 |
| 1v2 | 0.9497 | 0.9503 | +0.0006 |
| 2v3 | 0.8915 | 0.8921 | +0.0006 |
| 3v4 | 0.8038 | 0.8041 | +0.0003 |
K* = > max_depth (both). semantic_cosine_sim rank=15/17, entity_diversity rank=16/17.

## Qwen-cont
| Pair | 15D AUC | 17D AUC | Diff |
|------|---------|---------|------|
| 0v1 | 0.9919 | 0.9921 | +0.0002 |
| 1v2 | 0.6324 | 0.6299 | -0.0025 |
| 2v3 | 0.5644 | 0.5666 | +0.0022 |
| 3v4 | 0.5457 | 0.5476 | +0.0019 |
| 4v5 | 0.5289 | 0.5282 | -0.0007 |
K* = 2 (both). semantic_cosine_sim rank=11/17, entity_diversity rank=17/17.

## Cross-Model Summary (3 models total)
| Model | K* 15D | K* 17D | cosine_sim rank | entity_div rank |
|-------|--------|--------|-----------------|-----------------|
| Qwen-1.5B | 2 | 2 | 11/17 | 17/17 |
| Pythia-1.4B | >5 | >5 | 15/17 | 16/17 |
| Qwen-cont | 2 | 2 | 11/17 | 17/17 |