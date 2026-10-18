# ops fix westd41074 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-westd41074-seed43_20260520T132403_result.json`
- **Structured JSON:** [`fe098394794a5e3f50bd.json`](../../sessions/fe/fe098394794a5e3f50bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已完成操作：**

| 步骤 | 状态 |
|------|------|
| Kill PID 461502 (GPU 0, 错误脚本) | ✅ |
| Kill PID 461577 (GPU 1, 错误脚本) | ✅ |
| 同步 eval_openvla_libero.py 到 westd-41074 | ✅ (288行，base64传输) |
| 搭建依赖 (openvla_deps + openvla-repo) | ✅ |
| 旧实验标记 failed + notes | ✅ |
| 新实验 k=0.7 seed43 v2 (GPU 0, PID 468324) | ✅ RUNNING，`256→179 tokens` |
| 新实验 k=0.5 seed43 v2 (GPU 1, PID 468858) | ✅ RUNNING，`256→128 tokens` |
| Registry 新条目注册 | ✅ |

**注意**：westd-41074 上原本不存在 eval_openvla_libero.py 和 OpenVLA 依赖（openvla_deps/openvla-repo），已从 westd-27271 同步。GPU 2/3 的 M96/M64 训练未受影响。

---
