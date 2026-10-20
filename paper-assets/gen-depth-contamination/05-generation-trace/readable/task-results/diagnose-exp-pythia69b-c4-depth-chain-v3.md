# diagnose exp pythia69b c4 depth chain v3

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_pythia69b_c4_depth_chain_v3_20260521T123110_result.json`
- **Structured JSON:** [`9eaf5acef41d03ab826d.json`](../../sessions/9e/9eaf5acef41d03ab826d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**失败阶段**：Step 4 Feature Extraction，depth 2 的 surprisal 计算

**错误**：`RuntimeError: cannot reshape tensor of 0 elements into shape [2, 0, -1, 128]`

**根因**：continuation 模式下 Pythia-6.9B 在深层生成了空文本（depth_2=68条, depth_3=33, depth_4=22, depth_5=21，共 144 条空文本）。`compute_surprisal_features` 直接将空文本送入 Qwen2.5-1.5B scorer，tokenizer 产出 0-length 序列，Qwen2 self-attention 的 reshape 操作崩溃。函数内虽有 `seq_len < 3` 兜底，但在 `model(**inputs).logits` 之后才检查，崩溃发生在 forward pass 内部。

**中间产出**：depth_{0-5}.jsonl 全部完整（各 5000 条），features.csv 和 results/ 未生成

**可恢复性**：可用 `--skip_generation` 从 Step 4 恢复，省约 9 小时生成时间

**修复**：`run_pipeline.py` ~L240，`batch_texts` 赋值后加一行：
```python
batch_texts = [t if t.strip() else " " for t in batch_texts]
```
将空文本替换为单空格，确保 tokenizer 至少产出 1 个 token，后续 `seq_len < 3` 兜底会自动返回零向量。

---
