# eval multiseed batch 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_multiseed-batch-35807_20260528T090743_result.json`
- **Structured JSON:** [`ffdc3e94076309ee2acc.json`](../../sessions/ff/ffdc3e94076309ee2acc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 eval 全部提交成功：

| exp_id | GPU | PID | 模型 | eval_seed |
|--------|-----|-----|------|-----------|
| `eval_multiseed_lora_s0_eseed0` | cuda:0 | 85158 | LoRA s0 | 0 |
| `eval_multiseed_lora_s0_eseed99` | cuda:1 | 85239 | LoRA s0 | 99 |
| `eval_multiseed_sdf_l01_s0_eseed0` | cuda:2 | 85318 | SDF λ=0.01 s0 | 0 |
| `eval_multiseed_sdf_l01_s0_eseed99` | cuda:3 | 85399 | SDF λ=0.01 s0 | 99 |

日志路径：`~/runs/diff_collision_sdf/&lt;exp_id>.log`，timeout 5h。预计 ~3.4h 完成（参考之前 eseed42 的 wall_clock）。

---
