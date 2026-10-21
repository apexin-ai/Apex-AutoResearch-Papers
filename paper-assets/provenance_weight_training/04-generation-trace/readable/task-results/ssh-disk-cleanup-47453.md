# ssh disk cleanup 47453

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_disk_cleanup_47453_20260517T082125_result.json`
- **Structured JSON:** [`010ab7dea63a39e436e3.json`](../../sessions/01/010ab7dea63a39e436e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。结果汇总：

## 清理报告

### 数据盘 `/dev/md0`（checkpoint 所在盘）
| | 大小 | 已用 | 可用 |
|---|---|---|---|
| 清理前 | 250G | 226G | 25G |
| 清理后 | 250G | 153G | 98G |
| **释放** | | | **+73G** |

- 删除 **65 个中间 checkpoint**（~73.5G），每个已完成实验仅保留最高 step 的 checkpoint
- 跳过了 4 个 RUNNING 实验的所有文件

### 根文件系统 `overlay`
| | 大小 | 已用 | 可用 |
|---|---|---|---|
| 当前 | 30G | 24G | 6.9G |

根文件系统空间未变化，因为 checkpoint 不在此盘。根盘主要被 miniconda3（12G）和 data（11G）占用，这些是运行必需的。

### RUNNING 实验 output_dir 确认：**YES**
全部 4 个 RUNNING 实验均指向 `/root/autodl-tmp/`：
- `grid_b0_3_seed123` → `/root/autodl-tmp/output/models/grid_b0_3_seed123/`
- `rho02_adaptive_tau09_seed42` → `/root/autodl-tmp/output/models/rho02_adaptive_tau09_seed42/`
- `batch_adaptive_tau_rho06_seed42` → `/root/autodl-tmp/output/models/batch_adaptive_tau_rho06_seed42/`
- `bs8_auto_nmin_seed42` → `/root/autodl-tmp/output/models/bs8_auto_nmin_seed42/`

---
