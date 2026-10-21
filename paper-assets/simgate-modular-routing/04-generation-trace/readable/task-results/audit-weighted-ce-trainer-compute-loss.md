# audit weighted ce trainer compute loss

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_weighted-ce-trainer-compute-loss_20260514T064238_result.json`
- **Structured JSON:** [`e5cad46a309f652dea71.json`](../../sessions/e5/e5cad46a309f652dea71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审查结果

### 1. WeightedCETrainer.compute_loss 代码（line 265-274）

```python
def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
    labels = inputs.pop("labels")
    outputs = model(**inputs)
    logits = outputs.logits
    if self._class_weights is not None:
        loss_fn = torch.nn.CrossEntropyLoss(weight=self._class_weights.to(logits.device))
    else:
        loss_fn = torch.nn.CrossEntropyLoss()
    loss = loss_fn(logits, labels)
    return (loss, outputs) if return_outputs else loss
```

`compute_loss` 本身逻辑没有 bug — `reduction='mean'` 的 weighted mean 归一化不会放大绝对 loss，`ignore_index` 不需要（labels 只有 0/1），weight dtype float32 不影响。

### 2. 根因确认：class_weights + WeightedRandomSampler 双重补偿

v3 日志直接证据：

| 日志行 | 含义 |
|--------|------|
| `Class weights: [3.93, 0.57]` | `--class_weights auto` 生效 |
| `Upsampling enabled: WeightedRandomSampler with 1650 draws/epoch` | sampler 生效 |
| `Minority oversampling: enabled` | 两者同时活跃 |
| **无 WARNING 输出** | line 382-385 的 guard **当时不存在** |

双重补偿的效应链：
1. **WeightedRandomSampler** 把 batch 从自然分布（87% det / 13% int）变成 ~50/50
2. **class_weights [3.93, 0.57]** 在 CE loss 中再给 internal 放大 3.93x，deterministic 缩小 0.57x
3. 梯度被 internal 信号压倒 → 模型学会**全部预测 internal**
4. 训练 loss 3.5-4.2（balanced batch 上一半 confidently wrong → CE per sample 很高）

### 3. 模型完全退化 — eval 指标全零

```
epoch 1: eval_loss=1.78, eval_accuracy=0.0, ALL precision/recall/f1=0.0
epoch 2: eval_loss=2.00, eval_accuracy=0.0, ALL=0.0
epoch 3: eval_loss=1.51, eval_accuracy=0.0, ALL=0.0
```

模型全预测 class 0 (internal)，val set 以 deterministic 为主 → 几乎所有预测都错。3 个 epoch 完全没有改善。

### 4. class_weights 实际值

```
internal (id=0):      3.9286  = 1650 / (2 × 210)
deterministic (id=1): 0.5729  = 1650 / (2 × 1440)
```

inverse frequency 公式本身正确，单独使用问题不大。但叠加 WeightedRandomSampler 后 internal 的有效权重放大了 ~7x × 3.93x ≈ 27x。

### 5. Dryrun 为什么正常

所有运行都用 `WeightedCETrainer`（line 498 无条件创建），但 dryrun 不传 `--class_weights` 也不传 `--upsample_minority`：
- `class_weights=None` → compute_loss 走 else 分支 = 标准 CrossEntropyLoss
- `weighted_sampler=None` → get_train_dataloader 走 super() = 自然分布
- 等价于标准 Trainer → loss 0.48-0.63 正常

### 6. 修复建议

**当前代码已有 guard（line 382-385）阻止同时使用**，这解决了直接触发问题。但还有改进空间：

1. **class_weights 归一化**：当前 weights 和不等于 num_classes（3.93+0.57=4.50），建议归一化到和=2：`[1.75, 0.25]`。这让 weighted CE 的 scale 更接近标准 CE
2. **推荐单独跑一版只用 `--class_weights auto`（不用 `--upsample_minority`）验证**，确认 loss 降到正常范围
3. 或反过来只用 `--upsample_minority` 不用 class_weights，效果通常更稳定（采样调分布，loss 不变形）

---
