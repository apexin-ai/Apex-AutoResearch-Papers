# viz retrain decay curve

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_retrain-decay-curve_20260519T010907_result.json`
- **Structured JSON:** [`bb4e683a14910004a591.json`](../../sessions/bb/bb4e683a14910004a591.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出：

- 服务器：`/root/autodl-tmp/gen-depth-contamination/figures/retrain_decay_curve.{pdf,png}`
- 本地 artifact：`retrain_decay_curve.png`（已注册，ID `art_20260519_490934`）
- 脚本：`/root/autodl-tmp/gen-depth-contamination/scripts/plot_retrain_decay.py`

图中 retrain-chain 从 0.984 缓慢衰减到 0.641（depth 6v7 仍高于 θ=0.60，K*≥7），prompt-chain 在 1v2 即骤降到 0.629 并在 2v3 跌破阈值（K*=2），对比清晰。

---
