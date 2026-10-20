# ops gpu audit 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_audit_10894_20260524T185225_result.json`
- **Structured JSON:** [`40a1f562b40e1b424182.json`](../../sessions/40/40a1f562b40e1b424182.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验正常运行，健康度报告误报。

| 实验 | GPU | PID | 状态 | GPU 利用率 | 显存占用 | 运行时间 |
|------|-----|-----|------|-----------|---------|---------|
| ablation_occ_detach_s0_retrain | cuda:0 | 775953 | **R** (running) | 99% | 62194/97887 MiB | 50m50s |
| full_occ_ln_s0 | cuda:1 | 742741→742821* | **S** (sleeping) | 94% | 62194/97887 MiB | 9h52m28s |
| full_occ_ln_s1 | cuda:2 | 777222 | **R** (running) | 99% | 62200/97887 MiB | 47m48s |
| full_occ_ln_s2 | cuda:3 | 777428 | **R** (running) | 99% | 62203/97887 MiB | 47m45s |

**说明：**
- full_occ_ln_s0 的 GPU 进程 PID 是 742821（由 torchrun 产生的子进程），父 bash PID 742741 仍存活，符合预期。
- 4 卡利用率 94%-99%，显存各占约 62GB/98GB，全部正常训练中。
- tmux ls 因 read-only 限制无法执行，但进程检查已确认全部存活，无需进一步查看。

---
