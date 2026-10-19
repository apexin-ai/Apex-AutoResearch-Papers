# fix per step objects layout

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_per-step-objects-layout_20260515T153327_result.json`
- **Structured JSON:** [`516efd3d98e43b19f041.json`](../../sessions/51/516efd3d98e43b19f041.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收集完成，验证通过。

## 结果总结

**根因**：不是脚本 bug。原始 `collect_per_step.py` 按顺序收集 6 个 perturbation 类型，objects_layout 排第 5。之前的运行被中断（留下 1.3KB 空文件），新运行在 sensor_noise（第 4 个）时还没到 objects_layout。

**产出**：
- 文件：`/root/meta_brain_lora_routing/activations/per_step/objects_layout.pt`
- 大小：**294MB**（之前 1.3KB）
- Episodes：**32 个**（90 次尝试，58 次因 LIBERO-Plus 的 `new_objects` asset 缺失跳过）
- 每 episode 44 个 replan points
- 包含 12 层激活（8 PaliGemma + 4 Expert）
- labels：label_6class=4, label_3class=1, label_binary=1

**附注**：sensor_noise 和 robot_initial_states 的 per_step 文件同样是空的（之前中断残留）。如需收集，可用同样的脚本 `python collect_per_step_single.py --ptype sensor_noise --num_episodes 90`。

---
