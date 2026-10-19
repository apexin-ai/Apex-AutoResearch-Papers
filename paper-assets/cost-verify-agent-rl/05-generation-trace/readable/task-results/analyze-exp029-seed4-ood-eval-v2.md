# analyze exp029 seed4 ood eval v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp029_seed4_ood_eval_v2_20260521T221757_result.json`
- **Structured JSON:** [`134f4073b9e19020dd19.json`](../../sessions/13/134f4073b9e19020dd19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/exp029_seed4_ood_eval_v2/report/exp029_seed4_ood_eval_v2_analysis.md`。

## 结果

**OOD success rate: 30.60% (41/134)**——目前所有 seed 中最高。

Cross-seed 对比：

| Seed | OOD | 状态 |
|------|-----|------|
| SFT baseline | 5.97% | — |
| Seed 3 | 10.45% | success |
| Seed 1 | 23.88% | success |
| Seed 5 step10 | 29.10% | OOM killed |
| Seed 6 | 29.10% | success |
| **Seed 4 step15** | **30.60%** | **collapse** |

**Hypothesis 成立**。Collapse seed 不仅有 OOD 泛化，而且比所有正常 seed 都强。代价是 response_length 膨胀到 7212 tokens，action_is_valid 仅 63.67%——模型用更长的输出"暴力搜索"动作空间，虽然训练集上退化（pass@1=0.4375），但 OOD 场景下这种过度探索反而带来更好覆盖。

---
