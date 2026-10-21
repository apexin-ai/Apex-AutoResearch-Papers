# package supplementary code

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_package_supplementary-code_20260524T030731_result.json`
- **Structured JSON:** [`514d8fffd3c3ce88cd46.json`](../../sessions/51/514d8fffd3c3ce88cd46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

打包完成。汇总：

**文件数量**: 41 个文件（去掉 3 个 .pyc 后为 38 个）

**总大小**: 476K

**目录结构**:
```
artifacts/supplementary/
├── README.md
├── requirements.txt
├── code/
│   ├── dreamer.py, models.py, networks.py, tools.py, exploration.py, parallel.py
│   └── envs/ (dmc.py, atari.py, crafter.py, maniskill.py, wrappers.py, ...)
├── configs/
│   └── configs.yaml
├── scripts/
│   ├── civo_detector.py, compute_gradient_decomposition.py, grad_decomp_008d_corrected.py
│   ├── nve_threshold_analysis_v2.py, nve_threshold_analysis_v3.py
│   ├── nve_audit.py, nve_audit_v2.py, extract_paper_data.py, compute_bootstrap_cis.py
├── analysis/
│   ├── gradient_decomposition_008d_corrected.json, civo_decomposition_data.json
│   ├── entropy_dynamics_data.json, value_vs_eval_data.json
│   ├── nve_threshold_v3.json, nve_4seed_robustness_summary.json
│   ├── baseline_4seed_mean_ve_ratio.csv, bootstrap_cis.json
└── figures/
    ├── fig2_nve_trajectory.py, fig6_collapse_pathways_d054.py, fig_style.py
```

**缺失文件**: 无。所有 `cp` 命令均成功（exit code 0），未出现 "No such file" 错误。

---
