# restart crashed experiments

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_restart_crashed_experiments_20260523T032137_result.json`
- **Structured JSON:** [`a805381d125ad87a994b.json`](../../sessions/a8/a805381d125ad87a994b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇报如下：

---

## 汇报

### 各实验可恢复 checkpoint

| 实验 | checkpoint-500 | checkpoint-1000 | 恢复策略 |
|------|---------------|-----------------|----------|
| **rho03_adaptive_seed456** | ❌ 不存在 | 已删除（损坏） | **需从头开始** |
| **bs8_nmin4_adaptive_seed123** | ✅ 完整（model.safetensors 验证OK，1.11GB） | 已删除（损坏） | **可从 checkpoint-500 恢复** |
| **bs8_nmin4_uniform_seed123** | ✅ 完整（model.safetensors 验证OK，1.11GB） | 已删除（损坏） | **可从 checkpoint-500 恢复** |

### 磁盘空间
- `/root/autodl-tmp`: 250G 总量，已用 152G，**可用 99G (61%)**

### rho03_uniform_seed456 (PID 833056) 进度
- **正在运行**，当前 step **1082/6103**，进度 **~18%**
- 预估剩余约 3h27m（2.47s/it）
- 从 checkpoint-1000 恢复成功，训练正常
- 运行在 GPU 2 (`CUDA_VISIBLE_DEVICES=2`)

### 额外发现
- `rho03_adaptive_seed456` 的 tmux session 存在但**无活跃 python 进程**——可能因 checkpoint-1000 损坏导致恢复失败已退出
- `bs8_nmin4_adaptive_seed123` 和 `bs8_nmin4_uniform_seed123` 同样**无活跃训练进程**

---
