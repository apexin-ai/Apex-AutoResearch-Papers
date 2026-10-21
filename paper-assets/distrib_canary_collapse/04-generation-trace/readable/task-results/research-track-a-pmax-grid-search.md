# research track a pmax grid search

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_track-a-pmax-grid-search_20260522T074208_result.json`
- **Structured JSON:** [`64525b0143ad3ec98b47.json`](../../sessions/64/64525b0143ad3ec98b47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 结果

**P_max=0.75 是最优值**，精确对应 6/8 ceiling：

| 指标 | 旧模型 (P_max=1) | 新模型 (P_max=0.75) |
|------|-----------------|-------------------|
| Test MAE (T=5,15) | 0.1060 | ≈0 |
| T=25 MAE | 0.2190 | 0.0312 |

**P_max profile 规律**：
- P_max=0.50→0.75: test MAE 线性下降至 0（z₀ 全在边界=20，步函数退化）
- P_max=0.75: 完美匹配验证集（T=5 全 0/8，T=15 全 6/8=0.75）
- P_max=0.80→0.90: β 跳到 0.17-0.18（γ≈2.8），z₀ 仍在边界
- P_max=0.95→1.00: z₀ 恢复到 4.5-5.2（内点解），β=0.24-0.28，即旧模型

**关键问题**：P_max=0.75 时模型退化为步函数（z₀ hit boundary → Φ 变成阶跃），β=0.05（γ=10）无物理意义，α_c(T) 值不可靠。

**建议**：论文中将 P_max=0.75 作为固定 ceiling（经验确定，不拟合），smooth transition 部分仍用原始 Φ 模型描述 sub-ceiling 行为。

产出已注册：`theory_verification_d102_pmax_grid.json`、`pmax_grid_analysis.md`、脚本。

---
