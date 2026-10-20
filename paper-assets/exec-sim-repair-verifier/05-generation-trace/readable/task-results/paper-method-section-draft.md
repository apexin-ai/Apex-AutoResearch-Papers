# paper method section draft

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_method-section-draft_20260512T202359_result.json`
- **Structured JSON:** [`b95beaf403a80c79c40b.json`](../../sessions/b9/b95beaf403a80c79c40b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method 章节已写入 `paper/method.tex`（v5, 16/16 claims covered）。

结构：
- §3.1 Problem Setup — 定义 patch $p$, test suite $T$, F2P/P2P 分解
- §3.2 CLS — 单 token 输出 $f(c_p, t_i) \to \{\text{PASS}, \text{FAIL}\}$，conjunction 聚合到 patch 级
- §3.3 CWM — 生成 output string，exact match 推导 verdict，inference cost = $\sum|\hat{o}_i|$ tokens
- §3.4 TRAJ — 全 test suite 输入，单 binary 输出，作为 granularity control
- §3.5 CWM Failure Modes — token-budget exhaustion + string-value prediction errors，CLS by construction 规避；提出 complexity-dependent advantage 假说
- §3.6 Oracle Framework — block-correlation model（ICC $\rho$, DEFF, $k_{\text{eff}}$），推导 $P_{\text{detect}}(k) = 1-(1-r)^{k_{\text{eff}}}$，三个 testable predictions（$k=1$ 无优势、$\Delta(k)$ 随 $k$ 增长被 $\rho$ 抑制、优势集中在 multi-F2P tail），P2P regression 阈值分析

5 条 claims 已注册 provenance tracking，关联 D007/D008/D015/D018 等决策。

---
