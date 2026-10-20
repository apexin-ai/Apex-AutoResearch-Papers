# check transformers offline status

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_transformers_offline_status_20260513T163930_result.json`
- **Structured JSON:** [`841511f22af61ab93365.json`](../../sessions/84/841511f22af61ab93365.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

**两个实验都未运行，启动即失败。**

### 日志内容（两个文件完全一致，91 字节）

```
bash: line 1: cd: /root/phase-gated-compound-sparse: No such file or directory
EXIT_CODE=1
```

### nvidia-smi

- 2x NVIDIA RTX PRO 6000 Blackwell (98GB)
- GPU 利用率 0%，无运行进程
- GPU 0 有 ~49GB 显存占用但无进程（可能是之前实验的残留）

### 根因

实验启动时有某个步骤尝试 `cd /root/phase-gated-compound-sparse`（该目录不存在）。`env.sh` 本身没有这个 cd，问题可能出在 tmux session 启动命令或 `.bashrc` 中。脚本 `set -e` 导致遇到错误立即退出，实验从未真正开始。

### 结论

- **网络/模型下载问题**：不适用——实验从未执行到加载模型的阶段
- **`TRANSFORMERS_OFFLINE=1` 缺失**：同样不适用，实验未启动
- **需要干预**：**是**。需要排查 `cd /root/phase-gated-compound-sparse` 的来源（检查 `.bashrc` 或 tmux 启动命令），修复后重新启动两个实验

---
