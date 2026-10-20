# analyze generalize pythia1b c4 a100 s43 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_generalize_pythia1b_c4_a100_s43_v2_20260521T051205_result.json`
- **Structured JSON:** [`f47752636970b4b654ad.json`](../../sessions/f4/f47752636970b4b654ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总结果：

```json
{
  "lead_lag": {
    "perm_granger_fdr_fwd": "8/8",
    "perm_granger_fdr_rev": "0/8",
    "K_gte3": "8/8",
    "K_gte4": "1/8",
    "threshold_onset_3sigma": "0/8",
    "diff_xcorr_fdr_fwd": "8/8",
    "TY_fdr_fwd": "1/8",
    "robust_pairs": 8
  },
  "trajectory_summary": {
    "gen0_entropy": 2.956, "gen10_entropy": 1.231,
    "gen0_ppl": 20.60, "gen10_ppl": 1402.54,
    "gen0_distinct1": 0.1137, "gen10_distinct1": 0.1032,
    "gen0_mauve": 0.811, "gen10_mauve": 0.412
  },
  "vs_v1": "PermG 一致 8/8；K≥3 从 6/8 提升至 8/8；threshold_onset 从 2/8 降至 0/8（均无 3sigma 突破点）；diff_xcorr 一致 8/8。v2 共识更强但 onset 信号消失。",
  "conclusion": "success — PermG 8/8 (FPR=0) 完美正向因果，反向 0/8 确认方向性。α=1.0 全替换下 Pythia-1B/C4 domain 展现强 collapse 信号（ppl 68x 恶化，entropy 降 58%），lead-lag 因果关系稳健复现。"
}
```

关键发现：
- **PermG 完美**：正向 8/8 全显著，反向 0/8，方向性无可置疑
- **共识提升**：K≥3 从 v1 的 6/8 升至 8/8，ece→distinct_3 达到 K=4（含 TY）
- **threshold_onset 0/8**：canary 在 gen1 就突变（entropy 从 2.96 骤降至 1.39），但 downstream 无 3sigma onset 检出——信号太强太快，onset 方法失效
- **collapse 剧烈**：ppl 20.6→1402.5（68x），entropy 2.96→1.23，mauve 0.81→0.41

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "lead_lag": {
      "perm_granger_fdr_fwd": "8/8",
      "perm_granger_fdr_rev": "0/8",
      "K_gte3": "8/8",
      "K_gte4": "1/8",
      "threshold_onset_3sigma": "0/8",
      "diff_xcorr_fdr_fwd": "8/8",
      "TY_fdr_fwd": "1/8",
      "robust_pairs": 8
    },
    "trajectory_summary": {
      "gen0_entropy": 2.956,
      "gen10_entropy": 1.231,
      "gen0_ppl": 20.6,
      "gen10_ppl": 1402.54,
      "gen0_distinct1": 0.1137,
      "gen10_distinct1": 0.1032,
      "gen0_mauve": 0.811,
      "gen10_mauve": 0.412
    },
    "vs_v1": "PermG 一致 8/8；K≥3 从 6/8 提升至 8/8；threshold_onset 从 2/8 降至 0/8（均无 3sigma 突破点）；diff_xcorr 一致 8/8。v2 共识更强但 onset 信号消失。",
    "conclusion": "success — PermG 8/8 (FPR=0) 完美正向因果，反向 0/8 确认方向性。α=1.0 全替换下 Pythia-1B/C4 domain 展现强 collapse 信号（ppl 68x 恶化，entropy 降 58%），lead-lag 因果关系稳健复现。"
  }
}
```

</details>

---
