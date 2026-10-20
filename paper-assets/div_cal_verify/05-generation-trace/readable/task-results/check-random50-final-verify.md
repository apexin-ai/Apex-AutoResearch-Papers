# check random50 final verify

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_random50_final_verify_20260513T170919_result.json`
- **Structured JSON:** [`778cb6ec96d510cd9fb8.json`](../../sessions/77/778cb6ec96d510cd9fb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

---

**nvidia-smi:**
```
Thu May 14 01:09:57 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:38:00.0 Off |                  Off |
| N/A   59C    P0            467W /  600W |   73618MiB /  97887MiB |    100%      Default |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |
| N/A   29C    P8             36W /  600W |       0MiB /  97887MiB |      0%      Default |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|=========================================================================================|
|    0   N/A  N/A          250452      C   python3                               12216MiB |
|    0   N/A  N/A          250453      C   python3                               12216MiB |
+-----------------------------------------------------------------------------------------+
```

---

**tmux capture-pane (seed123 & seed456):**
```
[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode.
```

---

**tail -20 random50_seed123.log:**
```
设置成功
注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证
`torch_dtype` is deprecated! Use `dtype` instead!
```

**tail -20 random50_seed456.log:**
```
设置成功
注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证
`torch_dtype` is deprecated! Use `dtype` instead!
```

---

**head -5 run_random50_seed123.sh:**
```
#!/bin/bash
set -e
source /root/div_cal_verify/env.sh

GPU_ID=${1:-0}
```

**head -5 run_random50_seed456.sh:**
```
#!/bin/bash
set -e
source /root/div_cal_verify/env.sh

GPU_ID=${1:-0}
```

---

`tmux` 被 `ssh_read_only` 白名单拦截，需要用 `ssh_execute` 才能执行。两个 log 文件只有 3 行输出（network_turbo 提示 + torch_dtype 警告），内容很少。

---
