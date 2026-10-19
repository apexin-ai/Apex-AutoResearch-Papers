# diag westd 34887 hf cache

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-34887-hf-cache_20260518T071049_result.json`
- **Structured JSON:** [`b7d57e45a73de832c394.json`](../../sessions/b7/b7d57e45a73de832c394.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整诊断结果如下：

---

### 1. ENV（环境变量）
```
=== ENV ===
（无 HF/TRANSFORM/XDG 相关环境变量）
```

### 2. CACHE LOCATIONS（find 结果）
```
=== CACHE LOCATIONS ===
ai2_arc: （未找到）
wikitext: /root/autodl-tmp/.hf_cache/datasets/wikitext
datasets (huggingface 路径): （未找到）
```

### 3. DEFAULT HF HOME（/root/.cache/huggingface/）
```
total 0
drwxr-xr-x 3 root root  59 May 18 11:53 .
drwx------ 8 root root 158 May 18 12:00 ..
-rw-r--r-- 1 root root   0 May 15 13:03 .check_for_update_done
drwxr-xr-x 4 root root  95 May 15 20:02 hub

--- datasets ---
（空，/root/.cache/huggingface/datasets/ 不存在或为空）
```

### 4. PYTHON
```
which python → （bare shell 下不在 PATH）
conda envs → 只有 base (/root/miniconda3)
conda activate base → /root/miniconda3/bin/python
CUDA: 2
HF_HOME: NOT SET
HF_DATASETS_CACHE: NOT SET
```

### 5. /etc/profile
```
PATH=/root/miniconda3/bin:/usr/local/bin:$PATH
```
（无 HF/CACHE 相关设置）

### 6. .bashrc
```
（标准 Ubuntu .bashrc，无 HF/CACHE/conda 相关 export。
 末尾 source /etc/profile 和 source /etc/autodl-motd）
```

### 7. 实际缓存位置：/root/autodl-tmp/.hf_cache/
```
顶层：
  Xnhyacinth___long_bench/
  datasets/
  hub/
  xet/
  + 若干 .lock 文件

datasets/ 子目录内容（前30）：
  Xnhyacinth___long_bench/
  大量 .lock 文件（allenai___ai2_arc, allenai___winogrande, cais___mmlu 各子集）

datasets/wikitext/ 内容：
  wikitext-103-raw-v1
  wikitext-2-raw-v1
```

### 8. nvidia-smi
```
Mon May 18 15:11:15 2026
Driver: 580.95.05    CUDA Version: 13.0

GPU 0: NVIDIA RTX PRO 6000 Blackwell   30C  P8  33W/600W   0MiB/97887MiB  0%
GPU 1: NVIDIA RTX PRO 6000 Blackwell   29C  P8  35W/600W   0MiB/97887MiB  0%

No running processes found
```

### 9. 进程 & tmux
```
ps aux | grep benchmark_eval/train.py → （无匹配）
tmux ls → no server running on /tmp/tmux-0/default
```

---

两张 GPU 空闲，无训练进程，无 tmux session。HF_HOME 和 HF_DATASETS_CACHE 均未设置，实际数据集缓存在 `/root/autodl-tmp/.hf_cache/datasets/`（非默认路径），而 `/root/.cache/huggingface/` 下只有 `hub/` 没有 `datasets/`。`python` 在 bare shell 不可用（需 conda activate base 或完整路径 `/root/miniconda3/bin/python`）。

---
