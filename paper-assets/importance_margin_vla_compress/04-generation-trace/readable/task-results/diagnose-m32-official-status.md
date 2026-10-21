# diagnose m32 official status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_m32_official_status_20260519T035051_result.json`
- **Structured JSON:** [`77c84a0fd27f1984d235.json`](../../sessions/77/77c84a0fd27f1984d235.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断完成

**结论：训练正常运行中，非异常退出。**

- 进程通过 nohup 后台运行（PID 742212），tmux session 不存在是因为启动方式不同，不代表进程退出
- 当前进度 **23,900/100,000**（23.9%），预计还需 ~5.2 小时完成
- Loss 稳定在 0.05-0.19 范围，训练正常
- **已知问题**：checkpoint 保存在 `/root/checkpoints/smart_compress_m32_official/` 而非项目目录，训练结束后需手动移动
- Registry 已更新：状态 RUNNING，notes 中记录了 CWD 问题和当前进度

---
