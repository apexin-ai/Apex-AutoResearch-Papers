# code fix twostage s2 freeze

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_twostage_s2_freeze_20260516T042059_result.json`
- **Structured JSON:** [`cef965121dfefef5929f.json`](../../sessions/ce/cef965121dfefef5929f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结论：Stage 2 冻结策略**已正确实现**，无需修改。

### Stage 2 代码实际行为

**参数冻结（main 函数）：**
- `freeze_params(acis_params)` — 所有 ACIS 参数 `requires_grad=False` ✓
- `unfreeze_params(lora_params)` — 所有 LoRA 参数 `requires_grad=True` ✓
- `verify_grad_state(model, "stage2")` — 断言 ACIS 全冻结、LoRA 全可训 ✓
- `make_stage_optimizer(lora_params, ...)` — 优化器只含 LoRA 参数 ✓

**梯度隔离（stage2_forward → model.forward with gradient_isolation=True）：**
- L246: `vis_for_acis = vis_tokens.detach()` — margin_loss 梯度无法回传到 backbone/LoRA
- L247: `suffix_for_acis = suffix_embs.detach()` — 同上
- L252: `scores_for_select = importance_scores.detach()` — action_loss 梯度无法回传到 ACIS

**Loss 组成：**
- `total = action_loss + lambda * margin_loss`（lambda=1.0）
- margin_loss 仍在计算，但由于 ACIS 冻结 + detach 隔离，其梯度无处可去
- 这浪费了一点计算量，但功能上完全正确

### 三层防护确保无 co-adaptation：
1. ACIS `requires_grad=False` — 梯度不会累积
2. `gradient_isolation` detach — action_loss ↛ ACIS，margin_loss ↛ LoRA
3. 优化器只含 LoRA 参数 — 兜底保障

### 当前训练状态
- 进程 133659 刚启动约 4 分钟，仍在加载模型（"Loading SmolVLA policy..."）
- 命令无 `--resume_stage2`，将从 Stage 1 重新跑（10K steps → Stage 2 20K steps）
- `stage1_done` checkpoint 是前次运行的产物
- 不需要任何干预，训练可以继续

---
