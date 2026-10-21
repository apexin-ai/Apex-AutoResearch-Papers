# diagnose grpo random 20 wandb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_random_20_wandb_20260518T014234_result.json`
- **Structured JSON:** [`5c246b249abcb999efee.json`](../../sessions/5c/5c246b249abcb999efee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整。以下是报告。

---

## grpo_random_20 W&B Metrics 报告

**Run**: `grpo_random_20` | ID: `z9nqlucg` | State: running (实际已被 timeout 杀死)
**记录到 step 90**（logging_steps=10，max_steps=100，缺最后 step 100 的 log）

### Step-level Reward 轨迹

| Step | Reward | Loss | KL | Grad Norm |
|------|--------|---------|--------|-----------|
| 10   | 0.161  | -0.021  | 0.0042 | 3.75  |
| 20   | 0.142  | -0.037  | 0.0047 | 8.63  |
| 30   | 0.166  | 0.003   | 0.0046 | 3.67  |
| 40   | 0.145  | -0.028  | 0.0046 | 4.19  |
| 50   | 0.175  | -0.007  | 0.0046 | 4.75  |
| 60   | 0.184  | -0.032  | 0.0042 | 3.59  |
| 70   | 0.190  | 0.009   | 0.0045 | 7.09  |
| 80   | 0.142  | -0.011  | 0.0049 | 3.69  |
| 90   | 0.173  | 0.037   | 0.0042 | 7.53  |

### Collapse Pattern 判断：**No collapse — flat-low (never learned)**

- Reward 始终在 **0.14–0.19** 窄带内振荡，无上升趋势，也无突降
- KL 极稳定 (~0.004)，说明模型几乎没有偏离 reference policy
- Loss 在 0 附近振荡，无有效学习信号
- 这不是 "collapse"（collapse 意味着先涨后崩），而是 **从未学会** — random pruning 在 20% sparsity 下已破坏模型能力到无法通过 GRPO 恢复的程度

### 与其他实验对比

| 实验 | Pattern | 特征 |
|------|---------|------|
| RASP | Early collapse ~step 10 | 有短暂学习后崩溃 |
| Standard | Late collapse ~step 60 | 持续学习后崩溃 |
| **Random 20%** | **Flat-low (no learning)** | **从未出现有效学习** |

### 建议

- **不需要重跑**。90 步数据已完整覆盖整个训练过程，pattern 清晰：reward 始终 flat-low，无 collapse 转折点。缺失的 step 91-100 不会改变结论。
- 这个结果对论文有价值：random pruning 不仅导致 collapse（如 RASP/Standard），而是**完全阻断了 GRPO 的学习能力**，形成第三种 distinct pattern。

---
