# code gsm8k analysis prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k-analysis-prep_20260519T220443_result.json`
- **Structured JSON:** [`76065891abbc4e732c4e.json`](../../sessions/76/76065891abbc4e732c4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。

结果：
- **GSM8K**: 找到 1 条结果（Qwen2.5-7B d000, accuracy=0.7104）——目前只有 baseline，d100 eval 还在 cqa1 上跑
- **MMLU**: 找到 25 条结果（5 个 model families × 5 dosages），完整的 dose-response 数据
- 输出了 3 个 CSV（gsm8k_summary, mmlu_summary, combined）和 2 个 PNG 图（side-by-side comparison + per-model overlay）
- 所有输出在 `/root/contamcal-irt-calibration/analysis/results/gsm8k/`

等更多 GSM8K eval 完成后重跑脚本即可自动发现新数据、计算 delta、更新图表。

---
