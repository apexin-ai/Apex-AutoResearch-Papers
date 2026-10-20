# code plan 017 downstream impact

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_017_downstream_impact_20260520T234507_result.json`
- **Structured JSON:** [`ee08d04a6df02e94814e.json`](../../sessions/ee/ee08d04a6df02e94814e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan_017 完成。6 个 artifact 已注册。

## 核心发现

**1. 排名高度鲁棒**：移除 31.3% DIF items 后，模型排名与 full benchmark 的 Spearman ρ ≈ 0.996-0.999。

**2. DIF items 不是噪声——它们携带浓缩的差异化信息**：
- DIF-based removal 在所有 21/21 条件下造成的排名扰动都**显著大于**随机移除（z = -8 到 -49σ）
- 这意味着 DIF items 系统性地区分了模型，不是随机噪声

**3. DIF items 捕捉了时间不稳定性**：
- 跨代 super-family 比较（8 个 family：llama, qwen, mistral 等）中，DIF items 的准确率变化幅度是 full benchmark 的 **1.09×**，stable items 仅 **0.96×**

**4. 排名变动最大的模型**：
- 从 DIF items 获益最多（移除后排名下降最大）：phi-3、llama-3 衍生模型、一些 14B+ 模型（Δrank +700-850）
- 被 DIF items 压制（移除后排名上升最大）：mistral 系 merge 模型（Δrank -400 to -587）

**论文叙事角度**：DIF items 不是可以简单丢弃的"坏题"——它们是对不同时代模型有差异化效应的题目。移除它们虽然在跨代准确率比较上产生小幅稳定效果（~4%），但会显著改变模型排名，表明这些 items 承载了关于模型能力差异的结构化信息。

---
