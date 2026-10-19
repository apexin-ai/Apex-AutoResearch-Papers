# eval spatial reeval fixed

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_spatial-reeval-fixed_20260513T154626_result.json`
- **Structured JSON:** [`e53a43e4631877656b4c.json`](../../sessions/e5/e53a43e4631877656b4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 阶段性报告（3/10 tasks 完成，eval 仍在后台运行）

### 1. camera_names 修复
- **已修复**。evaluate.py 的 env_args 原来缺少 `camera_names`，只渲染 agentview
- 已添加 `"camera_names": ["agentview", "robot0_eye_in_hand"]`
- Smoke test 确认 env 现在返回两个 256×256 图像

### 2. 图像管线确认
- env 渲染 agentview_image + robot0_eye_in_hand_image (256×256)
- 3 个 action 函数（vla_only / crm / reconvla）都正确提取双摄像头图像
- wrapper 对每个图像做 flip + resize_with_pad(512×512) + normalize[-1,1]
- 模型 config 有 3 个 camera slot (camera1/2/3)，`empty_cameras=0`；wrapper 传入 2 个实际图像

### 3. 前 3 个 task 结果（libero_spatial, K=1, 3 rollouts）

| Task | 成功率 |
|------|--------|
| pick_up...between_plate_and_ramekin...place_on_plate | **66.7% (2/3)** |
| pick_up...next_to_ramekin...place_on_plate | **66.7% (2/3)** |
| pick_up...from_table_center...place_on_plate | **33.3% (1/3)** |
| **累计** | **55.6% (5/9)** |

### 4. 关键结论

**从 0% → 55.6%，bug 修复有效。** 之前完全失败是因为：
- 缺少 eye_in_hand 摄像头（本次修复）
- 图像预处理 6 项错误（之前诊断 Worker 修复）

### 5. 后续

- Eval 仍在后台运行（PID 87385），10 个 task × 3 rollouts，预计还需 ~1.5 小时
- 结果会写入 `/root/acr-vla-conformal-refinement/artifacts/eval_spatial_k1.json`
- 当前 55.6% 是 K=1 单样本结果（无 averaging）；K=10 取均值会更稳定
- SmolVLA 论文报告 libero_spatial 的 baseline 约 78-85%（20 rollouts），当前 3 rollouts 结果波动较大

如需等完整结果，我继续轮询；或者你可以后续手动检查 `tail /tmp/eval_spatial.log` 和 JSON 文件。

---
