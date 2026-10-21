# eval geometric prior k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_geometric_prior_k05_20260517T160512_result.json`
- **Structured JSON:** [`d30f46759b5b27bfc4de.json`](../../sessions/d3/d30f46759b5b27bfc4de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Task 0 完成: 0/50 (0% SR)，Task 1 正在进行。eval 运行正常，预计全部 FAIL。

当前状态总结：

**Geometric Prior Pruning k=0.5 eval 已在 cqa1-33015 GPU 1 运行 (PID 244007)**

- 脚本：`eval_geometric_prior_k05.py`
- Checkpoint：`libero_full_ft/step_099999/checkpoint.pt`
- 使用现有 `GeometricPriorPruner` (Sobel edge + true_removal hook)
- 进度：Task 0 完成 (0/50)，Task 1 进行中
- 预期结果：**全部 0% SR**（k=0.7 和 k=0.9 也是 0%）
- 输出：`eval_results/eval_geometric_prior_k05.json`

**关键结论（已确认）：**
- Geometric prior pruning 即使只去掉 10% tokens (k=0.9) 也导致 0% SR
- ACIS-based pruning 去掉 70% tokens (k=0.3) 仍有 45% SR
- 这完美证明了 cliff-edge phenomenon 和 ACIS 的价值

eval 还需 ~30 分钟完成全部 500 episodes。完成后 JSON 会自动写入 `eval_results/eval_geometric_prior_k05.json`。需要我等完成后汇报最终结果吗？

---
