# fix adaptive fix final cleanup resubmit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_adaptive_fix_final_cleanup_resubmit_20260514T175044_result.json`
- **Structured JSON:** [`84112b7d0038a3c21034.json`](../../sessions/84/84112b7d0038a3c21034.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。从 registry 历史可以看到之前的失败原因。

## 汇总

### 诊断：之前 EXIT_CODE=2 的原因

Registry 记录 `failure_reason: "EXIT_CODE=2 (shell misuse / syntax)"`。从 seed456 的 reproduce 记录看，之前的命令包含 `--eval_data_path data/human/eval_holdout.jsonl` 和 `--eval_steps 500`，这些参数在后续修改中被去掉了。EXIT_CODE=2 通常是 argparse 参数解析失败（unrecognized arguments）或 shell 语法错误。**最可能的原因是之前的命令带了脚本不识别的参数（如 --eval_data_path / --eval_steps），导致 argparse 以 exit code 2 退出。**

当前版本的命令已去掉这些参数，于 01:47 UTC 重新提交后成功运行。

### 当前状态

| GPU | 实验 | Python PID | 恢复自 checkpoint | 当前进度 | 异常 |
|-----|------|------------|-------------------|----------|------|
| cuda:0 | grid_b_seed42_batch | 112475 | - | 运行中（不动） | 无 |
| cuda:1 | adaptive_fix_seed42 | 126801 | checkpoint-1500 | ~1602/6103 (26%) | 无 |
| cuda:2 | adaptive_fix_seed123 | 126944 | checkpoint-1500 | ~1600/6103 (26%) | 无 |
| cuda:3 | adaptive_fix_seed456 | 127285 | checkpoint-1000 | ~1098/6103 (18%) | 无 |

Registry 中 status 仍为 RUNNING，notes 已更新。注意 conclusion 字段显示 "failed"（来自之前的失败），registry 的状态转换验证可能不允许直接改——需要你手动处理。

---
