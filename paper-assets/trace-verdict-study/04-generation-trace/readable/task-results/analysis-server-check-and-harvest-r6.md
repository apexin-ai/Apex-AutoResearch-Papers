# analysis server check and harvest r6

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_server_check_and_harvest_r6_20260518T201527_result.json`
- **Structured JSON:** [`38e0594d49113e5acb0d.json`](../../sessions/38/38e0594d49113e5acb0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部收割完成。汇总：

```
SERVER: 可达 (westd-11235)
GPU STATUS: 双卡空闲
  cuda:0  NVIDIA RTX PRO 6000 Black — 49GB VRAM 占用(残留显存，无进程) / 0% util
  cuda:1  NVIDIA RTX PRO 6000 Black — 0MB / 0% util
DISK: 151G/250G used (60%)
TMUX: 无活跃 session

EXPERIMENT STATUS:
┌─────────────────────────────────────────┬──────────┬──────────┬─────────────────────┐
│ Experiment                              │ Status   │ Accuracy │ CI 95%              │
├─────────────────────────────────────────┼──────────┼──────────┼─────────────────────┤
│ deepseek_full_trace_tail512_seed123_v2  │ DONE ✓   │ 95.04%   │ [93.9%, 96.3%]      │
│ qwen7b_full_trace_tail512_seed456       │ DONE ✓   │ 97.65%   │ [96.8%, 98.5%]      │
│ loop_only_seed123                       │ DONE ✓   │ 85.88%   │ [84.0%, 87.7%]      │
│ loop_only_seed456                       │ DONE ✓   │ 86.64%   │ [84.7%, 88.4%]      │
│ qwen15b_exception_only_seed42           │ DONE ✓   │ 99.83%   │ [99.6%, 100%]       │
└─────────────────────────────────────────┴──────────┴──────────┴─────────────────────┘

Registry 更新：deepseek_seed123_v2 和 qwen7b_seed456 已从 ALLOCATED → DONE(success)。
其余三个已是 DONE。

qwen15b_exception_only_seed42 训练配置：
  模型: Qwen2.5-Coder-1.5B-Instruct
  条件: exception_only
  seed: 42, 444 steps, ~3.9s/it
  LR: 2e-4 warmup → cosine decay

FREE GPUs: cuda:0, cuda:1（双卡完全可用）
```

---
