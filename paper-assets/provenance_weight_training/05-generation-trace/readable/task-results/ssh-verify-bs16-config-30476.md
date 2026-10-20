# ssh verify bs16 config 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_bs16_config_30476_20260517T193656_result.json`
- **Structured JSON:** [`883fa3fdc76f8113980d.json`](../../sessions/88/883fa3fdc76f8113980d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果：batchsize16_nmin8_r2 配置正确

| 项目 | 值 | 状态 |
|---|---|---|
| **PID** | 48891 | 运行中，GPU 3，100% 利用率 |
| **per_device_train_batch_size** | **16** | 正确 |
| **gradient_accumulation_steps** | **1** | 正确 |
| **GPU 显存** | 71,164 MiB / 97,887 MiB (72.7%) | 正常 |
| **weighting_method** | adaptive | 正确 |
| **n_min** | 8 | 正确 |
| **tau** | 0.8 | 正确 |

### b* 值样本（steps 90-99，全部非零）

| step | b* | alpha_eff | ESS | mean_q |
|---|---|---|---|---|
| 90 | 0.84 | 0.708 | 8.03 | 0.658 |
| 91 | 0.50 | 0.523 | 8.13 | 0.770 |
| 92 | 1.00 | 0.800 | 11.21 | 0.439 |
| 93 | 0.76 | 0.664 | 8.09 | 0.685 |
| 97 | 1.52 | 0.661 | 8.01 | 0.640 |
| 99 | 0.64 | 0.649 | 8.06 | 0.709 |

b* 在 0.47-1.85 范围内波动，ESS 稳定在 ~8（符合 n_min=8 约束），adaptive 机制工作正常。当前在 step ~99/6103，刚启动约 5 分钟。

---
