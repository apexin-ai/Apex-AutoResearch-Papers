# infra full status check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-status-check_20260513T230608_result.json`
- **Structured JSON:** [`8afb87c888f1cd92ace1.json`](../../sessions/8a/8afb87c888f1cd92ace1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 全面状态报告

### 1. 服务器连通性：✓ 正常
- Uptime: 99 天
- 根分区：**87% 已用**（27GB/30GB，仅剩 4GB）
- 数据盘：`/root/autodl-tmp` 14GB/250GB（剩余 237GB）

### 2. GPU 状态：全部空闲

| GPU | 利用率 | 显存占用 | 总显存 | 温度 |
|-----|--------|----------|--------|------|
| 0 | 0% | 3 MiB | 97887 MiB | 29°C |
| 1 | 0% | 0 MiB | 97887 MiB | 27°C |
| 2 | 0% | 0 MiB | 97887 MiB | 26°C |
| 3 | 0% | 0 MiB | 97887 MiB | 27°C |

**无任何 GPU 计算进程。**

### 3. Uniform Baseline（3 seeds）：全部崩溃

**根因：磁盘满。** 3 个训练全部在 **step 1000/6103（16%）** 崩溃：
```
SafetensorError: I/O error: No space left on device (os error 28)
```

| Seed | 最后 step | 最终 loss（micro-batch） | Checkpoint | Final Model |
|------|-----------|-------------------------|------------|-------------|
| 42 | 999 | ~0.95-2.5 | ✓ 500, 1000 | ✗ |
| 123 | 999 | ~2.4-2.8 | ✓ 500, 1000 | ✗ |
| 456 | 999 | ~1.8-2.5 | ✓ 500, 1000 | ✗ |

- 3 个 uniform 输出共占 **10.7GB**（seed42: 3.9G, seed123: 3.4G, seed456: 3.4G）
- tmux sessions 已不存在
- 配置：Qwen3-0.6B, max_steps=6103, batch_size=4, lr=5e-5, 371K 样本

### 4. Detector 10pct：进程卡死

- PID 41716 仍在运行，但 GPU 已释放，处于 `wait_woken` 睡眠状态
- 到达 **step 100/1020**（epoch 0.29），eval AUC=**0.9998**，loss=0.0502
- **自 07:06:47 起无任何新文件产出**（卡死 3+ 分钟）
- 无 final_model、无 predictions、无 calibration_results
- 数据：6796 human + 8524 synthetic 样本
- 输出占 1.7GB

### 5. 需要的操作

1. **Kill 卡死的 detector 进程**（PID 41716）
2. **释放根分区磁盘**：删除 3 个失败的 uniform checkpoint（可释放 ~10.7GB），或将 output 目录迁移到数据盘 `/root/autodl-tmp/`
3. **所有输出目录改到 `/root/autodl-tmp/provenance_weight_training/output/`**，避免再次磁盘满
4. **重启 detector 10pct**（output 指向数据盘）
5. **重启 3 个 uniform baseline**（output 指向数据盘，可从 checkpoint-1000 resume）

**核心问题：所有实验输出写在根分区（30GB），而非数据盘（250GB）。** 需要修改输出路径后全部重跑。

---
