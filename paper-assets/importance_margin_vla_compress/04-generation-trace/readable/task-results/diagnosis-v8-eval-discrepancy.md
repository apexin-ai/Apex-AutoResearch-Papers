# diagnosis v8 eval discrepancy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_v8_eval_discrepancy_20260516T025043_result.json`
- **Structured JSON:** [`62575c6b616d8bddfad7.json`](../../sessions/62/62575c6b616d8bddfad7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有了完整的图景。让我验证最后一个关键点：dataloader 确实使用 shuffle=True。

数据已经足够，下面是完整诊断结论。

---

## 诊断结论

### 1. 关键代码差异表

| 属性 | Trajectory eval (100 batch) | Final eval (500 batch) |
|------|---------------------------|----------------------|
| 脚本 | evaluate.py | evaluate.py |
| Checkpoint | step_029999 | step_029999 |
| max_batches | 100 | 500 |
| seed | 42 | 42 |
| **Action loss 的 model mode** | **train (soft sigmoid mask)** | **train (soft sigmoid mask)** |
| **pruning flag 对 action_loss 的影响** | **无** | **无** |
| 每个 condition 独立 RNG reseed | 是 (md5 hash of condition name) | 是 |
| Dataloader shuffle | True | True |

### 2. 根因：evaluate.py 的 IMM 路径从未实际测试 pruning

`evaluate_full` 函数 (evaluate.py:358-362) 中，IMM 路径计算 action_loss 的代码是：

```python
# eps=0 时，无论 pruning=True 还是 False：
eval_input = batch  # 完全相同的输入
model.train()       # soft sigmoid mask（不是 hard pruning）
_, info = model(eval_input, step=0)  # 内部重新采样 noise/time
all_action_loss.append(info["action_loss"].item())
model.eval()
```

**三个致命问题：**

1. **`pruning` 布尔变量对 eps=0 的 action_loss 计算没有任何影响。** 代码 `eval_input = batch if epsilon == 0 else ...`，当 eps=0 时 eval_input 恒为 batch，无论 pruning 是 True 还是 False。

2. **model.train() 使用 soft sigmoid mask，不是 hard binary pruning。** `token_selector.forward(training=self.training)` 在 train mode 下走 `_soft_forward`，所有 token 都保留（只是乘以 sigmoid 权重），这不是 50% token pruning。

3. **每个 condition 的 `torch.manual_seed(seed + condition_offset)` 导致不同的 RNG 状态。** model.forward() 内部的 `bm.sample_noise()` 和 `bm.sample_time()` 使用全局 RNG，不同 seed → 不同 noise/time → 不同 MSE loss。加上 `DataLoader(shuffle=True)`，不同 seed 还导致不同的 batch 顺序。

**结果：`eps0.0_pruneFalse` 和 `eps0.0_pruneTrue` 是对同一个量（soft-masked action loss）用不同随机种子做的两个独立估计，差异纯属 RNG 噪声。**

- 100 batch 方差大 → 碰巧出现 0.0033 vs 0.0066（2x 差距，方向"反直觉"）
- 500 batch 方差小 → 0.0053 vs 0.0059（差距收敛，方向"符合直觉"）
- 两个方向都没有意义，因为根本没测 pruning

### 3. 哪个更可信

**两个都不可信。** 两个 eval 用的是同一段有 bug 的代码，从未实际执行 ACIS 50% hard pruning。报告的 "acis_prune action_loss" 只是换了个随机种子的 soft-masked loss。

不过 500-batch eval 的 **bypass_acis 结果** (`eval_imm_v8_bypass_final.json`) 是可信的 — 它绕过 ACIS 调用 `baseline_forward`，直接测量了无 ACIS 时的 action loss。

### 4. 推荐后续动作

**修复 evaluate.py 的 IMM pruning 测试，然后重跑。** 具体修改：

1. **受控对比**：对每个 batch 用固定的 noise/time，分别测试 clean forward 和 pruned forward：
   - Clean: 全部 visual tokens（bypass ACIS 或 no mask）
   - Pruned: hard binary mask 保留 top-k tokens（eval mode 的 `_hard_forward`）
   
2. **消除 RNG 污染**：不要 per-condition reseed。改为外层遍历 batch、内层遍历 conditions，对同一个 batch 用相同的 noise/time 做对比。

3. **action_loss 应在 eval mode 下用 hard mask 计算**（这对应实际部署场景），或者同时报告 soft 和 hard 两个值。

需要我编写修复后的 eval 函数吗？

---
