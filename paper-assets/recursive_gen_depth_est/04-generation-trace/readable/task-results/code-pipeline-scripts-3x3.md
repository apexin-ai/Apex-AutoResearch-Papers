# code pipeline scripts 3x3

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pipeline_scripts_3x3_20260514T171704_result.json`
- **Structured JSON:** [`abc9a3b10cfbfce2cdc1.json`](../../sessions/ab/abc9a3b10cfbfce2cdc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。6 个脚本（含已有的 `pythia_temp09` 和 `pythia_topk50`）全部就位，语法检查通过，权限已设为可执行。

**服务器上的脚本清单**（`/root/autodl-tmp/recursive_gen_depth_est/scripts/`）：

| 脚本 | 模型 | 策略 | 状态 |
|------|------|------|------|
| `run_pipeline_pythia_topk50.sh` | Pythia-1.4B | topk k=50 | 已有 |
| `run_pipeline_pythia_temp09.sh` | Pythia-1.4B | temp_only τ=0.9 | 已有 |
| `run_pipeline_olmo_temp09.sh` | OLMo-1B | temp_only τ=0.9 | **新建** |
| `run_pipeline_olmo_topk50.sh` | OLMo-1B | topk k=50 | **新建** |
| `run_pipeline_gpt2xl_temp09.sh` | GPT-2 XL | temp_only τ=0.9 | **新建** |
| `run_pipeline_gpt2xl_topk50.sh` | GPT-2 XL | topk k=50 | **新建** |

本地 `scripts/` 目录也同步了所有 6 个文件。没有 git 仓库，跳过了 commit/push 步骤。

---
