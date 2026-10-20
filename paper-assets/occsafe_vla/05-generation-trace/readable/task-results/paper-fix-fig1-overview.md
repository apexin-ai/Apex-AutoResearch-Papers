# paper fix fig1 overview

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_fig1_overview_20260527T201038_result.json`
- **Structured JSON:** [`c66c6cb5fd2b898ac63c.json`](../../sessions/c6/c66c6cb5fd2b898ac63c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已正确更新。所有数据点验证：
- Full OCC BN: 0.725 ± 0.064 (n=3) ✓
- Full OCC+LN: 0.777 (n=3, 实心圆) ✓
- Detach+LN: 0.826 (n=1, 空心圆 + "n=1" 标注) ✓
- Detach OCC: 0.767 ± 0.024 (n=4) ✓
- Vanilla 基线: 0.745 ✓
- LN pair 连接线: −4.9 pp ✓

**修改汇总：**

| 数据点 | 旧值 | 新值 |
|--------|------|------|
| Full OCC+LN CAR | 0.740 | **0.777** |
| Full OCC+LN n_seeds | 1 | **3** |
| Detach+LN CAR | 0.765 | **0.826** |
| Detach+LN sd | 0.023 | **None** |
| Detach+LN n_seeds | 3 | **1** (preliminary) |
| LN pair pp 差值 | −2.5 pp | **−4.9 pp** |
| x 轴上限 | 0.815 | **0.88** |

PDF/PNG 已生成在 `docs/paper/figures/`。注意 Full OCC+LN 现在 n=3 但 sd=None（你未提供 sd 值），如果有 sd 数据请补充。

---
