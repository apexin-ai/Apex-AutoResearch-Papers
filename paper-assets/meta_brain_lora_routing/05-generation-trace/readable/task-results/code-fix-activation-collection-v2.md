# code fix activation collection v2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_activation_collection_v2_20260516T212711_result.json`
- **Structured JSON:** [`511e114853f5ec4e5d77.json`](../../sessions/51/511e114853f5ec4e5d77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

**3 个 Bug 已修复：**
1. `torch._dynamo.config.suppress_errors` 改为 `False`
2. `model(obs_b, actions_b)` → `model.sample_actions(device, obs_b, num_steps=1)` (inference path，无需 ground truth actions)
3. Layer path 加了 `.model.`：`paligemma_with_expert.paligemma.model.language_model.layers.6`

**Dry run 结果：**
- 5/5 forward pass 成功，0 errors
- Hook 正确触发，activation shape = `(2048,)` (PaliGemma hidden dim)
- 非零 activation，norm ~2100-2650，符合预期

---
