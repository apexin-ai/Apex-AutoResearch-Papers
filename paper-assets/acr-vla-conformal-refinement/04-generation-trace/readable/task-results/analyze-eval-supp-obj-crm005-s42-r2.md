# analyze eval supp obj crm005 s42 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-obj-crm005-s42-r2_20260523T063828_result.json`
- **Structured JSON:** [`5dda81b1239b8727a2f8.json`](../../sessions/5d/5dda81b1239b8727a2f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**实验 eval-supp-obj-crm005-s42-r2 结果汇总：**

- **Overall SR: 77.0% (154/200)**，10 tasks × 20 rollouts，完整跑完无异常
- **CRM 配置**: mode=crm_obs_only, norm=0.05, conformal_threshold=0.074855, K=10
- **Per-task SR 范围**: 70%–90%，最高 bbq_sauce (90%)，最低四个 task 并列 70%
- **耗时**: ~2.46 GPU-hours (wall clock 8873s)

**待定**: Object VLA-only baseline (r2) 跑完后需要对比，才能确认 CRM norm=0.05 在 Object suite 的增益幅度。Goal suite CRM norm=0.05 为 85.5%，Spatial 为 80% (+1.5pp)。Object 的 77% 看起来合理但需 baseline 才能判断 delta。

---
