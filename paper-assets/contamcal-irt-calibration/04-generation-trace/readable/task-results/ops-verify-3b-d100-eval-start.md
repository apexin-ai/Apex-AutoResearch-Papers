# ops verify 3B d100 eval start

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-3B-d100-eval-start_20260514T121028_result.json`
- **Structured JSON:** [`91110c591aa9b6d319fb.json`](../../sessions/91/91110c591aa9b6d319fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Auto-relay 成功触发，eval 正常运行。

**汇总**：

| 项目 | 状态 |
|------|------|
| Relay 脚本 | `run_eval_3B_d100_auto.sh` (PID 361360) 19:55 启动，成功等待 SFT 完成 |
| Eval 进程 | PID **362942**，20:06 启动，GPU 3，94% 利用率 |
| Checkpoint | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter/` ✓ 存在，adapter_model.safetensors 114MB |
| 输出目录 | `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned/` ✓ 已创建（尚空，eval 进行中） |
| 日志 | `/root/runs/contamcal-irt-calibration/eval_3B_d100_aligned.log` ✓ |
| 当前进度 | MMLU 评估中，~66% (9316/14042)，~37 it/s |
| bitsandbytes 警告 | `libnvJitLink.so.13` 加载失败，非致命，不影响 eval |

预计 MMLU 剩余约 2 分钟完成，之后还有 gsm8k、arc_challenge、humaneval 三个 benchmark。

---
