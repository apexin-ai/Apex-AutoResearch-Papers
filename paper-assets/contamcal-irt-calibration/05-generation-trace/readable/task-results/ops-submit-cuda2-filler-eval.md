# ops submit cuda2 filler eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit-cuda2-filler-eval_20260515T051633_result.json`
- **Structured JSON:** [`0651fb2efc8d5ded9a0b.json`](../../sessions/06/0651fb2efc8d5ded9a0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**情况变化**：SFT 3B d100 s123 (PID 471296) 已经完成（train_loss=1.1846, epoch=1.0, runtime=18252s），checkpoint 完整。因此跳过 0.5B filler，直接提交了 3B eval。

**已完成操作**：

1. **exp_001_sft_3B_d100_s123** → 标记 DONE (success)，metrics 已记录
2. **exp_001_eval_3B_d100_v2_s123_aligned** → 已创建并提交到 cuda:2
   - PID: 506625
   - GPU 2 内存占用: 7530 MiB
   - tmux session: `exp_001_eval_3B_d100_v2_s123_aligned`
   - 输出目录: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned`
   - Registry status: RUNNING

**GPU 状态**：
| GPU | 占用 | 任务 |
|-----|------|------|
| 0 | 12471 MiB | exp_001_sft_05B_d025_s123_v2 (PID 498153) |
| 1 | 8985 MiB | exp_001_eval_3B_d000_v2_s123_aligned (PID 492660) |
| 2 | 7671 MiB | **exp_001_eval_3B_d100_v2_s123_aligned (PID 506625)** ← 刚提交 |
| 3 | 8985 MiB | exp_001_eval_3B_d025_v2_aligned (PID 503791) |
| 4 | 3695 MiB | exp_001_eval_05B_d000_s42_v7 (PID 494109) |
| 5 | 0 MiB | 空闲（SFT 3B d100 s123 已完成释放） |

---
