# ssh cleanup 29046 root

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cleanup-29046-root_20260522T125108_result.json`
- **Structured JSON:** [`1c9974ffd8157fcd6660.json`](../../sessions/1c/1c9974ffd8157fcd6660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根分区从 **93% (2.4G 可用) → 83% (5.3G 可用)**，腾出约 **2.9G** 空间。

清理明细：
| 项目 | 释放空间 |
|------|---------|
| HF datasets arrow 缓存 | ~2.9G |
| `/tmp` 临时文件（日志、旧脚本、tmp 目录） | ~20M |
| `__pycache__` | ~几十K |
| apt/pip/conda cache | 已为空 |

**未删除（安全约束）：**
- `/tmp/exp003_s2_ckpts.tar.gz` (661M) — checkpoint 存档
- `/tmp/test_c1_v2/checkpoint-5` (961M) — checkpoint 数据
- `/root/.cache/huggingface/hub/` 下的模型权重 (DeBERTa ~1.4G) — 可能用于评估
- 所有训练日志、实验数据、运行中的进程

如果需要进一步释放空间，可以考虑清理 HF hub 中不再使用的 dataset 下载（ultrachat_200k 1.6G + ShareGPT 151M），或确认 DeBERTa 模型权重是否还需要。

---
