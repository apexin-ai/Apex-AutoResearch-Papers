# ops exp 001 completion

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp_001_completion_20260517T172543_result.json`
- **Structured JSON:** [`b2f3306d9db912c34640.json`](../../sessions/b2/b2f3306d9db912c34640.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。

---

## exp_001 退出状态
- PID 59365: **已退出**
- 退出原因: **Gen 0-10 全部完成**，在最后写 `phase0_analysis.json` 时因 `numpy.bool_` 不可 JSON 序列化而崩溃（`TypeError: Object of type bool is not JSON serializable`）。核心训练和 metrics 收集均正常完成，`phase0_results.json` 已成功保存。
- cuda:0 VRAM: **已释放**（3MiB idle）

## Gen 0-10 完整 Metrics 表

| Gen | eff_rank | log_det | ppl | distinct4 | hellaswag_norm | train_loss |
|-----|----------|---------|-----|-----------|----------------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7414 | 0.4130 | — |
| 1 | 491.77 | 2464.76 | 11.38 | 0.6256 | 0.3897 | 1.6228 |
| 2 | 496.44 | 2469.93 | 13.58 | 0.5154 | 0.3764 | 1.2682 |
| 3 | 493.31 | 2440.57 | 16.25 | 0.4900 | 0.3658 | 1.1340 |
| 4 | 485.67 | 2405.05 | 19.80 | 0.4679 | 0.3558 | 1.0980 |
| 5 | 479.21 | 2370.17 | 24.59 | 0.4630 | 0.3439 | 1.0474 |
| 6 | 473.00 | 2335.17 | 30.91 | 0.4655 | 0.3311 | 1.0252 |
| 7 | 464.20 | 2304.19 | 38.89 | 0.4474 | 0.3187 | 1.0151 |
| 8 | 456.76 | 2252.12 | 49.29 | 0.4401 | 0.3103 | 0.9868 |
| 9 | 448.45 | 2207.57 | 63.32 | 0.4262 | 0.3009 | 0.9968 |
| 10 | 442.46 | 2178.95 | 76.78 | 0.4259 | **未评估** | 0.9782 |

趋势: eff_rank 从 Gen 2 (496.44) 开始单调下降到 Gen 10 (442.46)，log_det 同步下降。ppl 从 9.55 恶化到 76.78（8x）。distinct4 从 0.74 降至 0.43。hellaswag_norm 从 0.413 降至 0.301。collapse 信号非常清晰。

## Gen 9-10 HellaSwag
- Gen 9: acc_norm = 0.3009
- Gen 10: **未评估**（`hellaswag_gen10` 目录不存在，需要补跑）

## Checkpoint 位置
- Gen 0-10 全部在: `/root/spectral_collapse_ews/checkpoints/gen_{0..10}/`
- Gen 10: `/root/spectral_collapse_ews/checkpoints/gen_10/model.safetensors` (1.5GB, 2026-05-18 01:20)
- Gen 9: `/root/spectral_collapse_ews/checkpoints/gen_9/model.safetensors` (1.5GB, 2026-05-17 22:45)
- 备份: `/root/autodl-tmp/spectral_collapse_ews/checkpoints_410m/` (同步)

## exp_005 Gen 3 检查
- PID 116947: **存活**，已运行 4h09m，在 cuda:1 (25008MiB)
- Phase1 adaptive 已完成 Gen 0-2（共 3 条记录）:
  - Gen 0: ratio=N/A, log_det=2366.68 (baseline)
  - Gen 1: ratio=0.5, log_det=2366.46, ppl=10.09, distinct4=0.661
  - Gen 2: ratio=0.5, log_det=2395.23, ppl=10.42, distinct4=0.615
- Gen 3 正在运行中（results 里还没有 Gen 3 数据）

**注意**: cuda:1 上还有一个 PID 132207 (python3, 9970MiB) 的未知进程。

---
