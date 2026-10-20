# ssh exp012 status and nvidia

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp012_status_and_nvidia_20260522T005735_result.json`
- **Structured JSON:** [`2ec580d261986c57c139.json`](../../sessions/2e/2ec580d261986c57c139.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-012 状态报告

### 进程状态
| PID | 运行时间 | CPU | MEM | 状态 |
|-----|---------|-----|-----|------|
| 54823 | 1h53m32s | 105% | 0.9% | **运行中** |

### 进度
- **设计**: σ ∈ {0.0, 0.1, 0.2, 0.5} × 20 seeds = **80 runs**
- **已完成**: 38 runs（σ=0.0 全部20 seeds + σ=0.1 前18 seeds）
- **进度**: **47.5%**
- **速率**: ~3 min/run
- **ETA**: 剩余 42 runs × 3 min ≈ **2h06m**（约 11:04 完成）

### 已有数据预览（σ=0.0, 20 seeds 完成）

| 指标 | 均值 | std |
|------|------|-----|
| theta_rmse | 0.127 | 0.017 |
| theta_tau | 0.916 | 0.011 |
| cn_rmse | 0.531 | 0.183 |
| cn_corr | 0.871 | 0.076 |
| r_hat | 1.01 | 0.007 |
| ess | 443 | 89 |

σ=0.1（前18 seeds）看起来与 σ=0.0 非常接近，退化极小——theta_rmse 均值约 0.129（+1.6%），cn_rmse 约 0.511（-3.8%，可能是采样波动）。需要等全部 4 个 σ 完成后才能做正式退化分析。

### nvidia-smi
```
Fri May 22 08:58:05 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.119.02             Driver Version: 580.119.02     CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:49:00.0 Off |      0MiB /  97887MiB |      0%   P8   31C |
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |  73639MiB /  97887MiB |     65%   P0   36C |  ← exp-012
|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |      0MiB /  97887MiB |      0%   P8   29C |
|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:B8:00.0 Off |      0MiB /  97887MiB |      0%   P8   29C |
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|    1   N/A  N/A   54823   C   /root/miniconda3/bin/python3   73630MiB                   |
+-----------------------------------------------------------------------------------------+
```

**总结**: exp-012 正常运行，GPU 1 占用 73.6GB / 98GB，温度正常（36°C）。收敛指标良好（r_hat ≤ 1.02）。GPU 0/2/3 空闲可用。预计约 2 小时后完成，届时可做完整退化分析。

---
