# code exp027 config revision

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp027_config_revision_20260515T140745_result.json`
- **Structured JSON:** [`2997aa3b8510d1b06452.json`](../../sessions/29/2997aa3b8510d1b06452.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry run 通过。修改汇总：

| 参数 | 修改前 | 修改后 |
|------|--------|--------|
| kl_loss_coef | 0.04 | **0.005** |
| train env_groups | 4 | **8** |
| train n_groups | [4] | **[8]** |
| LR | 5e-7 | 5e-7 (不变) |
| entropy_coeff | 0.01 | 0.01 (不变) |
| total_steps | 50 | 50 (不变) |
| save_freq | 5 | 5 (不变) |
| val env_groups | 16 | 16 (不变) |
| W&B | enabled | enabled (不变) |

train env_groups=8 × group_size=16 = **128 rollouts/step**（之前 64）。配置文件顶部注释和启动脚本注释均已更新为 Reviewer-revised 版本。

---
