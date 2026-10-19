# ops bjb1 gpu fix v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-gpu-fix-v2_20260513T052414_result.json`
- **Structured JSON:** [`5d2f39a3654d562cff59.json`](../../sessions/5d/5d2f39a3654d562cff59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 5 步完成，双卡修复成功。**

---

### 执行结果汇总

| Step | 结果 |
|------|------|
| **1. Kill 进程** | tmux sessions (m2_embed_verify, plan_013_starcoder) 已 kill，GPU 残留进程已清除 |
| **2. 验证清空** | nvidia-smi 输出为空，tmux NO_SESSIONS — 双卡完全清空 ✓ |
| **3. 脚本修复** | 两个脚本均添加 `trap 'kill $(jobs -p) 2>/dev/null' EXIT`，参数确认正确，语法检查通过 ✓ |
| **4. 重新提交** | m2_embed_verify → PID 23717 (cuda:1)，plan_013_starcoder → PID 23798 (cuda:0) |
| **5. 启动验证** | 每卡各 1 个进程 ✓，两个 tmux session 运行中 ✓，两个任务均已进入 Epoch 1 训练 ✓ |

GPU 显存占用：
- GPU 0 (plan_013_starcoder): 23558 MiB
- GPU 1 (m2_embed_verify): 40910 MiB

---
