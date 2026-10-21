# diag exp012 sigkill

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp012_sigkill_20260515T171456_result.json`
- **Structured JSON:** [`c65718afffd5f4aa1c2e.json`](../../sessions/c6/c65718afffd5f4aa1c2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 已完全释放：0MiB 占用，无残留进程。

---

## 诊断报告

### 1. dmesg OOM killer 记录
容器内无 dmesg 权限（`Operation not permitted`），无法直接确认 OOM killer。

### 2. 根因分析
日志明确显示 **不是 host RAM OOM (SIGKILL/137)**，而是 **GPU VRAM 冲突**：

```
ValueError: Free memory on device cuda:0 (7.01/94.97 GiB) on startup is less than
desired GPU memory utilization (0.9, 85.48 GiB).
```

exp012_llama_8b 启动时（00:26），GPU 已被另一个 exp012 实例占用 ~88GB VRAM（该实例在 `artifacts/exp012/` 产出了成功结果，时间戳 00:37-00:45）。**两个实验并行运行同一 GPU 导致 VRAM 不足**。

### 3. 清理前/后 free -h 对比

| 指标 | 清理前（诊断时） | 清理后 |
|------|---------|--------|
| Total RAM | 1.0 TiB | 1.0 TiB |
| Used | 85 GiB | 87 GiB |
| Available | 913 GiB | 911 GiB |
| GPU VRAM | 0 MiB (已自行释放) | 0 MiB |

Host RAM 从未紧张（1TB 总量，>900GB 可用）。

### 4. vLLM 裸跑结果：**成功**

- 模型加载耗时 15.66 秒，占用 14.99 GiB VRAM
- KV cache 分配 63.58 GiB（`gpu_memory_utilization=0.80`）
- 推理正常，生成输出 "Hope you're having a great day so far..."
- `EXIT_CODE=0`，引擎正常关闭

### 5. 重试 exp012 条件
- **确保 GPU 无其他进程占用**：运行前 `nvidia-smi` 确认 0MiB
- **不要并行启动多个 vLLM 实例到同一 GPU**
- `gpu_memory_utilization=0.80` 已验证可行（留 ~20GB 余量比 0.9 更安全）
- Host RAM 完全不是瓶颈

---
