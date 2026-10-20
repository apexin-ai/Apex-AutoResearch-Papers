# ops gpt2m weights fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpt2m-weights-fix_20260515T115129_result.json`
- **Structured JSON:** [`903ecbac9d1db33e0a8d.json`](../../sessions/90/903ecbac9d1db33e0a8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果**：
- **权重路径**: `/root/autodl-tmp/models/gpt2-medium/`（symlinks → HF cache blobs）
- **参数量**: 354,823,168 ✓
- **vocab**: 50,257 ✓
- **目录内容**: config.json, generation_config.json, merges.txt, model.safetensors (1.5GB FP32), tokenizer.json, tokenizer_config.json, vocab.json — 全部完整
- **清理**: ModelScope `._____temp` 残留已删除

问题根因：HF Hub 已经完整下载了 gpt2-medium 到 cache（`/root/autodl-tmp/.hf_cache/models--gpt2-medium/`），但 ModelScope 的并行下载卡在 temp 目录未 finalize。实际权重完好，无需重新下载。

---
