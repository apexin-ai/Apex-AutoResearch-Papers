# code check camera names eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-camera-names-eval_20260513T191213_result.json`
- **Structured JSON:** [`afc12a4af7f18278119c.json`](../../sessions/af/afc12a4af7f18278119c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整信息已获取。以下是分析报告：

---

## 报告：evaluate.py 中 camera_names 传递问题

### 1. env_args 中未指定 camera_names — **有缺陷**

第104-109行：
```python
env_args = {
    "bddl_file_name": task_bddl,
    "camera_heights": 256,
    "camera_widths": 256,
    "render_gpu_device_id": 0,
}
```

**`camera_names` 未传入。** LIBERO 的 `OffScreenRenderEnv` 默认只渲染 `agentview`，不包含 `robot0_eye_in_hand`。

### 2. obs 获取使用了安全回退 — 掩盖了问题

第125-126行（及144-145、175-176，三个 action selection 函数都一样）：
```python
agentview = obs["agentview_image"]
eye_in_hand = obs.get("robot0_eye_in_hand_image", None)
```

因为 env 没渲染 wrist camera，`obs` 中不会有 `robot0_eye_in_hand_image` 这个 key，`.get()` 静默返回 `None`。

### 3. SmolVLA wrapper 接受 None 的 eye_in_hand — 静默降级

`smolvla_wrapper.py` 第125-126行：
```python
if eye_in_hand_rgb is not None:
    imgs.append(self._preprocess_image(eye_in_hand_rgb))
```

当 `eye_in_hand_rgb=None` 时，SmolVLA 只用 agentview 一个摄像头输入，img_masks 只有一个 True。模型在训练时用了两个摄像头，eval 时只给一个，**性能会显著下降**。

### 4. 修复方案

**第104行，env_args 中添加 `camera_names`：**
```python
env_args = {
    "bddl_file_name": task_bddl,
    "camera_heights": 256,
    "camera_widths": 256,
    "camera_names": ["agentview", "robot0_eye_in_hand"],
    "render_gpu_device_id": 0,
}
```

只需这一行。下游的 `obs.get("robot0_eye_in_hand_image")` 就能拿到数据，SmolVLA wrapper 会自动处理双摄像头输入。

### 结论

**Reviewer 的判断是对的。** `camera_names` 缺失导致 eval 时 SmolVLA 只用单摄像头，而训练时用了双摄像头，这会系统性地压低所有 eval 结果。修复点唯一：`evaluate.py` 第107行插入 `"camera_names": ["agentview", "robot0_eye_in_hand"],`。

---
