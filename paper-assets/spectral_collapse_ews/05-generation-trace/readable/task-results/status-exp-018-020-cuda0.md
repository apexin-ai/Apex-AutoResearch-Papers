# status exp 018 020 cuda0

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_exp_018_020_cuda0_20260523T092445_result.json`
- **Structured JSON:** [`4b5f76f5c3ce9cb9b1e2.json`](../../sessions/4b/4b5f76f5c3ce9cb9b1e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

tmux scrollback 为空，无法查看实时进度。但根据时间线推算，Gen 10 应在 ~5 分钟内完成。

## 当前状态汇总

**exp_018 (r=0.5, seed43, cuda:0)**:
- PID 716261，GPU-Util 96%，仍在训练 Gen 10（最终代）
- Gen 0-9 指标已完成写入 results JSON
- 预计 ~17:30 完成（每代 ~1.5h，gen_9 @ 15:59）
- Checkpoint: `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_seed43/`

**exp_019 (r=0.2, seed44, cuda:1)**: PID 757601，正常运行

**exp_020**: cuda:0 被 exp_018 占用，需等完成后启动

**Gen 0-9 metrics 概览**（exp_018, r=0.5, seed43）:

| Gen | eff_rank | log_det | PPL | D-4 | sigma1 |
|-----|----------|---------|------|------|--------|
| 0 | 417.5 | 2366.7 | 9.55 | 0.741 | 1942.8 |
| 1 | 475.9 | 2361.7 | 10.08 | 0.671 | 956.5 |
| 2 | 488.0 | 2393.6 | 10.41 | 0.571 | 873.1 |
| 3 | 493.9 | 2419.3 | 10.73 | 0.544 | 849.7 |
| 4 | 503.1 | 2454.9 | 11.12 | 0.463 | 817.0 |
| 5 | 510.1 | 2479.8 | 11.60 | 0.419 | 785.6 |
| 6 | 519.2 | 2507.7 | 12.12 | 0.411 | 752.5 |
| 7 | 526.8 | 2528.1 | 12.69 | 0.361 | 728.2 |
| 8 | 537.0 | 2548.0 | 13.46 | 0.299 | 676.8 |
| 9 | 545.4 | 2560.1 | 14.21 | 0.231 | 647.4 |

趋势符合预期：eff_rank ↑、PPL ↑、D-4 ↓、sigma1 ↓ — 典型 collapse 缓解但仍在退化。

**下一步**：等 ~5 分钟后重新检查 exp_018 是否完成。完成后提取 Gen 10 metrics、更新 registry 为 DONE、然后启动 exp_020。要我现在等几分钟后再查吗？

---
