# code fix repo datacollator strict

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-repo-datacollator-strict_20260512T163300_result.json`
- **Structured JSON:** [`e4393ce4c7395972dc0a.json`](../../sessions/e4/e4393ce4c7395972dc0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都在稳定进行。以下是完整诊断报告：

---

## 诊断结果

### Root Cause

v2 的 `WeightedDataCollator.__call__` 使用了 `self.base_collator(features)` 委托给 `DataCollatorForSeq2Seq`，后者调用 `tokenizer.pad(features)`。虽然 collator 先 pop 了 `class_label` 和 `labels`，剩余的 feature dict `{'input_ids': [...], 'attention_mask': [...]}` 被传入 `tokenizer.pad()` 时，tokenizer 无法识别该 dict 格式，抛出：

```
ValueError: type of {'input_ids': [...], 'attention_mask': [...]} unknown: &lt;class 'dict'>
```

### v2 → v3 修复 (已在当前代码中)

v3 代码完全重写了 `WeightedDataCollator`，**去掉 `self.base_collator`**，改为手动 padding：

```python
# v2 (崩溃):
class WeightedDataCollator:
    def __init__(self, tokenizer):
        self.base_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True)
    def __call__(self, features):
        class_labels = ...
        labels_list = ...
        batch = self.base_collator(features)  # ← 崩溃点
        ...

# v3 (修复):
class WeightedDataCollator:
    def __init__(self, tokenizer):
        self.pad_token_id = tokenizer.pad_token_id
        self.padding_side = tokenizer.padding_side
    def __call__(self, features):
        class_labels = torch.tensor([f.pop("class_label") ...])
        labels_list = [f.pop("labels") ...]
        # 手动 padding → 直接返回 tensor dict
        for f, lab in zip(features, labels_list):
            pad_len = max_len - len(f["input_ids"])
            batch_ids.append(f["input_ids"] + [self.pad_token_id] * pad_len)
            ...
        return {"input_ids": torch.tensor(...), "attention_mask": ..., "labels": ..., "class_label": ...}
```

### 训练状态

| 实验 | PID | GPU | 状态 | 进度 |
|------|-----|-----|------|------|
| repo-level-cls-v3 | 69782 | cuda:2 | 训练中 | step 12/6633, ~7.4s/it |
| repo-level-cwm-v3 | 69888 | cuda:3 | 训练中 | step 3/6633, ~10.7s/it |

两个 v3 进程均成功通过 v2 的 step 0 崩溃点，bug 已修复，训练正常进行。无需额外操作。

---
