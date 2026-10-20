# research bcp failure diagnosis

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bcp-failure-diagnosis_20260512T150410_result.json`
- **Structured JSON:** [`70327fb182b318ee8ad8.json`](../../sessions/70/70327fb182b318ee8ad8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the structured diagnostic report.

---

# BCP 失败诊断报告

## 1. 失败模式分布表

| Variant | n | Completion | Q-Rate | P-Rate | SUCCESS | TRANSFER | WRONG_PARAMS | NO_ACTION | OTHER |
|---|---|---|---|---|---|---|---|---|---|
| **baseline** | 20 | **35.0%** | 4.2% | 53.1% | 7 (35%) | 4 (20%) | 4 (20%) | 0 | 5 (25%) |
| **aave_target** | 20 | **10.0%** | 1.5% | 46.8% | 2 (10%) | **9 (45%)** | 7 (35%) | 1 (5%) | 1 (5%) |
| **indian_english** | 20 | **15.0%** | 1.4% | 46.0% | 3 (15%) | 4 (20%) | 7 (35%) | 1 (5%) | 5 (25%) |
| **overcorrected** | 20 | **25.0%** | 1.7% | 57.5% | 5 (25%) | 4 (20%) | 6 (30%) | 0 | 5 (25%) |
| **single_dim_q** | 16 | **25.0%** | 8.2% | 41.2% | 4 (25%) | 5 (31%) | 4 (25%) | 0 | 3 (19%) |

**关键数字**：AAVE variant 的 transfer_to_human 从 baseline 的 20% 飙升到 **45%**（9/20 tasks），是 completion 骤降的首要原因。

## 2. 6个回归 Task 的失败根因

逐个检查 baseline SUCCESS → AAVE FAIL 的 task：

| Task | AAVE Failure Mode | Root Cause |
|------|-------------------|------------|
| **3** | WRONG_PARAMS | User sim 问了 11 轮无关问题（"return label details"、"login page URL"），hallucinate了退货流程，虽然最终 agent 执行了正确 action，但对话偏离导致参数匹配问题 |
| **4** | TRANSFER_TO_HUMAN | 指令是 modify t-shirt M→S，但 user sim 说 "I need to **return** the shirt" → agent 无法完成修改，转人工。Baseline 只有 14 turns vs 对话直接中断 |
| **6** | WRONG_PARAMS | 指令是 modify jacket + change address，user sim 说 "**exchange** it for a larger size"（modify≠exchange），对话仅 10 turns（baseline 24），agent 执行了错误操作 |
| **14** | WRONG_PARAMS | 同类问题——user sim 偏离 task instruction，提供错误的操作意图 |
| **15** | WRONG_PARAMS | 指令期望特定处理，user sim 说 "return the item and get the correct one"，hallucinate 了不同方案 |
| **17** | NO_ACTION | user sim 说 "return the item" 但最终直接 ###STOP### 退出，agent 未执行任何 action |

**共同模式：User simulator 在 BCP prompt 下系统性地偏离 task instruction，把 modify 变成 return/exchange。**

## 3. 代表性失败 Case

### Case A: Task 4 — Modify → Transfer (AAVE)

**指令**: "Order ends in 5, modify t-shirt from M to S"

**Baseline user**（成功）:
> "I'd like to modify my recent order. I ordered a medium t-shirt but I actually need a small. The order number ends in 5."

**AAVE user**（失败）:
> "I need to return the shirt because the size is wrong. I want to exchange it for a Small."

→ agent 认为用户要 return/exchange（不同的 tool），无法完成 modify，转人工。对话 14 turns 后终止。

### Case B: Task 6 — Modify → Wrong Action (AAVE)

**指令**: "Change address + modify jacket S→M"

**Baseline user**（成功，24 turns）:
> "I want to change my delivery address and also modify the jacket size from small to medium in my order."

**AAVE user**（失败，10 turns）:
> "I need to modify an order I placed. The jacket I ordered is too small and I want to exchange it for a larger size."

→ "exchange" 触发了不同的 agent tool（exchange_delivered_order vs modify_pending_order），action params 不匹配。

### Case C: Task 17 — No Action Taken (AAVE)

**指令**: Tea kettle doesn't match website, expected: get resolution

**AAVE user**: 经过 9 turns 讨论后说 "I'll take care of the return and place a new order soon. Have a great day!" 然后 ###STOP### — **agent 从未执行任何 action**。

## 4. AAVE 方言特征检测

| Variant | Tasks with AAVE features | copula_deletion | habitual_be |
|---|---|---|---|
| baseline | 5/20 | 4 | 2 |
| aave_target | 7/20 | 7 | 3 |
| indian_english | 10/20 | 36 | 4 |

**BCP prompt 完全没有产生 AAVE 方言**。检测到的少量 "copula_deletion" 是 regex 误报（匹配了 "I already" 等普通英语结构）。两个 variant 使用相同的 behavioral rate targets (Q=10%, P=20%)，但都没有方言指令，所以 user sim 全程 Standard English。

## 5. Question Rate 反向过冲机制

| Variant | Target Q | Actual Q | Direction |
|---|---|---|---|
| baseline | — | 4.2% | — |
| aave_target | 10% | **1.5%** | ↓ (反向) |
| indian_english | 10% | **1.4%** | ↓ (反向) |
| overcorrected | 5% | **1.7%** | ↓ |
| single_dim_q | 10% | **8.2%** | ↑ (接近目标) |

**single_dim_question（只有 Q-rate 约束，无 P-rate）是唯一接近目标的 variant**，但 completion 仍从 35% 降到 25%。

解释：当 BCP 同时约束 Q-rate 和 P-rate 时，模型将 "approximately 10%" 解读为 "questions should be rare"，并过度抑制提问。Q-rate 检测器过滤了 modal requests（"Can you help..."）和 confirmations，只计 genuine information queries — 这些恰好是完成 task 所需的关键信息获取行为。**BCP 抑制了 user sim 向 agent 索取信息的能力**。

## 6. 根因假说（1-2 句）

**BCP 在 agentic 评估中失败的根因是 capacity-interference tradeoff：当 user simulator 必须同时 (a) 遵循复杂的多步 task instruction 和 (b) 调节行为率以匹配 target distribution 时，behavioral guidelines 占据了 prompt attention budget，导致 task instruction fidelity 系统性退化。** 具体表现为 user sim hallucinate 错误的操作意图（modify→return/exchange），使 agent 执行错误 action 或被迫转人工。

## 7. 对论文 Negative Result 叙事的建议

**核心论点**：Prompt-based behavioral calibration (BCP) is fundamentally incompatible with agentic evaluation settings.

**叙事框架**：

1. **Text generation ≠ Agent interaction**: 在文本生成任务中，style 约束（语气、词汇选择）不会与 content 目标冲突。但在 agentic 场景中，behavioral constraints（Q-rate, P-rate targets）和 task goals（正确执行多步操作）竞争同一个 prompt 的 attention 资源。

2. **三重失败证据链**:
   - **(a) Task fidelity collapse**: Completion 35% → 10%，不是因为 agent 理解不了方言（根本没有方言），而是 user sim 自己偏离了 task。
   - **(b) Behavioral overshoot**: Q-rate 不升反降（4.2% → 1.5%），目标 10% 的 prompt 反而抑制了提问。
   - **(c) Transfer cascade**: Transfer rate 20% → 45%，user sim 的错误请求让 agent 无法完成任务。

3. **This motivates RL-based calibration**: 如果 prompt-level constraints 与 task completion 冲突，需要在 reward function 中同时编码 behavioral targets 和 task success，让模型通过 training（而非 inference-time instruction following）学会 trade-off。这正是 DPO/GRPO pipeline 的 justification。

4. **Ablation insight**: single_dim_question variant（只约束 Q-rate）的 Q-rate 最接近目标（8.2% vs target 10%），但 completion 仍降 10pp。说明即使是单维度约束也会干扰 task execution — 问题不在于约束数量，而在于 prompt-based calibration 的根本局限。

---
