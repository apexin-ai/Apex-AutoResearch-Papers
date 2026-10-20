# exp pythia temp eval

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_pythia-temp-eval_20260518T060602_result.json`
- **Structured JSON:** [`58f442836cc62d9c5783.json`](../../sessions/58/58f442836cc62d9c5783.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All results are in. Here's the summary:

---

## Pythia 温度敏感性结果

### 5-fold Stratified CV (within-model)

| 温度 | Binary F1 | 95% CI | entropy_mean ρ |
|------|-----------|--------|----------------|
| 0.5  | **0.8432** | [0.8301, 0.8558] | -0.5844 |
| 0.7  | 0.7389 | [0.7231, 0.7542] | -0.5753 |
| 0.9  | 0.5821 | [0.5655, 0.5985] | -0.3016 |
| 1.0  | — | — | — |

### LOGO (train on other generators, test on Pythia)

| 温度 | Binary F1 | 95% CI |
|------|-----------|--------|
| 0.5  | **0.8136** | [0.7984, 0.8282] |
| 0.7  | 0.7395 | [0.7254, 0.7548] |
| 0.9  | 0.4804 | [0.4645, 0.4976] |

### Qwen LOGO (含新 t=0.9)

| 温度 | Binary F1 | 95% CI | n_test |
|------|-----------|--------|--------|
| 0.5  | 0.7506 | [0.7348, 0.7656] | 3814 |
| 0.7  | 0.7505 | [0.7345, 0.7664] | 3621 |
| 0.9  | 0.5708 | [0.5496, 0.5941] | 1884 ⚠️ |
| 1.0  | 0.3670 | [0.3525, 0.3813] | 3706 |

---

## 关键判断

**t=0.9 vs t=0.7 F1 差值：**
- Pythia 5-CV: **-15.7pp**，LOGO: **-25.9pp**
- Qwen LOGO: **-18.0pp**（但基于部分数据）

**远超 3pp 阈值，不能扩展 claim 到 [0.5, 0.9]。** 深度信号在 t=0.9 显著退化，entropy_mean ρ 从 -0.58 骤降到 -0.30。

## Task B 状态

- **tc_phase3**：55% (545/996)，Qwen t=0.9 生成仍在跑，预计还需约 1 小时
- **feat_qwen_t09**：已完成，但基于部分生成数据 (2413 rows)。tc_phase3 跑完后需要**重新提取特征**
- **Pythia t=1.0**：**不存在生成数据**，需要单独启动生成任务才能填充该行

---
