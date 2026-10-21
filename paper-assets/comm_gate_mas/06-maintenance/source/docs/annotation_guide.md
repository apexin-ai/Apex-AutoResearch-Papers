# 人工标注指南：Agent 消息功能分类

## 任务概述

你需要对 LLM 多智能体数学解题对话中的单条消息进行功能分类。每条消息分配 **恰好一个** 功能类别（共 5 类）。每条消息大约需要 15–30 秒完成标注。

你将看到：
- **上一条消息**（提供上下文）
- **当前消息**（你要分类的消息）
- 元数据：backbone 模型、task ID、发送者角色、消息位置

## 类别定义

5 个功能类别按 **优先级从高到低** 排列。当一条消息可以归入多个类别时，选择适用的最高优先级类别。

**优先级：coordination > verification > reasoning_guidance > information_provision > acknowledgment**

---

### 1. Coordination（协调）— 最高优先级

**定义：** 管理对话的元结构 — 角色分配、轮次控制、任务委派或请求澄清 — 不贡献实质性任务内容。

**示例：**
- *"Please verify my calculation for step 3 while I work on step 4."* — 向另一个 agent 委派子任务。
- *"Could you clarify whether the discount applies before or after tax?"* — 请求澄清以推进流程。
- *"I'll have more problems for you to solve. If you're ready, I can provide the next one."* — 控制对话流程和轮次。

**反例（看似 coordination 但不是）：**
- *"Let's break down the problem step by step: (1) find the rate, (2) multiply by time, (3) apply discount."* — 这是 **reasoning_guidance**：提供了分步方案，而不是管理流程。

---

### 2. Verification（验证）

**定义：** 评估先前贡献的正确性 — 检查工作、指出错误、以实质性理由确认结果或验证步骤。

**示例：**
- *"The multiplication in step 2 is wrong: 15 × 4 = 60, not 45."* — 指出具体的计算错误。
- *"Your breakdown and calculations are correct. Let's verify each step again: [逐步重新推导]"* — 通过详细重新检查来确认正确性。
- *"The revised solution is clear and concise. However, I would like to point out that the final answer is actually the time it takes Tom to travel back, which is 5 hours, not the total time."* — 验证部分工作同时纠正解读错误。

**反例（看似 verification 但不是）：**
- *"Yes, the answer is 42."* — 这是 **acknowledgment**：确认但没有提供任何实质性检查或推理。

---

### 3. Reasoning Guidance（推理引导）

**定义：** 指令性的：告诉接收方如何处理或分解问题。包括建议方法、策略、分步计划或概念框架。消息引导问题解决过程。

**示例：**
- *"Let's approach this by first finding the rate per hour, then multiplying by total hours."* — 建议解题策略。
- *"We need to solve this in three parts: (1) find the cost per item, (2) calculate the total, (3) apply the discount."* — 将问题分解为子问题。
- *"Let's break down the bird's journey into segments and calculate the distance covered in each segment. First Segment: Direction: South, Time: 10 hours, Speed: 30 mph..."* — 提供结构化的分步推理框架，其中嵌入了计算。

**反例（看似 reasoning_guidance 但不是）：**
- *"The cost per item is $24 / 6 = $4, and the total for 3 items is $12."* — 这是 **information_provision**：提供计算结果，但没有指导如何处理问题。

---

### 4. Information Provision（信息提供）

**定义：** 提供事实、数据、中间计算或部分/最终结果，扩展共享知识状态。消息贡献内容但不指导如何使用。

**示例：**
- *"The answer is $5600."* — 提供最终计算结果。
- *"Each remora is 6 inches long. Since there are 12 inches in a foot, 6 inches / 12 = 0.5 feet. There are 2 remoras, so 2 × 0.5 = 1 foot combined."* — 提供逐步计算，扩展共享状态。
- *"From the problem, we know the rate is 15 miles per hour and the time is 4 hours."* — 陈述题目中的已知量。

**反例（看似 information_provision 但不是）：**
- *"Your solution is correct. The answer is indeed $5600."* — 这是 **verification**：主要功能是确认先前工作的正确性，虽然复述了结果。

---

### 5. Acknowledgment（确认）— 最低优先级

**定义：** 简单的确认、同意或复述，不添加任何新信息、推理或评估。消息只是回应或附和已经说过的内容。

**示例：**
- *"Yes, I agree that 2 + 2 = 4."* — 简单同意，无新内容。
- *"That's correct, the answer is 42."* — 确认但不解释原因或检查工作。
- *"The answer is $5600."*（当前一条消息已经给出相同答案时）— 纯粹的复述。

**反例（看似 acknowledgment 但不是）：**
- *"The solution is correct. However, let me add that step 3 can be simplified by factoring first."* — 这是 **verification**（确认正确性）或 **reasoning_guidance**（建议改进），不是 acknowledgment。

---

## 边界情况

| 情形 | 正确标签 | 原因 |
|------|---------|------|
| 消息包含答案 + "I agree" | 如果答案是新的则为 **information_provision**；如果只是复述则为 **acknowledgment** | 检查答案是否在之前的消息中出现过 |
| 消息说 "Let me verify: [进行计算]" | **verification** | 意图是检查正确性，即使包含计算 |
| 消息说 "Good work! The answer should be computed by..." | **reasoning_guidance** | 关于如何计算的引导优先于开头的确认 |
| 消息说 "I agree, and here's why: [详细解释]" | **verification** | 带有理由的实质性正确性评估 |
| 消息在计划中提供新结果 | **reasoning_guidance** | 计划/框架是主要功能（根据判定规则） |
| 消息提供新结果并检查先前工作 | **verification** | 检查优先于提供新结果 |
| 消息逐字复述上一条答案 | **acknowledgment** | 没有添加新信息 |
| 消息分配新问题去解决 | **coordination** | 管理对话流程，不是在当前任务上做贡献 |

## 判定规则（快速参考）

1. 消息同时提供新结果并检查先前工作 → **verification**
2. 消息提供推理计划并给出新结果 → **reasoning_guidance**
3. 消息确认正确性并给出实质性解释 → **verification**（不是 acknowledgment）
4. 消息仅仅同意或复述而无新信息 → **acknowledgment**
5. 有疑问时，按优先级排序：coordination > verification > reasoning_guidance > information_provision > acknowledgment

## ⚠️ 重点关注的分歧边界

GPT-4o 第三方标注发现以下边界存在系统性分歧，标注时请特别注意：

### Information Provision vs Coordination
- 当 agent "陈述答案"时，是在**提供信息**还是在**协调对话流程**？
- 判定标准：如果消息的核心是传递计算结果或事实 → information_provision；如果消息的核心是推动对话进入下一阶段 → coordination

### Acknowledgment vs Verification
- 当 agent 说 "correct" 或 "I agree" 时，是简单确认还是验证？
- 判定标准：如果只是简单同意而无解释 → acknowledgment；如果包含任何检查或理由 → verification

## 标注流程

1. **阅读上一条消息**（界面中灰色显示）获取上下文
2. **仔细阅读当前消息**
3. **分类**当前消息到 5 个类别之一
4. **设置置信度：**
   - **1** = 不确定，其他类别也合理
   - **2** = 中等信心，一个类别最可能
   - **3** = 非常确定，明确属于某一类别
5. **用备注栏**记录边界情况、不确定性或消息的特殊之处

## 样本信息

- **消息总数：** 225
- **每个 backbone：** Qwen (75)、Gemma (75)、Llama (75)
- **拓扑：** Round-robin（2 个 agent，最多 6 轮）
- **抽样方法：** 每个 backbone 15 个 task，按 task index 早/中/晚分层（每层 5 个），seed=42
- **包含所有 agent 消息**（round > 0；round 0 是初始问题描述）
