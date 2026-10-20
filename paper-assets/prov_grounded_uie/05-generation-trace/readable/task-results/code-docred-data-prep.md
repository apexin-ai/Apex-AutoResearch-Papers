# code docred data prep

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_docred-data-prep_20260512T110111_result.json`
- **Structured JSON:** [`8c030ea1d48d16f62ee8.json`](../../sessions/8c/8c030ea1d48d16f62ee8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出文件汇总：

**`artifacts/` 目录结构：**
- `prepare_docred.py` — 预处理脚本
- `docred_raw/data/` — 原始 DocRED gzip 数据
- `docred_processed/train.jsonl` — 3027 条训练样本 (12MB)
- `docred_processed/dev.jsonl` — 985 条验证样本 (3.6MB)
- `docred_stats.md` — 数据统计报告

**关键统计：**

| | train | dev |
|---|---|---|
| 文档数 | 3,027 | 985 |
| 总关系数 | 38,180 | 12,275 |
| 平均关系/文档 | 12.61 | 12.46 |
| evidence句/关系 (mean/median/max) | 1.61 / 1 / 11 | 1.59 / 1 / 9 |
| 句子/文档 (mean/median/max) | 7.95 / 7 / 25 | 8.05 / 8 / 20 |
| token/文档 (mean/median/max) | 197.72 / 179 / 511 | 200.57 / 181 / 510 |

test split (1000 文档) 无标注，已跳过。26 个文档没有标注关系，也被跳过 (3053 → 3027)。

每条关系平均 1.6 个 evidence 句子，说明大部分关系由 1-2 句支撑，适合作为 GRPO 的 provenance fidelity reward 验证基准。

---
