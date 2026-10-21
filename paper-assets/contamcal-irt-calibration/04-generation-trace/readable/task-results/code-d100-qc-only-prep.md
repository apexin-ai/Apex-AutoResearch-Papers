# code d100 qc only prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d100_qc_only_prep_20260514T005655_result.json`
- **Structured JSON:** [`78b8b562f7c9b378b54a.json`](../../sessions/78/78b8b562f7c9b378b54a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出总结：

**脚本** — `/root/contamcal-irt-calibration/exp001/prepare_qc_only_data.py`
- 从 `prepare_sft_data.py` 复用格式化函数，加 QC 过滤逻辑
- 支持 `--dry-run` 和 `--help`
- 输出 `sft_dosage_100_qc_only.jsonl` + 对应 contamination labels + `data_meta_qc_only.json`

**Dry-run QC 统计**：

| Benchmark | All | QC Pass | Pass% |
|-----------|-----|---------|-------|
| arc_challenge | 1,172 | 697 | 59.5% |
| gsm8k | 1,319 | 228 | 17.3% |
| humaneval | 164 | 26 | 15.8% |
| mmlu | 14,042 | 6,596 | 47.0% |
| **TOTAL** | **16,697** | **7,547** | **45.2%** |

QC-only 数据量约为 ALL 的 45%（7,547 vs 16,697 contamination items）。

**experiment_plan.yaml** — 新增 `exp-015 sft_d100_qc_only`（P1，依赖 exp-001）。

---
