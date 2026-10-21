# viz claim3 method variability

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_claim3_method_variability_20260518T130333_result.json`
- **Structured JSON:** [`c6f60f1f3ecb982b2587.json`](../../sessions/c6/c6f60f1f3ecb982b2587.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 和 PNG 均已生成：

| 文件 | 大小 |
|------|------|
| `figures/claim3_method_variability.pdf` | 34K |
| `figures/claim3_method_variability.png` | 154K |

**视觉效果**：
- **Dot-strip 层**：5 个方法的彩色散点在每个 condition 上展开，TY（vermillion 倒三角）波动最剧烈，从 0/8 跌到 6/8；Naive/Thresh 聚在顶部 7-8/8，Diff/PG_fwd 居中 5-6/8
- **Consensus 层**：绿色粗线 + 浅绿色带横贯全图，锁定在 5/8-6/8 极窄区间，与散点的宽幅散布形成强烈反差
- **标注**：TY range 双向箭头标出 0/8-6/8 跨度；右侧 "stable: 5/8 to 6/8" 强调共识稳定性
- **标题**为 insight 句："Individual methods vary widely; multi-method consensus absorbs the variance"

核心 narrative 一目了然：单方法不可靠，共识阈值 K≥4 跨条件吸收了方法间方差。

---
