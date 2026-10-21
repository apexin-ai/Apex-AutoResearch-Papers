# paper supplementary pack

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_supplementary-pack_20260529T140408_result.json`
- **Structured JSON:** [`584145647db8a0832301.json`](../../sessions/58/584145647db8a0832301.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

打包完成。

**产出**: `artifacts/supplementary/supplementary.zip` (76KB)，已注册为 `art_20260529_db582d`。

**内容**:
- `README.md` — 复现指南（依赖、数据集、训练/评估命令、超参、图表脚本映射）
- `code/src/` — 4 个核心 ColliForce 模块（SDF decoder, gradient refiner, data loader, training pipeline）
- `code/training/` — 4 个训练脚本（A1 hook, A1 pi0.5, LoRA baseline, full-FT baseline）
- `code/eval/` — 3 个评估脚本（pi0, pi0.5, OpenVLA zero-shot）
- `code/analysis/` — 3 个分析脚本（dfCAR, 跨 seed 聚合, permutation test）
- `code/figures/` — 7 个图表脚本 + 1 个 CSV 数据文件（Fig 1/2/3/5 + appendix threshold sensitivity）

**已确认**:
- 无作者信息、无 `.git`、无 `__pycache__`/`.pyc`
- 所有硬编码路径已替换为相对路径
- 附录在 main.pdf 中，无需单独 appendix PDF

---
