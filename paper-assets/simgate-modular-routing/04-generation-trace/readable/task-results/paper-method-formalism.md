# paper method formalism

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_method-formalism_20260515T095444_result.json`
- **Structured JSON:** [`7380ceb35ece05e315ff.json`](../../sessions/73/7380ceb35ece05e315ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改内容：

**main.tex**: 添加了 `\usepackage{algorithm}` 和 `\usepackage{algorithmic}`。

**method.tex** 扩写为四个小节：

1. **§3.1 Problem Setup** — 形式化定义环境 $\mathcal{E}$、策略 $\pi$、模态集 $\mathcal{M} = \{{\tt int}, {\tt det}\}$，以及路由策略 $\rho$ 的目标。
2. **§3.2 Counterfactual Episode Collection** — 在原有内容基础上新增 pure-strategy trajectory 的形式化定义 $\tau_m^{(t)}$，明确 death event 的数学表示 $d(\tau) \in \{0,1\}$, $s(\tau) = -P$。
3. **§3.3 Episode-Level Labeling** — 形式化 labeling function $L(\tau_{\tt int}, \tau_{\tt det}) \rightarrow \ell$，新增 **Algorithm 1** 伪代码（algorithmic 环境，含行号和注释），保留原有四类互斥规则的文字描述。
4. **§3.4 Death Avoidance Factor** — 新增 score gap 分解公式 $\Delta_{\text{full}} = \delta P + \Delta_{\text{nd}}$，DAF 定义更清晰，其余内容保留。

---
