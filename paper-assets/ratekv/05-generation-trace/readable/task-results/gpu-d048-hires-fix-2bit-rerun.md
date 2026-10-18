# gpu d048 hires fix 2bit rerun

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_d048_hires_fix_2bit_rerun_20260514T182835_result.json`
- **Structured JSON:** [`402f80fae275109e3f31.json`](../../sessions/40/402f80fae275109e3f31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**Bug 修复确认：**
- Line 108: `for bits in [2, 4, 8]:` — 2-bit 已加入 ✓
- Line 64: `shift_logits.float().view(-1, shift_logits.shape[-1])` — .float() 已存在 ✓

**Hires profiling 启动确认：**
- PID: 247429，tmux session: `qwen_hires_float32_d048`
- 模型已加载，GPU 0 占用 9.2GB，正在运行
- 模型: Qwen2.5-7B (28 layers × 4 KV heads = 112 heads × 3 bitwidths = 336 profile evals)
- 预计完成时间: 336 × ~12s ≈ 67 min（约 1 小时）

---
