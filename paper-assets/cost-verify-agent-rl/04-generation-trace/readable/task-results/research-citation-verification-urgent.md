# research citation verification urgent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation-verification-urgent_20260518T034753_result.json`
- **Structured JSON:** [`2155cf9ccb4731cea218.json`](../../sessions/21/2155cf9ccb4731cea218.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。报告已写入 `artifacts/citation_verification_report.md`。

**核心结论：0 篇 hallucinated，4 篇完全准确，4 篇部分准确需修正措辞。**

需要修正的 4 处问题：

| 论文 | 问题 | 修正 |
|------|------|------|
| **GRPO-λ** | Lemma 1 实际是 value difference bound，非 "normalized advantage bias"；论文不用 "systematic misattribution" | 改述 Lemma 1 内容；删除 misattribution 措辞 |
| **OAR** | 论文不用 "advantage misattribution"，用的是 "reward aliasing" 和 "coarse-grained credit assignment" | 替换术语 |
| **Decoupled Credit** | ICLR 2026 状态是 under review，非已录用 | 标注 "(under review)" |
| **RAGEN** | "20/10 步 collapse" 不准确，实际 collapse 在 training step ~170/110 | 区分 episode length 和 training steps |

另外 IRC 的 "6.5pp" 数字未在 HTML 全文中找到确切对应，建议也核实一下。

---
