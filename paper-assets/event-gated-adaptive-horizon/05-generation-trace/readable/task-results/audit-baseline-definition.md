# audit baseline definition

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_baseline_definition_20260524T063436_result.json`
- **Structured JSON:** [`a6a6a07ced24b165fb97.json`](../../sessions/a6/a6a6a07ced24b165fb97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整分析：

---

## NVE baseline 定义

**论文原文（methodology.tex:38）**：
> NVE_t = (v/e)_{config,t} / (v/e)_{baseline,t}
> baseline is the highest-performing seed (exp\_001, seed 1, 505K steps)
> 限制 35K+ window 避免早期膨胀

**appendix.tex:268 矛盾**：
> Walker NVE is normalized against the 4-seed mean baseline (seeds 1–4, each run to 505K+ steps)

**主文说单 seed，附录说 4-seed 均值。** appendix:266 进一步确认：单 seed 归一化 AUROC=0.933，4-seed 均值 AUROC=0.867。实际 `paper_data_walker_walk.json` 中 `baseline_ve_reference` 使用的是 **单 seed s1** 的值。

---

## baseline=0.331 来源

- **实验**：exp_001 (baseline_s1)，单次运行，seed 1
- **step**：45000
- **计算**：value_mean(170.066) / eval_return(513.766) = **0.3310**
- **性质**：单个 run 在单个 step 的瞬时值，非多 seed 平均

---

## baseline=0.683 来源

最接近匹配：exp_001 s1 在 **step 115K**：ve_ratio = **0.6826**（≈0.683）
- value_mean(627.884) / eval_return(919.814) = 0.6826

附录 Table baseline_seeds 中 4-seed 均值 ve@105K = (0.656+0.742+0.664+0.624)/4 = **0.6715**，不是 0.683。

---

## exp_001 vs exp_044 对比

| 属性 | exp_001 (baseline_s1) | exp_044 (gradient_stop_walker) |
|------|----------------------|-------------------------------|
| **任务** | walker_walk | walker_walk |
| **dt** | 1 (固定) | 2 (gate 固定输出 dt=2) |
| **dt_embed** | 无 (N/A) | **有**，但 reward 梯度被 detach (`reward_dt_emb_detach`) |
| **gate** | 无 | 有（但输出恒为 dt=2） |
| **subsample** | false | false |
| **horizon** | 15 | 15 |
| **CIVO 监控** | 无 civo/* 字段 | 有 civo/ve_ratio, civo/alert |
| **训练步数** | 505K+ | ~224K |
| **eval@105K** | 915.7 | ~148 (ve_ratio=0.75, peak CIVO) |
| **CIVO 行为** | 健康（NVE=1.0x） | 触发 CIVO（ve_ratio peak=4.4@95K），**自纠正**（→0.097@215K，eval→538） |

---

## 差异原因

exp_001 和 exp_044 是**完全不同类型的实验**：

1. **exp_001 是 vanilla DreamerV3 baseline**：dt=1，无 gate，无 dt_embed，无时间变率
2. **exp_044 是 SGS（选择性梯度停止）治疗实验**：有 gate（固定 dt=2），有 dt_embed 但 reward loss 梯度被 detach，用于测试"阻断 reward→dt_embed 梯度是否能防止 CIVO"

结论：**detach reward 梯度不阻止 CIVO 触发**（ve_ratio 仍达 4.4），但加速自修复（exp_044 修复用 40K 步 vs exp_045 无 detach 用 170K 步）。

exp_044 **不在论文数据 JSON 中**，未作为 NVE baseline 使用。论文中 exp_044 对应的讨论在附录 "gradient stopping" 相关段落，以 self-correction 案例出现（appendix 脚注 `†`：eval 44→538, 59% baseline, 224K run）。

---
