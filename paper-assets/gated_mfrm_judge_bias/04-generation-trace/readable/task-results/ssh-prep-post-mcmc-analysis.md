# ssh prep post mcmc analysis

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prep-post-mcmc-analysis_20260524T181708_result.json`
- **Structured JSON:** [`7172e8b7948bb5d91ba6.json`](../../sessions/71/7172e8b7948bb5d91ba6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个脚本全部通过 dry-run 验证。汇总如下：

---

### 产出

`/root/gated_mfrm_judge_bias/analysis/n17_update/` 下 4 个脚本：

| 脚本 | 用途 | 命令行 |
|------|------|--------|
| `compute_tau_n17.py` | MCMC θ̂ vs Arena ELO 的 τ/ρ（N=17 + N=8 子集） | `--mcmc-dir &lt;path> [--output CSV]` |
| `gen_table_latex.py` | 生成 Table 1（方法对比）和 Table 2（per-model θ̂/ĉ） | `--mcmc-dir &lt;path> --tau-csv &lt;path> [--output-dir DIR]` |
| `compare_n8_n17.py` | N=8 vs N=17 共有模型的 θ̂/ĉ/d̂ 差异分析 | `--n8-dir &lt;path> --n17-dir &lt;path> [--output CSV]` |
| `check_phase_diff.py` | Phase 1 vs Phase 2 安全性检查（SAFE/CAUTION/UNSAFE） | `--phase1-dir &lt;path> --phase2-dir &lt;path> [--output CSV]` |

### Dry-run 结果（用 dryrun 数据验证）

- **compute_tau_n17**: 8 行输出，N=17 joint_gmfrm τ=0.779, N=7 subset τ=0.810
- **gen_table_latex**: 成功生成 `table1_method_comparison.tex` 和 `table2_theta_estimates.tex`
- **compare_n8_n17**: joint_gmfrm θ̂ rank τ=0.905，7 个共有模型，max |Δθ|=0.668（dryrun 数据未收敛，正式结果会更稳定）
- **check_phase_diff**: 自比较 → SAFE（rank_tau=1.000, max|Δ|=0.000）

### MCMC 完成后的执行顺序
```bash
DIR=/root/gated_mfrm_judge_bias/exp003/output_n17_phase1
cd /root/gated_mfrm_judge_bias/analysis/n17_update

# 1. 计算 τ
python compute_tau_n17.py --mcmc-dir $DIR

# 2. 生成 LaTeX 表格
python gen_table_latex.py --mcmc-dir $DIR --tau-csv $DIR/results_tau.csv

# 3. N=8 vs N=17 对比
python compare_n8_n17.py --n8-dir /root/gated_mfrm_judge_bias/exp003/output_003b --n17-dir $DIR

# 4. Phase 差异检查（Phase 2 完成后）
python check_phase_diff.py --phase1-dir $DIR --phase2-dir /root/gated_mfrm_judge_bias/exp003/output_n17_phase2
```

---
