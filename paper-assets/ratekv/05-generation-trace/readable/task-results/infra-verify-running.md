# infra verify running

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-running_20260513T212832_result.json`
- **Structured JSON:** [`4eb57360c151337d708d.json`](../../sessions/4e/4eb57360c151337d708d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. nvidia-smi

```
Thu May 14 05:28:57 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |
| N/A   28C    P8             35W /  600W |       0MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |
| N/A   30C    P8             34W /  600W |       0MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+
| No running processes found                                                              |
+-----------------------------------------------------------------------------------------+
```

**GPU 完全空闲**，0MiB 占用，0% 利用率，无 GPU 进程。

### 2. 进程存活

PID 134996 和 135075 **均已不存在**。

### 3. tmux

tmux 命令被 read_only 白名单拦截，无法检查。

### 4. mvp_003 日志（`~/runs/ratekv/mvp_003.log`，1007字节，最后写入 04:56）

```
RuntimeError: No calibration sequences loaded. Provide --calibration_data pointing
to a JSON file with [{'text': ...}] entries, each having >= 512 tokens.
```

**崩溃原因：缺少 `--calibration_data` 参数。** 模型加载成功（Qwen2.5-7B），进入 distortion profiling 阶段时因无校准数据而报错。

### 5. sanity_003 日志（`~/runs/ratekv/sanity_003.log`，2889字节，最后写入 04:56）

```
huggingface_hub.errors.HFValidationError: Repo id must be in the form
'repo_name' or 'namespace/repo_name':
'/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B/'. Use `repo_type` argument if needed.
```

**崩溃原因：模型路径格式错误。** `Qwen2___5-1___5B` 中的 `___` 不是合法路径——ModelScope 下载时把 `.` 和 `-` 转义成了 `___`，导致 `AutoTokenizer.from_pretrained()` 把本地路径误当 HF repo ID 去验证。

### 6. 本地 tee 日志

`/root/ratekv/mvp_run.log` 和 `/root/ratekv/mvp_sanity.log` 内容与上述日志一致，确认是同一次运行。

---

## 结论：两个实验都已崩溃

| 实验 | 状态 | 崩溃点 | 根因 |
|------|------|--------|------|
| **mvp_003** | 已崩 | `profiler.profile()` | 启动命令缺少 `--calibration_data` 参数 |
| **sanity_003** | 已崩 | `AutoTokenizer.from_pretrained()` | 模型缓存路径 `Qwen2___5-1___5B` 含非法字符，ModelScope 下载后目录名与 HF 预期不匹配 |

---
