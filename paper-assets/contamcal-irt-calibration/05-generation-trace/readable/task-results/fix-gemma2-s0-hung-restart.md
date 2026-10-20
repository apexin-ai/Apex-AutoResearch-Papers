# fix gemma2 s0 hung restart

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gemma2-s0-hung-restart_20260520T094325_result.json`
- **Structured JSON:** [`27105c2dc8917e3b7204.json`](../../sessions/27/27105c2dc8917e3b7204.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动。

**汇报：**

| 项目 | 详情 |
|------|------|
| **挂死原因** | 进程实际未挂死。日志显示训练正常推进到 step 80/3125（~2.8s/step），被 kill 终止（EXIT_CODE=143）。用户观察到的 3MiB/0% 可能是模型加载前的瞬态状态或监控时间差 |
| **配置对比** | s0 与 s123 训练参数完全一致（batch_size=2, grad_accum=8, lr=5e-5, lora_r=16, alpha=32），无配置问题 |
| **修复措施** | 清理了中断产生的空 checkpoint 目录（gemma-2-9b_d000_s0），原样重启 |
| **新 PID** | 314035 |
| **GPU 状态** | cuda:1: 91294MiB / 99% util，正常训练中 |

注意：91GB/98GB 显存占用较高（s123 同配置仅 66GB），有轻微 OOM 风险。如果后续再次出问题，建议加 `--gradient-checkpointing` 降低显存占用。

---
