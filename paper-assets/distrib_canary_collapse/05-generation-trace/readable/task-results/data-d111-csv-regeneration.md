# data d111 csv regeneration

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_d111_csv_regeneration_20260520T001046_result.json`
- **Structured JSON:** [`19cbcd81ff2289665c41.json`](../../sessions/19/19cbcd81ff2289665c41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个 CSV 已写入 `artifacts/`。

**审计摘要：**

| α | naive | diff | thresh | permG | ty | K≥3 | K≥4 | regime | source |
|---|---|---|---|---|---|---|---|---|---|
| 0.00 | 6/8 | 0/8 | 3/8 | 0/8 | 1/8 | 1/8 | 0/8 | blind_zone | detailed |
| 0.05 | 7/8 | 3/8 | 5/8 | 0/8 | 3/8 | 3/8 | 0/8 | blind_zone | summary |
| 0.10 | 7/8 | 6/8 | 5/8 | 0/8 | 3/8 | 4/8 | 2/8 | blind_zone | summary |
| 0.25 | 8/8 | 3/8 | 5/8 | 0/8 | 3/8 | 4/8 | 0/8 | blind_zone | summary |
| 0.30 | 5/8 | 3/8 | 8/8 | 0/8 | 5/8 | 3/8 | 3/8 | blind_zone | detailed |
| 0.35 | 8/8 | 4/8 | 8/8 | 0/8 | 4/8 | 6/8 | 2/8 | blind_zone | summary |
| 0.40 | 8/8 | 3/8 | 8/8 | 0/8 | 4/8 | 6/8 | 1/8 | blind_zone | summary |
| 0.45 | 7/8 | 3/8 | 8/8 | 0/8 | 1/8 | 3/8 | 0/8 | blind_zone | summary |
| 0.50 | 5/8 | 1/8 | 8/8 | 6/8 | 4/8 | 6/8 | 2/8 | onset | detailed |
| 0.60 | 7/8 | 8/8 | 8/8 | 3/8 | 8/8 | 8/8 | 7/8 | sync_collapse | summary |
| 0.75 | 7/8 | 6/8 | 8/8 | 6/8 | 8/8 | 7/8 | 6/8 | detection | summary |
| 1.00 | 1/8 | 0/8 | 0/8 | 6/8 | 1/8 | 0/8 | 0/8 | detection | detailed |

**交叉验证全部通过：**
- α=0.00: permG=0/8 ✓, naive=6/8 ✓, threshold=3/8 ✓, TY=1/8 ✓
- α=0.50: permG=6/8 ✓
- α=0.75: permG=6/8 ✓
- α=1.00: permG=6/8 ✓

**数据来源：**
- 4 个 α 从 `analysis/5method_leadlag.json` 详细文件提取（0.00, 0.30, 0.50, 1.00）
- 8 个 α 从 `analysis_results.json` 汇总文件提取（已含 D111 方向检查的预计算值 + per-pair consensus_detail）

**关键观察：** PermG 是最严格的方法——仅在 α≥0.50 时显著，完美标记 onset boundary。α=1.00 的异常模式（permG=6/8 但 naive/threshold/diff=0）源于该实验是 Pythia-410M 在完整 α=1.0 条件下的 generalize 实验，信号模式不同于 alpha_sweep 系列。

---
