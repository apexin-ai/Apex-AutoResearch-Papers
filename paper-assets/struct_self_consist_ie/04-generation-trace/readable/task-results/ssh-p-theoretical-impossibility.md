# ssh p theoretical impossibility

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p-theoretical-impossibility_20260520T105516_result.json`
- **Structured JSON:** [`0af508f2da195b307e22.json`](../../sessions/0a/0af508f2da195b307e22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出已完成。核心结论：

**定理**: $\mathbb{E}[\Delta F_1] \leq (1-D) \cdot G_{nd} \cdot \alpha$

**数值验证 (16 configs, N=8)**:
- $G_{nd}$ ≈ 14.8pp (非退化实例的 oracle gap，跨 config 相对稳定)
- $\alpha$ ≈ 0.068 (signal alignment，最好的 config 也只恢复 oracle gap 的 ~12%)
- $\theta_{crit}$ = **0.70** (D 超过此值，SC gain 必低于 0.3pp 显著性阈值)

**验证一致性**:
- 所有 D > 0.62 的 config (CoNLL 全部) 的 best-method gain 均为负 → 符合 bound 预测
- 最大 gain 出现在低 D 的 FewNERD-FT (D≈0.12, +1.56pp) 和 SciERC-ZS (D≈0.21, +1.53pp)
- Bound 是 valid 的，但 loose (ratio 仅 3-12%)，瓶颈在 α 而非 D 本身

**产出文件** (`artifacts/p_impossibility/`):
- `theorem.tex` — 3 个定理 + 1 个推论 + partial degeneracy 扩展 + 有限样本修正
- `bound_verification.json` — 16 config 逐条数据
- `bound_plot.png` — D vs gain 散点 + bound 曲线 + θ_crit 标注
- `summary.md` — 完整分析报告

---
