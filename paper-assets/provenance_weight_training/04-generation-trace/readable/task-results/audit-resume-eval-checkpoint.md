# audit resume eval checkpoint

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_resume_eval_checkpoint_20260521T043335_result.json`
- **Structured JSON:** [`7b15afe95f389e8bd28e.json`](../../sessions/7b/7b15afe95f389e8bd28e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Resume + save_only_model 审计结果

### ✅ 安全（eval 用了 resume 前 checkpoint）

| 实验 | 说明 |
|------|------|
| **grid_b0_2_seed456** | eval 明确使用 checkpoint-5500（resume 前）。Registry 注明 "final checkpoint degraded due to --save_only_model LR reset on resume"，eval 已绕开。PPL=17.645 |
| **grid_b0_2_seed123** | 同上。eval 使用 checkpoint-5500。PPL=17.637 |

---

### ⚠️ eval 用了 resume 后 checkpoint，但风险低（resume 极早，剩余步数充足）

| 实验 | resume 点 | 剩余步数 | PPL | 判断依据 |
|------|-----------|---------|-----|---------|
| **uniform_seed42** | ckpt-500 | 5603 (92%) | 17.694 | 3 seed 一致 (17.69-17.70)，train_loss 一致 (~7.31)，无异常 |
| **uniform_seed123** | ckpt-500 | 5603 (92%) | 17.686 | 同上 |
| **uniform_seed456** | ckpt-500 | 5603 (92%) | 17.702 | 同上 |
| **grid_b0_3_seed123_r2** | ckpt-1000 | 5103 (84%) | 17.579 | 2026-05-18 re-eval 确认。PPL 在 grid_b0.3 组内正常 |
| **contamination_60_random_seed42** | ckpt-1000 | 5103 (84%) | 17.832 | 单 seed，无法交叉验证，但 resume 早，数值合理 |

> 这些实验 resume 在训练初期（≤16% 进度），optimizer 有充足步数重新收敛。PPL 无异常波动。

---

### ⚠️ eval 用了 resume 后 checkpoint，中等风险（resume 在中期）

| 实验 | resume 点 | 剩余步数 | PPL | 服务器 | 备注 |
|------|-----------|---------|-----|--------|------|
| **ess_only_seed456_r2** | ckpt-2500 | ~3603 (59%) | 17.762 | westd-41312 ✅ | eval 确认用 final/。两 seed 差异 0.04，不算异常但无 from-scratch 基准对比 |
| **ess_only_seed123_r2** | ckpt-2000 | ~4103 (67%) | 17.721 | westd-41312 ✅ | 同上 |
| **random_reweight_seed456** | ckpt-1000 | ~5103 (84%) | 17.777 | westd-41312 ✅ | 单 seed 无法交叉验证。resume 较早，但该方法只有此一个 seed 数据点 |

> eval_results_batch_may18.json 确认这 3 个实验 eval 均指向 `{exp}/final/`（post-resume checkpoint）。

---

### ⚠️ 已知受影响，已从论文排除

| 实验 | resume 点 | 剩余步数 | PPL | 服务器 |
|------|-----------|---------|-----|--------|
| **grid_b2_0_seed456** | ckpt-3500 | 2603 (43%) | 17.989 | westd-47453 已退役 |
| **grid_b3_0_seed456** | ckpt-3000 | 3103 (51%) | 17.921 | westd-47453 已退役 |
| **grid_b5_0_seed456** | ckpt-3000 | 3103 (51%) | 17.993 | westd-47453 已退役 |

> Registry 已标注 "seed456 b≥2.0 PPL异常高（checkpoint问题），论文只报 2-seed 数据"。grid_b2_0_seed456 的 train_loss=10.625 是明确的 degradation 信号（正常值 ~5-7）。eval 均使用 post-resume final/ checkpoint。

---

### 总结

| 分类 | 数量 | 实验 |
|------|------|------|
| **安全**（eval 用 pre-resume ckpt） | 2 | grid_b0_2_seed456, grid_b0_2_seed123 |
| **低风险**（resume 极早，PPL 正常） | 5 | uniform_seed42/123/456, grid_b0_3_seed123_r2, contamination_60_random_seed42 |
| **中风险**（resume 中期，无 scratch 基准） | 3 | ess_only_seed456_r2, ess_only_seed123_r2, random_reweight_seed456 |
| **已确认受影响，已排除** | 3 | grid_b2_0/b3_0/b5_0_seed456 |

**建议关注的 3 个中风险实验**：ess_only 两个 seed 和 random_reweight_seed456 的 eval 确定用了 post-resume checkpoint。如果要彻底排除 optimizer reset 影响，需要 from-scratch 重跑作为对照。但从 PPL 数值看未见明显 degradation。

---
