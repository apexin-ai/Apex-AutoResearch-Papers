# analysis c prime step5 ood bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c_prime_step5_ood_bjb1_20260522T010546_result.json`
- **Structured JSON:** [`bf17a6ccc4fea1e0c0a5.json`](../../sessions/bf/bf17a6ccc4fea1e0c0a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE. Here's the summary for Director:

---

## c_prime_step5_ood_bjb1 结果摘要

**OOD 成功率: 0.0% (0/134)** — 所有 134 个 valid_unseen 任务全部失败。

| 指标 | 值 |
|------|-----|
| success_rate | **0.00%** |
| pass@1 | 0.00% |
| action_is_valid | 97.57% |
| action_is_effective | 100% |
| num_actions | 50 (每集都撞上限) |
| response_length | 4250 |
| avg_reward | 0.0 |

**对比其他 OOD 结果:**

| Checkpoint | OOD Success |
|------------|-------------|
| SFT baseline | 5.97% |
| Intervention C step5 | 10.45% |
| Seed 7 high-KL step5 | 9.70% |
| Intervention C step7 | 14.93% |
| Seed 1 | 23.88% |
| Seed 4 (collapsed) | 30.60% |
| **C' step5** | **0.00%** |

**关键发现:** C' step5 是所有 checkpoint 中 OOD 最差的，甚至低于 SFT baseline (5.97%)。模型生成的 action 语法合法 (valid 97.6%)，但在 OOD 场景下完全无法完成任务——每集都耗尽 50 步上限。val 21.875% 的成绩完全没有泛化到 OOD。response_length 从 val 的 8327 骤降至 4250，说明模型在 OOD 环境中生成了更短但无效的推理。

**结论:** trajectory cap 12000 虽然在训练中未实际触发（aborted_ratio=0），但 C' 训练出的策略严重过拟合训练分布，OOD 泛化能力为零。

---
