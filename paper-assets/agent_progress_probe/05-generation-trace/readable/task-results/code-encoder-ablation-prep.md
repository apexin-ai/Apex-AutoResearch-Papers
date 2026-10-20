# code encoder ablation prep

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_encoder-ablation-prep_20260514T114915_result.json`
- **Structured JSON:** [`a45eac1381dee245e53a.json`](../../sessions/a4/a45eac1381dee245e53a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 steps complete:

1. **`encoder_ablation_embeddings.py`** — written, patched with manual BertModel loading fallback for GTE-large (works around `from_pretrained` hang)
2. **3 models pre-downloaded** to `/root/autodl-tmp/.hf_cache/` (BGE-M3 via ModelScope, E5-large via ModelScope, GTE-large via ModelScope `damo/nlp_gte_sentence-embedding_english-large`)
3. **Dry-run verified** all 3 encoders on 10 windows:

| Encoder | embed_dim | Pooling | Speed | Status |
|---------|-----------|---------|-------|--------|
| BGE-M3 | 1024 | CLS | 11.44 it/s | PASS |
| E5-large-v2 | 1024 | mean (+prefix) | 8.39 it/s | PASS |
| GTE-large | 1024 | mean | 13.85 it/s | PASS |

4. **`encoder_ablation_train.py`** — written, loads fixed splits from `checkpoints/split_info.json`, same hyperparams as original training

运行全量 embedding + 训练的命令示例：
```bash
# 全量 embedding（以 bge-m3 为例）
python -u encoder_ablation_embeddings.py \
  --encoder bge-m3 \
  --model_path /root/autodl-tmp/.hf_cache/modelscope_models/bge-m3/BAAI/bge-m3 \
  --windows data/windows_labeled.jsonl \
  --trajectories data/swe_agent_trajectories_5000.jsonl \
  --output ablation_embeddings/bge-m3_embeddings.pt \
  --device cuda

# 训练 probe
python -u encoder_ablation_train.py \
  --encoder_name bge-m3 \
  --embeddings ablation_embeddings/bge-m3_embeddings.pt \
  --split_info checkpoints/split_info.json \
  --output_dir ablation_results/bge-m3
```

---
