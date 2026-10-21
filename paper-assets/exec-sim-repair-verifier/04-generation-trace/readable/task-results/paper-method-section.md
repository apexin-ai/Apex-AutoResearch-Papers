# paper method section

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_method-section_20260512T203832_result.json`
- **Structured JSON:** [`e5b41d2ab3fced15767e.json`](../../sessions/e5/e5b41d2ab3fced15767e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section 已写入 `paper/method.tex` 并注册为 artifact (`art_20260512_6ec3b7`)。

结构：
- **§3.1 Problem Setup** — 定义 patch $p$、test suite $T$（$T_{\textsc{f2p}}$/$T_{\textsc{p2p}}$ 分区）、patch-level correctness
- **§3.2 CLS** — 单 token 二分类 $f(\text{code}, t_i) \to \{\textsc{Pass}, \textsc{Fail}\}$，cross-entropy loss
- **§3.3 CWM** — 生成式输出预测 $g(\text{code}, t_i) \to \hat{o}_i$，exact-match 判定，推理代价 $|\hat{o}_i|$ tokens
- **§3.4 TRAJ** — 轨迹级打分 $h(\text{code}, T) \to \{\textsc{Resolved}, \textsc{Unresolved}\}$，作为粒度对照
- **§3.5 Failure Mode Analysis** — token-budget exhaustion + string-value prediction errors，CLS 天然免疫，预测 complexity-dependent divergence
- **§3.6 Oracle Framework** — ICC $\rho$、design effect $\textsc{Deff} = 1 + (\bar{n}-1)\rho$、三条 threshold conditions（$|T_{\textsc{f2p}}| \geq 2$, moderate $\rho$, sufficient accuracy）

符号表严格一致，所有 claim 指向 §5 实验验证，未引用具体数字。

---
