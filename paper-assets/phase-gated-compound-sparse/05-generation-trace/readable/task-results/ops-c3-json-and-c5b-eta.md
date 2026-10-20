# ops c3 json and c5b eta

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c3_json_and_c5b_eta_20260514T180034_result.json`
- **Structured JSON:** [`f7f39e876e706924d976.json`](../../sessions/f7/f7f39e876e706924d976.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 任务 1：c3_llama 完整统计数据

文件已复制到服务器 `artifacts/` 和本地 `artifacts/c3_llama_results.json`。

**c3_llama_results.json 完整数据**（model: DeepSeek-R1-Distill-Llama-8B, n=50, bootstrap=10000, Bonferroni k=4）:

| Sparsity | imp_vs_rand d_z | d_z CI | interpret | Wilcoxon p | p_bonf | sig? | mean_diff | phase_grad_imp d_z | phase_grad_rand d_z |
|----------|----------------|--------|-----------|-----------|--------|------|-----------|-------------------|-------------------|
| **s015** (0.15) | 0.192 | [-0.086, 0.496] | negligible | 0.0549 | 0.219 | **No** | 0.021 | **1.008** (large) | 0.350 (small) |
| **s020** (0.20) | 0.255 | [-0.025, 0.538] | small | 0.0632 | 0.253 | **No** | 0.072 | **1.108** (large) | 0.373 (small) |
| **s025** (0.25) | 0.290 | [0.008, 0.612] | small | 0.0209 | 0.083 | **No** | 0.151 | **1.123** (large) | 0.448 (small) |
| **s030** (0.30) | 0.335 | [0.061, 0.663] | small | 0.0074 | **0.029** | **Yes** | 0.323 | **1.004** (large) | 0.439 (small) |

关键数字：
- **imp_vs_rand**：只有 s030 在 Bonferroni 校正后显著（p=0.029）；效应量随 sparsity 单调增长 0.19→0.34
- **phase_gradient_importance**：所有 sparsity 下 d_z≈1.0-1.1（large），importance pruning 的 loss 在 phase 间有强梯度
- **phase_gradient_random**：d_z≈0.35-0.45（small），random pruning phase 梯度弱得多

---

## 任务 2：c5b_pilot 进度

**进程活跃**：PID 153367，CPU 105%，运行中。

```
python run_c5b_pilot.py --sparsity 0.25 --strategy all --gpu 0
```

配置：30 problems × all strategies × s025，单 GPU (CUDA_VISIBLE_DEVICES=3)

**已完成 5/30 problems**（日志 25 行）：

| Problem | 耗时 | gen_len | phases |
|---------|------|---------|--------|
| 1 (algebra/2470) | 42s | 935 | 9 |
| 2 (prealgebra/192) | 20s | 399 | 11 |
| 3 (intermediate_algebra/134) | 56s | 1050 | 17 |
| 4 (algebra/841) | 149s | 2048 | 31 |
| 5 (algebra/478) | 19s | 391 | 8 |

- 当前正在处理 problem 6 (algebra/988)
- 平均 ~57s/problem，方差大（19s~149s，取决于 gen_len）
- **ETA：剩余 25 problems × ~57s ≈ 24 min，预计 ~02:25 UTC 完成**（约 20 多分钟后）

---
