# code compute evaluate directions

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_compute_evaluate_directions_20260518T064026_result.json`
- **Structured JSON:** [`6477b920620c641c38ac.json`](../../sessions/64/6477b920620c641c38ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已编写完成，语法验证通过。

**compute_directions.py**：加载 Phase 2 激活 `.pt` → 按 `pair_id` 配对 → `StratifiedShuffleSplit` 按 domain 分层 80/20 划分 → 在 train set 上 difference-in-means 计算 `d_syc` 和 `d_gen` → L2 归一化 → 保存 `directions.pt`。

**evaluate_directions.py**：加载方向和激活 → 过滤 test set → per-layer/per-position AUROC（投影到 `d_syc` 的 dot product 作为分数）→ cosine(d_syc, d_gen) → 按 domain/evidence_strength/correction_turn 分层 AUROC → Go/No-Go 判定（PASS/GRAY/FAIL）→ 输出 JSON 报告 + stdout 摘要。

---
