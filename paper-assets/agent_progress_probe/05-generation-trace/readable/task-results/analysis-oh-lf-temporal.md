# analysis oh lf temporal

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oh-lf-temporal_20260514T174011_result.json`
- **Structured JSON:** [`11de1ee54e3b5d395c4b.json`](../../sessions/11/11de1ee54e3b5d395c4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果摘要：

## 跨域 Temporal Dynamics 验证结果

| LF | SWE-Agent | OpenHands | 角色一致? |
|---|---|---|---|
| **file_diff_delta** | leading (mean=-1.20, n=914) | **leading** (mean=-4.90, n=4428) | **YES** |
| **command_repetition** | leading (mean=-1.87, n=913) | **lagging** (mean=+3.32, n=2914) | **NO** |
| **outcome_backpropagation** | lagging (mean=+6.70, n=1837) | **lagging** (mean=+18.07, n=2449) | **YES** |

**Temporal ordering:**
- SWE-Agent: cmd_rep → file_diff → outcome_bp
- OpenHands: file_diff → cmd_rep → outcome_bp

**结论：MIXED。** 2/3 LF 的 temporal roles 跨域一致：
- **file_diff_delta** 在两个域都是 leading indicator（OH 上甚至更强，-4.9 vs -1.2）
- **outcome_bp** 在两个域都是 lagging indicator（OH 上更滞后，+18.1 vs +6.7）
- **cmd_rep 角色翻转**：SWE-Agent 上 leading，OH 上 lagging。这与已知的 OH 71% false positive rate 一致——cmd_rep 在 OH 上过早误触发（非 stagnation 窗口也标记 stagnation），导致"首次 stagnation 投票"失去时序信号

所有跨域差异均统计显著（Welch's t-test, p < 10⁻⁷⁰）。OH 内部所有 pairwise 差异也显著（Wilcoxon, Bonferroni 校正后 p < 10⁻¹⁴⁸）。

论文角度：file_diff 和 outcome_bp 的跨域一致性支持 Claim 1 的部分泛化；cmd_rep 的角色翻转可作为 LF domain-specificity 的讨论点，进一步论证 why domain adaptation matters。

---
