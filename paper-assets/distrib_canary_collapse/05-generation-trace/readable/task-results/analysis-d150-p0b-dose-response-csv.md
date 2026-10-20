# analysis d150 p0b dose response csv

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d150_p0b_dose_response_csv_20260520T134252_result.json`
- **Structured JSON:** [`5a6eac36616c121aafe2.json`](../../sessions/5a/5a6eac36616c121aafe2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**输出文件**:
- `artifacts/dose_response_d120_compiled.csv` — 49 行, 跨两台服务器的 D120-compliant 数据
- `artifacts/dose_response_d120_summary.md` — 含 dose-response 汇总

**关键数据点 (wikitext, GPT-2, mean PermG rate)**:
- α=0.00: 0.167 (3 seeds, 基线噪音)
- α=0.25: 0.125 (3 seeds, 低信号)
- α=0.50: **0.750** (3 seeds, 强信号跳跃)
- α=0.75: 0.667 (3 seeds)

**去重**: 8 个 19828 旧格式实验被 17855 fp32 重分析版本替代; 排除了 postd093 和 v3_d080 非标准变体。

---
