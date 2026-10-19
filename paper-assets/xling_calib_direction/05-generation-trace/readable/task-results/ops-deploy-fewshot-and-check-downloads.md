# ops deploy fewshot and check downloads

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_fewshot_and_check_downloads_20260521T010841_result.json`
- **Structured JSON:** [`d64b624dfd1c7ec66a86.json`](../../sessions/d6/d64b624dfd1c7ec66a86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 任务 1: transfer_eval.py 部署 ✅

| 检查项 | 结果 |
|--------|------|
| 两个位置行数 | 251 / 251 (≥ 250 ✓) |
| few_shot 出现次数 | 5 / 5 (> 0 ✓) |
| diff | 无差异 ✓ |

### 任务 2: 模型下载进度

| 模型 | 已下载 | safetensors | incomplete | 状态 |
|------|--------|-------------|------------|------|
| Llama4-Scout-W4A16 | **44GB** | 6 | 0 | 进程活跃 (PID 36589) |
| Qwen3-235B-A22B-GPTQ-Int4 | **38GB** | 6 | 0 | 进程活跃 (PID 36611) |

- 两个下载进程仍在运行（可能在下载配置/tokenizer 等小文件，safetensors 分片均已完成无 incomplete）
- 磁盘：350GB 总量，已用 170GB，**剩余 181GB (51%)**

### 任务 3: Procrustes Sensitivity 结果

- **无结果文件**，实验仍在运行（PID 40759，CPU 时间 3285 分钟）
- 进度：已完成 layer 27 全部语言 (zh/ar/hi/sw/ko) × pairs (10-1000)，当前正在处理 **layer 4, ar, n=10**
- 从日志看 Procrustes 对 AUROC 的提升有限，部分语言（如 ko layer 27 n=1000）有小幅正向提升 (+0.033)，而 ECE 改善在高资源语言（如 zh layer 4）上较显著（-0.36）

---
