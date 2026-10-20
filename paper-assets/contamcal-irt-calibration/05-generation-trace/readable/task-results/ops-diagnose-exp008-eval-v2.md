# ops diagnose exp008 eval v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-exp008-eval-v2_20260515T141702_result.json`
- **Structured JSON:** [`1378b277a042e83df5b3.json`](../../sessions/13/1378b277a042e83df5b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_008_base_pretrained_eval_v2 诊断结果：SUCCESS (4/4 benchmarks)**

| Benchmark | 结果 |
|-----------|------|
| MMLU | accuracy = 0.2294 (3221/14042) |
| GSM8K | accuracy = 0.1630 |
| ARC Challenge | accuracy = 0.2278 |
| HumanEval | pass@1 = 0.0000 (0/164) |

符合 base pretrained 预期——无 SFT 对齐，MC 格式近乎随机（~22-23%），HumanEval 完全无法生成有效代码。D046 约束：数据仅用于 Discussion "format incomprehension" 实证。

**cuda:2 状态**：PID 555936（3B d005 s123 SFT）仍在运行，占用 19316MiB，GPU-Util 100%。exp_008 进程已退出，cuda:2 无残留。

已完成：registry → DONE/success，cron 已删除。

---
