# code teal greedy allocation

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_teal-greedy-allocation_20260515T170823_result.json`
- **Structured JSON:** [`389d50c97a20ab9f0166.json`](../../sessions/38/389d50c97a20ab9f0166.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果总结：

## 实现内容

**新文件**: `src/baselines.py` (md5=`8ba03eb8`) — 438 行，包含：

| 函数 | 方法 | 状态 |
|------|------|------|
| `teal_greedy_allocation_masks()` | TEAL 论文 Algorithm 1: 逐层重建误差曲线 + 贪心分配 | 完整实现 |
| `wina_global_masks()` | WINA: score = \|act\| × ‖W_col‖₂, 全局 top-K | 完整实现 |
| `wina_greedy_allocation_masks()` | WINA scoring + TEAL 贪心分配 | 完整实现 |
| `r_sparse_masks()` | R-Sparse: magnitude channel selection (mask-only) | mask 部分完整 |
| `r_sparse_svd_cache()` | R-Sparse: 离线 SVD 分解 down_proj | stub，TODO: 集成到推理 forward |

**验证文件**: `src/test_greedy_dryrun.py` (md5=`0631fd03`)

## Dry-run 验证结果 (3 samples, seq_len=512, target=50%)

**TEAL greedy allocation** (4.6s):
- 全局平均稀疏率: **0.5000** (精确命中目标)
- 浅层 (0-5): 90% — 误差最小，可大幅剪枝
- 中层 (15-17): 45-55%
- 深层 (28-31): 0% — 误差最大，保持 dense
- **没有任何层达到 100% 剪枝** — 修复了原 vanilla TEAL 的致命问题

**WINA global** (0.2s):
- 浅层仍被过度剪枝 (Layer 0: 99.7%)，和 vanilla TEAL 类似的问题
- 说明全局 top-K 方法本身有缺陷，需要 greedy per-layer allocation

**WINA greedy** (4.1s):
- 分配与 TEAL greedy 几乎一致（误差曲线主导，scoring 差异影响小）

evaluate.py 未修改 (md5 不变)。

---
