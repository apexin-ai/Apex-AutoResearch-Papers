# code urgent kill restart launch a1

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent_kill_restart_launch_a1_20260519T222705_result.json`
- **Structured JSON:** [`ddab9d862f2b4facfb3d.json`](../../sessions/dd/ddab9d862f2b4facfb3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。总结：

| 任务 | 结果 |
|------|------|
| Kill seed 0 (PID 49555) | ✅ 已终止 |
| extra_delta_transform 修复 | 代码已是 `False`，无需改动。旧进程用的是过时代码 |
| seed 1 + object_pudding 验证 | ✅ 均无 bug，loss 正常，保留运行 |
| seed 0 重启 | ✅ PID 100319，前 10 步 loss ~0.2 |
| A1 LoRA 修复 | ✅ `on_step_start` 改为只解冻 `"lora" in name.lower()` 的参数 |
| A1 启动 | ✅ PID 101662 (cuda:3)，loss ~0.2，VRAM 仅 13.4 GB |

4 卡全部在跑。注意事项：
- 训练环境是 `conda activate libero`（不是 base）
- 现有 baselines 使用 `WANDB_MODE=disabled`
- A1 的 Phase 2 trainable param 数量会在 step 5000 时打印到日志，届时可验证 LoRA params 计数是否 ~26M

---
