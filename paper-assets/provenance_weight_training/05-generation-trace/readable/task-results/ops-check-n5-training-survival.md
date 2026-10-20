# ops check n5 training survival

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_n5_training_survival_20260524T061314_result.json`
- **Structured JSON:** [`8cc3ad3728400c85391f.json`](../../sessions/8c/8cc3ad3728400c85391f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果：4 个训练全部存活，无需重启

| 实验 | PID | GPU | 进度 | 已运行 | 预计剩余 | 状态 |
|------|-----|-----|------|--------|---------|------|
| adaptive_seed789 | 922510 | cuda:0, 100% | 2445/6103 (40%) | 1h30m | ~2h18m | **存活** |
| uniform_seed789 | 922589 | cuda:1, 100% | 2592/6103 (42%) | 1h30m | ~2h02m | **存活** |
| adaptive_seed234 | 922738 | cuda:2, 97% | 2446/6103 (40%) | 1h30m | ~2h17m | **存活** |
| uniform_seed234 | 923155 | cuda:3, 100% | 2592/6103 (42%) | 1h30m | ~2h02m | **存活** |

**GPU 占用**：4 卡各 ~45.6GB / 97.9GB VRAM，利用率 97-100%。

**服务器实际未重启** — 从 `ps` 输出看，init 进程 (PID 1) 启动时间是 May16，4 个训练进程启动时间是 12:42-12:43（今天），tmux session 也存活。训练在正常推进中，预计约 2h 后全部完成。

---
