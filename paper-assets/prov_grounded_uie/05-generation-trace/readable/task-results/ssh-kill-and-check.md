# ssh kill and check

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-and-check_20260512T155552_result.json`
- **Structured JSON:** [`2a7d411728fb1a8216f0.json`](../../sessions/2a/2a7d411728fb1a8216f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. PID 17582/17587 (重复 evaluate.py) — ✅ 已清理
- 确认前：`17582` = bash wrapper, `17587` = `python evaluate.py --model_path ./outputs/sft/merged ...`
- kill 17582 后 17587 也随之退出（bash 子进程），两个都已清理

### 2. PID 10513 (HF snapshot_download) — ✅ 已清理
- 确认前：`python -c "from huggingface_hub import snapshot_download; snapshot_download('cross-encoder/nli-deberta-v3-large', ...)"`
- kill 后已退出

### 3. sft-eval (PID 17835→17840, cuda:0)
- **运行时间**: 01:00:54
- **状态**: 模型已加载完成 (4/4 shards)，正在推理中
- **日志尾部**:
  ```
  Loading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 172.67it/s]
  The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']
  ```
  （无评估进度条输出，可能是 tqdm 未 flush 到日志）
- **结果文件**: ❌ `eval_results.json` 尚未生成
- **GPU**: cuda:0, 17092MiB / 97887MiB, GPU-Util 69%, 261W

### 4. posthoc-nli (PID 17369, cuda:1)
- **运行时间**: 01:02:05
- **状态**: 模型已加载完成，正在推理中
- **日志尾部**:
  ```
  Generating predictions from ./outputs/sft/merged
  Loading checkpoint shards: 100%|██████████| 4/4 [00:00<00:00, 168.73it/s]
  The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']
  ```
- **结果文件**: ❌ `outputs/posthoc_nli/` 目录为空
- **GPU**: cuda:1, 17092MiB / 97887MiB, GPU-Util 71%, 273W

### 5. nvidia-smi
```
+-------------------------------------------+------------------------+----------------------+
| GPU  Name                      Persist-M  | Bus-Id          Disp.A | Volatile Uncorr. ECC |
|   0  NVIDIA RTX PRO 6000 Black    On      | A8:00.0          Off   |       Off            |
|      49C  P0   261W / 600W                | 17101MiB / 97887MiB    |  69%   Default       |
|   1  NVIDIA RTX PRO 6000 Black    On      | C8:00.0          Off   |       Off            |
|      54C  P0   273W / 600W                | 17101MiB / 97887MiB    |  71%   Default       |
+-------------------------------------------+------------------------+----------------------+
| Processes:                                                                                |
|  GPU 0: PID 17840 (python evaluate.py)              17092MiB                              |
|  GPU 1: PID 17369 (python rerank_nli.py)            17092MiB                              |
+-------------------------------------------------------------------------------------------+
```

### 6. 所有 Python 进程
| PID | CPU% | 说明 |
|-----|------|------|
| 913 | 0.0% | jupyter-lab (系统服务) |
| 917 | 0.0% | tensorboard (系统服务) |
| 1011 | 0.0% | tensorboard_data_server |
| 17364 | 0.0% | bash wrapper for rerank_nli |
| **17369** | **100%** | `python rerank_nli.py` (cuda:1) — 活跃推理中 |
| 17835 | 0.0% | bash wrapper for evaluate.py |
| **17840** | **100%** | `python evaluate.py` (cuda:0) — 活跃推理中 |

**总结**: 重复进程和 HF 下载已全部清理。两个评估任务 (sft-eval + posthoc-nli) 正常运行，双 GPU 各 ~70% 利用率、17GB 显存占用，两者都已运行约 1 小时但尚未产出结果文件。日志中无进度条输出（可能是 tqdm 缓冲），但 100% CPU + 高 GPU 利用率说明推理在正常进行。

---
