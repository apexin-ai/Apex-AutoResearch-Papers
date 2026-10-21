# diagnose exp029 crash5

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_crash5_20260516T160430_result.json`
- **Structured JSON:** [`86e1f671e5ff039d8c1c.json`](../../sessions/86/86e1f671e5ff039d8c1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 崩溃分析结果

### 崩溃原因
**wandb 写 `/tmp` 临时文件失败**，不是 OOM，不是磁盘满。

完整调用链：
```
agent_trainer.py:1696 fit() → logger.log(metrics, step=0)
  → wandb _log_table_artifact() → artifact.add() → new_file()
    → tempfile.TemporaryDirectory() → mkdtemp() → os.mkdir()
    → FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmpzicbifxf'
```

wandb SDK 在序列化 table artifact 时调用 `tempfile.mkdtemp()`，`os.mkdir('/tmp/tmpzicbifxf')` 失败。说明当时 `/tmp` 目录本身可能被清理或短暂不可用（overlay fs 瞬态问题）。

### 退出前最后完成的阶段
**Step 0 validation 完成，在 wandb 记录 metrics 时崩溃**。最后 metrics（32 episodes）：

| 指标 | 值 |
|------|-----|
| val success rate | **12.5%** (4/32) |
| pass@1 | 12.5% |
| avg num_actions | 44.6 |
| action_is_valid | 78.3% |
| action_is_effective | 100% |
| response_length | 7088 |
| reward mean@32 | 1.25 |
| reward best@32 mean | 9.84 |

### Checkpoint
**无**。目录下只有 `train_restart.log`，没有保存任何 checkpoint（step 0 还没到保存点就崩了）。

### /tmp 当前状态
```
overlay  30G  14G  17G  46% /
```
空间充足。`/tmp` 当前几乎是空的（只有 `ray/` 和 `tmux-0/`），无 `cleanup_loop.log`。

### 修复建议
重启即可。如要防止复发，可在启动脚本中设 `TMPDIR=/root/autodl-tmp/tmp`（数据盘），避免依赖 overlay 的 `/tmp`。

---
