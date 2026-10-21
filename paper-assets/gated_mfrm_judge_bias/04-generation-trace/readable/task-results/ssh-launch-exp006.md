# ssh launch exp006

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_launch_exp006_20260522T200900_result.json`
- **Structured JSON:** [`120ba3bf4242e046c85f.json`](../../sessions/12/120ba3bf4242e046c85f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成，运行非常快（几分钟内）。

## 结果汇报

**启动命令**：
```bash
tmux new-session -d -s exp006 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gated_mfrm_judge_bias/exp006 && CUDA_VISIBLE_DEVICES=0 JAX_PLATFORMS=cuda,cpu XLA_PYTHON_CLIENT_PREALLOCATE=false XLA_PYTHON_CLIENT_MEM_FRACTION=0.25 python run_exp006.py --run-loocv 2>&1 | tee /tmp/exp006.log"
```

**状态**：已完成（40 subsets 全部跑完 + leave-one-out 分析 + 图表生成）

**产出文件**（`/root/gated_mfrm_judge_bias/exp006/results/`）：
| 文件 | 大小 |
|------|------|
| `sensitivity_results.csv` | 6.4 KB (40 rows) |
| `leave_one_out_results.csv` | 756 B |
| `results.json` | 991 B |
| `tau_vs_judge_count.{png,pdf}` | 图表 |
| `leave_one_out.{png,pdf}` | 图表 |

**核心结果 (Kendall-τ vs Arena, raw_average)**：
| k (judge count) | τ mean ± std |
|---|---|
| 2 | 0.7547 ± 0.0878 |
| 4 | 0.7786 ± 0.0405 |
| 6 | 0.8000 ± 0.0301 |
| 8 | 0.7857 ± 0.0000 |
| 9 | 0.7857 |

**注意**：只跑了 `raw_average` 一种方法，crossover 分析报 `insufficient data`。脚本只用了 raw_average 做 baseline，没有跑 G-MFRM 等方法（`--methods` 默认值只包含 `raw_average`）。如果需要对比 G-MFRM vs baseline 的 crossover point，需要重新运行并指定 `--methods raw_average mfrm_only sequential joint_gmfrm`。

---
