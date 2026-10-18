# code multi seed lowres

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi_seed_lowres_20260514T110226_result.json`
- **Structured JSON:** [`763cb69b75d1d164abf9.json`](../../sessions/76/763cb69b75d1d164abf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交，汇总：

- **脚本路径**: `/root/ratekv/run_multi_seed_lowres.py`（westd-37397）
- **tmux session**: `multi_seed_lowres`
- **GPU**: cuda:0（`CUDA_VISIBLE_DEVICES=0`）
- **日志**: `/root/ratekv/multi_seed_lowres.log`
- **关键参数差异**: `NUM_SAMPLES=16, SEQ_LEN=512`（hires 版为 64×2048）
- **结果输出**: `/root/ratekv/multi_seed_lowres_results.json`
- **预计完成**: ~45min 内（每 seed ~15min profiling + eval），约在 11:50 UTC 前完成

查看进度：`tmux attach -t multi_seed_lowres` 或 `tail -f /root/ratekv/multi_seed_lowres.log`

---
