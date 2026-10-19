# train acib v3 launch fixed

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_acib_v3_launch_fixed_20260515T232340_result.json`
- **Structured JSON:** [`a0fb6cec8ec3f77cd4d2.json`](../../sessions/a0/a0fb6cec8ec3f77cd4d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

### 产出

**1. GPU bug 修复**
- 删除 `train_acib.py` 第 219 行 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)`
- `device` 改为 `torch.device(f"cuda:{args.gpu}" if ...)`
- 验证：`CUDA_VISIBLE_DEVICES=1` → `cuda:0` = 物理 GPU 1 (NVIDIA RTX PRO 6000)

**2. 训练启动确认**
- PID 497308, tmux session `acib_v3_train`
- 命令：`python3 -u scripts/train_acib.py --model_id lerobot/smolvla_libero --hidden_dim 64 --alpha 0.01 --beta 0.01 --batch_size 64 --steps 20000 --gpu 0 --output_dir /root/acib/outputs/acib_v3_train --seed 42`
- wandb 禁用（服务器未配置 API key）

**3. 前 100 步 loss**
```
Step 100/20000 | loss=0.0501 task=0.0449 ib=0.0599 β=0.0000 | 1.0 steps/s
```
- loss 正常，无 NaN/爆炸
- β=0 (warmup 阶段，前 1000 步 β 保持 0)
- 预计 20000 步耗时 ~5.5h

**4. GPU 共存状态**
| GPU | 进程 | VRAM | 状态 |
|-----|------|------|------|
| GPU 0 | baseline_plus eval (PID 471056) | 5.4GB / 97.9GB | idle |
| GPU 1 | baseline_std eval (PID 308788) | 2.1GB | 运行中 |
| GPU 1 | ACIB v3 训练 (PID 497308) | 16.2GB | 训练中 25% util |
| **GPU 1 总计** | | **18.4GB / 97.9GB** | **安全** |

无停止条件触发。

---
