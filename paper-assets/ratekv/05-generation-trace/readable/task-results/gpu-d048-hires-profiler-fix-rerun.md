# gpu d048 hires profiler fix rerun

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_d048_hires_profiler_fix_rerun_20260514T181102_result.json`
- **Structured JSON:** [`8c4671fd23002775fef5.json`](../../sessions/8c/8c4671fd23002775fef5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载完成（~15.5GB VRAM），profiling 正在运行。logs 目录不存在导致 tee 副本失败，但主日志在 `~/runs/ratekv/qwen25-hires-profiling.log`，不影响运行。

**汇报：**

1. **Bug 已修复**：`hires_quant_profiler.py` L64 的 `shift_logits.view(...)` → `shift_logits.float().view(...)`，cross_entropy 现在在 float32 精度下计算，避免 bf16 累积精度截断。

2. **Profiling 已启动**：`qwen25-hires-profiling` 任务在 cuda:0 上运行，模型 Qwen2.5-7B，64 samples × 2048 tokens，batch_size=4。每个 head 需要 profile 两次（4-bit 和 8-bit），Qwen2.5-7B 有 28 layers × 4 KV heads = 112 heads × 2 = 224 次 forward pass + 1 baseline = 225 次完整推理。

3. **预计完成时间**：2-4 小时（取决于每次 forward pass 耗时）。日志在 `~/runs/ratekv/qwen25-hires-profiling.log`。

4. **关键输出**：`/root/ratekv/qwen25_7b_hires_float32_results.json` 和 `/root/ratekv/hires_profiles.json`，核心看 top-5% concentration 是否 > 0.50。

---
