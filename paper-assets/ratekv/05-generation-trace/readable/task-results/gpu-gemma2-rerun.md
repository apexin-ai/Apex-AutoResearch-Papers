# gpu gemma2 rerun

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_gemma2_rerun_20260514T153825_result.json`
- **Structured JSON:** [`0e9b10e6524207c3486b.json`](../../sessions/0e/0e9b10e6524207c3486b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 启动成功，全部确认：

1. **脚本同步** — 632 行已写入 `/root/ratekv/run_gemma2_full_pipeline.py`
2. **模型路径** — `/root/autodl-tmp/.hf_cache/google/gemma-2-9b` 匹配，42 layers / 8 KV heads / head_dim=256 / softcap=50.0
3. **模型加载** — 5.5s 完成，cuda:0 占用 ~32GB 显存
4. **Baseline PPL** — calibration PPL = **9.3816**（修复前是 711，确认 BOS fix 生效）
5. **Phase 1 profiling** — 已开始，336 heads × 3 bitwidths = 1008 次评估

Pipeline 正在跑 profiling，日志写入 `/root/runs/ratekv/gemma2_9b_rerun.log`。

---
