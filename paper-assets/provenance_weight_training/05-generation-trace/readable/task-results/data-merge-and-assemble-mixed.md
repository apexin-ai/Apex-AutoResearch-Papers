# data merge and assemble mixed

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_merge-and-assemble-mixed_20260513T215105_result.json`
- **Structured JSON:** [`a316f3f2a5fed921dbae.json`](../../sessions/a3/a316f3f2a5fed921dbae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。混合数据中可见 depth=1 (synthetic) 和 depth=0 (human/fineweb) 记录交替出现，shuffle 生效。

## 报告

| 项目 | 值 |
|------|-----|
| 合成数据合并后文档数 | 340,992 |
| 人类数据文档数 | 164,889 |
| **混合数据总文档数** | **505,881** |
| 人类占比 | 32.59% |
| 合成占比 | 67.41% |
| 文件路径 | `/root/provenance_weight_training/data/mixed_data.jsonl` |
| 文件大小 | 1.2 GB |

数据已 shuffle（seed=42），human 记录标注 `depth=0, source=fineweb`，synthetic 记录标注 `depth=1`。`GENERATION_DONE` 标记已创建。

---
