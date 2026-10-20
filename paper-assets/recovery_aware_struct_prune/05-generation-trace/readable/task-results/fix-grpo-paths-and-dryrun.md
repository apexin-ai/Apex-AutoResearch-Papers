# fix grpo paths and dryrun

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_grpo_paths_and_dryrun_20260514T170646_result.json`
- **Structured JSON:** [`5b1ce1f2a9b25c493c91.json`](../../sessions/5b/5b1ce1f2a9b25c493c91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。

**修复内容：**

| 文件 | 修复前 | 修复后 |
|------|--------|--------|
| `run_grpo_v4.sh:15` MODEL_PATH | `/root/autodl-tmp/recovery_aware_struct_prune/models/pruned_*` | `/root/autodl-tmp/pruned_*` |
| `run_grpo_v4.sh:16` OUTPUT_DIR | `/root/autodl-tmp/recovery_aware_struct_prune/models/recovered_*` | `/root/autodl-tmp/recovered_*` |
| `train_grpo.py:199` 默认 output_dir | 同上 | `/root/autodl-tmp/recovered_{model_name}` |

**Dry-run 结果 (`bash -x src/run_grpo_v4.sh rasp 20 0`)：**
- `MODEL_PATH=/root/autodl-tmp/pruned_rasp_20` — 路径存在，通过检查
- `OUTPUT_DIR=/root/autodl-tmp/recovered_rasp_20`
- 脚本正常解析参数并通过路径验证

`train_grpo.py:205` 的 log_dir (`/root/autodl-tmp/recovery_aware_struct_prune/logs/`) 保持不变——日志文件很小，不受根分区约束影响。

---
