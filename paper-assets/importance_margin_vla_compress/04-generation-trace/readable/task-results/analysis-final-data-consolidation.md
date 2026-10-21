# analysis final data consolidation

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_final-data-consolidation_20260528T113816_result.json`
- **Structured JSON:** [`76938f7e3a539daeba09.json`](../../sessions/76/76938f7e3a539daeba09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

表格已编制并注册（`art_20260528_495f87`）。

**核心结果:**

| k | L2norm | Random | Margin |
|------|---------|---------|--------|
| 0.95 | 86.8±0.8 (5s) | 61.3±0.8 (4s) | +25.5pp |
| 0.90 | 80.5±0.5 (4s) | 33.6±1.4 (4s) | **+46.9pp** ⭐peak |
| 0.85 | 78.3±0.6 (3s) | 45.4±1.3 (4s) | +32.9pp |
| 0.75 | 70.6±2.7 (5s) | 62.6±1.7 (4s) | +8.0pp |
| 0.70 | 64.3±1.6 (2s) | 65.3±0.8 (3s) | −1.0pp 🔄 |
| 0.50 | 51.5±2.0 (3s) | 50.5±0.8 (3s) | +1.1pp ≈0 |

**关键问题：数据缺口严重。** 只有 3/18 格有完整 5-seed 数据。ROADMAP 确认 s44 (18/18) 和 s45 (18/18) 全部完成，但大多数个体 SR 值未记录到 registry/decisions — 只存在于服务器 `eval_results/` 目录的 JSON 文件中。需要从服务器收割 s44/s45 数据才能完成论文级 5-seed 表格。

数据完整性 checklist 6 条全部通过（Attn k=0.75 s43 用 cqa1=52.0%，Random k=0.9 s43 用 v2=35.0%，Attn k=0.95 s42 用 D268 修正值 78.4%）。

---
