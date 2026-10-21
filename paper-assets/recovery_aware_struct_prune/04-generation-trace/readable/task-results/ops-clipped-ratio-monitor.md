# ops clipped ratio monitor

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_clipped-ratio-monitor_20260514T224349_result.json`
- **Structured JSON:** [`cd09a17a0cd6556bde4b.json`](../../sessions/cd/cd09a17a0cd6556bde4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 监测报告：grpo_standard_20_4096 前 10 步

### 判断：**FAIL** — `completions/clipped_ratio = 0.9938`

4096 长度仍然不够。情况与 D009（1024 限制）本质相同。

### 关键指标

| 指标 | 值 | 含义 |
|------|-----|------|
| `completions/clipped_ratio` | **0.9938** | 99.4% 被截断，远超 0.95 阈值 |
| `completions/mean_length` | 4089 | 均值接近 4096 上限 |
| `completions/mean_terminated_length` | 294.9 | 仅 ~0.6% 自然终止（约 295 token） |
| `loss` | -1.863e-10 | 有效为零 |
| `grad_norm` | 0 | **零梯度，无学习** |
| `reward` | 0.00625 | ~1/160 答对率 |
| `frac_reward_zero_std` | 0.975 | 97.5% prompt 各 generation 分数相同 |

### Completion 样本

模型输出全是无意义重复数字：
- `"Gary currently has 15.110.75111111111111…"` → reward 0.00
- `"Gary, 120. But 51.112222222222222222…"` → reward 0.00

### 根因分析

**问题不是 max_completion_length 不够，而是模型太弱。** pruned_standard_20 准确率仅 1%，模型已丧失：
1. 生成结构化推理的能力
2. 正确产出 EOS token 的能力
3. 形成连贯句子的能力

模型只是生成重复 token 填满整个窗口。即使设 8192/16384 也无济于事。

### 额外风险

Reward desert callback 不会触发——reward=0.00625≠0（有极少数偶然答对），训练会持续跑满 500 步，浪费约 24 小时 GPU 时间。

### grpo_rasp_20_4096 状态

尚未启动（无日志文件）。

### 建议

1. **停止 grpo_standard_20_4096**——继续训练无意义
2. **GRPO 无法直接恢复 1% accuracy 的模型**——需要 SFT warmup 先教模型基本回答格式
3. 或者：使用剪枝更少的模型（如 10% 剪枝而非 20%）

---
