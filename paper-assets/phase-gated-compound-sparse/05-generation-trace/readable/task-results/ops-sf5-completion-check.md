# ops sf5 completion check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sf5_completion_check_20260515T181007_result.json`
- **Structured JSON:** [`930b91ba4eedb7ad73db.json`](../../sessions/93/930b91ba4eedb7ad73db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**交付总结：**

- **状态**：Config A (h0.2/kv0.3) 和 Config B (h0.3/kv0.2) 均 50/50 完成，GPU 已释放
- **Phase gradient 方向**：两个 config 均为 II_low >> II_mid >> II_high，与 symmetric s025 baseline 方向一致。预注册判据（D = II_low − II_high > 0）通过
  - Config A: D = 19.51 − 0.38 = **+19.13**
  - Config B: D = 18.77 − 0.52 = **+18.25**
- **不对称分配效应**：kv sparsity 较高时（Config A）mid_sparsity II 更大（6.05 vs 3.97），head sparsity 较高时（Config B）high_sparsity II 略高（0.52 vs 0.38），但整体 gradient 方向稳健
- **Registry**：sf5_asymmetric_spot → DONE, conclusion=success

---
