# fix egl render gpu bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_egl-render-gpu-bjb1_20260514T000635_result.json`
- **Structured JSON:** [`c3ffc186c83ec01f851d.json`](../../sessions/c3/c3ffc186c83ec01f851d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。

**修改摘要**：

| | 内容 |
|---|---|
| **文件** | `/root/acr-vla-conformal-refinement/src/evaluate.py` |
| **行号** | 第 113 行 |
| **修改前** | `"render_gpu_device_id": 0,` |
| **修改后** | `"render_gpu_device_id": int(os.environ.get("MUJOCO_EGL_DEVICE_ID", "0")),` |
| **`import os`** | 已存在（第 31 行），无需添加 |

运行中的进程未受影响，它们使用的是已加载的旧代码。新启动的评估进程将从 `MUJOCO_EGL_DEVICE_ID` 环境变量读取渲染 GPU ID。

---
