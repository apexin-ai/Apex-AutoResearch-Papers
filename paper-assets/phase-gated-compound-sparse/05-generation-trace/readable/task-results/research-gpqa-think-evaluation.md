# research gpqa think evaluation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_gpqa_think_evaluation_20260516T045554_result.json`
- **Structured JSON:** [`5e4d8d49b78198a712fe.json`](../../sessions/5e/5e4d8d49b78198a712fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果出来了。汇总如下：

---

## 结果汇报

### 1. DS-R1 GPQA Raw Output 格式
**无 `&lt;think>` 标记，但 100% 存在自然语言推理链。**

| 样本 | 领域 | 耗时 | Input toks | Reasoning markers |
|------|------|------|-----------|------------------|
| P0 | Physics | 119.7s | 131 | "first" |
| P1 | Chemistry | 98.9s | 138 | "let me", "first", "step", "so," |
| P2 | Physics | 119.7s | 162 | "let me", "first", "step", "so," |

三条输出全部是 **先推理后结论** 格式（200 tokens 内都还在推理阶段，没到结论），有清晰的 chain-of-thought 结构。

### 2. System Prompt Elicitation
**关键发现：chat template 自动注入 `&lt;think>`。**

- v1 (显式 system prompt) 和 v2 (native chat) 的 template **都在 generation prompt 后自动附加了 `&lt;think>`**（`<｜Assistant｜>&lt;think>\n`）
- 两个版本输出内容几乎相同（都是在 `&lt;think>` 内部做推理），说明 system prompt 的额外指令是冗余的
- 模型在 chat template 模式下**天然进入 thinking 模式**，最终会生成 `&lt;/think>` 标记

→ **不需要 system prompt elicitation**。只要用 `apply_chat_template`，`&lt;think>`/`&lt;/think>` 就是内置的 phase 边界。

### 3. PPL Profile
**存在明显的 phase transition。**

| 区间 | Mean Loss |
|------|-----------|
| First 25% (prompt 部分) | **2.597** |
| Second 25% | 1.041 |
| Third 25% (推理中段) | **0.167** |
| Last 25% (推理后段) | **0.296** |

First 25% → Third 25% 的 loss 下降 **15.5x**（2.597 → 0.167），存在清晰的 transition point。per-token loss 从 prompt/推理起步的高不确定性区域，过渡到推理中后段的低 loss 区域。

### 4. 推荐方案

**用 chat template（`&lt;/think>` 标记）做 phase segmentation，PPL-based 作为补充验证。**

理由：
- DS-R1 的 chat template 内置 `&lt;think>` 开头，模型会自然生成 `&lt;/think>` 结束 thinking phase → **直接用 token-level `&lt;/think>` 定位 phase 边界**，无需 KDE/quantile
- PPL profile 确认了 phase transition 的存在，可作为 `&lt;/think>` 缺失时的 fallback
- GPQA 的 raw inference（无 chat template）也有自然推理链，但没有明确 boundary marker，不建议走这条路

**实操建议**：profiling pipeline 中对 DS-R1 + GPQA 的处理，直接在 token 序列中搜索 `&lt;/think>` token 做 segmentation，比 attention sparsity 方法更简单且更可靠。

---
