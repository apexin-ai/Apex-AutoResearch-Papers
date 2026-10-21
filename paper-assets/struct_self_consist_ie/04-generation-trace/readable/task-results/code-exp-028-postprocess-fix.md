# code exp 028 postprocess fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_028_postprocess_fix_20260517T132737_result.json`
- **Structured JSON:** [`27bb7f00698ec8b2cbbc.json`](../../sessions/27/27bb7f00698ec8b2cbbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修改完成，验证通过。

**修复 1: `03_analyze.py`** — `EXP021_REF` 改为从 `output/exp_027_fewnerd_n16/paired_n8_baseline.json` 的 `n8` 字段动态加载，文件不存在时 fallback 到硬编码值并打印 WARNING。参考文件中的精确值：
- `degeneracy_rate_pct`: 11.08%（旧硬编码 12.0%）
- `greedy_f1`: 0.7478
- `lp_sel_f1`: 0.7614
- `lp_delta_pp`: 1.37

**修复 2: `02_inference.sh`** — 第 10 行加入 `export CUDA_VISIBLE_DEVICES=0`（在 `cd` 之后、变量定义之前）。

---
