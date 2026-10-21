# fix pi05 gpu param bug

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_pi05-gpu-param-bug_20260525T214030_result.json`
- **Structured JSON:** [`12ace930d09a9a8f8969.json`](../../sessions/12/12ace930d09a9a8f8969.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器都没有 git repo。本地也不存在 `eval_pi05_pruning_libero.py` 文件。

## 完成情况

| 步骤 | 状态 |
|------|------|
| **修复 cqa1-33015** | ✅ 第 183 行 `DEVICE = "cuda:0"` → `DEVICE = f"cuda:{args.gpu}"` |
| **修复 westd-41074** | ✅ 第 151 行同样修复 |
| **k=0.75 实验 (PID 775730)** | ✅ 存活，GPU0 占用 10464 MiB，利用率 94%，正常运行中，让它跑完 |
| **本地 git commit** | ⚠️ 无法执行 — 本地和远程均无此文件的 git repo |

k=0.75 实验虽然跑在 cuda:0 而非指定 GPU，但计算结果不受影响，无需重启。修复已生效，后续新启动的实验会正确使用 `--gpu` 参数。

本地 git commit 需要你手动处理：远程服务器上的项目目录不是 git repo，本地 artifacts 目录也没有这个脚本的副本。如果有其他 git repo 包含此文件，请告知路径。

---
