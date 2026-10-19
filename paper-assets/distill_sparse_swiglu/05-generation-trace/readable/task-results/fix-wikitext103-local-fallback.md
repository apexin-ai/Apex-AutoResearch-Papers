# fix wikitext103 local fallback

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_wikitext103_local_fallback_20260517T101529_result.json`
- **Structured JSON:** [`f48c02d9b6be8d539e92.json`](../../sessions/f4/f48c02d9b6be8d539e92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **数据准备**：从 HF 缓存 (`/root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-103-raw-v1/`) 导出为 `save_to_disk` 格式到 `/root/autodl-tmp/data/wikitext103/`（1,801,350 samples）。

2. **代码修改**：`src/data_utils.py` 的 `get_calibration_loader` 中，wikitext-103 分支现在优先从 `/root/autodl-tmp/data/wikitext103/` 用 `load_from_disk` 加载，不存在时才回退到 HuggingFace 下载。

3. **验证通过**：`--dataset wikitext-103 --seed 123` 的 5 步 dry-run 训练正常完成，数据加载无网络依赖。

---
