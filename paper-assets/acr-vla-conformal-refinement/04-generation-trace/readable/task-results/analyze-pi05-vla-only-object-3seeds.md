# analyze pi05 vla only object 3seeds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-vla-only-object-3seeds_20260521T114140_result.json`
- **Structured JSON:** [`148d100d64561c5ac31e.json`](../../sessions/14/148d100d64561c5ac31e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（已有 metrics 和 failure_reason）。

## 汇总

| Seed | Overall SR | Rollouts | Status |
|------|-----------|----------|--------|
| 42 | **0.0%** (0/200) | 200 | EXIT_CODE=0 |
| 43 | **0.0%** (0/200) | 200 | EXIT_CODE=0 |
| 44 | **0.0%** (0/200) | 200 | EXIT_CODE=0 |
| **Mean ± Std** | **0.0% ± 0.0%** | **600 total** | |

所有 10 个 task 在 3 个 seed 上全部 0/20。无 W&B URL，无 sentinel 文件。

**关键问题：与 D103 quick verify (72% SR) 严重矛盾。** 日志显示模型加载后仍有 376 个 missing keys（multi_modal_projector, language_model.embed_tokens, language_model.layers.\*.self_attn 等），表明 PI05 的 language model 权重实际未被加载——vision tower keys 做了 remap，但其余核心组件的权重是随机初始化的，导致模型输出完全无意义的 action。

需要排查 D103 的加载路径与这次实验的差异，重点看 `model.safetensors` 的 key mapping 逻辑是否在代码更新后 regressed。

---
