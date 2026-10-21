# train d134 4b 10seed pipeline

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_d134-4b-10seed-pipeline_20260518T102646_result.json`
- **Structured JSON:** [`8039d41d7fda2dcd8fa0.json`](../../sessions/80/8039d41d7fda2dcd8fa0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动，运行正常。

汇报：

```
磁盘状态: 58GB 可用 / 每 run ~16GB（训练完 eval+classify 后自动清理 safetensors）
Config 确认: model_path=/root/autodl-tmp/models/Qwen3-4B, β=0.1, 500 steps, batch=4×2=8
GPU: cuda:0, RTX PRO 6000 Black (98GB), 占用 85.9GB, GPU-Util 87%
Pipeline PID: 206796
tmux session: d134-pipeline
第一个 run (ISR s47) 状态: step 2/500, ~11.6s/step
预计单 run: ~1.6h (500 steps × 11.6s)
预计总时长: ~16-20h (10 runs 串行 + eval/classify overhead)
```

用户计划中的几个错误已修正：
- eval 数据路径: `proofwriter_fol_100.jsonl`（C008）
- eval_sta.py: `--output_path`（文件）而非 `--output_dir`
- classify_h7.py: `--eval_path` + `--json_out`
- Python: `/root/miniconda3/bin/python3`
- 加了 `set -o pipefail` 防止管道吞错误
- 每 run 完成后清理 safetensors 释放磁盘

---
