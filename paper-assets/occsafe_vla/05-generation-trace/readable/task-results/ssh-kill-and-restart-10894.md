# ssh kill and restart 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-and-restart-10894_20260528T230841_result.json`
- **Structured JSON:** [`11bf98fcc46bb19c0456.json`](../../sessions/11/11bf98fcc46bb19c0456.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终结果：✅ 成功

全部验证通过：

| 检查项 | 结果 |
|--------|------|
| GPU 进程 | PID 49565, 占用 62194 MiB ✅ |
| OCC 数据加载 | Loaded occ index: 9 tasks, preload done: 9 files, 55370 条 ✅ |
| occ_loss | step=0, occ_loss=0.1068 > 0 ✅ |
| 错误检查 | 仅 TensorFlow CropAndResize cost estimator 警告（无害），无 Traceback/Exception/Crash ✅ |

训练 `random_occ_v2_s0_r4` 已在 westd-10894 cuda:0 上正常运行。

---
