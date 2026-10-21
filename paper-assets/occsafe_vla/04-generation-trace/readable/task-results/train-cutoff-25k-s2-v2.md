# train cutoff 25k s2 v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_cutoff_25k_s2_v2_20260525T043552_result.json`
- **Structured JSON:** [`4a8310463e9fbc50c57f.json`](../../sessions/4a/4a8310463e9fbc50c57f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job 已 kill，registry 已更新为 killed。

## 结果

**任务失败 — bug 未修复，已主动 kill 训练进程 (PID 6038)**

### 问题根因

`finetune.py` line 1163:
```python
gradient_step_idx = batch_idx // cfg.grad_accumulation_steps
```

`batch_idx` 来自 `enumerate(dataloader)`，resume 后从 **0** 重新计数。cutoff 逻辑 (line 1172):
```python
occ_weight_now = base_weight if gradient_step_idx < cfg.occ_loss_cutoff_step else 0.0
```

直接用未修正的 `gradient_step_idx` 判断。只有 `log_step` (line 1233) 加了 `resume_step` 偏移，但 cutoff 逻辑没有用 `log_step`。

### 影响

- resume 从 30K 开始，剩余 20005 步
- `gradient_step_idx` 最大 = 20005，永远 < 25000
- OCC loss **永远不会被 cutoff**，等于跑了一个全程 OCC loss 的实验
- 这正是 **C002 约束**禁止 cutoff 实验使用 `--resume` 的原因

### 修复建议

在 line 1163 后加偏移：
```python
gradient_step_idx = batch_idx // cfg.grad_accumulation_steps
if cfg.resume:
    gradient_step_idx += cfg.resume_step
```

修复后需要同步更新 line 1233 的 `log_step` 逻辑（避免重复加 offset）和 line 1262 的 save 逻辑。

---
