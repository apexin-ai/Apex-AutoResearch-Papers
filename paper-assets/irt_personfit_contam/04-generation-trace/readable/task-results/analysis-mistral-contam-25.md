# analysis mistral contam 25

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral_contam_25_20260524T043448_result.json`
- **Structured JSON:** [`3414b425bb7aa49f9924.json`](../../sessions/34/3414b425bb7aa49f9924.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析报告：mistral_contam_25

### 1. 训练状态：成功完成

| 指标 | 值 |
|------|-----|
| EXIT_CODE | 0 |
| Epochs | 3 |
| Steps | 1596 |
| 训练时长 | ~32 min |
| Final loss | 0.952 |
| Mean token accuracy | 0.750 |
| Train loss (avg) | 1.187 |

### 2. Checkpoint 路径

`/root/autodl-tmp/ctrl_contam_mistral/checkpoints/contam_25`

包含 3 个中间 checkpoint（532, 1064, 1596）和最终 adapter。

### 3. 评估状态：**未完成**

`results/` 目录中没有 `contam_25_results.json`。已有结果：
- `clean_results.json`, `contam_15_results.json`, `contam_50_results.json`
- 5 个 clean seed 变体
- `theta_fixed_n10_recompute.json`

### 4. 需要执行的评估命令

**Step 1 — lz\* 评估：**
```bash
cd /root/autodl-tmp/ctrl_contam_mistral
python eval_lz.py --condition contam_25 --gpu 0
```

**Step 2 — theta-fixed Cohen's d 计算：**
需要更新 `theta_fixed_n10_recompute.py` 加入 contam_25 条件后重跑（或手动用 fixed theta=-1.088 重新计算 contam_25 的 lz\*）。

### 5. 已有 Mistral 剂量对比

| 条件 | lz\*\_fixed | Cohen's d (point) | Cohen's d 95% CI | acc\_overall | acc\_seen | acc\_unseen |
|------|-----------|-------------------|-------------------|-------------|----------|------------|
| clean (N=10 seeds) | mean=3.29, std=2.52 | — | — | 0.514 | — | 0.514 |
| contam\_15 | -3.48 | 2.69 | [1.53, 9.06] | 0.595 | 0.744 | 0.569 |
| **contam\_25** | **待评估** | **待计算** | **待计算** | **待评估** | **待评估** | **待评估** |
| contam\_50 | -11.33 | 5.80 | [3.87, 18.45] | 0.673 | 0.752 | 0.594 |

> 注：你提到的 d(15%)=-3.01, d(50%)=-3.50 与 `theta_fixed_n10_recompute.json` 中的值（2.69, 5.80）不一致，可能来自不同的计算方法或版本。实际数据以服务器上 JSON 文件为准。

### 6. 预期

contam_25 的 Cohen's d 应落在 contam_15 (2.69) 和 contam_50 (5.80) 之间，验证剂量-响应关系的单调性。

**下一步：是否需要我执行 eval\_lz.py？**

---
