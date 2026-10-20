# code data consistency fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data-consistency-fix_20260521T063551_result.json`
- **Structured JSON:** [`6b55fcb2e674113eb735.json`](../../sessions/6b/6b55fcb2e674113eb735.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功，输出无 error。

---

```
=== 数值修正对比 ===

文件: compute_supplementary_stats.py
  Qwen CLS s42:  85.34 → 84.48 (source: cls8b-s42-resume-ckpt3600-test-v2)
  Qwen TRAJ s42: 72.92 → 70.83 (source: qwen3-8b-traj-repo-s42-best-eval, D159)

文件: integrate_cwm_results.py
  CLS_REPO Qwen s42:  85.34 → 84.48
  TRAJ_REPO Qwen s42: 72.92 → 70.83
  + DeepSeek CLS s123=74.93 标注 known_outlier，quality_check 不再触发 ANOMALY

文件: w5_mixed_effects_v2.py
  ✓ 无硬编码 CLS/TRAJ 值，从 eval_dirs 动态读取，无需修改

文件: plot_figure2_v2.py
  TRAJ Qwen mean: 73.61 → 72.91
  TRAJ Qwen std:  3.15 → 3.61
  CLS Qwen std:   0.66 → 0.67

统计结果变更 (artifacts/supplementary_statistics.txt):
  Bootstrap CI:
    CLS / Qwen3-8B:  mean 85.11 → 84.83, SD 0.63 → 0.67
    TRAJ / Qwen3-8B: mean 73.61 → 72.91, SD 3.18 → 3.61
  Cohen's d:
    CLS vs TRAJ (Qwen3-8B): 5.015 → 4.590 (still large)
  CLS mean → CWM delta:
    Qwen3-8B: Δ +20.75 → +20.47 pp
  Power Analysis:
    CLS vs TRAJ (Qwen3-8B): d_paired 4.346 → 4.054, Power 0.940 → 0.914
```

---
