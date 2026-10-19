# fix remove image flip and eval

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_remove_image_flip_and_eval_20260516T125945_result.json`
- **Structured JSON:** [`4c8d3e0e74fd6b4451a9.json`](../../sessions/4c/4c8d3e0e74fd6b4451a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

### 修改确认
- 已去掉 `evaluate_libero_plus.py` 第 211-212 行的 `[::-1, ::-1]` 翻转

### Nominal Eval 结果：**0/5 (0% 成功率)**

| Episode | Steps | Result |
|---------|-------|--------|
| 1       | 220   | FAIL   |
| 2       | 220   | FAIL   |
| 3       | 220   | FAIL   |
| 4       | 220   | FAIL   |
| 5       | 220   | FAIL   |

所有 episode 都跑满 max_steps=220 无法完成任务。

### 前 10 步 Action 值（7D: xyz + rot_axis_angle×3 + gripper）

```
step 0:  [-0.2445, -0.0298,  0.1372,  0.5116,  0.0887, -0.1051, -0.1477]
step 1:  [-0.2568, -0.1730,  0.0070,  0.6510,  0.0999, -0.0896, -0.3992]
step 2:  [-0.2340, -0.2888,  0.0435,  0.6679,  0.0965, -0.0888, -0.2535]
step 3:  [-0.2448, -0.2656,  0.0345,  0.6910,  0.1151, -0.0714, -0.2818]
step 4:  [-0.2691, -0.1568, -0.0514,  0.6053, -0.2759, -0.0864, -0.5848]
step 5:  [-0.0616,  0.0121,  0.6033,  0.2752,  0.2173, -0.0156, -0.6150]
step 6:  [-0.0446,  0.0565,  0.5295,  0.1307,  0.1838, -0.0325, -0.6503]
step 7:  [-0.0279, -0.0879,  0.5858,  0.3049,  0.3966,  0.0013, -0.7712]
step 8:  [-0.0295, -0.1357,  0.6851,  0.2342,  0.2653,  0.0073, -0.6017]
step 9:  [-0.0710, -0.1396,  0.6181,  0.2040,  0.0226, -0.0138, -0.5130]
step 10: [-0.3373, -0.1116,  0.7768,  0.7906, -0.2358, -0.3608, -0.1428]
```

### 关键观察

Action 幅度异常大（0.1~0.8），正常 delta action 应在 0.01~0.05 量级。Norm stats 显示：
- `action_mean[:7] = [0.067, 0.064, -0.805, -2.972, 0.227, 0.119]`
- `action_std[:7] = [0.329, 0.420, 0.617, 0.351, 0.910, 0.344]`

action_mean 第 4 维 = **-2.97** 明显异常。这指向 **norm_stats 与模型输出不匹配** 或 **denormalization 逻辑有误**（使用了 JSON norm_stats with delta transform, action=32D），而非图像翻转问题。

---
