# fix plan 004 v2 stratified launch

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan-004-v2-stratified-launch_20260514T062526_result.json`
- **Structured JSON:** [`08bc01f136bc34361f20.json`](../../sessions/08/08bc01f136bc34361f20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修改内容** (`src/training/implicit_router_sft.py`)：
1. **Stratified split** — `load_implicit_sft_data()` 改为按 `route_label` episode-level 分层，使用 sklearn `train_test_split(stratify=...)`
2. **class_weights auto** — 新增 `--class_weights` 参数，`WeightedTrainer.compute_loss()` 按 route_label 对每个样本的 loss 加权（inverse frequency）
3. **互斥检查** — 同时传 `--class_weights` 和 `--upsample_minority` 时警告并禁用后者
4. **gradient_accumulation_steps** — 新增 CLI 参数，替换原硬编码值
5. **report_to** — 改为 `"none"`（离线环境）

**验证结果**：
- Val split 包含两个类：internal=166, deterministic=90
- Class weights: internal=0.74, deterministic=1.53
- 训练正常启动，~1 it/s

**plan-004-v2** 已在 GPU1 启动，PID=235893，预计 ~8 分钟完成（147 steps × 3 epochs，有 grad_accum=8）。Registry 已更新为 RUNNING。

---
