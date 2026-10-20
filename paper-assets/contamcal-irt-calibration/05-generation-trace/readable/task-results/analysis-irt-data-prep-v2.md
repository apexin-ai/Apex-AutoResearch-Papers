# analysis irt data prep v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_irt-data-prep-v2_20260519T210926_result.json`
- **Structured JSON:** [`0d41ec7c7f538618d3ed.json`](../../sessions/0d/0d41ec7c7f538618d3ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

| Benchmark | Respondents | Items | Overall Acc |
|-----------|------------|-------|-------------|
| MMLU | 20 | 14,042 | 0.5279 |
| GSM8K | 16 | 1,319 | 0.4390 |
| ARC-Challenge | 21 | 1,172 | 0.6985 |
| HumanEval | 15 | 164 | 0.1163 |

实际发现 21 个 respondent（5 families，但只有 7B 有 d050，其余 4 families 各 4 dosages）。MMLU 缺 Qwen2.5-7B_d000（该 eval 无 mmlu 数据），所以 MMLU 只有 20 个。

每个 benchmark 子目录下生成了 3 个文件：
- `response_matrix.csv` — J×I binary matrix
- `exposure_scores.csv` — respondent, dosage, exposure
- `item_metadata.csv` — item_id, subject, domain, difficulty_baseline（MMLU 含 subject/domain，其他 benchmark 仅含 difficulty_baseline）

脚本位置：`/root/contamcal-irt-calibration/analysis/irt_data/irt_data_prep.py`

---
