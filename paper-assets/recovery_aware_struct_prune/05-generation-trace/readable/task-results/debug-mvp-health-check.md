# debug mvp health check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_mvp-health-check_20260514T044623_result.json`
- **Structured JSON:** [`cd740fb658a252e4627e.json`](../../sessions/cd/cd740fb658a252e4627e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 状态总结

| 项目 | 状态 |
|------|------|
| tmux session | 不存在（进程已死） |
| GPU 0 | 0% util, 0 MiB |
| GPU 1 | 0% util, 0 MiB |
| PID 150792 | 不存在 |
| 训练进程 | 无（仅有模型下载进程在跑） |

### 崩溃根因

**Standard pruning (cuda:0) 在 Step 3 forward pass 验证时失败**：

```
RuntimeError: Pruned model forward pass failed: Number of heads in key and value must divide the number of heads in query
```

`prune.py:387` — standard 模式按全局 importance 排序剪枝 Q heads，但没有保持 GQA 的 Q/KV head 整除约束。剪完之后某些层的 Q heads 数量无法被 KV heads 整除，导致 `scaled_dot_product_attention` 报错。

**RASP pruning (cuda:1) 成功**，`models/pruned_rasp_35` 已保存（含 config.json）。

**Pipeline 未能捕获失败**：`run_mvp.sh` 用 `wait $PID_STD $PID_RASP`，`wait` 返回最后一个 PID 的退出码（RASP 成功=0），所以 `set -e` 没触发，Pipeline 继续到 Step 4 试图加载不存在的 `models/pruned_standard_35`，再次崩溃。

### 需要修复的问题

1. **`prune.py` GQA 约束**：`compute_pruning_masks` 需要确保每层剪枝后的 Q head 数仍能被剩余 KV head 数整除。最简单的方式是按 KV group 为单位剪枝（一个 KV group 内的所有 Q heads 一起剪或一起留）。

2. **`run_mvp.sh` 错误处理**：改为分别 wait 并检查退出码：
   ```bash
   wait $PID_STD || { echo "Standard pruning FAILED"; exit 1; }
   wait $PID_RASP || { echo "RASP pruning FAILED"; exit 1; }
   ```

等待你的指令决定是否修复并重启。

---
