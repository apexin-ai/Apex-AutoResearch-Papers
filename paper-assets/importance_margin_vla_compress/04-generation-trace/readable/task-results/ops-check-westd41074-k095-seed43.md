# ops check westd41074 k095 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd41074-k095-seed43_20260520T223321_result.json`
- **Structured JSON:** [`a85c0ec986be7d170ad5.json`](../../sessions/a8/a85c0ec986be7d170ad5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

**总结**:
- `eval_openvla_prune_random_k095_seed43` 成功完成
- **SR = 66.8%, Wilson CI 95% = [0.626, 0.708]**
- metadata 验证通过：mode=random_prune, k_ratio=0.95, seed=43
- 对比 seed=7 的 69.4%，seed=43 结果 66.8% 在 CI 范围内，可复现性良好
- GPU 0 已空闲，GPU 1 在用，GPU 2/3 有显存占用但计算空闲

---
