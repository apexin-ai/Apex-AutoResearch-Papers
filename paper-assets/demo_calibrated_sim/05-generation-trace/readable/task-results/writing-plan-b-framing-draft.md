# writing plan b framing draft

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_plan-b-framing-draft_20260513T072756_result.json`
- **Structured JSON:** [`6642be0f1263e2866816.json`](../../sessions/66/6642be0f1263e2866816.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

paper_framing.md 已写入。结构包含：

- **3 个标题候选**（推荐 Title 1）
- **Core Story**：sim2real2026gap motivation → BCP+DPO 双路线 → 系统性失败 → taxonomy
- **4 个 Core Claims**（C1-C4），每个附 evidence strength 和 exp_id：
  - C1 (Strong): FM1/FM2/FM3，主要来自 mvp-004
  - C2 (Strong): FM4 DPO+BCP 反转，来自 hgate-dpo003-merged（10/12 checks gap 扩大）
  - C3 (Pending): 标记 `[PENDING: qwen14b-bcp-001]`，含 hedging 策略
  - C4 (Analytical): 4 条 implications
- **5 个预判 Reviewer Concerns** 及应对策略
- **Evidence Map**: claim → experiment → metric 完整映射
- **Contribution Statement** 和 **文献锚点表**

所有定量数字均来自 registry，Llama/Mistral 数据已降级为 auxiliary，Qwen14B 留占位符。

---
