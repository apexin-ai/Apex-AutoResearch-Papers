# research identifiability analysis

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_identifiability_analysis_20260522T045517_result.json`
- **Structured JSON:** [`db3ba88837c0b62d4e03.json`](../../sessions/db/db3ba88837c0b62d4e03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/identifiability_analysis.md`（404行）。核心内容：

**7个命题/定理：**
- **P1-P2**: Location indeterminacy 继承自 MFRM，但 $e_i$ 固定消除了 bilinear ambiguity，不引入新 indeterminacy
- **P3 (核心)**: $\text{Var}(e_i) = 0$ 时 $c_n$ 与 $\theta_n$ 完全混淆——exposure variation 是必要条件
- **P4-P5**: $J \geq 2$，每个 model 至少需要两个不同 $e_i$ 的 item
- **T1 (充分条件)**: 完全交叉 + $J \geq 2$ + $|\{e_i\}| \geq 2$ → Fisher information matrix 满秩（generic identifiability）
- **P7**: $\hat{c}_n$ 精度下界 $\propto 1/\text{Var}_w(e_i)$——连接到实验设计优化

**对审稿人的关键回应点：**
- Gating term 不是 trivial addition——它改变了 sufficient statistics 的结构（$c_n$ 的充分统计量是 $e_i$-加权响应和，与 $\theta_n$ 的未加权和不同）
- 固定 $e_i$ 不仅是实际考虑，而是 identifiability 的必要条件（否则 bilinear indeterminacy）
- 与 DIF 文献的"转置"关系（DIF: 已知 group indicator × 未知 item parameter; G-MFRM: 已知 exposure × 未知 model parameter）

**9篇引用全部经 WebSearch 验证真实存在**，包括 Rothenberg (1971)、San Martín (2016)、Xu & Zhang (2016) 等。

---
