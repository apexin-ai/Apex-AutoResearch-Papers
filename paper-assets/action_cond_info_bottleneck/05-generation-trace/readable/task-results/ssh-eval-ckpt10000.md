# ssh eval ckpt10000

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-ckpt10000_20260516T054425_result.json`
- **Structured JSON:** [`a5982221f54655930222.json`](../../sessions/a5/a5982221f54655930222.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告：

- **Eval PID**: 806823
- **ACIB loading 确认**: 日志第一行 `[ACIB-EVAL] checkpoint=/root/acib/outputs/acib_v5_div_reg/checkpoint-10000/checkpoint.pt step=10000` — 已确认加载
- **当前进度**: libero_spatial 环境已构建完毕（10个task），正在加载模型权重，即将开始 episode rollout
- **GPU 显存**: GPU 0 = 26734/97887 MiB（27%），GPU 1 = 22154/97887 MiB（23%）— 充裕，无溢出风险
- **共存状态**: 训练（PID 804479等）+ baseline_plus eval（PID 675231）+ ACIB eval（PID 806823）三者共存于 GPU 0，显存安全

注意：发现有 4 个 train_acib.py 子进程（PID 804479/804489/804490/804491），均写同一 output_dir `acib_v5_div_reg`，启动时间相同（13:43）。这些应该是 PyTorch DataLoader workers 而非重复训练进程，但建议后续确认。

---
