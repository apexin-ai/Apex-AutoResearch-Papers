# code fitd perseed inference

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fitd-perseed-inference_20260521T082224_result.json`
- **Structured JSON:** [`1254317f39e1b75cf0ef.json`](../../sessions/12/1254317f39e1b75cf0ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。F1 表中 Binary/Scrambled/Topic 的 FITD 列已全部填入实际值（不再是 "--"）。

**推理结果汇总：**

| Variant | s42 | s123 | s456 | Mean±Std |
|---------|-----|------|------|----------|
| Binary | 1.000 | 1.000 | 1.000 | 1.000±0.000 |
| Scrambled | 1.000 | 1.000 | 1.000 | 1.000±0.000 |
| Topic | 0.990 | 0.774 | 0.909 | 0.891±0.089 |

**更新的文件：**
- `results/fitd_supplement_binary_scrambled_topic.json` — 原始推理结果（含 per-sample predictions）
- `results/round7_seed_level_stats.json` — 补入 FITD F1 和 recall
- `results/round7_seed_table.tex` — LaTeX 表已更新

Binary 和 Scrambled 在 FITD 上全部完美（3 seed 均 F1=1.0）。Topic 表现中等（mean 0.891），seed 123 最弱（0.774），与其在 DD/AA 上的不稳定表现一致。

---
