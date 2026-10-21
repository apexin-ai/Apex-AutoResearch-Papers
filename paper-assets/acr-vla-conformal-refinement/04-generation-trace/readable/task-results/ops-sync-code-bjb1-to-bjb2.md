# ops sync code bjb1 to bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync-code-bjb1-to-bjb2_20260514T032005_result.json`
- **Structured JSON:** [`9d86ac7390ed7bf9c283.json`](../../sessions/9d/9d86ac7390ed7bf9c283.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

同步完成。结果汇总：

**MD5 对比（bjb1 → bjb2）**

| 文件 | MD5 | 匹配 |
|------|-----|------|
| evaluate.py | `5da05f00bcdcbafc532cb143325675b6` | ✓ |
| train_crm.py | `fa2073178059cff958c6bf28bbfb2357` | ✓ |
| crm.py | `a76e37e6310980994a87db30a2fdf12f` | ✓ |

**关键功能验证（bjb2）**
- `crm_scalar` 模式：5 处引用 ✓
- `_to_scalar_uf` 函数：L150 定义 + L177 调用 ✓
- `baseline_mode` 参数：4 处引用 ✓
- `MUJOCO_EGL_DEVICE_ID`：L116 ✓

**eval-vla-mean-spatial 进程**：PID 143106 运行 23 分钟，未受影响 ✓

---
