# analysis n16 readiness check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n16_readiness_check_20260515T100959_result.json`
- **Structured JSON:** [`5c70cfcbe5f18e0afa42.json`](../../sessions/5c/5c70cfcbe5f18e0afa42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。核心发现：

**seed42 和 seed123 的 N=16 实验已完成**（各 551 instances，含 logprobs），`exp001_n16_seed123_full` 只是被 kill 的旧尝试，`exp001_n16_seed123`（无 `_full` 后缀）实际已成功运行。

**唯一缺失的是 seed456 的 full N=16 运行**。`output/exp001_n16_seed456/` 为空目录，仅有 `_200only` 的 200 实例部分结果。

运行命令：
```bash
cd /root/autodl-tmp/struct_self_consist_ie && \
python code/run_mvp_pilot.py \
  --model_path checkpoints/qwen3-8b-scierc-merged-v2 \
  --data_dir data/ --dataset scierc --subtask joint \
  --n_samples 16 --temperature 1.0 --seed 456 \
  --output_dir output/exp001_n16_seed456 \
  --collect_logprobs \
  2>&1 | tee output/exp001_n16_seed456_run.log
```

预计 ~8-9 分钟完成。所有依赖（vLLM 0.18.1、xgrammar 0.1.33）和模型均就绪。

---
