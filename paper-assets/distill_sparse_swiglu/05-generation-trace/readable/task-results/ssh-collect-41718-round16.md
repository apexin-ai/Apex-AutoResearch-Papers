# ssh collect 41718 round16

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_41718_round16_20260520T180334_result.json`
- **Structured JSON:** [`743926eebcc2a23dbd6d.json`](../../sessions/74/743926eebcc2a23dbd6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验状态汇总：

## STE 30% s42 eval (cuda:0, PID 268293)
- **状态**: 运行中
- **当前阶段**: `loglikelihood` requests — 62% (24889/40168), 22.86 it/s
- 这是 MMLU（最大的 loglikelihood 任务），剩余 ~15279 items / 22.86 it/s ≈ **~11 min**
- MMLU 之后还有 GSM8K (generate_until)，预计额外 ~20 min
- **预计总完成时间**: ~30 min

## KL 50% global s456 eval (cuda:1, PID 272689)
- **状态**: 运行中
- **当前阶段**: `generate_until` requests (GSM8K) — 67% (889/1319), ~1.3 it/s
- 剩余 ~430 items / 1.3 it/s ≈ **~5.5 min**
- 这是最后一个任务（loglikelihood 类的 ARC/WG/MMLU/HS/PIQA 已完成）
- **预计完成时间**: ~5-6 min

## GPU 状态
| GPU | 温度 | 功耗 | 显存 | 利用率 |
|-----|------|------|------|--------|
| cuda:0 | 82°C | 613W/600W | 66.1/97.9 GB | 100% |
| cuda:1 | 55°C | 342W/600W | 66.1/97.9 GB | 93% |

结果目录都是空的，eval 完成后才会写入 results.json。KL 50% global s456 eval 很快就完成，STE 30% s42 eval 还需约半小时。

---
