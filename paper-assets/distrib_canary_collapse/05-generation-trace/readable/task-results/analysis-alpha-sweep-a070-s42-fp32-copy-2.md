# analysis alpha sweep a070 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a070_s42_fp32_20260521T054549_result.json`
- **Structured JSON:** [`6c845ebb545b3ea08ce9.json`](../../sessions/6c/6c845ebb545b3ea08ce9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 实验状态
- EXIT_CODE = 0（正常完成）
- 11 generations (gen 0–10), synthetic_ratio = 0.70, Pythia-410m, wikitext-103, seed 42, fp32
- **5-method 检测分析尚未运行**——服务器上只有 raw all_metrics.json，无 5method JSON

### Raw all_metrics.json（全部 11 代）

| gen | token_entropy | ece | distinct_1 | distinct_2 | distinct_3 | perplexity | mauve |
|-----|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 3.234 | 0.011 | 0.098 | 0.514 | 0.813 | 26.9 | 0.031 |
| 1 | 2.179 | 0.135 | 0.098 | 0.512 | 0.812 | 31.3 | 0.031 |
| 2 | 2.128 | 0.171 | 0.084 | 0.440 | 0.730 | 41.4 | 0.033 |
| 3 | 2.153 | 0.176 | 0.078 | 0.393 | 0.663 | 45.4 | 0.033 |
| 4 | 2.147 | 0.186 | 0.075 | 0.367 | 0.617 | 50.7 | 0.032 |
| 5 | 2.189 | 0.187 | 0.073 | 0.352 | 0.589 | 53.8 | 0.034 |
| 6 | 2.204 | 0.193 | 0.072 | 0.345 | 0.576 | 57.9 | 0.033 |
| 7 | 2.202 | 0.200 | 0.072 | 0.342 | 0.569 | 60.8 | 0.029 |
| 8 | 2.244 | 0.201 | 0.072 | 0.340 | 0.565 | 63.5 | 0.033 |
| 9 | 2.277 | 0.199 | 0.071 | 0.337 | 0.560 | 65.2 | 0.033 |
| 10 | 2.296 | 0.202 | 0.071 | 0.336 | 0.557 | 67.8 | 0.031 |

### Canary 信号特征
- **token_entropy**: gen 0→1 骤降 3.23→2.18（-32%），之后稳定在 2.1-2.3
- **ece**: gen 0→1 骤升 0.011→0.135（+12x），之后渐升至 0.20
- 两个 canary 均在 gen 1 出现明显 onset

### Downstream 退化
- **distinct_1/2/3**: 单调下降，distinct_1 从 0.098→0.071（-28%），distinct_3 从 0.813→0.557（-31%）
- **perplexity**: 单调上升 26.9→67.8（+152%）
- **mauve**: 始终极低（~0.031），无明显趋势

### 与 α=0.65 对比（已有 5-method 分析）

| 指标 | α=0.65 | α=0.70（预估）|
|------|--------|--------------|
| PermG_fdr_forward | **0/8** | 待计算 |
| diff_xcorr_fdr_forward | **6/8** | 待计算 |
| threshold_3sigma_forward | **0/8** | 待计算 |
| TY_forward | 4/8 | 待计算（C003 限制：不可引用） |
| robust_pairs (K≥3) | **1/8** | 待计算 |

### 评估

α=0.70 的 raw metrics 显示 collapse 信号比 α=0.65 更强（higher ece ceiling 0.20 vs ~0.19, steeper distinct_* decline）。考虑到 α=0.75 已知是强检测成功点，α=0.70 大概率位于 dip 区间向恢复区间的过渡带。

**下一步需要运行 5-method detection analysis** 才能得到 PermG、diff_xcorr 等检测指标。要我现在在服务器上跑分析脚本吗？

---
