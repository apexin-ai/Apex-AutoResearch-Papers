# urgent gpu status and results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_gpu_status_and_results_20260521T103534_result.json`
- **Structured JSON:** [`c10fc1f73c96e12db26e.json`](../../sessions/c1/c10fc1f73c96e12db26e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

phi3v-base 已就绪（7.8G, 2 safetensors, config.json 存在）。全部数据收集完毕，汇总如下：

---

## GPU 状态

| GPU | 型号 | 显存 | 状态 |
|-----|------|------|------|
| 0 | RTX PRO 6000 Blackwell | 96GB | **空闲** (0MiB, 0%) |
| 1 | RTX PRO 6000 Blackwell | 96GB | **空闲** (0MiB, 0%) |

无 tmux session，无 pipeline 进程。

---

## 实验 1: object_untrained_pipeline_v1 (cuda:0)

**状态**: Phase 1-5 完成，Phase 6 (counterfactual) 崩溃  
**错误**: `AssertionError: unnorm_key not in norm_stats` — untrained OpenVLA 没有 LIBERO 的 norm stats

### R² Action Probing (32 layers)

| Layer | image_mean | last_preaction |
|-------|-----------|----------------|
| L0 | 0.7455 | 0.6084 |
| L4 | 0.7586 | 0.7304 |
| L8 | 0.7612 | 0.7413 |
| L10 | **0.7769** | 0.7491 |
| L16 | 0.7708 | 0.7552 |
| L19 | 0.7747 | **0.7608** |
| L24 | 0.7789 | 0.7442 |
| L27 | **0.7898** | 0.7153 |
| L29 | 0.7908 | 0.7051 |
| L31 | 0.7810 | 0.6850 |

**Peak**: img_mean = 0.7908 @ L29; last_preaction = 0.7608 @ L19

### L1 Attention Profile

- **Instruction-dominant**: 24/32 heads
- **Mixed**: 8/32 heads  
- **Image-dominant**: 0/32 heads
- Strongest instruction heads: h22 (0.773), h0 (0.869), h25 (0.768), h10 (0.710)

### Cross-Instruction Classification

- **All layers, both positions**: 1.000 (perfect classification)
- Chance = 0.1

### RSA Analysis (9 layers sampled)

| Layer | image_mean | last_preaction |
|-------|-----------|----------------|
| L0 | 0.5934 | 0.5020 |
| L4 | 0.5952 | 0.4783 |
| L8 | 0.5668 | 0.5831 |
| L12 | 0.5644 | **0.6040** |
| L16 | **0.5982** | 0.5917 |
| L24 | 0.5787 | **0.6092** |
| L28 | 0.5815 | 0.5998 |
| L31 | 0.5901 | 0.5779 |

**Best RSA**: L24_last_preaction = 0.6092 (CI: [0.550, 0.662])

### Counterfactual: **MISSING** (crash)

---

## 实验 2: nora_spatial_pipeline_v2 (cuda:1)

**状态**: 完成 (EXIT_CODE=0, 55.5 min)

### R² Action Probing — TRAINED (36 layers, Phi-3-Vision)

| Layer | image_mean | last_preaction |
|-------|-----------|----------------|
| L0 | 0.7106 | 0.6710 |
| L8 | 0.7164 | 0.7034 |
| L10 | **0.7207** | 0.7004 |
| L16 | 0.7074 | 0.6956 |
| L22 | 0.6897 | **0.7113** |
| L24 | 0.6894 | **0.7195** |
| L31 | 0.6291 | 0.5395 |
| L35 | 0.5532 | 0.4171 |

**Peak**: img_mean = 0.7207 @ L10; last_preaction = 0.7195 @ L24 — 后层急剧下降

### R² Action Probing — UNTRAINED

| Layer | image_mean | last_preaction |
|-------|-----------|----------------|
| L0 | 0.7193 | 0.5809 |
| L8 | 0.7207 | 0.6323 |
| L11 | **0.7253** | 0.6204 |
| L16 | 0.6956 | 0.6194 |
| L24 | 0.6780 | 0.6021 |
| L32 | 0.6881 | 0.6018 |
| L35 | 0.6680 | 0.5958 |

**Peak**: img_mean = 0.7253 @ L11; last_preaction = 0.6323 @ L8

### L1 Attention — TRAINED

- **Instruction-dominant**: 12/16 heads
- **Mixed**: 4/16 (h2, h4, h10, h14)
- Strongest: h1 (0.987), h5 (0.980), h7 (0.968), h8 (0.809)

### L1 Attention — UNTRAINED

- **Instruction-dominant**: 14/16 heads
- **Mixed**: 2/16 (h2, h4)
- Strongest: h7 (0.997), h1 (0.996), h5 (0.988), h8 (0.966)

### Cross-Instruction Classification — TRAINED

- All layers: 0.993–1.000 (img: 0.993–0.999; last_pre: 1.000)
- Chance = 0.1

### Cross-Instruction Classification — UNTRAINED

- All layers: 0.997–1.000 (img: 0.997–1.000; last_pre: 0.997–1.000)
- Chance = 0.1

### Counterfactual — TRAINED (4 conditions, last layer = L35)

| Condition | cos_dist (L35) | Cohen's d |
|-----------|---------------|-----------|
| wrong | 0.2748 | 2.158 |
| empty | 0.2381 | — |
| shuffled | 0.1141 | — |
| paraphrased | 0.0233 | — |

Cosine distance 随 layer 递增（L0=0.002 → L35=0.275 for wrong）。
Per-task Cohen's d 均值 = 2.547 (std=0.249, CV=0.098) — 非常一致。

---

## 下一批实验就绪状态

| 资源 | 状态 |
|------|------|
| OFT checkpoint | 15G, 就绪 |
| Phi-3-Vision base (untrained) | 7.8G, 就绪 |
| TracVLA pipeline scripts | `tracvla_object_full_pipeline.py`, `tracvla_spatial_full_pipeline.py` 就绪 |
| 磁盘 | 82G 可用 (68% used) |
| GPU | 两张均空闲，可立即启动 |

---

## 待修复

**object_untrained counterfactual 崩溃**：untrained OpenVLA 没有 LIBERO 的 action norm stats。counterfactual 分析需要 `generate_action()` 做 unnormalization，但 untrained 模型只有预训练时的 dataset keys。需要绕过 unnormalization 或用 representation-based 方法（像 nora_spatial 那样用 cosine distance）。

---
