# ssh gpu status check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_status_check_20260515T125554_result.json`
- **Structured JSON:** [`072f340af1378f0b498f.json`](../../sessions/07/072f340af1378f0b498f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU STATUS ===
cuda:0: 71567/97887 MiB (73%), GPU util 100% — PID 93494 (deepseek_vota_seed42 训练)
cuda:1: 16201/97887 MiB (17%), GPU util 100% — PID 104643 (calibration.py batch eval)

=== vota_seed123_v2 (PID 103781) ===
进程状态: GONE — 已崩溃
原因: CUDA OOM — 尝试在 cuda:0 分配 4.64 GiB，但 deepseek_vota_seed42 已占用该卡
崩溃时机: 0/444 steps (0%)，训练根本没开始
Eval 结果: 无
Checkpoint: 无（仅有空的 tensorboard runs 目录）
⚠️ 根因: vota_seed123_v2 被调度到了已被占用的 cuda:0，应该用 cuda:1

=== deepseek_vota_seed42 (PID 93484) ===
当前进度: step 437 / 444
完成度: 98%
已运行: ~2h09m
速度: ~17.5s/step
预计剩余: ~2 分钟完成训练
训练后自动执行: eval/evaluate.py

=== 意外发现: cuda:1 calibration.py ===
PID 104643 在 cuda:1 运行 calibration.py --batch
条件: no_trace, full_trace, label_only, loop_only, ae_only, exception_only, vota
输出目录: /root/autodl-tmp/trace-verdict-study-checkpoints/calibration/
```

**需要关注的问题：**
1. vota_seed123_v2 因 GPU 分配错误 OOM 崩溃，需要重新提交到 cuda:1（等 calibration.py 完成后）
2. deepseek_vota_seed42 即将完成（~2分钟），之后会自动跑 eval

---
