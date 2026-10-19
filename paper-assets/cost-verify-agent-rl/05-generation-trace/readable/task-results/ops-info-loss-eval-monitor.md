# ops info loss eval monitor

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_info-loss-eval-monitor_20260520T143222_result.json`
- **Structured JSON:** [`3008a5053bed496c4068.json`](../../sessions/30/3008a5053bed496c4068.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程状态**: 存活，PID **875971**

| 项目 | 值 |
|------|-----|
| PID | 875971 |
| 启动时间 | 22:23 (约 10 分钟前) |
| CPU 占用 | 74.5% |
| 命令 | `eval_scienceworld_info_loss.py --checkpoint qwen3_scienceworld_sft --temperature 0 --history_length -1 --tensor_parallel_size 2 --max_model_len 16384` |
| 进度 | **5/89 episodes** 完成 |
| 输出文件 | `/root/autodl-tmp/eval_info_loss/scienceworld_full_t0.jsonl` (743 bytes) |

**最新 5 episodes 结果**:
- `[1/89] FAIL(37)` boil v14 — 100 steps, valid=15%, fmt=19%, 121.4s
- `[2/89] FAIL(3)` boil v15 — 100 steps, valid=14%, fmt=18%, 121.9s
- `[3/89] FAIL(3)` boil v16 — 100 steps, valid=50%, fmt=92%, 142.1s
- `[4/89] FAIL(3)` change-the-state-of-matter-of v14 — 100 steps, valid=14%, fmt=18%, 123.3s
- `[5/89] OK` change-the-state-of-matter-of v15 — 22 steps, valid=77%, fmt=100%, 9.8s

按每 episode ~120s 估算，剩余 84 episodes 约需 **~2.8 小时**完成。

另外注意：同一服务器上还有一个 ScienceWorld GRPO 训练进程在跑（PID 766825, `train.py --config-name _scienceworld_cell_c_grpo`）。

---
