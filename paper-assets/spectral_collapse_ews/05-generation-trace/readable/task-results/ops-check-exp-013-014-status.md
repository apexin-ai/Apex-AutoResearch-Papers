# ops check exp 013 014 status

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_exp_013_014_status_20260521T012525_result.json`
- **Structured JSON:** [`9fb0c22447d7202450b7.json`](../../sessions/9f/9fb0c22447d7202450b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 67% | 25,017 / 97,887 MiB |
| 1 | 76% | 25,017 / 97,887 MiB |

---

### exp_013 — `pure_collapse_seed44` (r=0.0, 10 gen)
- **当前**: Gen 7/10, **generating** 阶段, 42,560/50,000 samples (~85%)
- **已完成 gen 0-6 指标**:

| Gen | eff_rank | PPL | D-4 | train_loss |
|-----|----------|------|------|------------|
| 0 | 417.55 | 9.55 | 0.7305 | — |
| 1 | 490.77 | 11.36 | 0.6019 | 1.626 |
| 2 | 495.83 | 13.54 | 0.4943 | 1.233 |
| 3 | 493.45 | 16.22 | 0.4283 | 1.024 |
| 4 | 488.35 | 19.97 | 0.3731 | 0.905 |
| 5 | 480.04 | 24.30 | 0.3569 | 0.817 |
| 6 | 472.30 | 30.21 | 0.3326 | 0.768 |

- **结果文件**: `/root/spectral_collapse_ews/results/phase1_pure_collapse_seed44_results.json`
- **预估剩余**: Gen 7 生成快完成，还需 gen 7 train+eval + gen 8-10 全流程

---

### exp_014 — `fixed_mix_r025_seed43` (r=0.25, 10 gen)
- **当前**: Gen 2/10, **generating** 阶段, 21,120/37,500 samples (~56%)
- **已完成 gen 0-1 指标**:

| Gen | eff_rank | PPL | D-4 | train_loss |
|-----|----------|------|------|------------|
| 0 | 417.55 | 9.55 | 0.7415 | — |
| 1 | 475.66 | 10.23 | 0.6584 | 1.802 |

- **结果文件**: `/root/spectral_collapse_ews/results/phase1_fixed_mix_r025_seed43_results.json`
- **预估剩余**: Gen 2 生成过半，还需 gen 2 train+eval + gen 3-10 全流程

---

两个实验日志均在持续写入（最后修改 09:26 +0800），均正常运行中。

---
