# ops urgent status check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_status_check_20260517T165846_result.json`
- **Structured JSON:** [`165942fad240aec18d07.json`](../../sessions/16/165942fad240aec18d07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the full status report:

---

## GPU 状态

| GPU | Model | Temp | Power | VRAM Used | VRAM Total | Util |
|-----|-------|------|-------|-----------|------------|------|
| 0 | RTX PRO 6000 Blackwell | 62°C | 337W/600W | **65,909 MiB** | 97,887 MiB | 95% |
| 1 | RTX PRO 6000 Blackwell | 63°C | 322W/600W | **25,017 MiB** | 97,887 MiB | 56% |

---

## exp_001 (Phase 0 Baseline, cuda:0)

**PID 59365: 存活**, 运行时间 17h39m17s

**当前状态**: Gen 10 刚完成 50000 样本生成，正在 fine-tuning

Gen 0-9 已全部完成，metrics 如下：

| Gen | eff_rank | log_det | perplexity | distinct_4 | hellaswag_norm | train_loss |
|-----|----------|---------|------------|------------|----------------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7414 | 0.4130 | - |
| 1 | 491.77 | 2464.76 | 11.38 | 0.6256 | 0.3897 | 1.623 |
| 2 | 496.44 | 2469.93 | 13.58 | 0.5154 | 0.3764 | 1.268 |
| 3 | 493.31 | 2440.57 | 16.25 | 0.4900 | 0.3658 | 1.134 |
| 4 | 485.67 | 2405.05 | 19.80 | 0.4679 | 0.3558 | 1.098 |
| 5 | 479.21 | 2370.17 | 24.59 | 0.4630 | 0.3439 | 1.047 |
| 6 | 473.00 | 2335.17 | 30.91 | 0.4655 | 0.3311 | 1.025 |
| 7 | 464.20 | 2304.19 | 38.89 | 0.4474 | 0.3187 | 1.015 |
| 8 | 456.76 | 2252.12 | 49.29 | 0.4401 | 0.3103 | 0.987 |
| 9 | 448.45 | 2207.57 | 63.32 | 0.4262 | 0.3009 | 0.997 |

**趋势**: 经典 model collapse 模式清晰可见
- eff_rank: 417 → 448 (先升后降，Gen 2 峰值 496 → Gen 9 回落至 448)
- log_det: 2367 → 2208 (Gen 2 峰值 2470 后持续下降)
- perplexity: 9.55 → 63.32 (6.6x 恶化)
- hellaswag: 0.413 → 0.301 (持续下降)
- distinct_4: 0.741 → 0.426 (多样性持续丧失)

---

## exp_005 (Phase 1 Adaptive k=20, cuda:1)

**PID 116947: 存活**, 运行时间 3h41m57s

**当前状态**: Gen 2 完成，正在为 Gen 3 生成样本 (18,880/25,000 ≈ 76%)

| Gen | mix_ratio | eff_rank | log_det | perplexity | distinct_4 | train_loss |
|-----|-----------|----------|---------|------------|------------|------------|
| 0 | - | 417.55 | 2366.68 | 9.55 | 0.7414 | - |
| 1 | 0.50 | 476.93 | 2366.46 | 10.09 | 0.6608 | 1.986 |
| 2 | 0.50 | 486.85 | 2395.23 | 10.42 | 0.6149 | 1.881 |

**Controller trajectory**: ratio 始终为 0.5 (log_det 未显著下降，controller 未触发调整)

**对比 Phase 0 同期**: Gen 2 时 Phase 1 ppl=10.42 vs Phase 0 ppl=13.58, adaptive mixing 显著减缓退化

---

## VRAM 评估

| GPU | 已用 | 总量 | 剩余 |
|-----|------|------|------|
| cuda:0 | 65,909 MiB | 97,887 MiB | ~32 GB |
| cuda:1 | 25,017 MiB | 97,887 MiB | ~73 GB |

- cuda:0 占用 67%，exp_001 Gen 10 fine-tuning 阶段占用最高，剩余 ~32GB 不够再跑一个 410M 实验
- cuda:1 占用 26%，剩余 ~73GB，理论上可再加 1-2 个实验
- **双实例可行性**: cuda:1 可行（剩余充足）；cuda:0 不可行（需等 exp_001 完成释放）

---

## 脚本状态

- **launch_exp_004.sh**: 存在，内容为 fixed_mix 条件实验 (`run_phase1.py --condition fixed_mix --seed 42 --generations 10`)
- **eval_hellaswag.py**: 存在 (10,457 bytes, May 17 13:06)

---
