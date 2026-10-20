# analysis padding side check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_padding_side_check_20260519T053226_result.json`
- **Structured JSON:** [`d0234aa03673a8d72e96.json`](../../sessions/d0/d0234aa03673a8d72e96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**确认存在 right-padding bug，影响所有实验。**

核心发现：
1. **`iterative_train.py` 没有设置 `padding_side='left'`**，Pythia tokenizer 默认 right-padding
2. **`gen_batch_size=16`**，6.9B 和小模型实验均如此
3. **日志中有数千条 transformers 警告**：6.9B 有 3130 条，小模型有 3443 条
4. 仅 generation 阶段受影响，training 和 metrics 计算不受影响

**影响评估**：所有 alpha/seed/model 一致受影响，相对比较仍有效，不建议重跑。建议修复代码后在一个代表性配置上做 robustness check。

修复方式：在 `generate_synthetic_data()` 内临时将 `tokenizer.padding_side = 'left'`，函数结束后恢复。

报告已写入 `artifacts/padding_side_check.md`。

---
