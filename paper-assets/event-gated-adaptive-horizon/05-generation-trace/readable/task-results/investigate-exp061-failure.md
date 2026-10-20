# investigate exp061 failure

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_exp061-failure_20260524T164651_result.json`
- **Structured JSON:** [`cde65dcb13336008f4d9.json`](../../sessions/cd/cde65dcb13336008f4d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 死因: `CUDA_VISIBLE_DEVICES` 重映射导致 `cuda:1` 不可访问

**错误**: 3 个 seed 全部在 RSSM `__init__` (`networks.py:111`) 崩溃，报错：
```
torch.AcceleratorError: CUDA error: invalid device ordinal
```

**根因**: `submit_training_job` 大概率根据 `--device cuda:1` 设置了 `CUDA_VISIBLE_DEVICES=1`。这使物理 GPU 1 在进程内被重映射为 `cuda:0`，但代码仍使用 `--device cuda:1` 创建 tensor，导致 invalid ordinal。

**佐证**:
- nvidia-smi 确认服务器有 2 块 GPU（RTX PRO 6000 Blackwell, 各 96GB），cuda:1 物理存在
- 当前 conda python 直接跑 `torch.cuda.device_count()` 返回 2，无 CUDA_VISIBLE_DEVICES 限制时 cuda:1 可用
- exp_060 用 `--device cuda:0` 正常运行（CUDA_VISIBLE_DEVICES=0 → cuda:0 映射不变）
- exp_061 prefill 阶段（CPU 操作）正常完成，建模阶段首次触及 GPU 就崩溃

**当前 GPU 状态**:
| GPU | 显存使用 | 状态 |
|-----|---------|------|
| cuda:0 | 4688 MiB / 97887 MiB | exp_060 运行中 |
| cuda:1 | 1 MiB / 97887 MiB | 空闲，可用 |

**修复方案**: 重新提交时将 `--device cuda:1` 改为 `--device cuda:0`，让 `submit_training_job` 的 `CUDA_VISIBLE_DEVICES` 完成 GPU 隔离。或者在启动命令中显式 `export CUDA_VISIBLE_DEVICES=0,1` 保留两卡可见，再用 `--device cuda:1`。

可以安全重新提交，cuda:1 空闲。

---
