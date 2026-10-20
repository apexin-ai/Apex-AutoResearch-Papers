# precheck p0 script preparation

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_precheck_p0_script_preparation_20260516T023957_result.json`
- **Structured JSON:** [`bea10a5d55ec365a2363.json`](../../sessions/be/bea10a5d55ec365a2363.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有脚本关键参数验证通过。汇总结果：

---

## 已完成 P0 确认

| plan_id | registry_id | 状态 |
|---------|-------------|------|
| p0_contamination_60_datagen | p0_contamination_60_datagen | ✅ success |
| p0_contamination_60_uniform | contamination_60_uniform_seed42 | ✅ success, PPL=17.766 |
| p0_contamination_60_adaptive | contamination_60_seed42_r2 | ✅ success, PPL=17.74 |
| p0_contamination_60_grid_b0_5 | contamination_60_grid_b0_5_seed42 | ✅ success, PPL=17.704 |
| p0_nmin_4 | nmin4_seed42 | ✅ success, PPL=17.6947 |
| p0_batchsize_8 | bs8_nmin2_seed42_r2 | ✅ negative, PPL=17.73 |

## 脚本预检 & 新建

✅ **p0_grid_b_low** 预检通过 — `scripts/run_grid_b_low_seed42.sh`，循环 b=0.1/0.2/0.3，参数正确

✅ **p0_nmin_5** 预检通过 — `scripts/run_nmin5.sh` 已存在，n_min=5, batch_size=4, wandb 启用

⚠️ **p0_nmin_5 行为说明** — 代码 `find_optimal_b` 中 `if n_min > n: n_min = n`，n_min=5 被 clamp 到 batch_size=4，ESS(b=0)=4 是唯一满足 ESS≥4 的点，所以 b\*=0 恒成立 → 等价 uniform weights。这正是预期的退化 case。

✅ **p0_batchsize_16** 预检通过 — `scripts/run_batchsize16.sh` 已存在，batch_size=16, grad_accum=1, n_min=2

⚠️ **p0_batchsize_16 OOM 风险** — 当前 batch_size=4 per GPU 占 ~46.5GB/98GB。batch_size=16 激活内存约 4× ≈ 186GB → 单卡 OOM。建议加 `--gradient_checkpointing`（代码已支持），可降至 ~80-90GB。若仍 OOM 需降 max_length 或用 grad_accum=4 + batch_size=4 保持总 batch=16 不变。

🆕 **p0_contamination_60_tau06** 已新建 — `scripts/run_contamination_60_tau06.sh`，data=scored_data_60.jsonl, ρ=0.6, τ=0.6, n_min=2, batch=4, wandb 启用，参数验证 OK

⚠️ **注意**：现有 `run_tau_06_nmin2.sh` 是 ρ=0.4 的 tau sweep 实验（scored_data.jsonl），与此 contamination_60_tau06 是不同实验，不要混淆。

---
