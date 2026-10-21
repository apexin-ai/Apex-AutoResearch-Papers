# fix phase1 blockers

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_phase1_blockers_20260516T092109_result.json`
- **Structured JSON:** [`37121f7879c4b5f18d89.json`](../../sessions/37/37121f7879c4b5f18d89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项验证均通过：

**验证 1 (Controller off-by-one)**: 5 代全部运行，`B_rem` 归零，所有 ratio ≥ r_min。Budget 被完整消耗。

**验证 2 (Pipeline dry-run)**: Controller 正确创建（budget=2.5, T=5），`get_first_gen_ratio()` 返回 0.50，后续各代根据 effective rank 下降自适应调高 ratio，最终 B_rem=0。

两个 blocker 已修复：
- `controller.py`: upper_clip 预留从 `remaining_gens` 改为 `max(0, remaining_gens - 1)`
- `pipeline.py`: 初始化传入 `total_budget`/`total_generations`，循环内用 controller 驱动 ratio 而非固定 config 值，删除末尾重复的 controller update

---
