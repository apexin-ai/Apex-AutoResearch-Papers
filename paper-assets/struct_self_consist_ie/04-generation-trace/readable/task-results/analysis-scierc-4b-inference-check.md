# analysis scierc 4b inference check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc_4b_inference_check_20260515T195900_result.json`
- **Structured JSON:** [`f28f960c8b7ef2418492.json`](../../sessions/f2/f28f960c8b7ef2418492.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE，cron 已清除。

## 4B vs 8B SciERC Delta 对比

| 指标 | 4B (Qwen3) | 8B (LLaMA) | Delta |
|------|-----------|-----------|-------|
| **NER** | | | |
| greedy_f1 | 0.6612 | 0.6601 | **+0.11pp** |
| oracle_f1 | 0.7839 | 0.7813 | +0.27pp |
| oracle_headroom | 12.28pp | 12.12pp | +0.16pp |
| fleiss_kappa | 0.363 | 0.451 | **-8.83pp** |
| soft_jaccard | 0.642 | 0.741 | **-9.92pp** |
| SJ ρ (full) | 0.422 | 0.363 | **+5.91pp** |
| SJ ρ (cond) | 0.381 | 0.311 | **+6.94pp** |
| FK ρ (full) | 0.326 | 0.327 | -0.08pp |
| LP ρ (full) | 0.280 | 0.183 | **+9.73pp** |
| LP AUROC (full) | 0.644 | 0.596 | **+4.75pp** |
| structural_beats_surface | YES | YES | -- |
| rho_advantage_pp | +9.62 | +3.64 | **+5.98pp** |
| **RE** | | | |
| greedy_f1 | 0.4136 | 0.4335 | **-2.00pp** |
| oracle_f1 | 0.5846 | 0.5683 | +1.62pp |
| oracle_headroom | 17.10pp | 13.48pp | +3.62pp |
| fleiss_kappa | 0.219 | 0.368 | **-14.85pp** |
| soft_jaccard | 0.522 | 0.683 | **-16.07pp** |
| SJ ρ (full) | 0.267 | 0.298 | -3.12pp |
| SJ ρ (cond) | 0.347 | 0.405 | **-5.85pp** |
| FK ρ (full) | 0.359 | 0.305 | +5.45pp |
| LP ρ (full) | 0.351 | 0.288 | **+6.28pp** |
| LP AUROC (full) | 0.666 | 0.643 | +2.30pp |
| structural_beats_surface | NO | NO | -- |
| rho_advantage_pp | -9.20 | -0.64 | **-8.56pp** |
| sample_f1_pct_zero | 47.6% | 41.2% | +6.45pp |
| **Verdict** | FAIL | FAIL | -- |

### 关键发现

1. **NER 子任务 4B 略优于 8B**：greedy F1 持平，但 SJ ρ 和 LP ρ 均大幅领先（+5.9pp / +9.7pp），structural_beats_surface 优势从 +3.6pp 扩大到 +9.6pp。
2. **RE 子任务 4B 明显劣于 8B**：一致性大幅下降（κ -14.9pp, SJ -16.1pp），SJ ρ_cond 从 0.405 降至 0.347（低于 0.40 阈值），F1=0 比例升至 47.6%。
3. **两个模型在 SciERC RE 上都 FAIL**，主因是 RE 任务 ρ_sj < 0.40 且 structural 未能 beat surface。4B 的 RE 退化更严重——agreement 指标塌陷说明 4B 模型在 RE 上生成的多样本一致性差。
4. **Logprob baseline 4B 全面更强**：LP ρ 和 AUROC 在 NER/RE 的 full 集上都超过 8B，表明 4B 的 logprob 信号更有区分力。

---
