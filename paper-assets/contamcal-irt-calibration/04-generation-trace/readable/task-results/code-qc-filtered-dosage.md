# code qc filtered dosage

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qc_filtered_dosage_20260514T001031_result.json`
- **Structured JSON:** [`1bf86d142cc93489eb2f.json`](../../sessions/1b/1bf86d142cc93489eb2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。产出汇总：

**QC-filtered dosage 文件**：`/root/autodl-tmp/exp001/sft_data_qc_filtered/`

| Dosage | QCF total | QCF contam | QCF ratio | ALL total | ALL contam |
|--------|-----------|------------|-----------|-----------|------------|
| 5%     | 50,377    | 377        | 0.75%     | 50,826    | 826        |
| 25%    | 51,886    | 1,886      | 3.63%     | 54,133    | 4,133      |
| 50%    | 53,773    | 3,773      | 7.02%     | 58,266    | 8,266      |
| 100%   | 57,547    | 7,547      | 13.11%    | 66,533    | 16,533     |

QC-filtered contamination pool 7,547 items（ALL 版本 16,533 的 45.6%）。d100 时所有 QC-passed paraphrases 全部注入，contamination labels 使用 full benchmark sizes（arc:1172, gsm8k:1319, humaneval:164, mmlu:14042）。元数据写入 `data_meta_qcf.json`。

---
