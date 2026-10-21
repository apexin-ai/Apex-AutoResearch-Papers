# code ssh check server a

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ssh_check_server_a_20260519T081921_result.json`
- **Structured JSON:** [`f45d10b9731081cdd254.json`](../../sessions/f4/f45d10b9731081cdd254.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

**GPU**: 4× RTX 5090 (32GB each)，全部空闲，0% 利用率，无 GPU 进程。

**32B 模型下载**: **进行中，未完成**。`Qwen2.5-32B-Instruct` 当前已下载 38GB，进程 PID 764903 在跑，日志显示 fetching 27 files 进度约 22% (6/27)。`config.json` 尚未出现，模型不完整。

**磁盘**: `/root/autodl-tmp/` 总 250GB，已用 179GB (72%)，剩余 **72GB**。32B 模型完整约 65GB，空间应该刚好够。

**活跃进程**:
- Qwen2.5-32B-Instruct 下载进程 (PID 764903, 14:40 启动，已运行约 1.5h)
- Tensorboard (port 6007)
- JupyterLab
- 一个旧的 tmux session `exp_001_n16_seed456`

**Tmux sessions**: 17 个，包括多个实验 session（fewnerd、qwen_conll、scierc、各温度/seed 组合），无 screen session。

---
