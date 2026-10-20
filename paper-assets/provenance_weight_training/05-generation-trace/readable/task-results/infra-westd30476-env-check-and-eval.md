# infra westd30476 env check and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd30476_env_check_and_eval_20260520T040101_result.json`
- **Structured JSON:** [`175314abf7031b0adca4.json`](../../sessions/17/175314abf7031b0adca4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个 eval 已完成并更新 registry 为 DONE。

## 最终汇总

| exp_id | Checkpoint | Loss | PPL | 耗时 |
|--------|-----------|------|-----|------|
| **eval_epoch_matched_seed123** | epoch_matched_dr_seed123 | 2.8713 | **17.66** | 104s |
| **eval_epoch_matched_seed456** | epoch_matched_dr_seed456 | 2.8712 | **17.66** | 104s |
| **eval_q03_r2** | detect_remove_q03_seed42_r2 | 2.8480 | **17.25** | 111s |
| **eval_q04** | detect_remove_q04_seed42 | 2.8485 | **17.26** | 104s |
| **eval_q06** | detect_remove_q06_seed42 | 2.8507 | **17.30** | 107s |
| **eval_q07_final** | detect_remove_q07_seed42 | 2.8519 | **17.32** | 104s |
| **eval_q01_final_v2** | detect_remove_q01_seed42 | 2.8563 | **17.40** | 105s |

**关键发现**：
- Epoch-matched baseline PPL = 17.66（两个 seed 完全一致）
- 所有 detect-remove 变体均低于 baseline（PPL 17.25–17.40），确认数据过滤有效
- q=0.3 最优（PPL 17.25），q=0.1 反而不如 q=0.3（17.40 vs 17.25），说明过度过滤导致数据量不足
- PPL 随 q 阈值单调递增的趋势在 q=0.1 处打破，呈 U 型曲线，最优点在 q=0.3 附近

**缺失 checkpoint**：无，所有 7 个 checkpoint 均存在（路径修正为 `/root/autodl-tmp/output/models/`）。

---
