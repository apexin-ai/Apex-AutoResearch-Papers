# code multiseed bcs prep v2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multiseed_bcs_prep_v2_20260518T073730_result.json`
- **Structured JSON:** [`aa6e81af537eb1f50428.json`](../../sessions/aa/aa6e81af537eb1f50428.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常运行中。

**汇报：**

| 项目 | 详情 |
|------|------|
| **脚本** | `/root/schema-dag-extraction/scripts/run_multiseed_bcs.sh` (已存在) |
| **核心 Python** | `/root/schema-dag-extraction/src/run_fewshot_bcs_v2.py` |
| **输出** | `artifacts/multiseed_bcs_re/seed_123/` 和 `seed_456/` |
| **PID** | 531145 (nohup) |
| **日志** | `artifacts/multiseed_bcs_re/run_all.log` 和各 seed 目录下 `run.log` |
| **进度** | seed=123 正在推理，4/150 batch，288/14400 results |
| **吞吐** | ~4-5s/batch (96 samples)，~1900 toks/s input |
| **预估时间** | ~12-15 min/seed，两个 seed 共 ~25-30 min |
| **GPU** | RTX PRO 6000 Blackwell 98GB，已占用 89GB |
| **模型** | Qwen3-32B-FP8，vLLM 0.20.2 |

实验配置：50 batches (25 low-BCS + 25 high-BCS) x 3 shot conditions (0/1/5-shot) = 150 批次，每批 96 samples = 14,400 inferences/seed。

---
