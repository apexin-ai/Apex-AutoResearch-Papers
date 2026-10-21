# diagnose factorial seed2 exit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_factorial-seed2-exit_20260518T224538_result.json`
- **Structured JSON:** [`e9cd5525976e07210089.json`](../../sessions/e9/e9cd5525976e07210089.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**退出原因：正常完成（success）**

实验跑完了全部 15 steps，进度条显示 `14/15`（0-indexed，即 step 15 已完成）。日志中有完整的 step 15 metrics 输出和 checkpoint 保存记录。尾部的 `BrokenPipeError` 仅是 W&B atexit teardown 的无害异常，不影响训练。

### Step 15 关键 Metrics

| Metric | 值 |
|---|---|
| **train success rate** | 55.5% |
| **train pass@8** | 87.5% |
| **val OOD success (pass@1)** | 0.75% |
| **val OOD action_is_valid** | 17.3% |
| **KL divergence (ppo_kl)** | 0.618 |
| **KL loss** | 5.905 |
| **val-core reward mean@6688** | 0.057 |

### Checkpoint 状态

完整保存，3 个 checkpoint（step 5/10/15），step 15 包含完整的 model、optim、extra_state（2-rank FSDP），总大小约 20GB。

### 关键观察

- Train success 55.5% 表明训练分布上有明显学习
- **Val OOD success 仅 0.75%**，泛化极差，与 train 55.5% 形成巨大 gap
- Val OOD action_is_valid 仅 17.3%（train 68.7%），说明 OOD 任务上模型生成的动作大部分无效
- KL = 0.618 处于合理范围，未爆炸

---
