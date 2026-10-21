# analyze borderline feature analysis

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_borderline-feature-analysis_20260518T161647_result.json`
- **Structured JSON:** [`c5749b31cb33b44a87e3.json`](../../sessions/c5/c5749b31cb33b44a87e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**Mistral K\*=1 的原因**：mean |d| 最低 (0.112)，所有核心特征的 1v2 effect size 都很弱 (surp_d1_std d=-0.21, surp_std d=-0.19)。加上 depth-0 的 surp_mean 基线就偏低 (2.32 vs 其他模型 2.9-3.0)，压缩了可检测的动态范围。特征重要性也最分散 (top-1 仅 12.9%)。

**Pythia-t12/LLaMA borderline 的原因**：
- Pythia-t12: 高温增加生成随机性，delta(1→2) = -0.059 是所有模型中最小的
- LLaMA: 虽然 mean |d| (0.137) 反而高于 Qwen (0.125)，但它是唯一 delta(1→2) > delta(0→1) 的模型 (ratio=1.08 vs 其他 0.06-0.27)，说明 LLaMA 的生成不稳定收敛，分类器难以找到稳定决策边界

**Mechanistic insight**: 0→1 的 surprisal 衰减幅度强预测 1v2 可区分性。更强的模型更好地逼近训练分布，每步生成退化更小，1v2 信号消失。这是方法的根本 scaling 挑战。

产出文件：
- `artifacts/borderline_analysis/summary.md`
- `artifacts/borderline_analysis/borderline_features.tex`
- `artifacts/borderline_analysis/cohens_d_full.tex`

---
