# diagnose exp 001 eval 3B d000 s42 a32 para aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_3B_d000_s42_a32_para_aligned_20260516T070634_result.json`
- **Structured JSON:** [`9c9553803235c8e077a0.json`](../../sessions/9c/9c9553803235c8e077a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：实验已正常完成，cron 误报。**

- PID 716470 已退出，tmux session 不存在
- 所有输出文件完整：`eval_results.json`、`correctness_matrix.json`、`item_responses.json`、`.done` sentinel
- 日志确认 4 个 benchmark 全部跑完，结果已写入
- cuda:4 当前无进程运行

已更新 registry 状态 RUNNING → DONE (success)。Metrics：

| Benchmark | Score |
|-----------|-------|
| mmlu_para | 0.6431 |
| gsm8k_para | 0.0526 |
| arc_para | 0.8106 |
| humaneval_para | 0.1923 |

---
