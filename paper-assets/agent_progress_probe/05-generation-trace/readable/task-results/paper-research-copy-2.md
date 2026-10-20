# paper research

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_20260514T200749_result.json`
- **Structured JSON:** [`d661164425c1c8a085cb.json`](../../sessions/d6/d661164425c1c8a085cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已添加 2 篇论文到 `background` 类别末尾：

1. **huang2024selfcorrect** — "Large Language Models Cannot Self-Correct Reasoning Yet" (ICLR 2024, `2310.01798`)  
   核心证据：LLM 无外部反馈时 intrinsic self-correction 失败甚至降低性能。

2. **kamoi2024selfcorrection** — "When Can LLMs Actually Correct Their Own Mistakes?" (TACL 2024, `2406.01297`)  
   系统性综述确认：prompted self-correction 无一成功，self-correction 仅在有可靠外部反馈时有效。

两篇都直接支持我们的 "external monitoring > self-reflection" 论点——agent 不能可靠自检 stagnation，需要外部 monitor（即 TLM）。

---
