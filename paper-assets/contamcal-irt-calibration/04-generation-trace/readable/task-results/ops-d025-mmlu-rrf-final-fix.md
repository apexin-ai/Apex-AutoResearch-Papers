# ops d025 mmlu rrf final fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d025_mmlu_rrf_final_fix_20260517T003746_result.json`
- **Structured JSON:** [`62541bd44c4e6003a059.json`](../../sessions/62/62541bd44c4e6003a059.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

## 结果

| 指标 | 旧值 (s1+s2 only) | 新值 (s1+s2+s4) |
|------|-------------------|-----------------|
| **MMLU γ mean** | 0.7095 | **0.2132** |
| **MMLU γ 95% CI** | [-0.3775, 1.8215] | **[-0.7813, 1.2546]** |
| **CI excludes zero** | False | False |
| **N respondents** | ? (likely fewer) | **20** |
| **N items** | 300 | 300 |
| **PPP** | — | **0.8652** |
| **residual MAE** | — | **0.0166** |
| **Rhat** | — | 1.0076 (ok) |
| **Divergent** | — | 0 |

关键变化：加入 s4_selfcritique 后，MMLU contamination effect (γ) 从 0.71 降至 0.21，CI 更集中。N 从旧运行升至 20（包含 0.5B/1.5B/3B 全量模型但 0.5B eval 未匹配所以实际是 1.5B+3B 共 20 个）。

已完成：
1. 确认并删除旧 RRF 文件
2. 用 3 信号重生成 `rrf_d025/per_model/` 和 `exposure_scores.json`
3. 更新 `rrf_cross_family_v3/exposure_scores.json`（7 个 d025 模型）
4. 重跑 MMLU IRT (2PL+γ, scales=0.5B/1.5B/3B, N=20)
5. 结果写回 `results_cross_family_irt_v3/pooled_rrf_irt_results.json`

---
