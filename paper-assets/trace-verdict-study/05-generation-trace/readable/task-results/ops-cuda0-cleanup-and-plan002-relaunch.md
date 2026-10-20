# ops cuda0 cleanup and plan002 relaunch

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0-cleanup-and-plan002-relaunch_20260515T044258_result.json`
- **Structured JSON:** [`f60b3d4adf3bb68daf87.json`](../../sessions/f6/f60b3d4adf3bb68daf87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都稳定运行。汇报如下：

---

## 执行结果

### 1. cuda:0 清理状态

| | 清理前 | 清理后（实际） |
|--|--------|---------------|
| 显存占用 | 49175 MiB（孤儿，无进程） | **无法清除** |
| 原因 | 无可 kill 的进程，GPU reset 不支持（共享服务器硬件限制），MPS/drain 均不可用 | — |

**孤儿显存 49175 MiB 仍在 cuda:0 上**，属于硬件/驱动级残留，无软件手段清除。

### 2. 被 kill 的进程

无可 kill 的进程。nvidia-smi 进程表中 cuda:0 无任何条目，fuser 也未找到关联进程。

### 3. plan_002 启动

第一次尝试因 OOM 失败（EXIT_CODE=137）。

**解决方案**：修改 `train/train_sft.py` 添加 `--gradient_checkpointing` 参数，以时间换空间降低激活显存。

| 项目 | 值 |
|------|-----|
| PID | 955301（GPU 进程） |
| tmux session | `full_trace_label_only_seed42` |
| 显存 | 41174 MiB（进程自身） + 49175 MiB（孤儿） = 90355 MiB |
| 状态 | **训练中，step 1/444 已通过** |
| 速度 | ~18.8s/it |
| 代码修改 | 新增 `--gradient_checkpointing` CLI 参数 + SFTConfig 传参 |
| wandb run name | `full_trace_label_only_seed42_v2` |

### 4. plan_001 进度

| 项目 | 值 |
|------|-----|
| 实验 | vota_no_ae_seed42 |
| PID | 953138 |
| 进度 | **119/444 steps（27%）** |
| 运行时间 | ~27 min |
| ETA | ~1h24m |
| 速度 | ~14.5s/it |
| 显存 | 52779 MiB |

### 5. 最终 nvidia-smi 快照

```
GPU 0: NVIDIA RTX PRO 6000 Black  |  90355MiB / 97887MiB  |  87%  |  470W  |  63°C
  └─ PID 955301 (python) 41174MiB  [plan_002: full_trace_label_only_seed42_v2]

GPU 1: NVIDIA RTX PRO 6000 Black  |  52779MiB / 97887MiB  | 100%  |  496W  |  70°C
  └─ PID 953138 (python) 52770MiB  [plan_001: vota_no_ae_seed42]
```

**注意**：cuda:0 仅剩 ~7 GB 空闲，gradient_checkpointing 使训练可行但速度略慢（~18.8s/it vs plan_001 的 ~13.5s/it）。建议下次服务器重启时确认孤儿显存是否释放。

---
