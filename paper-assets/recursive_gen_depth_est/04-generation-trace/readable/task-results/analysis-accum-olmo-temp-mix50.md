# analysis accum olmo temp mix50

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_accum_olmo_temp_mix50_20260522T050620_result.json`
- **Structured JSON:** [`273aa2cd84ad5face473.json`](../../sessions/27/273aa2cd84ad5face473.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程 PID 722400 仍在运行，实验尚未完成。**

当前状态：
- 进程运行了约 11 分钟，正在执行 `accumulation_pipeline_olmo_temp09.py --mix_ratio 0.5 --seed 42`
- 已完成：mixed_d1_train.jsonl (5000 条) + accum_depth_1.jsonl (1069 条，还在生成中)
- 未完成：depth 2/3 生成、feature extraction、RF 分类
- 参考 mix25 完整运行耗时 1.81 小时，预计 mix50 还需 ~1.5 小时

mix25 参考结果已确认与任务描述一致：
- overall_accuracy = 73.47%, d1d3_balanced_acc = 64.72%
- per-class recall: d0=99.72%, d1=75.68%, d2=48.16%, d3=70.32%
- 5-fold CV range: [72.10%, 74.85%]

**建议**：等进程跑完后再分析。预计完成时间约 2026-05-22 14:30 左右。需要我稍后再来检查吗？

---
