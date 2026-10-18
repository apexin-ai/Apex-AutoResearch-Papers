# investigate prune inconsistency critical

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_prune-inconsistency-critical_20260516T025354_result.json`
- **Structured JSON:** [`ded6220a0c945fc4debf.json`](../../sessions/de/ded6220a0c945fc4debf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获取所有关键信息。现在整理完整的调查结论。

---

## 调查报告：100-batch vs 500-batch pruneTrue 结果不一致根因

### 1. evaluate.py 是否被修改过？

**是。** 存在 `evaluate.py.bak`（438 行，04:14 创建）和当前 `evaluate.py`（470 行，06:24 修改）。差异：
- 新增 `--bypass_acis` CLI 参数（line 59）
- `evaluate_full()` 增加 `bypass_acis` 参数传递
- `_meta` 输出增加 `bypass_acis` 字段
- Gate Metric Summary 输出格式微调

**但这不是根因**——两次 eval 使用的是**同一版本**的 evaluate.py（详见下节）。

### 2. 两次 eval 使用的代码/参数是否一致？

**代码一致，参数几乎一致。** 关键时间线：

| 事件 | 时间 |
|------|------|
| evaluate.py 最后修改 | 06:24 |
| 100-batch trajectory eval (step_029999_standard.json) | 10:29 |
| 500-batch final eval (eval_imm_v8_final.json) | 10:31 |

两次 eval 都在 06:24 之后运行，使用同一版本代码。参数对比：

| 参数 | 100-batch | 500-batch |
|------|-----------|-----------|
| checkpoint | step_029999 | step_029999 |
| config | imm_anchor_v8.yaml | imm_anchor_v8.yaml |
| seed | 42 | 42 |
| bypass_acis | false | false |
| **max_batches** | **100** | **500** |

### 3. 根因判断：**代码设计缺陷导致的 sampling bias（非代码 bug，非代码差异）**

发现两个层叠问题：

#### 问题 A（核心）：条件间 dataloader 重排列

`evaluate_full()` 中每个 condition 重置随机种子：

```python
# evaluate.py line ~290
condition = f"eps{epsilon}_prune{pruning}"
condition_offset = int(hashlib.md5(condition.encode()).hexdigest()[:8], 16) % 10000
torch.manual_seed(seed + condition_offset)

for batch_idx, batch in enumerate(dataloader):  # ← 新迭代器，用了新种子的 randperm
```

而 `make_dataloader`（train.py:198-207）使用 `shuffle=True`：

```python
return DataLoader(dataset, batch_size=..., shuffle=True, num_workers=4, ...)
```

**后果：** `torch.manual_seed(seed + condition_offset)` 改变了 `RandomSampler` 的 `torch.randperm()` 输出。`eps0.0_pruneFalse` 和 `eps0.0_pruneTrue` 的 condition_offset 不同，导致**两个条件看到的是数据集的不同随机子集**。

#### 问题 B（加剧）：eps0.0 下 prune 标志对 IMM 模型无效

对于 IMM 模型（imm_enabled=True, bypass_acis=False），eps0.0 路径的 action_loss 计算：

```python
# evaluate.py line ~355
eval_input = batch if epsilon == 0 else (batch_noisy if pruning else perturb_images(batch, epsilon))
#                ^^^^^^^^^^^^^^^^^
#  eps=0 时，eval_input = batch，pruning 标志被忽略

model.train()
_, info = model(eval_input, step=0)  # ACIS 始终激活，不受 pruning 标志控制
```

**eps0.0 下 pruneFalse 和 pruneTrue 执行完全相同的计算**（相同模型、相同输入），唯一区别是看到不同的 batch 子集。

#### 数学验证

如果 100-batch 是 500-batch 的前 100 个样本（同一条件内），可以反推剩余 400 batch 的平均值：

| 条件 | 前 100 batch | 500 batch avg | 推算的后 400 batch avg |
|------|-------------|---------------|----------------------|
| pruneFalse | 0.00659 | 0.00530 | 0.00498 (↓24%) |
| pruneTrue | 0.00330 | 0.00594 | 0.00660 (↑100%) |

pruneTrue 的前 100 batch loss 仅为后 400 batch 的一半——这完全是 `torch.manual_seed` 给 pruneTrue 条件抽到了一批"简单"样本。

### 4. 结论与建议

**500-batch 结果更可靠**，但即便 500 batch 的 pruneFalse(0.00530) vs pruneTrue(0.00594) 差异（+12%）仍然混入了 batch 选择偏差，不能作为 pruning 效果的可靠判断。

**根因不是代码变更**——两次运行用的是同一份代码。**根因是 evaluate.py 的设计缺陷**：条件级 `torch.manual_seed()` 改变了 dataloader 的 shuffle 排列，导致跨条件对比被 sampling bias 污染。100 batch 时方差极大，500 batch 有所缓解但仍不够干净。

**修复方向**（不要自行修改，供决策参考）：
1. **最佳**：重构评估循环为 outer=batch, inner=condition，所有条件看到相同 batch
2. **次选**：eval 时使用 `shuffle=False`（SequentialSampler），确保确定性且跨条件一致
3. **最低限度**：仅在每个 condition 循环内用独立 `Generator` 控制扰动噪声，不要用 `torch.manual_seed` 污染全局 RNG

**需要重跑 eval**：修复 evaluate.py 的 batch 选择逻辑后，重跑 500-batch final eval 以获得可靠的 prune 效果判断。当前所有 trajectory eval 的 pruneFalse vs pruneTrue 对比数据均不可信。

---
