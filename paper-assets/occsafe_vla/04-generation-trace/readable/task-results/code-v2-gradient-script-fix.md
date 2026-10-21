# code v2 gradient script fix

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v2-gradient-script-fix_20260526T161827_result.json`
- **Structured JSON:** [`f895c69e1e2b9e060db6.json`](../../sessions/f8/f895c69e1e2b9e060db6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v2 脚本当前状态已经与 v1 方法论对齐，用户描述的两个问题在当前版本中不存在：

**1. 数据来源**：v2 已经使用真实 RLDS DataLoader（`RLDSDataset` at line 225），无 `torch.randn`。`grep -n "randn"` 返回空。`--num_samples=200`（默认），`num_batches = 200 // 4 = 50` 批次。

**2. 梯度测量点**：v2 已经使用逐层 backbone 参数梯度：
- `get_layer_groups(vla)` (line ~97) 按 `vision_backbone.named_parameters()` 的 transformer block 分组
- `torch.autograd.grad(action_loss, all_params, ...)` (line 303) 对 backbone 参数求梯度
- `compute_per_layer_grads()` (line 307, 318) 对每组参数独立计算 L2 norm
- `patch_features` (line 295-296) 仅用于 OCC head 前向传播输入（与 v1 完全一致）

**v1 vs v2 方法论对比确认**：

| 维度 | v1 | v2 |
|------|----|----|
| 数据源 | RLDSDataset + DataLoader | RLDSDataset + DataLoader |
| 梯度目标 | vision_backbone params | vision_backbone params |
| 分组方式 | get_layer_groups (by block) | get_layer_groups (identical) |
| 每层指标 | L2 norm + cosine + conflict | L2 norm + cosine + conflict |
| 输出格式 | per_layer dict in JSON | per_layer dict in JSON |

唯一差异：v1 默认 `--num_batches=200`，v2 默认 `--num_samples=200`（即 50 batches with bs=4）。如果需要对齐到 200 batches（800 samples），可以调 `--num_samples 800`。

脚本不需要修改。是否需要调整 `num_samples` 默认值，或者你描述的问题对应的是一个更早版本的文件？

---
