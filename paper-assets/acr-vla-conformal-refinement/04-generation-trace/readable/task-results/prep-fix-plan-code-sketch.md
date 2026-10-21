# prep fix plan code sketch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_fix-plan-code-sketch_20260514T073852_result.json`
- **Structured JSON:** [`8d3462c9965cd44a2571.json`](../../sessions/8d/8d3462c9965cd44a2571.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案已写入 `artifacts/fix_plan_code_sketch.md` 并注册。

核心内容：

- **C1**: `load_libero_demos` 额外读 `obs/gripper_qpos`，拼接到 `ee_states` 使其从 6D→8D，消除 train/eval state 维度不一致。需重新 precompute。
- **W2**: CGS `compute_features` 返回 argmin-selected sample 而非 mean 作为 CRM base action，避免多模态下 mean 落入低密度区域。推荐在 CGS 内部改（方案 A）保持训练/评估一致。
- **W3**: alpha 从 0.1 → 0.3。当前 alpha=0.1+K=10 时 quantile index=9（最大值），conformal radius 退化。alpha=0.3 → index=7，适度保守。
- **W4**: CRM forward 加 L2 norm clipping (`max_norm=0.5`) 防止灾难性修正。用 `delta * clamp(norm, max) / norm` 实现，训练推理均生效。

执行顺序：C1(重新precompute) → W2+W3(CGS) → W4(CRM) → 重新训练 → 评估。

---
