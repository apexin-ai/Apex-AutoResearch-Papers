# ops openvla l2norm pruning

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_openvla-l2norm-pruning_20260520T114919_result.json`
- **Structured JSON:** [`7d8fc1e23d6410085010.json`](../../sessions/7d/7d8fc1e23d6410085010.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

L2 norm pruning sweep 正在 GPU 1 上运行：
- k=0.7 已启动（256 → 179 tokens）
- Task 1/10 进行中
- PID: 935715

**实现总结：**
- 基于 `eval_openvla_libero.py` 创建了 `eval_openvla_l2norm_libero.py`
- 新增 `L2NormPruningHook`：在 `vla.projector` 输出后，按每个 vision token 的 L2 norm 排序，保留 top-k 最大 norm 的 token（真正移除，非置零），与现有 random pruning 方式一致
- Hook 注册位置与 X-VLA 的 L2 norm pruning 逻辑一致（projector 输出后、LLM 前）
- 保留了 spatial order（`indices.sort()`）
- Sweep 参数：k=0.7, 0.5, 0.3 × 10 tasks × 50 episodes, seed=42, GPU 1
- 预计每个 k 约 4 小时（~2 eps/min × 500 episodes），总计 ~12 小时

---
