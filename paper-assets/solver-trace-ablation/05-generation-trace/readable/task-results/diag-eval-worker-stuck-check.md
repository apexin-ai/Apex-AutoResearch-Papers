# diag eval worker stuck check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-worker-stuck-check_20260514T031119_result.json`
- **Structured JSON:** [`d8fca5ea974e6ae52af7.json`](../../sessions/d8/d8fca5ea974e6ae52af7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

### 进程状态

| 任务 | 状态 | 详情 |
|------|------|------|
| **plan001-exec-only-s43-r4** | **已完成** | 500/500 steps，日志最后修改 11:12:03（约30分钟前）。耗时 ~1h31m。无 exit marker 文件写入。 |
| **plan002-additive-b03-s42** | **在跑** | 当前 step 394/500（79%），日志仍在更新。 |
| **eval_sta.py** | **未运行** | 无 eval_sta 进程。 |

### GPU 使用

| GPU | 利用率 | 显存 |
|-----|--------|------|
| GPU 0 | 94% | 80077 / 97887 MiB |
| GPU 1 | 90% | 80291 / 97887 MiB |

两张 GPU 均高负载，应该是 plan002 在用（或 plan001-r4 训练完成后模型保存/checkpoint 进程还在）。

### 结论

**eval worker 卡死原因**：plan001-s43-r4 训练已完成（500/500），但 `/tmp/agent-ml-exit/plan001-exec-only-s43-r4.exit` **未写入**。eval worker 很可能在轮询这个 exit marker 等待训练完成信号，因此一直卡住。

**建议**：手动创建 exit marker 文件（`touch /tmp/agent-ml-exit/plan001-exec-only-s43-r4.exit`）触发 eval worker 继续，或者直接取消 eval worker 重新启动评估。

---
