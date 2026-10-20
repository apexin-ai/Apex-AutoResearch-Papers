# analysis ty granger 3seed a025

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ty_granger_3seed_a025_20260516T022731_result.json`
- **Structured JSON:** [`b74214d99043c6ca9917.json`](../../sessions/b7/b74214d99043c6ca9917.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**C001 约束不能缓解，反而被强化。** 3-seed 数据暴露了 TY 在 T=11 下的系统性缺陷：

| Seed | TY sig rate (FDR) | df_resid (entropy pairs) |
|------|-------------------|--------------------------|
| 42   | 38% (3/8)         | **7**                    |
| 43   | 0% (0/8)          | 4                        |
| 44   | 0% (0/8)          | **1**                    |

**根因**：ADF 单位根检验在 T=11 下功效极低，不同 seed 给出不同的积分阶数 d_max（1/2/3），导致 df_resid 从 1 到 7 剧烈波动。s42 恰好获得最大 df_resid 所以显著，s43/s44 则完全无功效。这证实 C001 描述的非单调模式是方法学人工构件，不是真实信号。

- 报告：`artifacts/ty_3seed_a025_analysis.md`（服务器 + 已注册 artifact）
- 数据：`results/alpha_sweep/ty_3seed_a025_results.json`

---
