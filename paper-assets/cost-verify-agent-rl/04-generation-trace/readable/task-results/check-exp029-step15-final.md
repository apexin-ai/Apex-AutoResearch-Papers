# check exp029 step15 final

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_step15_final_20260517T040803_result.json`
- **Structured JSON:** [`4d0af3c2c746d148b92d.json`](../../sessions/4d/4d0af3c2c746d148b92d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Step 15 val 结果出来了。

## Exp029 Step 15 Validation Results

| Metric | Step 5 | Step 10 | Step 15 |
|--------|--------|---------|---------|
| **val success** | 25.0% | 25.0% | **28.125%** |
| **val pass@1** | 25.0% | 25.0% | **28.125%** |
| **val action_is_valid** | — | 60.19% | **54.52%** |
| **val action_is_effective** | — | 99.94% | **76.72%** |
| **val manager_invalid_action** | — | 0.06% | **23.28%** |

**Pass@N (from best@N reward, reward=10 per success):**
- pass@2: 4.69/10 = **46.9%**
- pass@4: 7.26/10 = **72.6%**
- pass@8: 9.29/10 = **92.9%**
- pass@16: 9.96/10 = **99.6%**

**Train metrics at step 15:**
- train success: 43.75%, train pass@8: 75%

**关键观察：**
- Val success 从 25% 微升至 28.125%（+3.125pp），改善有限
- action_is_valid 从 60.19% 下降到 54.52%，action_is_effective 从 99.94% 大幅下降到 76.72%
- manager_invalid_action 从 0.06% 暴涨到 23.28%，说明模型变得更激进但产生了大量无效动作
- pass@8 = 92.9% 很高，说明模型有能力完成大部分任务，但一致性（pass@1）仍然较低

---
