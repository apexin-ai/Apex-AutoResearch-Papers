# code batch logprob mcq

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_batch-logprob-mcq_20260518T123443_result.json`
- **Structured JSON:** [`2c84ffd517d2a698249c.json`](../../sessions/2c/2c84ffd517d2a698249c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

50/50 per-item 完全一致。

## 改造结果

**修改的函数**：
1. **新增 `batch_compute_choice_logprobs`** (L158-188)：接收一批 prompts + choices，left-pad tokenize → 单次 batch forward → 取每条 `logits[:, -1, :]` 计算 log_softmax → 返回每条的 choice logprobs
2. **改写 `evaluate_mcq`** (L190-283)：先预处理所有 items 到列表，非 generation 模式下按 `batch_size` 分批调用 `batch_compute_choice_logprobs`；generation 模式保持逐条不变

**关键 diff**：
- `tokenizer.padding_side = "left"` 保证 batch padding 正确（结束后恢复原值）
- `padding=True, truncation=True, max_length=2048` 用于 batch tokenize
- `logits[:, -1, :]` 取最后位置（left-pad 下所有序列的真实最后 token 都在末尾）
- `compute_choice_logprobs` 保留不动（`evaluate_paraphrased` 仍在使用）

**验证**：Qwen2.5-0.5B d000_s42, MMLU 50 items
- batch-size=16: accuracy=0.2200, 4 batch iterations
- batch-size=1: accuracy=0.2200, 50 iterations
- **Per-item match: 50/50**

---
