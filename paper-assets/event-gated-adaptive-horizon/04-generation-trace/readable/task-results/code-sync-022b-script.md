# code sync 022b script

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sync-022b-script_20260517T104434_result.json`
- **Structured JSON:** [`7b1cabbfcddd3ee2ec64.json`](../../sessions/7b/7b1cabbfcddd3ee2ec64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成，汇总：

| 检查项 | 结果 |
|--------|------|
| 脚本同步 | `scripts/exp_022b_no_curriculum.sh` 已写入并 `chmod +x` |
| `import dreamer` | 通过（gym deprecation warning 无影响） |
| `gate_curriculum_phase1` 参数 | 存在于 `[defaults]` 配置，默认值 50000，脚本覆盖为 0 |
| logdir 冲突 | 无冲突。exp_022 用 `logdir/exp_022_untrained_dt_emb_learned_gate`，exp_022b 用 `logdir/exp_022b_no_curriculum` |
| exp_022 进程 | **正在运行**（PID 661600，cuda:1，CPU 时间 2142 分钟） |

脚本已就绪，可随时启动 exp_022b。

---
