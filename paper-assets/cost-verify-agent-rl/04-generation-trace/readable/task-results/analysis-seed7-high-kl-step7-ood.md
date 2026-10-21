# analysis seed7 high kl step7 ood

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed7_high_kl_step7_ood_20260521T233611_result.json`
- **Structured JSON:** [`93d2e46f41811f3499b1.json`](../../sessions/93/93d2e46f41811f3499b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/success。

## 结果摘要

**OOD success rate: 13.43%** (18/134 tasks)

| 指标 | 值 |
|------|-----|
| pass@1 | 13.43% |
| action_is_valid | 72.53% |
| action_is_effective | 99.28% |
| response_length | 7885 |
| num_actions | 44.1 |

### 对比定位

13.43% 落入 **intervention cluster (10–15%)**，与 intervention-c step5 (10.45%) 和 intervention-c step7 (14.93%) 聚在一起，远低于自然训练的 seeds (23–31%)，但仍高于 SFT baseline (5.97%)。

### Hypothesis 验证

**部分 confirmed**。OOD 确实偏低，但原因比 "collapse → low OOD" 更细致：
- Seed 4 同样 collapsed 却拿到 30.6% OOD，说明 collapse 本身不决定 OOD
- 关键区别在于 **训练质量**：Seed 4 跑了 15 步 val=43.75%，seed7_high_kl 只跑 7 步 val=31.25%
- 更准确的 pattern：**policy-constraining interventions (high KL / hard cap) 限制了泛化能力**，形成与自然训练明显分离的 10–15% OOD cluster

### 一个意外发现

action_is_valid 72.53% 是所有 OOD eval 中最高的（与 Seed 5 的 72.66% 并列），说明 high KL penalty 把 policy 正则化到了语法正确但任务完成率低的方向——有效动作多，但不会解题。

报告已写入 `artifacts/seed7_high_kl_step7_ood/analysis.md`。

---
