# ssh prep falcon7b profiling

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prep_falcon7b_profiling_20260516T015709_result.json`
- **Structured JSON:** [`3ba2b36ff42bd377fb04.json`](../../sessions/3b/3ba2b36ff42bd377fb04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the summary:

### Pre-check Results

| Item | Status | Detail |
|------|--------|--------|
| **Profiling 脚本** | **不存在** | `/root/ratekv/run_falcon7b_hires_profiling.py` 不在服务器上，需要同步 |
| **Falcon-7B 模型** | **未下载** | HF cache 中无 falcon 相关目录，需下载 (~14GB) |
| **GPU 0** | 占用中 | `run_internlm2_hires_profiling.py --gpu cuda:0` 运行中，23.2/97.9 GB，100% util |
| **GPU 1** | **空闲** | 3 MiB / 97.9 GB，0% util |
| **依赖** | OK | torch 2.10.0+cu128, transformers 4.57.6 |
| **数据盘** | 45GB 可用 | /root/autodl-tmp 250G 用了 206G |

### 阻塞项

1. **脚本需同步** — 本地有 `run_falcon7b_hires_profiling.py`，需 push 到 remote 后在服务器 `git pull`，或直接 SSH 创建
2. **模型需下载** — `tiiuae/falcon-7b` (~14GB)，数据盘剩 45GB 够用。脚本默认路径 `/root/autodl-tmp/.hf_cache/tiiuae/falcon-7b`
3. **脚本默认 `--gpu cuda:0`** — 启动时需指定 `--gpu cuda:1`

### 结论

**不能立即启动。** 需要先同步脚本 + 下载模型。是否继续执行这两步？

---
