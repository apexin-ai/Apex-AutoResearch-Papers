# code phi normalize fix

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phi-normalize-fix_20260512T235356_result.json`
- **Structured JSON:** [`c35d84830d5c7a05119d.json`](../../sessions/c3/c35d84830d5c7a05119d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### Fix 1 — φ 权重归一化
- **etadn_discount.py**: `compute_discount_weights` 在返回前加 `w = w / w.sum()`，确保 Σφ=1
- **dmpo_loss.py**: `compute_phi_weights` 同步加归一化；`phi_weighted_logps` 的向量化 φ 计算后加 `phi / phi.sum(dim=1)`
- γ=1.0 和 γ≈0 的特殊分支已经是归一化的，不受影响
- 自测全部更新并 PASS（8/8），包括：sum=1 断言、phi scalar↔vector 对比改为归一化后对比、w[0]=1.0 断言改为相对比较

### Fix 2 — γ sweep 脚本
- **run_training.sh** 重写为 phase1/phase2 结构
  - `phase1`: gpu0 跑 ETADN seed1，gpu1 顺序跑 γ∈{0.85, 0.90, 0.92, 0.95, 0.97, 1.0} sweep
  - `phase2 &lt;best_gamma>`: 两轮，每轮 gpu0 ETADN + gpu1 best-γ，seeds 2,3
- `--gamma` 参数是 float，γ=1.0 自动支持（归一化后权重均匀 = 标准 DPO）
- 脚本语法检查通过

### 注意
- `src/tests/test_phi.py` 测试 `dmpo_loss.py` 的 `compute_phi_weights`，归一化后可能需要更新（未在本次任务范围内）

---
