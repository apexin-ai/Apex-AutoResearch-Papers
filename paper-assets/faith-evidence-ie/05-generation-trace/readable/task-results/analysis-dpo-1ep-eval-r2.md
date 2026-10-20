# analysis dpo 1ep eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dpo_1ep_eval_r2_20260515T234333_result.json`
- **Structured JSON:** [`f9b20eb081c5d0480809.json`](../../sessions/f9/f9b20eb081c5d0480809.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已在 registry 中，状态 DONE，metrics 已填充。无需更新。

**DPO 1ep eval 结果：**

| Metric | DPO 1ep | DPO 3ep | SFT baseline | Delta vs SFT |
|--------|---------|---------|-------------|-------------|
| rel_f1 | 0.4034 | 0.3429 | 0.4057 | -0.0023 |
| evi_f1 | 0.8088 | 0.8403 | 0.798 | +0.011 |
| EDCR | 0.7139 | 0.7294 | — | — |
| precision | 0.3809 | — | — | — |
| recall | 0.4287 | — | — | — |

**判断：**
- DPO 1ep (0.4034) >> DPO 3ep (0.3429)：过拟合已修复
- DPO 1ep (0.4034) ≈ SFT (0.4057)：本质持平，delta = -0.0023
- Registry 结论 `negative` 合理——DPO 未带来任何增益，只是回到了 SFT 水平

**predictions.json** 已确认存在于 `/root/autodl-tmp/eval_results/dpo_ced_1ep_fixed/`（8.1MB），可供 plan_003 EDCR diagnostic 使用。

---
