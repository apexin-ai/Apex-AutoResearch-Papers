# infra download 32b models

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download_32b_models_20260516T194835_result.json`
- **Structured JSON:** [`6c2c92a500a84383f095.json`](../../sessions/6c/6c2c92a500a84383f095.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总当前空间情况：

| 目录 | 大小 |
|------|------|
| structfuse/ | 183GB（归档项目，可清理） |
| models/ | 18GB（Qwen 5.8G + bigcode 12G） |
| contrastive_trace_safety/ | 1.3GB |
| 可用空间 | 33GB |

structfuse 主要占用：
- `checkpoints/` — 71GB
- `full_m1_data/` — 77GB
- `full_m2_training_data/` — 19GB
- `full_m2_starcoder_data/` — 13GB

删除整个 `structfuse/` 可释放 ~183GB，加上现有 33GB 总共 ~216GB，足够两个 32B 模型（~128GB）。

`models/` 下的 Qwen(5.8G) 和 bigcode(12G) 也是 structfuse 用的，清理后总共可释放 ~201GB。

**确认**：是否可以直接删除 `/root/autodl-tmp/structfuse/` 和 `/root/autodl-tmp/models/`（bigcode 是 structfuse 的）？还是需要保留 `models/Qwen/`（可能是 Qwen2.5 小模型，当前项目可能用到）？

---
