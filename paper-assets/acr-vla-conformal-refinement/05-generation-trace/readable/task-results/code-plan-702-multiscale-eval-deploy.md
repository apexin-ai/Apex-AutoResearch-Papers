# code plan 702 multiscale eval deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_702-multiscale-eval-deploy_20260517T182030_result.json`
- **Structured JSON:** [`fddcf74d911cc36964b4.json`](../../sessions/fd/fddcf74d911cc36964b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。3 个 seed 都已启动 rollout，multi-scale 特征提取正常工作。

**部署总结**：

| Seed | Server | GPU | PID | 状态 |
|------|--------|-----|-----|------|
| 42 | bjb2-28827 | cuda:0 | 455518 | rollout 进行中 |
| 43 | bjb1-32546 | cuda:1 | 503178 | rollout 进行中 |
| 44 | bjb1-32546 | cuda:4 | 504682 | rollout 进行中 |

**关键改动**：
- `evaluate.py` 的 `select_action_crm_k1_accg` 从 fallback（单 960D 特征）改为真正的 multi-scale 模式：通过 `MultiScaleFeatureExtractor` hooks 从 VLM layers [3,7,11,15] 提取 4×960D 特征，传入 `MultiScaleCRM.forward` 的 multi-scale 分支（带 learned layer importance weighting）
- bjb1-32546 上的 checkpoint 是旧的未训练版本，已将训练好的 checkpoint 另存为 `crm_k1_best_multiscale.pt`，未覆盖原有文件
- bjb1-32546 GPU 共享运行（与既有 eval 共享 GPU 1 和 4），资源充裕（24GB VRAM，128 CPU，1TB RAM）

---
