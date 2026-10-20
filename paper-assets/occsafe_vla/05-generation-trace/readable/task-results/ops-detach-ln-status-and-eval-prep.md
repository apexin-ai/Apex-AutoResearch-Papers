# ops detach ln status and eval prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_detach_ln_status_and_eval_prep_20260524T061129_result.json`
- **Structured JSON:** [`a9787679f7174a1b0d75.json`](../../sessions/a9/a9787679f7174a1b0d75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度

| 实验 | Step | 进度 | 速度 | ETA |
|------|------|------|------|-----|
| detach_ln_s0 | 44727/50005 | 89.4% | ~1.09 it/s | ~1h 21m |
| detach_ln_s1 | 44433/50005 | 88.9% | ~1.08 it/s | ~1h 26m |
| detach_ln_s2 | 44452/50005 | 88.9% | ~1.08 it/s | ~1h 26m |

3 个 GPU 均被占用（各 ~62GB 显存），GPU 0 不空闲。

最新 loss（step 44400-44700）：
- s0: occ=0.0076, action=0.0579
- s1: occ=0.0084, action=0.0679
- s2: occ=0.0160, action=0.0811

## Eval 命令

`/tmp/detach_ln_eval_commands.sh` 已重新写入，3 个 seed 分别对应 GPU 0/1/2。预计约 1.5h 后训练完成可启动 eval。

---
