# figure fig4 svd subspace

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig4-svd-subspace_20260523T125455_result.json`
- **Structured JSON:** [`18133d6904cd84bbc149.json`](../../sessions/18/18133d6904cd84bbc149.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Fig 4 完成。

- **(a) Vanilla**: 两类充分混杂，vanilla encoder 的 top-2 SVD 方向不具备判别性
- **(b) 9-Class DAPT**: benign 紧聚在 dim 1 ≈ 40，jailbreak 分布在 -20~0，类间清晰分离

DAPT 的第一奇异值 (295.63) 远超第二个 (39.78)，说明 adaptation 在表示空间中雕刻出一个强主导方向。Vanilla 的奇异值谱则平坦得多 (8.48, 0.99, 0.70...)。

输出文件：
- `docs/paper/figures/paper/fig4_svd_subspace.pdf` (32K)
- `docs/paper/figures/paper/fig4_svd_subspace.png` (64K)

---
