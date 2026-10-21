# analysis eval completeness audit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_completeness_audit_20260524T194425_result.json`
- **Structured JSON:** [`09a20c2eeab6b30455e5.json`](../../sessions/09/09a20c2eeab6b30455e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。关键结论：

**Dose-response 核心 CAR/TSR 覆盖率 = 100%** — 所有条件（Full OCC ×3, Detach ×3, Vanilla ×3, Random OCC ×3, cutoff_15k/25k/35k/45k, reverse_cutoff ×2, Detach+LN ×3, Depth ×4）均有 50r@50000 eval，不阻塞论文图表。

**5 个实验缺 per-task breakdown**（registry 未录入）：
1. ablation_occ_detach_s2（Detach s2）
2. ablation_random_occ_s2（Random s2）
3. cutoff_45k_s0_eval
4. detach_ln_s0_eval
5. vanilla_retrain_s0_eval

这些 per-task 数据很可能在服务器的 eval result JSON 中已存在，只需从 JSON 提取补录到 registry，无需重跑 eval。

**1 个训练实验无 eval**：full_occ_retrain_s0（P2，仅梯度分析参考需要）。

**1 个数据异常**：ablation_occ_detach_s2 的 TSR=0.624 远低于 s0/s1（0.914/0.898），需核查。

---
