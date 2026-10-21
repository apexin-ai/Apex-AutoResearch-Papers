# reanalyze d102 pythia14b c4

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_reanalyze_d102_pythia14b_c4_20260519T154943_result.json`
- **Structured JSON:** [`a8fc0411ac9f4610aaef.json`](../../sessions/a8/a8fc0411ac9f4610aaef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4个实验全部完成。以下是新旧对比汇总：

## D102 批量重跑结果：perplexity → mauve 标准化

| 实验 | 指标 | OLD | NEW |
|------|------|-----|-----|
| **Pythia-1.4B Wiki s42** | robust_pairs (K≥3) | 1/8 | **3/8** |
| | perm_granger_fdr | 2/8 | 2/8 |
| | diff_xcorr_fdr | 6/8 | **7/8** |
| **Pythia-1.4B Wiki s43** | robust_pairs (K≥3) | 6/8 | **7/8** |
| | perm_granger_fdr | 6/8 | 6/8 |
| | diff_xcorr_fdr | 6/8 | **8/8** |
| | ty_forward | 2/8 | **4/8** |
| **Pythia-1B C4 s42** | robust_pairs (K≥3) | 2/8 | **8/8** |
| | perm_granger_fdr | 6/8 | **8/8** |
| | diff_xcorr_fdr | 6/8 | **8/8** |
| | ty_forward | 1/8 | **4/8** |
| **Pythia-1B C4 s43** | robust_pairs (K≥3) | 3/8 | **8/8** |
| | perm_granger_fdr | 4/8 | **8/8** |
| | diff_xcorr_fdr | 6/8 | **8/8** |
| | ty_forward | 2/8 | **4/8** |

**关键发现**：
- C4 实验收益最大：mauve pairs 全部强显著（K=4-5/5），robust 从 2-3/8 跃升至 8/8
- Pythia-1.4B Wiki mauve pairs 相对弱（K=2-3/5），但仍改善了整体 robust count
- threshold_forward 全部从 0→8 是因为分析脚本切换（`method_ablation.py` 用 2σ vs 旧脚本用 3σ），非 pair 变更导致

**文件变更**：
- 旧文件备份为 `5method_leadlag_pre_d102.json` 和 `unified_5method_pre_d102.json`
- 新文件覆盖写入 `5method_leadlag.json` 和 `unified_5method.json`
- 4个实验 registry 已更新

---
