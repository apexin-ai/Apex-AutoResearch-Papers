# ops rasp clipped ratio monitor

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rasp-clipped-ratio-monitor_20260514T231735_result.json`
- **Structured JSON:** [`3cdcaf11f794797d12bc.json`](../../sessions/3c/3cdcaf11f794797d12bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Step 10 metrics obtained.** Here's the complete report:

---

## grpo_rasp_20_4096 — 前 10 步指标报告

### 判断：FAIL

### Step 10 完整指标

| 指标 | RASP 4096 (当前) | Standard 4096 (D011) |
|------|:---:|:---:|
| **completions/clipped_ratio** | **1.0** | 0.994 |
| **grad_norm** | **0** | 0 |
| loss | -3.725e-10 | — |
| completions/mean_length | 4096 | 4096 |
| completions/min_length | 4096 | 4096 |
| completions/max_length | 4096 | 4096 |
| mean_terminated_length | **0** | 0 |
| reward | 0.03125 | — |
| reward_std | 0.06972 | — |
| frac_reward_zero_std | 0.925 | — |
| entropy | 0.01547 | — |
| clip_ratio (all) | 0 | — |
| step_time | 170.5s | — |

### 关键发现

1. **clipped_ratio = 1.0**：所有 completion 都撞到 4096 上限，没有任何自然终止。比 Standard (0.994) 还差。

2. **grad_norm = 0**：零梯度信号，GRPO 完全无法学习。

3. **mean_terminated_length = 0**：零 completion 自然终止。

4. **Completion 样本质量极差**：
   - 样本 1：重复循环 "But wait, so the number of chickens after two years is 32. So, 32 chickens. But wait..." 无限重复直到撞 4096
   - 样本 2：退化数字序列 "2.222. 5 1 1 2 2 2 2 2 2 2 2..." — reward=0.00

5. **reward = 0.03125（3.1%）**：有微弱 reward 信号，但因为 clipped_ratio=1 导致 policy gradient 被完全截断，梯度为零。

6. **entropy = 0.01547**：极低，模型 token 分布高度集中（退化生成）。

### 与 RASP 1024 fast run 对比

| 指标 | RASP 1024 | RASP 4096 |
|------|:---:|:---:|
| clipped_ratio | 1.0 | 1.0 |
| grad_norm | 0 | 0 |
| reward | 0.01875 | 0.03125 |
| entropy | 0.03602 | 0.01547 |

4096 没有解决问题。reward 略高（3.1% vs 1.9%），但 clipped_ratio 同样为 1.0，entropy 反而更低。

### 根因分析

RASP 模型虽然在 GSM8K eval 时有 29% accuracy（greedy decoding），但在 GRPO 训练的 sampling 模式下（temperature=0.7, num_generations=4），产出的是退化文本：要么陷入重复循环，要么输出随机数字序列。这些退化 completion 永远无法自然终止（hit EOS），导致 4096 tokens 仍然不够。

核心矛盾：**模型能推理（29% eval），但不能正确终止**。模型在 greedy 模式下表现不同于 sampling 模式——sampling 暴露了剪枝后模型的退化生成问题。

### 预估训练总时长（参考）

500 steps × 173s/step = ~24 小时。但由于 grad_norm=0，跑完也没有意义。

---
