# code training skeleton

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_training_skeleton_20260512T100142_result.json`
- **Structured JSON:** [`108723c61933ef5882a0.json`](../../sessions/10/108723c61933ef5882a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个文件已创建并注册，路径 `artifacts/code/training/` 下：

**`contrastive_model.py`** — `StructFuseEncoder` bi-encoder + `FusionHead`
- 共享 Qwen2.5-Coder-3B backbone，mean pooling + optional MLP projection
- Learnable temperature (`log_temperature` parameter)
- InfoNCE loss：batch 内 positive 在 index 0，支持 `pos_weights = exp(-alpha * distance)` 加权
- Fusion head：6 维输入（embed_sim + 5 explicit features）→ relevance score
- 支持 LoRA（peft `q_proj`/`v_proj`）和 gradient checkpointing

**`hard_negative_mining.py`** — 3 种策略
- `RandomMiner`：同 repo 随机采样
- `EmbeddingDistanceMiner`：cosine 最近邻（CoCoHaNeRe baseline）
- `DataFlowAwareMiner`：embedding top-K similar → 过滤 data-flow 连通的 → 可选 BM25 re-rank；不足时 fallback random
- `build_miner()` 工厂 + `mine_batch()` 批量接口

**`train.py`** — 训练入口
- Accelerate 多 GPU、W&B logging、cosine LR schedule with warmup
- 每 epoch 重新 mine negatives（dynamic sampling）
- 验证：recall@1/5/10 + val_loss
- 完整 argparse CLI（所有要求的参数）
- checkpoint 保存 model + tokenizer + training_config.json

---
