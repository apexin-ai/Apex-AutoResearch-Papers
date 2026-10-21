# code fix verify pipeline

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-verify-pipeline_20260524T091603_result.json`
- **Structured JSON:** [`8e964761f4fa7d59e7fd.json`](../../sessions/8e/8e964761f4fa7d59e7fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总如下：

### 产出

1. **`src/prepare_gemma_data_v2.py`** — 已写入服务器，修复了三个 bug：
   - **relabel bug**：旧脚本翻转 label 时未更新 `parametric_answer`/`contextual_answer`，导致 68% conflict 样本答案相同。新脚本在翻转时同步更新答案字段，并有 post-filter 兜底。
   - **classify 优先级 bug**：旧脚本先检查 `ground_truth`，ConflictQA 中大量 `memory_answer ≈ ground_truth` 的条目被误分类为 `"ground_truth"` 触发不必要翻转。新脚本改为优先检查 `memory_answer`。
   - **缺少 chat_template**：旧脚本直接 tokenize prompt，新脚本使用 `tokenizer.apply_chat_template()`。

2. **Qwen 管线检查**：无 Qwen 准备脚本，无 Qwen 数据目录，无 `prepare_qwen*.py` 文件。Qwen 不受此 bug 影响，不需要修复。

3. **Dry-run 验证**：50 条采样 → 94 个样本（47 对），0 个 conflict 样本有相同答案，字段与 Llama 格式完全匹配。

### 运行正式数据

ConflictQA 原始数据已在服务器缓存中：
```bash
cd /root/clkc_mech_interp
python src/prepare_gemma_data_v2.py \
  --model /root/autodl-tmp/models/AI-ModelScope/gemma-2-9b-it \
  --conflictqa_path /root/.cache/huggingface/hub/datasets--osunlp--ConflictQA/snapshots/056384049e63c1ddae853891c24610fa07d85744/conflictQA-popQA-chatgpt.json \
  --n_sample 2000 \
  --output_dir data/gemma2
```

---
