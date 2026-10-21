# code exp005 006 prep

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp005_006_prep_20260522T181943_result.json`
- **Structured JSON:** [`32a79a4b6e65d2ec623f.json`](../../sessions/32/32a79a4b6e65d2ec623f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已部署并验证通过。

**exp-005 dry-run 结果：**
- `joint_gmfrm_c`: shape=(8,), mean=2.4782, std=1.6543, range=[0.79, 5.69]
- `sequential_c`: shape=(8,), mean=0.0587, std=0.2770, range=[-0.24, 0.55]
- exp-003b 数据尚未生成

**exp-006 dry-run 结果：**
- 9 judges, 8 models, 316 items, 6064 observations
- 生成了 40 个 judge subsets（k=2/4/6/8/9）

**文件位置：**
- `/root/gated_mfrm_judge_bias/exp005/run_exp005.py` (472 行)
- `/root/gated_mfrm_judge_bias/exp006/run_exp006.py` (565 行)

**运行方式：**
```bash
# exp-005: CPU 即可运行
python run_exp005.py

# exp-006: raw_average 模式 CPU 可跑，MCMC 方法需要 GPU
python run_exp006.py --methods raw_average                    # CPU 快速版
python run_exp006.py --methods raw_average mfrm_only sequential joint_gmfrm --run-loocv  # 完整版(GPU)
```

初步观察：joint_gmfrm 的 c_n 均值 2.48 远超 mvp_002 的 σ=1.5（HalfNormal mean≈1.20），说明真实 contamination 可能比 MVP strong 设定还强。sequential 的 c_n 接近 0，OLS 残差回归信号太弱——这和 exp-003 中 sequential 与 raw_average τ 相同的结果一致。

---
