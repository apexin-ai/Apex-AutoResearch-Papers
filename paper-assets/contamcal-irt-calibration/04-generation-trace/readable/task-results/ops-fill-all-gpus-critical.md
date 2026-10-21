# ops fill all gpus critical

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill-all-gpus-critical_20260516T182204_result.json`
- **Structured JSON:** [`3a436b740ba5ca379d69.json`](../../sessions/3a/3a436b740ba5ca379d69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。最终 GPU 分配：

| GPU | 任务 | PID | 显存 | 预计完成 |
|-----|------|-----|------|----------|
| cuda:0 | 既有任务 | 825638 | 8081 MiB | - |
| cuda:1 | **Llama d000 signals MMLU** | 830115 | 8281 MiB | ~30-45 min |
| cuda:2 | 1.5B ARC signals（收尾） | 823710 | 595 MiB | ~5-10 min |
| cuda:3 | 既有任务 | 822390 | 8313 MiB | - |
| cuda:4 | **Llama d000 signals GSM8K** (831936) + arc_challenge (831353, 另一 worker) | 共享 | ~579 MiB (加载中) | ~40-60 min |
| cuda:5 | **Llama d100 eval** (4 benchmarks) | 831033 | 6505 MiB | ~45-60 min |

**处理的冲突：**
- 杀掉了我在 cuda:1 的重复 MMLU 进程（另一 worker 的 830115 先到）
- 杀掉了 cuda:5 上另一 worker 的重复 eval 进程（我的 831033 先到）

**Registry 更新：**
- `exp_001_sft_llama32_3B_d100_s42`: DONE, metrics 已补全（loss=1.5435, acc=0.6505, runtime=9847s）
- `exp_001_eval_llama32_3B_d100_s42`: RUNNING (cuda:5)
- `exp_002_signals_llama32_3B_d000_mmlu`: RUNNING (cuda:1)
- `exp_002_signals_llama32_3B_d000_gsm8k`: RUNNING (cuda:4)

**注意**: cuda:4 上另一 worker 还提交了 Llama d000 arc_challenge signals（PID 831353），两任务不冲突（不同 benchmark 写不同文件），24GB 显存可容纳两个 3B signals 进程。

---
