# eval act supplement 3gpu

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_act-supplement-3gpu_20260521T114353_result.json`
- **Structured JSON:** [`b74f99d896079eb48944.json`](../../sessions/b7/b74f99d896079eb48944.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已提交 3 个 ACT eval（westd-28034）：**

| Eval | Checkpoint | GPU | PID | Registry |
|------|-----------|-----|-----|----------|
| exp-004-eval-ckpt500 | checkpoint-500 | cuda:3 | 915193 | RUNNING |
| exp-004-eval-ckpt2000 | checkpoint-2000 | cuda:1 | 915690 | RUNNING |
| exp-004-eval-ckpt8000 | checkpoint-8000 | cuda:2 | 916215 | RUNNING |

**调整说明**：GPU 0 被 exp003-s2-ckpt4000 eval 占用（14944 MiB），ckpt-500 改到 GPU 3（原计划给 seed2 ckpt-4000，但该任务已在 GPU 0 运行）。

Cron 监控已设置（每 8 分钟检查），完成后自动更新 registry。

---
