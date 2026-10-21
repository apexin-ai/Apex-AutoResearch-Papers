# code openvla eval todo fix

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla_eval_todo_fix_20260523T055542_result.json`
- **Structured JSON:** [`60781e759542926e89de.json`](../../sessions/60/60781e759542926e89de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个 TODO 全部解决，脚本语法正确，无残留 TODO。改动摘要：

| TODO | 解决方案 |
|------|----------|
| **unnorm_key** | 默认 `"bridge_orig"`（BridgeData V2），支持 `"raw"` 跳过反归一化获取 [-1,1] 原始输出 |
| **图像旋转** | 不需要旋转，OpenVLA processor 内部处理 resize 到 224×224，直接传 agentview_image |
| **Rotation 转换** | 新增 `euler_to_axis_angle(roll, pitch, yaw)` 函数，RPY → axis-angle |
| **Action scaling** | position 裁剪到 [-0.05, 0.05]，rotation 裁剪到 [-0.5, 0.5]；gripper 做 `normalize_gripper_action` (binarize [0,1]→[-1,+1]) + `invert_gripper_action`（翻转符号，匹配 OpenVLA 训练约定）|
| **模型路径** | `openvla/openvla-7b` 确认正确 |
| **env 初始化** | 已与 `eval_pi05_safelibero.py` 一致（相同的 env_args、obstacle tracking、collision detection）|

---
