# ssh verify dcol early logs

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_dcol_early_logs_20260514T203553_result.json`
- **Structured JSON:** [`cec0c7c4c25eabda6b04.json`](../../sessions/ce/cec0c7c4c25eabda6b04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DCOL 训练状态

**进程**: PID 193684 存活，运行 16 分 39 秒。

**GPU**:
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 100% | 58,733 / 97,887 MiB |
| 1 | 70% | 15,671 / 97,887 MiB |

**训练进度**: Epoch 1, step 1280/2187（~59%），无报错。

**Loss 趋势**（正常下降）:
| Step | loss | ce | cl | acc |
|------|------|------|------|------|
| 300 | 1.6283 | 1.3842 | 0.4881 | 0.2743 |
| 500 | 1.6310 | 1.3844 | 0.4932 | 0.2725 |
| 800 | 1.6224 | 1.3792 | 0.4864 | 0.2796 |
| 1000 | 1.6150 | 1.3762 | 0.4776 | 0.2822 |
| 1280 | 1.6029 | 1.3720 | 0.4618 | 0.2849 |

- 总 loss 从 1.63 降到 1.60，ce 和 cl 都在稳步下降
- acc 从 0.274 升到 0.285
- lr 在 warmup 阶段（2.7e-6 → 1.2e-5）
- 速度约 12s/20steps

**Checkpoints**: 已有 `best_model.pt`（830MB）和 `results.json`。

结论：训练正常运行，loss 稳步下降，无异常。

---
