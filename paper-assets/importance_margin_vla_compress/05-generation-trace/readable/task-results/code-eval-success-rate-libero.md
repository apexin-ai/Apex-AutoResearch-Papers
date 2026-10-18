# code eval success rate libero

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_success_rate_libero_20260516T163309_result.json`
- **Structured JSON:** [`cf59915735567e82c68d.json`](../../sessions/cf/cf59915735567e82c68d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完全通过，JSON 输出格式正确。

**总结**：

`eval_success_rate_libero.py` 已完成，核心修复：
1. **Image 180° flip** — `torch.flip(img_t, dims=[2, 3])`，与 `LiberoProcessorStep` 一致
2. **State quat→axis_angle** — 实现 `quat_to_axis_angle()`，提取 8D state `(eef_pos + axis_angle + gripper_qpos)`
3. **Per-suite max episode length** — `SUITE_MAX_STEPS` dict，spatial/object=280, goal=300, long=520
4. **LIBERO benchmark init states** — 使用 `get_task_init_states()` 加载固定初始状态
5. **Per-task language description** — 从 `task.language` 获取，自动加 `\n` 后缀

**Dry-run 结果** (task 0, 3 episodes, max_steps=10):
- env reset/step/close 全部正常
- 模型推理无错误（LoRA checkpoint + LIBERO config 兼容）
- 输出 per-task + overall SR + Wilson CI + JSON

脚本在 westd-27271 的 `/root/autodl-tmp/importance_margin_vla_compress/eval_success_rate_libero.py`，等 cqa1 上 LIBERO checkpoint 可用后即可正式跑评测。

---
