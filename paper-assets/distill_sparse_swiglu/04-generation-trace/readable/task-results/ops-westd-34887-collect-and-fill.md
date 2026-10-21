# ops westd 34887 collect and fill

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-34887-collect-and-fill_20260518T084941_result.json`
- **Structured JSON:** [`b551c24e955e630bc369.json`](../../sessions/b5/b551c24e955e630bc369.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

kl50_s42_uniform_eval 运行中（PID 13571, cuda:0, 模型已加载, allocation=uniform）。

cuda:1 空闲。kl_comp_30pct_s42 在 41718 上 step 900/1000 接近完成但还没有 checkpoint。没有其他就绪的 PREPARING 任务可以立即跑在 cuda:1。

**汇总：**

| 任务 | 状态 | 结果 |
|------|------|------|
| c4_ood_kl50_s42 | DONE ✓ | c4_ppl = **23.53** |
| c4_ood_kl50_s456 | DONE ✓ | c4_ppl = **23.99** |
| C4 OOD 50% 均值 | — | **23.76 ± 0.23** (2-seed) |
| kl50_s42_uniform_eval | RUNNING (westd-34887 cuda:0) | 重新提交，模型加载中 |
| kl_comp_30pct_s42 | RUNNING (westd-41718 cuda:0) | step 900/1000 |
| kl_comp_30pct_s123 | RUNNING (westd-41718 cuda:1) | step 300/1000 |
| westd-34887 cuda:1 | **空闲** | 等 compensation checkpoint 或其他任务 |

---
