# analysis bootstrap result pickup

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-result-pickup_20260515T145850_result.json`
- **Structured JSON:** [`7d1f7e4e9a57fe0257d1.json`](../../sessions/7d/7d1f7e4e9a57fe0257d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本**已崩溃**，未完成 bootstrap 测试。

**状态**:
- Model 1 (random_s43): 加载成功，R@1 = 0.5449
- Model 2 (embedding_distance_s43): 加载 checkpoint 时报 `AssertionError: Missing keys`，脚本终止

**错误原因**: `load_model()` 加载 embedding_distance_s43 checkpoint 时，checkpoint 只包含 LoRA adapter 权重，但代码用 `assert not result.missing_keys` 检查，导致所有 base model 权重（`backbone.base_model.model.layers.*.weight` 等）被报为 missing。

这说明 embedding_distance_s43 的 checkpoint 是 adapter-only 格式（未 merge base weights），而 `load_model()` 期望的是完整权重或需要先加载 base model 再加载 adapter。

**需要修复**: `bootstrap_paired_test.py` 的 `load_model()` 函数需要支持 LoRA adapter 加载方式——先加载 base model，再用 `PeftModel.from_pretrained()` 加载 adapter，而不是直接 `load_state_dict` 然后 assert missing_keys 为空。

需要我查看脚本代码并修复吗？

---
