# ops pilot completion check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pilot-completion-check_20260513T114348_result.json`
- **Structured JSON:** [`c084058d84698aad6fdb.json`](../../sessions/c0/c084058d84698aad6fdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## 双卡状态

| | m2_embed_verify (cuda:1) | plan_013_starcoder (cuda:0) |
|---|---|---|
| GPU利用率 | 95% / 22.9GB | 100% / 24.4GB |
| embedding ✅ | **DONE** | **DONE** |
| dataflow 🔄 | step 500/1640 (Epoch 1) | step 1000/1640 (Epoch 2) |

## 已完成策略 — Embedding Distance

| 指标 | m2_embed_verify (Qwen) | plan_013_starcoder (StarCoder) |
|---|---|---|
| best val_loss | **0.4603** (step 500) | **0.4816** (step 1000) |
| best recall@1 | **0.5557** | **0.5078** |
| best recall@5 | 0.9808 | 0.9843 |
| final val_loss | 0.5935 | 0.5060 |

两个实验都是 early stopping 趋势明显（best 在前半段，后面持续退化）。Qwen 的 embedding 策略 recall@1 比 StarCoder 高 ~5pp。

## Dataflow Aware 进度

- **StarCoder**: eval@500 已出 — val_loss=0.5257, recall@1=0.4756（比 embedding best 差，但才第一个 checkpoint）。已进入 Epoch 2，eval@1000 即将产生。
- **Qwen**: 刚到 step 500，eval@500 即将产生。

## 关键发现

1. **dataflow_aware 自动启动成功** — 之前失败的问题已修复，两个实验都无缝衔接。
2. StarCoder dataflow 预计 ~1-2h 完成，Qwen dataflow 预计 ~2-3h 完成。
3. 目前无策略完全完成（3/3 strategies），两个实验都在最后一个策略 dataflow_aware 阶段。

---
