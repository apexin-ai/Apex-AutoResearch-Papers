# code plan002 phase2 pooled panel

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan002-phase2-pooled-panel_20260515T042930_result.json`
- **Structured JSON:** [`14fbf94eed7393270ea0.json`](../../sessions/14/14fbf94eed7393270ea0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码部署并验证完成。3 个输出文件全部生成：

**`pooled_panel_analysis.py`** 已写入服务器，包含 5 个分析模块：

1. **Pooled panel regression** — 6 对 canary→diversity pairs（token_entropy/ECE × distinct_1/2/3），Δdownstream ~ lag-1_Δcanary + α + α×lag-1_Δcanary，HC1 robust SE + BH FDR
2. **α-monotonicity** — Spearman(α, |drift slope|) + 散点图
3. **Cross-α permutation Granger** — 每个 α 的 F-stat + Spearman 趋势
4. **BH FDR** — 对 interaction term p-values 联合校正
5. **可视化** — 2×3 monotonicity 散点图

Dry-run 结果（2 个 α 点）：
- `lag1_d_canary` 系数在 token_entropy→distinct_1/2/3 上显著（β>0, p<0.001），确认差分序列的 lead-lag 关系存在
- Interaction terms 全部 FDR 不显著（预期：2 个 α 点 underpowered）
- α=0.25 的 Granger F-stat 普遍高于 α=0.00（如 token_entropy→distinct_1: 163 vs 48），方向符合预期
- 所有 warning 正确触发

等 α=0.50 完成后再跑一次即可获得 ≥3 点的 Spearman 和 FDR 校正结果。

---
