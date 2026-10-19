# exp phase d lora gpu01 and eval

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phase_d_lora_gpu01_and_eval_20260516T121331_result.json`
- **Structured JSON:** [`da2f90bb46a30d53f548.json`](../../sessions/da/da2f90bb46a30d53f548.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。状态汇总：

| GPU | 任务 | PID | 状态 | 显存 |
|-----|------|-----|------|------|
| 0 | spatial LoRA v2 + nominal eval | 681479 / 680639 | **training (step=0, loss=1.95)** + eval running | 21799 MiB, 98% |
| 1 | universal LoRA v2 | 683770 | **加载模型中** | 8166 MiB |
| 2 | visual LoRA v2 (已有) | 665129 | training | 12705 MiB, 99% |
| 3 | physical LoRA v2 (已有) | 665209 | training | 12819 MiB, 99% |

**3 个新进程 PID：**
- Spatial: 681479
- Universal: 683770
- Eval: 680639

Spatial 已开始训练（step=0, loss=1.9529）。Universal 正在加载模型。Eval 正在运行（已加载 task orders）。4 张卡全部占满。

---
