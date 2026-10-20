# eval ablation occ detach s2 50r retry

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ablation_occ_detach_s2_50r_retry_20260522T210859_result.json`
- **Structured JSON:** [`5c5a06c6d58f2b9a5a54.json`](../../sessions/5c/5c5a06c6d58f2b9a5a54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估已成功启动并在正常运行：

- **PID 60481** 在 GPU 1 (`00000000:38:00.0`)，占用 16760 MiB
- 模型加载完成，已开始 rollout（Task 0, 1/50 完成，~4s/rollout）
- 10 个 task × 50 rollouts，预计 ~35-50 分钟完成

**修正关键**：`MUJOCO_EGL_DEVICE_ID=1`（不是 0）。EGL 设备编号不受 `CUDA_VISIBLE_DEVICES` 影响，仍使用物理设备号。robosuite 的断言做字符串检查 `"1" in "1"` 通过。日志路径：`/tmp/eval_ablation_occ_detach_s2.log`。

---
