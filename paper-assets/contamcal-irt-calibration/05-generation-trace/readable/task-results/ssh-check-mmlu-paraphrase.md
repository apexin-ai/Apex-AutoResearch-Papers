# ssh check mmlu paraphrase

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-mmlu-paraphrase_20260513T235148_result.json`
- **Structured JSON:** [`b91c44fcc4ab61b92d04.json`](../../sessions/b9/b91c44fcc4ab61b92d04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### mmlu_paraphrases.json — 已就绪

| 项目 | 值 |
|------|-----|
| 路径 | `/root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json` |
| 大小 | 27.3 MB |
| 行数 | 407,015 |
| 条目数 | 14,042（JSON array，每条含 `index`, `benchmark`, `original`, `paraphrase_raw`, `paraphrase_text`, `similarity`, `bleu`, `passed_qc`） |
| 生成时间 | 2026-05-14 06:57 |
| 完整性 | JSON 正常闭合（末尾 `]`），文件完整 |

每条含 `question` 出现约 41,059 次（原题 + paraphrase 各含 question 字段 + paraphrase_raw 内嵌），结构正常。MMLU 标准测试集 14,042 题，全部覆盖。

### dosage 文件现状

| 文件 | 行数 | 大小 |
|------|------|------|
| `sft_dosage_000.jsonl` | 50,000 | 88 MB |
| `sft_dosage_005.jsonl` | 50,826 | 89 MB |
| `sft_dosage_025.jsonl` | 54,133 | 90 MB |
| `sft_dosage_050.jsonl` | 58,266 | 92 MB |
| `sft_dosage_100.jsonl` | 66,533 | 96 MB |

另有 12 个 `contamination_labels_*.json` 文件（mmlu/arc_challenge/gsm8k × 4 dosage levels）和 `data_meta.json`。数据全部就绪。

---
