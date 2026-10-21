# monitor westb gpu confirm

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westb_gpu_confirm_20260516T133849_result.json`
- **Structured JSON:** [`e472dd57aa4c26ad3d3f.json`](../../sessions/e4/e472dd57aa4c26ad3d3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### nvidia-smi

| GPU | Util | VRAM | 总显存 | 型号 |
|-----|------|------|--------|------|
| cuda:0 | **99%** | 28,931 MiB | 97,887 MiB | RTX PRO 6000 Blackwell |
| cuda:1 | **0%** | 0 MiB | 97,887 MiB | RTX PRO 6000 Blackwell |

### 进程状态

**cuda:0 — eval_sft_rasp_25 (PID 602990)**: 正常运行
- 运行时间：5h16m09s
- 命令：`python src/eval_gsm8k.py --model_path .../sft_rasp_25 --max_samples 1319 --seed 42`

**cuda:1 — sft_rasp_rlvr_20 (PID 619848)**: 已崩溃，进程不存在

### 异常：cuda:1 空闲

`sft_rasp_rlvr_20` 启动即失败，原因是**参数名错误**。日志显示：

```
sft_recovery.py: error: unrecognized arguments: --lr 2e-5 --epochs 2 --grad_accum 8
EXIT_CODE=2
```

脚本期望的参数名是：
| 传入的（错误） | 正确的 |
|----------------|--------|
| `--lr` | `--learning_rate` |
| `--epochs` | `--num_train_epochs` |
| `--grad_accum` | `--gradient_accumulation_steps` |

需要用正确的参数名重新启动 sft_rasp_rlvr_20。

---
