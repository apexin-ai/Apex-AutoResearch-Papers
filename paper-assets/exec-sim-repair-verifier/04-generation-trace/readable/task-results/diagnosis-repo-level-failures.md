# diagnosis repo level failures

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_repo-level-failures_20260512T112603_result.json`
- **Structured JSON:** [`ebc87a951c3b84fd633c.json`](../../sessions/eb/ebc87a951c3b84fd633c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根本原因（两个实验相同）

**`KeyError: 'sample_weight'`** — 代码 bug，不是 OOM/数据/依赖问题。

Bug 链：
1. `preprocess_split` 在 Dataset 中正确添加了 `sample_weight` 列
2. HuggingFace `Trainer` 在训练前调用 `_remove_unused_columns()`，移除不在模型 `forward()` 签名中的列 — `sample_weight` 被移除
3. `compute_loss` 中 `inputs.pop("sample_weight")` → `KeyError`

function-level 的 `train_verifier.py` 没用 `sample_weight`，所以没有这个问题。repo-level 脚本新增了 class weighting 但没处理 Trainer 的列过滤机制。

### 修复方案

需要改两处（两个脚本同样修改）：

**1. TrainingArguments 加 `remove_unused_columns=False`**

```python
# 在 ta dict 中加：
"remove_unused_columns": False,
```

**2. 自定义 collator 包装 DataCollatorForSeq2Seq，把 sample_weight 单独处理**

因为 `DataCollatorForSeq2Seq` 会尝试对 `sample_weight`（标量）做 padding，会出错。需要包装一层：

```python
class WeightedDataCollator:
    def __init__(self, base_collator):
        self.base_collator = base_collator

    def __call__(self, features):
        sample_weights = [f.pop("sample_weight") for f in features]
        batch = self.base_collator(features)
        batch["sample_weight"] = torch.tensor(sample_weights, dtype=torch.float32)
        return batch
```

然后初始化改为：
```python
base_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True)
collator = WeightedDataCollator(base_collator)
```

### 可以修复重试

纯代码 bug，修复后直接重跑即可。数据（70748 train / 9335 val）和模型都已就绪，15 分钟的 wall clock 主要花在 tokenization 上，实际训练还没开始（0/6633 steps）。

需要我直接在服务器上修复这两个脚本吗？

---
