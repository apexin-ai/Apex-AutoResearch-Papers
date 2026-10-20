# fix eval gsm8k sft alpha4 20 timeout

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_gsm8k_sft_alpha4_20_timeout_20260521T222131_result.json`
- **Structured JSON:** [`4868f8a4eacef8a65583.json`](../../sessions/48/4868f8a4eacef8a65583.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成报告

### 1. Timeout 延长：N → 已重启

`kill 422002` 发 SIGTERM 给 timeout 进程，timeout 将信号转发给 python 子进程，导致 python 被杀（EXIT_CODE=143）。正确做法应是 `kill -9`（SIGKILL 阻止转发）。

**补救**：已用 timeout 28800s (8h) 重新启动。新进程链：
- 424712 (bash) → 424716 (timeout 28800) → **424717** (python eval_gsm8k.py)

### 2. Python 进程当前状态

- **PID 424717**，已开始评估 (1/1319)
- GPU 0，当前 VRAM 12712 MiB（模型权重加载完毕）
- 预计运行 ~4.2h，8h timeout 有充足余量

### 3. GPU 0 诊断

| 项目 | 结果 |
|------|------|
| 竞争进程 | **无**，GPU 0 仅 PID 424717 |
| VRAM（当前） | 12712 MiB（模型权重） |
| VRAM（峰值预估） | ~29GB（KV cache 随 4096 tokens 增长） |
| 29GB vs 17-18GB 差异原因 | eval_gsm8k 未传 `--max_new_tokens`，**默认 4096**；其他 eval_math500 用 2048 |

### 4. Stall 根因

**`--max_new_tokens` 默认 4096（命令行未指定）。** 当模型未生成 EOS（eos_rate=96.67%，~3.3% 的样本），会生成完整 4096 tokens：
- 正常样本：avg_len=287 tokens，~2-3s
- 无 EOS 样本：4096 tokens，~5-6 min（14x 慢）

这同时解释了 stall 和 VRAM 异常（4096 tokens 的 KV cache 比 2048 大一倍）。

---
