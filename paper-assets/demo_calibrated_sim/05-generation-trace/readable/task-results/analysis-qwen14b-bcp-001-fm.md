# analysis qwen14b bcp 001 fm

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b-bcp-001-fm_20260513T151952_result.json`
- **Structured JSON:** [`3d656b34bdb54fccec87.json`](../../sessions/3d/3d656b34bdb54fccec87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。核心结论：

**FM1 未复现** — 所有 BCP variant completion 保持率 > 97%，14B 无行为抑制。

**FM2 弱复现** — 跨维度干扰存在但幅度小（politeness -8%, question_rate -2.2pp），远弱于 7B。

**FM3 未复现** — overcorrected politeness 比 baseline **低** 7.1pp，方向相反。

**关键发现：14B 的 BCP 失败机制与 7B 根本不同。** 7B 是"灾难性崩溃"（BCP prompt 摧毁了模型行为），14B 是"选择性忽略"（模型正常工作但无视 BCP 校准指令）。两者 H2 都 FAIL，但原因相反：7B 过度响应，14B 不够响应。这是一个 scale-dependent failure mode transition，说明 BCP 的缺陷是方法论层面的。

---
