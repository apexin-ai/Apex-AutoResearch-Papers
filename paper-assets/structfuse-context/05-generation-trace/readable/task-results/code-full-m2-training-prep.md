# code full m2 training prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full-m2-training-prep_20260513T104329_result.json`
- **Structured JSON:** [`4979383d98d1a0354e40.json`](../../sessions/49/4979383d98d1a0354e40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建并注册。

**产出文件:**
- `artifacts/full_m2/run_full_m2_training.sh` — 单次训练 wrapper
- `artifacts/full_m2/schedule_m2_runs.sh` — 双卡 9-run 调度器

**GPU 分配:**
| GPU 0 (5 runs) | GPU 1 (4 runs) |
|---|---|
| random_42 | random_44 |
| embedding_42 | embedding_44 |
| dataflow_42 | dataflow_44 |
| random_43 | dataflow_43 |
| embedding_43 | |

GPU1 少一个 run，因为 dataflow_aware 比 random/embedding 慢（需额外图计算），这样两卡完成时间更接近。

**需要注意:**
1. **train.py 没有 `--early-stopping-patience` 参数** — 如果需要 early stopping (ES=3)，须先给 train.py 加这个功能
2. train.py 第 2 行硬编码了 `CUDA_VISIBLE_DEVICES=4`，wrapper 脚本通过环境变量在 import 前覆盖，但更稳妥的做法是删掉 train.py 里的硬编码
3. 数据路径假设为 `/root/autodl-tmp/structfuse/full_m1_data/`，全量 M1 完成后需确认实际路径并按需调整

---
