# ssh exp003b analysis script

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp003b_analysis_script_20260522T185021_result.json`
- **Structured JSON:** [`fc68f6f2e6db246ca812.json`](../../sessions/fc/fc68f6f2e6db246ca812.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 产出

**1. 脚本路径和使用方法**

`/root/gated_mfrm_judge_bias/exp003/analyze_003b.py`

```bash
# 003b 完成后一键分析（partial mode — 用 point estimates）
cd /root/gated_mfrm_judge_bias/exp003
python analyze_003b.py

# 需要完整后验诊断（trace plots、CI、per-param R-hat）
python analyze_003b.py --refit    # 重跑 MCMC ~2h
```

输出到 `output_003b/analysis/`：
- `summary.json` — 完整结果 JSON
- `theta_vs_elo.png` — θ vs Arena Elo 散点图
- `c_ranking.png` — c_n 排序柱状图
- `trace_theta/c/d/sigma_c.png` — trace plots（仅 full mode）
- `posterior_c/d.png` — posterior density（仅 full mode）

**2. 依赖是否齐全**

全部就绪：arviz 1.1.0, numpyro 0.21.0, jax 0.10.1, matplotlib 3.10.5, scipy 均已安装。

**3. 预期运行时间**

- Partial mode（默认）：< 5 秒
- Full mode（`--refit`）：~2h（重跑 4000+4000 × 4 chains MCMC）

### 注意事项

当前正在运行的 003b 进程用的是未修改的 `run_exp003.py`，**不会保存完整 MCMC samples**。只会产出 `joint_gmfrm_theta.npy`、`joint_gmfrm_c.npy`、`results.json` — 足以运行 partial mode 分析（Arena correlation + 参数排名 + 2 张图）。

已修改 `run_exp003.py` 增加 InferenceData 保存（行 100-107），未来重跑 exp-003 系列实验时会自动生成 `joint_gmfrm_idata.nc`，届时 `analyze_003b.py` 自动进入 full mode（完整 R-hat/ESS/trace plots/CI）。

---
