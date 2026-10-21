# status gpu check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_gpu-check_20260516T145402_result.json`
- **Structured JSON:** [`4f73609bd6455ad9ae5d.json`](../../sessions/4f/4f73609bd6455ad9ae5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完成。结果摘要：

**GPU 状态：** 4 块占用 (0/2/4/5)，2 块空闲 (1/3)

**4 个 RUNNING 实验：**
- `exp_001_eval_15B_instruct` (cuda:5) — ALIVE，mmlu paraphrased 71%，预计还需 ~10 min 完成全部
- `exp_001_eval_05B_instruct` (cuda:2) — ALIVE，运行 13 min
- `exp_006_mmlu_domain_gamma_n24_v4` (CPU) — **COMPLETED**，7/7 domain 结果齐全
- `exp_006_pooled_irt_rrf_n25_v2` (CPU) — **COMPLETED**，结果已写入

**额外发现：**
- GPU 0 有未注册的 compute_signals 进程 (3B_d000_s123_a32, s4 mmlu, ~80% done, 运行 2h09m)
- GPU 4 有未注册的 Llama-3.2-3B_d000_s42 aligned eval (运行 17 min)
- 所有历史 PID (691872, 760236, 764449, 752961, 746777) 均已结束

报告已保存至 `artifacts/gpu_status_loop17.md`。

---
