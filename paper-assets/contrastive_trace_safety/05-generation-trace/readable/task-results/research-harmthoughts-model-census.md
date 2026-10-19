# research harmthoughts model census

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_harmthoughts_model_census_20260517T060103_result.json`
- **Structured JSON:** [`2b72516ba6e2e1a8db55.json`](../../sessions/2b/2b72516ba6e2e1a8db55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/harmthoughts_census/report.md`。

**核心发现：**

| Code | 全称 | 架构 | Traces | Sentences |
|------|------|------|--------|-----------|
| **ot-7b** | OpenThinker-7B | Qwen2.5-7B | 333 | 26,653 |
| r1-8b | DeepSeek-R1-Distill-**Llama**-8B | Llama-3.1-8B | 324 | 14,746 |
| r1-32b | DeepSeek-R1-Distill-Qwen-32B | Qwen2.5-32B | 221 | 8,525 |
| QwQ | QwQ-32B | Qwen2.5-32B | 140 | 7,007 |

**关键结论：**

1. 缺失的 26,653 条 = **OpenThinker-7B**（Qwen2.5-7B 架构，trace 最长 avg 80 句/trace）

2. **r1-8b 是 Llama 架构**（不是 Qwen！）—— 这直接提供了 cross-architecture 对比能力

3. Architecture confound 部分解决：Llama (324 traces) vs Qwen (694 traces) 的 self-jailbreak 率几乎相同（~83%），支持 "现象跨架构存在" 的论证

4. 没有 Mistral/Gemma 等第三架构 —— 完全排除 confound 仍需外部数据

5. OpenThinker-7B 的 strict refusal-suppression 率最高 (18.9%)，是研究 RS 机制的最佳候选

---
