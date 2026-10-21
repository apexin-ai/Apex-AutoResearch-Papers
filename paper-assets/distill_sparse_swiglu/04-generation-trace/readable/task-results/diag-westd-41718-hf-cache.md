# diag westd 41718 hf cache

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-41718-hf-cache_20260518T072946_result.json`
- **Structured JSON:** [`e5a2c631d038e81407bc.json`](../../sessions/e5/e5a2c631d038e81407bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是 westd-41718 完整诊断输出：

---

### 1. ENV（环境变量）
```
=== ENV ===
（无 HF/TRANSFORM/XDG 相关环境变量）
```

### 2. CACHE LOCATIONS
```
=== CACHE LOCATIONS ===
/root/autodl-tmp/.hf_cache/datasets/wikitext
/root/.cache/huggingface/datasets/wikitext
/root/.cache/huggingface/datasets
```
（未找到 ai2_arc）

### 3. DEFAULT HF HOME
```
=== DEFAULT HF HOME ===
total 8
drwxr-xr-x 4 root root   45 May 18 08:31 .
drwx------ 5 root root   97 May 18 08:27 ..
drwxr-xr-x 3 root root 4096 May 18 08:32 datasets
drwxr-xr-x 8 root root 4096 May 18 02:44 hub
_root_.cache_huggingface_datasets_wikitext_wikitext-103-raw-v1_0.0.0_b08601e04326c79dfdd32d625aee71d232d685c3.lock
_root_.cache_huggingface_datasets_wikitext_wikitext-2-raw-v1_0.0.0_b08601e04326c79dfdd32d625aee71d232d685c3.lock
wikitext
```

### 4. PYTHON
```
which python → 失败（不在 PATH 中）

/root/miniconda3/bin/python:
CUDA: 2
HF_HOME: NOT SET
HF_DATASETS_CACHE: NOT SET
```

### 5. .bashrc 中 HF/CONDA 相关
```
export PATH=/root/miniconda3/bin:$PATH
export HF_HUB_OFFLINE=1
export HF_DATASETS_OFFLINE=1
```

### 6. GPU / 进程 / tmux
```
NVIDIA-SMI 580.95.05    CUDA Version: 13.0

GPU 0: NVIDIA RTX PRO 6000 Black   0MiB/97887MiB   0%   29C
GPU 1: NVIDIA RTX PRO 6000 Black   0MiB/97887MiB   0%   30C

No running processes found
No benchmark_eval/train.py processes
tmux: no server running
```

---
