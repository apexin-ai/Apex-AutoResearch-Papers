# ssh force start v73

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_force_start_v73_20260517T225706_result.json`
- **Structured JSON:** [`fd9ceec63275d10c494e.json`](../../sessions/fd/fd9ceec63275d10c494e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态报告

**训练正在运行：是**

### nvidia-smi
| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| GPU 0 | 15287MiB / 97887MiB | 99% | PID 745668 (v7.3 connector_lora) |
| GPU 1 | 13561MiB / 97887MiB | 95% | PID 745746 (connector_only ablation) |

### 日志（训练步在推进）

**v7.3 connector_lora (GPU 0):**
```
Step 100/20000 | loss=1.2698 task=0.0945 ib=0.5483 div=-0.1406 ctr=11.8419 β=0.0000 | 1.7 steps/s
Step 200/20000 | loss=1.1653 task=0.1212 ib=0.6560 div=-0.1445 ctr=10.5606 β=0.0000 | 1.8 steps/s
```

**connector_only ablation (GPU 1):**
```
Step 100/20000 | loss=0.0757 task=0.0757 | 2.7 steps/s
Step 200/20000 | loss=0.0867 task=0.0867 | 2.9 steps/s
Step 300/20000 | loss=0.0868 task=0.0868 | 2.9 steps/s
```

### PID
- LoRA 主进程: 745668 (GPU 0)
- Connector-only 主进程: 745746 (GPU 1)

两个训练约 2 分钟前启动，步数在正常推进，无需干预。按当前速度估计：LoRA ~3h (1.8 steps/s × 20000)，connector_only ~1.9h (2.9 steps/s × 20000)。

---
