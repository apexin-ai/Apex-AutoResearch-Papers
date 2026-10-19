# ops check downloads verify llama4

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_downloads_verify_llama4_20260521T003952_result.json`
- **Structured JSON:** [`64a1ede33587ceab83c1.json`](../../sessions/64/64a1ede33587ceab83c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Llama4 下载状态：**进行中**
- 模型：`RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16`（W4A16量化，非GPTQ）
- 路径：`/root/autodl-tmp/models/Llama4-Scout-W4A16/`
- 已下载：**42GB**，已完成 **6/14** 个 safetensors 分片
- 当前有 5 个 `.incomplete` 文件正在下载
- 进程运行 ~80 分钟（07:20 开始），速度约 **525 MB/min (~8.7 MB/s)**
- 预估总大小 ~98GB，ETA 约 **1.5-2 小时**

### 2. Qwen3 下载状态：**进行中**
- 模型：`Qwen/Qwen3-235B-A22B-GPTQ-Int4`
- 路径：`/root/autodl-tmp/models/Qwen3-235B-A22B-GPTQ-Int4/`
- 已下载：**34GB**，已完成 **6/32** 个 safetensors 分片
- 当前有 4 个 `.incomplete` 文件正在下载
- 预估总大小 ~120-130GB，ETA 约 **3-4 小时**

### 3. 磁盘空间
- `/root/autodl-tmp`：350GB 总量，已用 163GB，剩余 **188GB**
- 两个模型预计还需下载 ~110-140GB，空间充足

### 4. 验证
尚未执行。两个模型均未下载完成，等下载结束后再做完整性验证。

### 注意
任务中指定的目录名（`Llama-4-Scout-17B-16E-Instruct-GPTQ-4b-128g`）与实际下载目录不同。实际使用的是 `RedHatAI` 的 W4A16 量化版本（vLLM 优化），而非 GPTQ-4b-128g 版本。

---
