# research baseline diagnosis

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_baseline-diagnosis_20260512T123300_result.json`
- **Structured JSON:** [`646e5242f2c97cd80034.json`](../../sessions/64/646e5242f2c97cd80034.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据非常完整。由于 vLLM engine core 已 defunct，默认 prompt 对比实验无法完成。基于已有数据编写诊断报告。

---

## 诊断报告：Baseline question_rate=65% 异常高的根因分析

### 1. 检测器 Precision 抽检

**数据源**: 全量实验 trace（9 条完整对话，82 个 user turns）

| 指标 | 值 |
|------|-----|
| Total user turns | 82 |
| Turns detected as question | 42 (51.2%) |
| Mean question_rate (per-trace) | 0.588 ± 0.219 |

**被检测为 "question" 的 42 个 turn 的语义分类：**

| 类别 | 数量 | 占比 | 说明 |
|------|------|------|------|
| **polite_request** | 21 | 50% | "Can you check...?", "Could you help...?" — 动作请求，非信息寻求 |
| **confirmation** | 13 | 31% | "Is that correct?", "Can we proceed?" — 确认/推进请求 |
| **info_seeking** | 8 | 19% | "What color options are available?", "How much will it cost?" — 真正的信息查询 |

**Precision = 8/42 = 19.0%**（仅以信息寻求型问题为 true positive）

### 2. False Positive 的典型模式

三类占 81% 的 false positive：

1. **Polite request**（50%）：LLM 用 "Can you...?", "Could you please...?" 形式提出每一个动作请求。真实用户更倾向于直接陈述 "I want to cancel the order"，而不是 "Can you cancel the order for me?"

2. **Confirmation request**（31%）：LLM 在对话推进中反复使用 "Is that right?", "Can we go ahead?", "Shall I confirm?" 等确认式问句。真实用户通常直接说 "Yes, proceed" 或 "Confirmed"。

3. **模式根源**：Qwen 2.5 7B 的 instruction-tuning 偏向产生 **过度礼貌、interrogative** 的输出，这与客服场景叠加放大。

### 3. 默认 Prompt 对比

**无法完成**。vLLM engine core 进程（PID 76139）已 defunct（zombie state），全量实验自 20:16 起也在无限重试 `/chat/completions`。需要重启 vLLM 才能继续。

但从 prompt 分析可以推断：
- τ-Bench 默认 prompt："You are a user interacting with an agent" — 角色设定中性
- DemoCalib base prompt："You are a customer of an online retail store" — 明确客户角色

两者**都没有约束 question 比例**，因此在 Qwen 模型下预期 question_rate 都会远超真实用户。差异主要在措辞风格而非 question 频率。

### 4. 结论

| 假说 | 结论 |
|------|------|
| 检测器 false positive | **部分成立**。检测器匹配所有 `?` 结尾句子，但 81% 是 polite request/confirmation 而非信息寻求型问题。如果目标是测量 "questioning behavior"（如 Seshadri 定义），需要区分 request vs genuine question。 |
| Prompt 问题 | **不是主因**。base prompt 没有抬高 question rate 的指令。 |
| 模型/任务特性 | **主因**。Qwen 2.5 7B 的 instruction-following 偏好产生 interrogative 形式的输出（"Can you...?"），叠加客服场景本身鼓励礼貌表达，导致约 50% 的 user turn 包含 `?`。Seshadri 论文的 18.8% 测自真实人类用户——真人远不会如此频繁地用问句形式。 |

### 建议（如需改进）

1. **检测器改进**：过滤掉 modal verb request pattern（`Can/Could/Would you + VP + ?`），只计入 wh-question 和 yes/no 信息查询
2. **Prompt calibration**：在 user simulator prompt 中加入 "State requests directly rather than asking — say 'Cancel my order' instead of 'Can you cancel my order?'"
3. **vLLM 需重启**：engine core defunct，全量实验已停滞约 25 分钟

---
