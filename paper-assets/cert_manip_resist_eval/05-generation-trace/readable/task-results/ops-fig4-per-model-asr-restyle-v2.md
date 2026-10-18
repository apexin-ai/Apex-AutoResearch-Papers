# ops fig4 per model asr restyle v2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fig4-per-model-asr-restyle-v2_20260525T200401_result.json`
- **Structured JSON:** [`bde337acaed11c3ae622.json`](../../sessions/bd/bde337acaed11c3ae622.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**根因**：`apply_position_attack` 只对 gt=A 的 pairs 做 swap（使 gt winner 始终在 position B），gt=B 的 pairs 不做 swap。原脚本对所有 position_bias scores 做 A↔B inversion，导致 gt=B（未 swap）的 cases 被错误反转，ASR 虚高到 ~50%。

**修复**：移除 `_invert()` 调用，改为在 `compute_individual_asr` 中对 position_bias 直接比较 `attacked_winner != "B"`（因为 swapped_gt 恒为 B）。

**修复后 Position Bias ASR**：
- 顶级 API 模型：0-3%（之前 43-55%）
- GPT-4.1-Mini：11%，GPT-4.1-Nano：17%（较弱模型有一定 position bias）
- Haiku Prompt Injection：81.7% 不变

图已保存到 `docs/paper/figures/fig_per_model_asr.pdf` 和 `.png`。

---
