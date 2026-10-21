# paper theory draft plan 023

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_theory_draft_plan_023_20260517T143535_result.json`
- **Structured JSON:** [`fae78bdcf93f5252b2bf.json`](../../sessions/fa/fae78bdcf93f5252b2bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Theory section 草稿完成，已保存到 `artifacts/theory_draft.tex` 并注册为 `art_20260517_54df88`。

**结构概要：**

1. **\S4.1 Distributional Dynamics** — 定义 $\mathcal{D}_0 \to M_1 \to \mathcal{D}_1 \to \cdots$ 迭代框架；Theorem 1 (Tail Contraction) 形式化 tail mass $T_k(\alpha)$ 单调递减至零，引用 Shumailov (Nature 2024) 的 Gaussian collapse 结果和 Dohmatob (NeurIPS 2024) 的线性/指数 test risk 增长公式。

2. **\S4.2 Why Features Distinguish Depth** — 分别解释 `p90_ppl`（tail 消失 → 高 surprisal token 减少）和 `var_surprisal`（entropy 下降 → surprisal 分布收窄）的单调性；Proposition 1 给出形式化陈述，对照实验 $\rho \in [-0.89, -0.82]$。

3. **\S4.3 EDD Upper Bound** — 引入 contraction mapping 假设（引用 Alemohammad ICLR 2024），推导 $\text{EDD}(\tau) \leq \lfloor \log(\delta/d_0) / \log\gamma \rfloor + 1$，含完整证明。对数形式解释了为什么即使初始差异大，检测深度也有限。

4. **\S4.4 Alignment with Experiments** — 三组验证：pairwise AUC 几何衰减（拟合 $\gamma \approx 0.80$）、三个模型一致 EDD=4、feature 单调性。

**风格检查通过：** 零 em-dash，零 -ing 短语结尾，环境全部闭合，大括号平衡。

---
