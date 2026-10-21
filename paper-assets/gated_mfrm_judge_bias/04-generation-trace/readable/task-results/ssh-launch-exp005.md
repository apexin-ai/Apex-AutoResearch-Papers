# ssh launch exp005

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_launch_exp005_20260522T200907_result.json`
- **Structured JSON:** [`f981e9ed0ef50917b8f0.json`](../../sessions/f9/f981e9ed0ef50917b8f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-005 已完成运行，汇报如下：

**1. 启动命令**
```
cd /root/gated_mfrm_judge_bias/exp005 && python run_exp005.py 2>&1 | tee /tmp/exp005.log
```

**2. 进程状态**：已完成（运行时间 <15 秒，CPU-only 轻量实验）

**3. 关键结果**
- `joint_gmfrm`: real c_n ≈ **MVP-002 (strong)**，mean=2.4782，strong_ratio=2.07x
- `sequential`: real c_n ≈ **MVP-001 (weak)**，mean=0.0587，weak_ratio=0.15x
- `joint_gmfrm_003b`: real c_n ≈ **MVP-002 (strong)**，mean=2.4625，strong_ratio=2.06x
- τ improvement (joint vs raw): **+0.0714 (+9.1%)**
- KS test vs mvp_003: D=0.4474, p=0.0561

**4. 产出文件** (`/root/gated_mfrm_judge_bias/exp005/results/`)
- `results.json` (5.2KB)
- `calibration_comparison.png` / `.pdf`
- `ranking_impact.png`

**5. exp-003b 输出**：可用，`joint_gmfrm_c.npy`、`results.json` 等齐全

---
