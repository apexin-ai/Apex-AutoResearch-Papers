# autodl-5090 实验进程状态检查

**检查时间**: 2026-05-14 22:28 UTC

## 服务器状态

- **GPU**: 4x GPU, 全部空闲 (0% utilization, 2 MiB each)
- **Python 进程**: 无 run_mvp_pilot 进程存活 (PID 75172 已退出)

---

## exp_007_llama_inference — ✅ 已完成 (FAIL verdict)

| 指标 | NER | RE |
|------|-----|------|
| Greedy F1 | 0.660 | 0.434 |
| Oracle F1 | 0.781 | 0.568 |
| Headroom | +0.121 | +0.135 |
| ρ(κ, F1) full | 0.327 | 0.305 |
| ρ(SJ, F1) full | 0.363 | 0.299 |
| ρ(κ, F1) cond | 0.226 | 0.259 |
| ρ(SJ, F1) cond | 0.311 | 0.405 |
| ρ(logprob) full | 0.183 | 0.288 |
| ρ(logprob) cond | 0.109 | 0.092 |
| Structural > Surface | ✅ YES (+0.036) | ❌ NO (-0.006) |
| Sample F1=0 % | 11.6% | 41.2% |

**Verdict**: FAIL — Joint mode requires RE ρ_sj_full ≥ 0.40 (got 0.299) AND ρ_sj > ρ_fk AND headroom ≥ 2pp.

**亮点**: NER subtask structural consistency (SJ) 胜过 surface (FK)，ρ_sj_cond=0.311 > ρ_fk_cond=0.226。RE conditional ρ_sj_cond=0.405 也不错，但 full 维度 structural 未胜出。

**问题**: RE 41.2% samples F1=0，建议降温至 T=0.7 重试。

---

## exp_003_wnut17_eval — ✅ 已完成 (FAIL verdict)

| 指标 | 值 |
|------|------|
| Greedy F1 | 0.523 |
| Oracle F1 | 0.664 |
| Headroom | +0.141 |
| ρ(κ, F1) full | 0.125 |
| ρ(SJ, F1) full | 0.089 |
| ρ(κ, F1) cond | 0.169 |
| ρ(SJ, F1) cond | 0.288 |
| ρ(logprob) full | -0.409 |
| ρ(logprob) cond | 0.350 |
| Structural > Surface | ❌ NO (-0.036) |
| Sample F1=0 % | 53.7% |
| Gold-empty filtered | 598/1287 (46.5%) |

**Verdict**: FAIL — structural_beats_surface=false, >50% samples F1=0.

**问题**:
1. 53.7% samples F1=0 极高，模型在 WNUT17 上采样质量差
2. 46.5% gold-empty 实例被过滤，有效评估实例仅 689
3. Full logprob ρ 为负 (-0.409)，说明高置信度样本反而更差（可能是 calibration 问题）
4. Conditional logprob ρ=0.350 反而最强，说明过滤 gold-empty 后 logprob 信号恢复

---

## Registry 更新

- `exp_007_llama_inference`: RUNNING → DONE (conclusion=success)
- `exp_003_wnut17_eval`: RUNNING → DONE (conclusion=success, 原为 killed 已修正)
