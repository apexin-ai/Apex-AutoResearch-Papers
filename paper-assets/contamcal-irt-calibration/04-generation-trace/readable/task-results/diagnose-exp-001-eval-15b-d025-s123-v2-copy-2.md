# diagnose exp 001 eval 15B d025 s123 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_15B_d025_s123_v2_20260515T163010_result.json`
- **Structured JSON:** [`2fb686538bb589034600.json`](../../sessions/2f/2fb686538bb589034600.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结果：实验成功（EXIT_CODE=0）**

| Benchmark | Score |
|-----------|-------|
| MMLU | 0.5881 (8258/14042) |
| GSM8K | 0.6550 (864/1319) |
| ARC-Challenge | 0.7577 (888/1172) |
| HumanEval | 0.2500 (41/164) |

- 日志：`~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log`（cron 注册时 ID 后缀为 `_v2`，但实际日志文件名不含 `_v2`）
- 结果目录：`/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned/`
- Registry 已更新为 DONE/success + metrics
- Cron 不存在（可能已被其他流程清除）

---
