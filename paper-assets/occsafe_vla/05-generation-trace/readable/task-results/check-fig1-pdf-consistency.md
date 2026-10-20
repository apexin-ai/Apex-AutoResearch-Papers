# check fig1 pdf consistency

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_fig1-pdf-consistency_20260527T053923_result.json`
- **Structured JSON:** [`030202f59f78e75a9859.json`](../../sessions/03/030202f59f78e75a9859.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**本地 PDF 文件**: `docs/paper/figures/fig1_overview.pdf`，修改时间 **May 27 03:13 UTC**

**远程服务器**: 两台服务器（westd-34685, westd-10894）上均无 fig1 相关文件，生成脚本仅在本地。

**数据对比** — `docs/paper/figures/fig1_overview.py` panel (c) 硬编码值 vs Table 1 v2：

| 条件 | Fig1 脚本 | Table 1 v2 | 一致？ |
|------|-----------|------------|--------|
| Vanilla | 0.745 | 0.745 ± 0.024 | ✓ |
| Full OCC BN | 0.725 ± 0.064 (n=3) | 0.725 ± 0.064 (n=3) | ✓ |
| Full OCC LN | 0.740 (n=1) | 0.740 (n=1) | ✓ |
| Detach OCC BN | 0.767 ± 0.024 (n=4) | 0.767 ± 0.024 (n=4) | ✓ |
| Detach LN | 0.765 ± 0.023 (n=3) | 0.765 ± 0.023 (n=3) | ✓ |

**结论**: `fig1_overview.pdf` 与当前 Table 1 v2 数据**完全一致**，不需要重新生成。

另外注意：`artifacts/fig1_overview_v2.py` 是一个旧版本的交互图脚本，其数据（BN: 0.746→0.797, LN: 0.765→0.743, Vanilla: 0.780）与当前 Table 1 **完全不同**，已过时，不影响论文使用的 `docs/paper/figures/` 版本。

---
