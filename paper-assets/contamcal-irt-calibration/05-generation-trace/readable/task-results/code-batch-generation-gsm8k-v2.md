# code batch generation gsm8k v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_batch-generation-gsm8k-v2_20260518T125856_result.json`
- **Structured JSON:** [`472f25423c4952c6d410.json`](../../sessions/47/472f25423c4952c6d410.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改内容：

1. **evaluate_gsm8k** (line 278): 改为 batch generation，left-pad tokenization，`max_new_tokens=256`，按 `--batch-size` 分批调用 `model.generate`
2. **evaluate_humaneval** (line 347): 同样改为 batch generation，`max_new_tokens=512`
3. 两个函数都会保存/恢复 `tokenizer.padding_side`，处理最后不足 batch_size 的尾 batch
4. 函数签名、调用链、评估逻辑（答案提取、正则匹配、代码执行）、`max_items`/`subsample_seed` 均不变
5. 语法检查通过，main() 中的调用点完好

---
