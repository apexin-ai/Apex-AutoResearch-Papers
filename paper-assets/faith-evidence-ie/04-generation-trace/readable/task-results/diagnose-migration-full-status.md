# diagnose migration full status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_migration-full-status_20260520T090557_result.json`
- **Structured JSON:** [`cc4263a251d6a134b1db.json`](../../sessions/cc/cc4263a251d6a134b1db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 迁移状态 + GPU 状态汇总

### 磁盘
| 指标 | 值 |
|------|-----|
| 总容量 | 350G |
| 已用 | 30G (9%) |
| 可用 | 321G |

**未达 200G**，迁移仍在进行中。

### 传输进程
| 进程 | 状态 |
|------|------|
| **rsync** | 运行中 (PID 5150/5151/5152)，从旧服务器全量同步 |
| **scp** | 运行中 (PID 8065)，正在传输 `meta-llama` 基座模型 |
| 监控脚本 | rsync_monitor / progress_reporter / milestone_checker 均在运行 |

### SCP 优先传输进度
SCP 刚启动（17:01:22），正在传第 1 项（meta-llama base model），尚未完成。

### rsync 日志
rsync 正在传输 `Qwen3-14B/model-00001-of-00008.safetensors`，当前约 31%，速度 ~7MB/s。

### 里程碑
| 里程碑 | 状态 |
|--------|------|
| Milestone A | **未达成** |
| Milestone B | **未达成** |

### nvidia-smi
```
4× NVIDIA RTX PRO 6000 Blackwell (各 97887 MiB)

GPU 0: 31°C, P8, 35W,  0MiB used, 0% util
GPU 1: 31°C, P8, 34W,  0MiB used, 0% util
GPU 2: 39°C, P0, 102W, 0MiB used, 100% util  ⚠️
GPU 3: 40°C, P0, 104W, 0MiB used, 100% util  ⚠️

No running processes found
```

**cuda:2 和 cuda:3 有 ghost utilization**——GPU-Util 100% 但显存 0MiB 且无进程。可能是之前进程异常退出后 GPU 未正确释放。空闲后可能自行恢复，否则需要 `nvidia-smi --gpu-reset`。

### 关键文件完整性
| 资产 | 状态 |
|------|------|
| LLaMA base (safetensors) | **2/4 shards** (2.1G)，SCP 正在传输中 |
| LLaMA SFT adapter | **MISSING**（SCP 排队中，在 meta-llama 之后） |
| DocRED data | ✅ OK |
| freige code | ✅ OK |
| 14B SFT adapter | **MISSING**（SCP 排队第 6 项） |
| 14B generations | **MISSING**（SCP 排队第 5 项） |
| Qwen3-14B base | **3/8 shards**（rsync 正在传第 1 shard 31%） |
| adapter 目录总数 | 29 个（已通过 rsync 迁移） |

### 结论
- 迁移整体 30G/预估 200G+，**约 15% 完成**
- SCP 优先通道刚开始传 meta-llama，预计 meta-llama 完成后才会传 SFT adapter 和 data（data 已到位说明 rsync 先同步了小文件）
- cuda:2/3 ghost utilization 需关注，当前 4 卡显存全部空闲，不影响后续使用（但 util 异常可能需 reset）

---
