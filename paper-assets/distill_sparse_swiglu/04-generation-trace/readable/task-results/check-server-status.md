# check server status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server_status_20260516T034658_result.json`
- **Structured JSON:** [`ec7b6902f81dfc516d25.json`](../../sessions/ec/ec7b6902f81dfc516d25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：`run_bench_cuda1.sh` 设了 `CUDA_VISIBLE_DEVICES=1`，所以 PID 195911 (bench_teal50) 实际用的也是**物理 cuda:1**，与 mistral eval 共享同一块 GPU。

```
== STATUS SUMMARY ==
PID 195242 (mistral eval): ALIVE — 运行 51 分钟，generate_until 进度 873/1319 (66%)，~2.8s/it，预计剩余 ~21 分钟
PID 194814 (teal eval): DEAD — 已完成退出
cuda:0: FREE (0 MiB, 0% utilization)
cuda:1: BUSY (62082/97887 MiB, 95% util) — 被两个进程共享：
  - PID 195242: lm_eval_mistral_kl_50pct
  - PID 195911: benchmark_eval.py bench_teal50 (run_bench_cuda1.sh 的 [1/5]，该脚本共 5 个 condition 串行跑)
```

**Teal 30% eval 结果 (已完成)**:

| Benchmark | Score |
|-----------|-------|
| arc_challenge | acc=0.393, acc_norm=0.416 |
| winogrande | acc=0.656 |
| **mmlu** | **acc=0.360** (STEM=0.313, Social=0.411, Other=0.401, Humanities=0.330) |
| gsm8k | EM(strict)=0.085, EM(flexible)=0.092 |
| actual_sparsity | 0.300 |

**注意事项**：`run_bench_cuda1.sh` 是一个 5-condition 批处理脚本（teal50 → teal30 → kl70 → bce_iso50 → mistral_kl50），当前在跑第 1 个 (bench_teal50，585/1319 generate_until)。它与 mistral eval 共享 cuda:1，可能互相拖慢。该脚本未在任务背景中提及——可能是之前启动的遗留任务。

---
