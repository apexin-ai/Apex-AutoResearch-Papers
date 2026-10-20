# ops d017 ghost cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d017-ghost-cleanup_20260515T035426_result.json`
- **Structured JSON:** [`9b3e907b8a210d6b48e6.json`](../../sessions/9b/9b3e907b8a210d6b48e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### GPU 状态
- GPU 0: PID 274156（rasp v2），GPU 1: PID 276978（standard v2）
- 幽灵进程 PID 277310 **已不存在**

### output_dir 检查
`/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v2/` **未被污染**——仅含空 `completions/` 目录（11:47 创建，与当前进程启动时间吻合），无文件。

### wandb 残留（已清理）
通过检查所有 wandb run 的 `wandb-metadata.json`，定位到幽灵进程的 wandb run：

| 属性 | 值 |
|---|---|
| wandb run_id | `t1q2i5oe` |
| 目录 | `wandb/run-20260515_114702-t1q2i5oe/` |
| run_name | `grpo_stage2_standard_20_v2_debug` |
| 启动时间 | 03:47:02 UTC |
| 大小 | 36K |
| 判定依据 | run_name 含 `_debug` 后缀，与幽灵进程 277310 的 run_name 完全匹配 |

**已删除** `run-20260515_114702-t1q2i5oe/`。`latest-run` 仍正确指向 `iinlgfqk`。剩余 9 个 wandb run 均为合法 run。

---
