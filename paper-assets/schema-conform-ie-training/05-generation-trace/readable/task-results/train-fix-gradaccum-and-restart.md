# train fix gradaccum and restart

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_fix-gradaccum-and-restart_20260512T113823_result.json`
- **Structured JSON:** [`85811001f50f7ded0f8f.json`](../../sessions/85/85811001f50f7ded0f8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完毕。**`gradient_accumulation_steps=8` 已经在正确生效，2790 步是 GRPO 下的正确值，不是 bug。**

### 根因分析

| 场景 | 公式 | 总步数 |
|------|------|--------|
| **grad_accum=8（当前，正确）** | `1861 × 8_gen / (2_bs × 8_ga) × 3` | **2793** ≈ 2790 ✓ |
| grad_accum=1（如果真没生效） | `1861 × 8_gen / (2_bs × 1) × 3` | **22332** |
| 用户预期（SFT 公式，漏算 num_gen） | `1861 / (2_bs × 8_ga) × 3` | **351** ≈ 349 ✗ |

GRPO 中每个 prompt 生成 `num_generations=8` 个 completion，训练数据量是 `1861 × 8 = 14888`。TRL 默认将 `steps_per_generation` 设为 `gradient_accumulation_steps`，导致 `num_generations` 和 `grad_accum` 在分子分母抵消，总步数恰好等于 `num_samples / batch_size × epochs`，**看起来像 grad_accum=1 但实际上每个 optimizer step 确实累积了 8 个 micro-batch（16 个 completion）的梯度**。

### 结论

**不需要修复代码。** 配置完全正确，直接重启训练即可。是否继续重启两组训练（A: baseline, B: conformance）？

---
