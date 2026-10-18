# gpu yi15 9b submit

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_yi15_9b_submit_20260514T142318_result.json`
- **Structured JSON:** [`b6ba0249b587a1df74b6.json`](../../sessions/b6/b6ba0249b587a1df74b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- tmux session `yi15_9b_full_pipeline` 在 `westd-37397` cuda:1 上运行
- 等待脚本正在轮询 `/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B` 下载完成（检查 config.json 存在 + 无 .incomplete/.tmp/.lock 文件 + safetensors 文件数稳定）
- 下载完成后自动执行 `CUDA_VISIBLE_DEVICES=1 python -u run_yi15_full_pipeline.py --model ... --gpu cuda:0`
- 日志：`~/runs/ratekv/yi15_9b_full_pipeline.log`

---
