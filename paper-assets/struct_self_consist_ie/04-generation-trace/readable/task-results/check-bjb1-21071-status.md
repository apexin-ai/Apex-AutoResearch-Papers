# check bjb1 21071 status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1_21071_status_20260514T142748_result.json`
- **Structured JSON:** [`92406d36d502f0b99fbe.json`](../../sessions/92/92406d36d502f0b99fbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-21071 服务器状态汇总

| 检查项 | 状态 |
|--------|------|
| **连通性** | OK — uptime 31 天，754GB 内存（25GB used），根分区 37% used，数据盘 55% used (113GB 可用) |
| **GPU** | 4× RTX 5090 (32GB)，全部空闲（0% 利用率，2MiB 显存），无 GPU 进程 |
| **CUDA** | Driver 595.58.03, CUDA 13.2 |
| **僵尸进程** | **无训练僵尸进程**。仅有系统自带服务：tensorboard (PID 935, port 6007) 和 jupyter-lab (PID 939)，这两个是 AutoDL 默认启动的，不需要清理 |
| **tmux** | 无残留 session |
| **项目环境** | Python 3.12.3 (conda base)，torch 2.10.0+cu128, transformers 4.57.1, vllm 0.18.1 |
| **Checkpoints** | 11 个模型 checkpoint (qwen3-8b 多个变种 + llama3.1-8b，含 lora 和 merged 版本) |
| **数据** | SciERC / CoNLL2003 / WNUT17 三个数据集均存在 |
| **网络加速** | network_turbo 可用 |

**结论：服务器完全就绪，4 卡空闲，环境齐全，可以立即跑实验。**

---
