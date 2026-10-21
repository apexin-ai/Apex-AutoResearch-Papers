# verify d004 no hardcoded 0833

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_d004-no-hardcoded-0833_20260515T124800_result.json`
- **Structured JSON:** [`f956b54d7dc91e486e98.json`](../../sessions/f9/f956b54d7dc91e486e98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

**1. 0.833 硬编码搜索**

仅 `analyze_mvp.py` 存在 3 处 0.833，全部是 CLI 参数默认值和帮助文档，属于 MVP 脚本的遗留。`train_probes.py` 和 `analyze_results.py` 均无 0.833 硬编码。

**2. `train_probes.py` best_layer 选择逻辑** — 正确

- 第 606 行：`best = max(results, key=lambda k: results[k].get("per_task_mean_rho", results[k]["spearman_rho"]))` — 优先用 `per_task_mean_rho`，fallback 到 `spearman_rho`
- 第 607-609 行：`summary["best_layer"]`、`summary["best_rho"]`、`summary["best_pooled_rho"]` 均从实际计算结果取值

**3. `analyze_results.py` DINO 比较逻辑** — 正确，无硬编码

- 第 241-243 行：从 `all_data["dinov2"]` 提取实际 `spearman_rho`，取 `rho_dino.max()`
- 第 366-379 行：`compute_judgment` 中 DINO 基线值全部从数据动态提取（`dino_mean_rho`、`rho_dino_pooled`），比较逻辑 `vla_ge_dino = vla_mean_rho >= dino_mean_rho` 用变量而非硬编码

**结论**：`train_probes.py` 和 `analyze_results.py` 无 0.833 残留，逻辑正确。`analyze_mvp.py` 的 0.833 是旧 MVP 脚本的 CLI 默认值，不影响当前流水线。

---
