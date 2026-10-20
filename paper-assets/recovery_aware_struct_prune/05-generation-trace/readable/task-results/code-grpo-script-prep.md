# code grpo script prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo_script_prep_20260514T165355_result.json`
- **Structured JSON:** [`2b0e9dbaa0ed4ec831e4.json`](../../sessions/2b/2b0e9dbaa0ed4ec831e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部参数正确，脚本就绪。

**改动汇总：**

| 项目 | 原值 | 新值 |
|------|------|------|
| `--output_path` (必填) | 用户指定 | `--output_dir` (可选，默认 `/root/autodl-tmp/.../recovered_&lt;model_name>`) |
| `--max_new_tokens` | 2048 | `--max_completion_length` = 4096 |
| `save_total_limit` | 无限制 | 2（只保留最近 2 个 checkpoint） |
| `logging_dir` | 根分区 `/root/recovery_aware_struct_prune/logs/` | 数据盘 `/root/autodl-tmp/.../logs/` |
| Reward desert 检测 | 无 | `RewardDesertCallback`：连续 50 次 log event reward=0 时自动停止（`--reward_desert_patience` 可调） |

**新增文件：**
- `src/run_grpo_v4.sh` — 一键运行脚本，用法：`bash src/run_grpo_v4.sh &lt;method> &lt;sparsity> &lt;gpu_id>`（如 `bash src/run_grpo_v4.sh standard 20 0`）

eval 跑完后即可直接启动 GRPO。

---
