# ops irt no05b extract now

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_irt_no05b_extract_now_20260517T073247_result.json`
- **Structured JSON:** [`589e7ae1a20e49a206be.json`](../../sessions/58/589e7ae1a20e49a206be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果写入 `artifacts/mmlu_domain_irt_no05b_results.md`。

核心发现：

| Domain | gamma_mean | 95% CI | CI excludes 0? |
|--------|-----------|--------|----------------|
| STEM_Math | 0.499 | [-0.21, 1.20] | No |
| STEM_Science | 0.504 | [-0.19, 1.20] | No |
| STEM_CS_Eng | 0.497 | [-0.43, 1.40] | No |
| Medical | 0.235 | [-0.42, 0.88] | No |
| **Humanities** | **-0.309** | [-0.85, 0.26] | No |

- STEM 三域 gamma 高度一致 (~0.50)，Medical 偏弱 (0.24)
- **Humanities gamma 为负 (-0.31)**，暗示污染对人文类题目反而有害（或 RRF exposure 在该域标定有误）
- 所有域 95% CI 都包含 0，J=13 per-domain 仍不够 powered
- 诊断优秀：Rhat<1.01, ESS>1300, 零 divergence
- Theta 未保存到磁盘，无法提取 1.5B vs 3B ability 差异

Social_Sciences 正在跑（~60% sampling），Business_Law 和 Other 待跑。预计全部完成还需约 30-40 分钟。

---
