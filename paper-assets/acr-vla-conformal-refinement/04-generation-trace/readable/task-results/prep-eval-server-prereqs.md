# prep eval server prereqs

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_eval-server-prereqs_20260521T174612_result.json`
- **Structured JSON:** [`af9c690b2a822081ae82.json`](../../sessions/af/af9c690b2a822081ae82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总：三台服务器准备状态

| 项目 | bjb1-18228 | bjb1-32546 | bjb2-28827 |
|------|-----------|-----------|-----------|
| **evaluate.py 版本** | 33058 bytes ✅ | 33058 bytes ✅ | 33058 bytes ✅（已通过控制节点 rsync 同步） |
| **π0.5 模型** | ✅ 存在，model.safetensors 7.47GB | ✅ 存在，model.safetensors 7.47GB | ✅ 存在，model.safetensors 7.47GB |
| **mujoco** | 3.8.1 ✅ | 3.8.1 ✅ | 3.8.1 ✅ |

### 需要注意的问题
1. **bjb2-28827 的 git 没有 remote**：只有一个本地 initial commit，无法 git pull。本次通过控制节点 rsync 从 bjb1-18228 中转同步。后续代码更新也需要走这个路径。
2. **bjb1-18228 和 bjb1-32546 完全没有 .git 目录**：代码历史上都是通过 rsync 部署的。

三台服务器均已就绪，可以部署 eval runs。

---
