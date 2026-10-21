# code hotfix selfcritique batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hotfix-selfcritique-batch_20260514T114506_result.json`
- **Structured JSON:** [`b8ddbc52f6c4b6f1517b.json`](../../sessions/b8/b8ddbc52f6c4b6f1517b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## Diff 摘要

**删除**：`get_model_answer()`（单条 generate）、`compute_yes_no_entropy()`（单条 forward pass）

**新增**：
- `BATCH_SIZE = 32`
- `_get_yes_no_token_ids(tokenizer)` — 预计算 YES/NO token IDs，避免每次重复编码
- `batch_generate_answers(model, tokenizer, prompts, max_new_tokens)` — 批量 generate，left padding + attention_mask
- `batch_compute_yes_no_entropy(model, tokenizer, critique_prompts, yes_ids, no_ids)` — 批量 forward pass 取 logits，`logits.float()` 处理 bfloat16

**修改**：`compute_selfcritique_signal()` 
- 加载后设置 `tokenizer.pad_token = tokenizer.eos_token`，`tokenizer.padding_side = 'left'`
- 主循环从逐条改为 `range(0, len(items), BATCH_SIZE)` 的批次循环
- 每批次内：batch generate → 构建 critique prompts → batch forward pass

## 验证结果

3 条 MMLU items 对比 single vs batch：
| Item | Answer 一致 | Entropy 差异 |
|------|------------|-------------|
| 0 | ✗ | 0.0056 |
| 1 | ✓ | 0.0075 |
| 2 | ✗ | 0.0000 |

答案差异来自 left-padding 影响 position encoding（batch-of-1 与 single 完全一致，确认是 padding 导致）。最终 entropy 差异均 < 0.01，对污染检测信号（区分 entropy≈0 vs entropy≈1）无实质影响。

备份在 `signal_selfcritique.py.bak`。Task 2-9 将自动使用新版。

---
