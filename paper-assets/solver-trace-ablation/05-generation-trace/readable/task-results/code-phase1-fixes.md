# code phase1 fixes

**solver trace ablation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1_fixes_20260513T101915_result.json`
- **Structured JSON:** [`4d769338722877bc247e.json`](../../sessions/4d/4d769338722877bc247e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件语法检查通过。

修改摘要：

**recursive_loop.py**:
- 新增 `_is_degenerate()` 静态方法：过滤 <10 词或非 ASCII >5% 的样本
- 将原生成逻辑提取为 `_generate_batch()`，`_generate_synthetic()` 在生成后执行最多 2 轮 sanity filter + 重新生成，最终丢弃仍退化的样本并记录日志

**property_scorer.py**:
- `set_reference_corpus()` 新增 TF-IDF vectorizer fit + corpus mean 计算
- `lexical_conformity()` 改为 TF-IDF cosine similarity（单参数签名，`score_batch` 调用无需改动）
- 旧 BLEU-4 实现保留为 `_lexical_conformity_bleu()`，标注弃用原因
- 顶部新增 `sklearn` import

---
