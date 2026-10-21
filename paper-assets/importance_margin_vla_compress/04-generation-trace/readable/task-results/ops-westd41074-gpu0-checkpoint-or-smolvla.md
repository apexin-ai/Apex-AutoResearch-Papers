# ops westd41074 gpu0 checkpoint or smolvla

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-gpu0-checkpoint-or-smolvla_20260520T234313_result.json`
- **Structured JSON:** [`37ea7327877dc2eb17bf.json`](../../sessions/37/37ea7327877dc2eb17bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**Checkpoint 下载状态**: 进行中（PID 673289，仅 1/16 文件 = 6%）

**GPU 状态 (westd-41074)**:
| GPU | PID | 任务 | 显存 |
|-----|-----|------|------|
| 0 | 659206 | OpenVLA random_prune k=0.5 libero_object | 15961 MiB |
| 1 | 682009 | **新启动** OpenVLA SC M=128 spatial | 36240 MiB |
| 2 | 68539 | Training OpenVLA SC M=96 | 28546 MiB |
| 3 | 68852 | Training OpenVLA SC M=64 | 27526 MiB |

**决策变更说明**: 两个预设选项均不可行：
- 3a (OpenVLA baseline spatial): checkpoint 下载仅 6%
- 3b (SmolVLA pruning k=0.5 spatial): **已完成**，SR = 0%（500 episodes）

**替代实验**: 启动 **OpenVLA SmartCompress M=128 on LIBERO-Spatial**（`eval_openvla_sc_m128_spatial_seed42`）
- PID: 682009
- tmux session: `sc_m128_spatial`
- 初始日志确认：模型加载成功（M=128, 403M compressor params），Task 0 已开始执行
- 科学价值：Object suite M=128 SR=59.8%，Spatial 结果将验证学习压缩的跨 suite 泛化能力（C3）

---
