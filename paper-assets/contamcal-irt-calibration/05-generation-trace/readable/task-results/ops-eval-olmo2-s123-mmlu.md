# ops eval olmo2 s123 mmlu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-olmo2-s123-mmlu_20260520T112538_result.json`
- **Structured JSON:** [`1a6e4262442adfa45c3c.json`](../../sessions/1a/1a6e4262442adfa45c3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并注册。汇总：

| 项目 | 值 |
|------|-----|
| **exp_id** | `eval_olmo2_s123_mmlu` |
| **PID** | 331086 |
| **服务器/GPU** | westd-29999 / cuda:2 |
| **脚本** | `/root/contamcal-irt-calibration/scripts/eval_olmo2_s123_mmlu.sh` |
| **Checkpoints** | `/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d{000,005,025,050,100}_s123/lora_adapter` |
| **Base model** | `/root/autodl-tmp/models/OLMo-2-1124-7B` |
| **evaluate.py md5** | `17673bf373f00f83ccc41fc1d355a4cd` ✓ |
| **lora_alpha** | 32 ✓ |
| **输出目录** | `/root/contamcal-irt-calibration/results/mmlu_eval/olmo2/d{dosage}_s123/` |
| **日志** | `/tmp/eval_olmo2_s123_mmlu.log` |

d000_s123 正在评估中（~29 it/s，预计每个 dosage ~8 分钟，5 个共 ~40 分钟）。

---
