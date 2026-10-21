# ssh progress check 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_progress_check_30476_20260517T205103_result.json`
- **Structured JSON:** [`e55112a9da798bec3a91.json`](../../sessions/e5/e55112a9da798bec3a91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

## 训练进度汇总 (截至 2026-05-17 20:55 UTC)

| 实验 | Step/Total | Loss (weighted) | Speed | eval_data_path | 预估完成 (UTC) |
|------|-----------|----------------|-------|----------------|---------------|
| grid_b0_1_seed42 | 1999/6103 (33%) | ~1.84 | 6.4 s/step | ✓ | May 18 ~04:15 |
| grid_b0_3_seed123 | 1499/6103 (25%) | ~2.37 | 6.3 s/step | ✓ | May 18 ~04:55 |
| rho02_adaptive_tau08_seed42 | 4009/6103 (66%) | ~2.84 | 2.4 s/step | ✗ | May 17 ~22:18 |
| batchsize16_nmin8_r2 | 1979/6103 (32%) | ~2.73 | 2.5 s/step | ✗ | May 17 ~23:45 |

## GPU 状态

| GPU | 实验 | 显存 | 利用率 | 温度 |
|-----|------|------|--------|------|
| 0 | grid_b0_1_seed42 | 75G/98G | 84% | 59°C |
| 1 | grid_b0_3_seed123 | 75G/98G | 99% | 66°C |
| 2 | rho02_adaptive_tau08 | 47G/98G | 99% | 59°C |
| 3 | batchsize16_nmin8_r2 | 71G/98G | 100% | 64°C |

## 注意事项

1. **命名不匹配**：PID 42432 的实际 output_dir 是 `grid_b0_3_seed123`（不是 `_r2`），PID 48891 的实际 output_dir 是 `/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_r2`（不是 `_r3`，且路径不在 `/root/autodl-tmp/output/models/` 下）。
2. **无 eval**：rho02_adaptive_tau08_seed42 和 batchsize16_nmin8_r2 的命令行均无 `--eval_data_path`，不会执行 eval 步骤。
3. **速度差异**：实验 3、4 每步 ~2.4-2.5s（batch_size 较大或 grad_accum 较少），实验 1、2 每步 ~6.3s（batch_size=4, grad_accum=4）。
4. **实验 3 最快完成**：约 1.4 小时后结束。

---
