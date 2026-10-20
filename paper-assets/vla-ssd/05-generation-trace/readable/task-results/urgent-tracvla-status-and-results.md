# urgent tracvla status and results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_tracvla_status_and_results_20260521T124554_result.json`
- **Structured JSON:** [`0175fecf580994da979c.json`](../../sessions/01/0175fecf580994da979c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都还在 **Trained Phase 5 (counterfactual)**，都还没到 untrained。下面是完整状态报告。

---

## GPU 状态

| GPU | 型号 | 显存占用 | 利用率 | PID |
|-----|------|---------|--------|-----|
| cuda:0 | RTX PRO 6000 Blackwell (96GB) | 9025/97887 MiB | 42% | 551650 |
| cuda:1 | RTX PRO 6000 Blackwell (96GB) | 9023/97887 MiB | 50% | 551322 |

PID 551645 (Spatial wrapper) 运行 2h05m，ALIVE。

---

## 1. TraceVLA Spatial (cuda:0) — `tracvla_spatial_full_v2`

### 进度
- Phase 1-4 (trained): **完成**
- Phase 5 counterfactual (trained): **shuffled 4600/5000**，paraphrased 未开始
- Untrained: **未开始**

### Trained — Action R² Probing (img_mean / last_preaction)

| Layer | img_mean | last_pre | 
|-------|----------|----------|
| L0 | 0.8059 | 0.6656 |
| L8 | 0.8134 | 0.7908 |
| L16 | **0.8311** | 0.8035 |
| L19 | **0.8347** ← peak | 0.8051 |
| L24 | 0.8169 | 0.7463 |
| L31 | 0.7907 | 0.6712 |

**Peak img_mean: L19 = 0.8347** | Peak last_pre: L17 = 0.8090 | 深层(L29-L30) last_pre 骤降至 0.50/0.45

### Trained — L1 Attention Profile

| 统计 | 值 |
|------|-----|
| Instruction-dominant heads | **30/32** |
| Image-dominant heads | 0 |
| Mixed | 2 (head_13=0.450, head_22=0.474) |
| Top heads | head_8=**0.945**, head_26=0.913, head_19=0.903, head_20=0.859, head_1=0.839 |

### Trained — Cross-instruction Classification (10-class, chance=0.1)

| Layer | img_mean | last_pre |
|-------|----------|----------|
| L0 | 1.000 | **0.923** |
| L1 | 1.000 | 0.998 |
| L2-L31 | 1.000 | **1.000** |

**所有层 img_mean 全部 1.0，last_pre 从 L2 起也 1.0** — 指令信息在每一层完美可分。

### Trained — Counterfactual (实时 log 数据，当前 full run)

| Condition | Global Cohen's d | Cross-task mean | Status |
|-----------|-------------------|-----------------|--------|
| wrong | 1.1724 | 1.2407 | done |
| empty | 1.3268 | 1.3569 | done |
| shuffled | — | — | **running 4600/5000** |
| paraphrased | — | — | pending |

> 注：results 目录下已有旧的 counterfactual_combined.json（2 tasks, 4 samples 的小规模测试），当前 full run (10 tasks × 5000) 完成后会覆盖。

---

## 2. TraceVLA Object (cuda:1) — `tracvla_object_full_v1`

### 进度
- Phase 1-4 (trained): **完成**
- Phase 5 counterfactual (trained): **paraphrased 1400/5000**
- Untrained: **未开始**

### Trained — Action R² Probing (img_mean / last_preaction)

| Layer | img_mean | last_pre |
|-------|----------|----------|
| L0 | 0.7458 | 0.6214 |
| L8 | 0.7562 | 0.7506 |
| L16 | 0.7687 | 0.7544 |
| L19 | **0.7741** ← peak | 0.7433 |
| L22 | 0.7757 ← (true peak) | 0.7016 |
| L24 | 0.7620 | 0.6605 |
| L31 | 0.7483 | 0.4699 |

**Peak img_mean: L22 = 0.7757** | Peak last_pre: L9 = 0.7636 | 深层 last_pre 崩溃更严重 (L30=0.186)

### Trained — L1 Attention Profile

| 统计 | 值 |
|------|-----|
| Instruction-dominant heads | **30/32** |
| Image-dominant heads | 0 |
| Mixed | 2 (head_13=0.472, head_22=0.472) |
| Top heads | head_8=**0.939**, head_26=0.920, head_19=0.901, head_20=0.867, head_1=0.851 |

### Trained — Cross-instruction Classification (10-class, chance=0.1)

| Layer | img_mean | last_pre |
|-------|----------|----------|
| L0 | 1.000 | **0.858** |
| L1 | 1.000 | 0.999 |
| L2-L31 | 1.000 | **1.000** |

Object L0 last_pre (0.858) 比 Spatial (0.923) 低，其余层全 1.0。

### Trained — Counterfactual (实时 log 数据)

| Condition | Global Cohen's d | Cross-task mean | Status |
|-----------|-------------------|-----------------|--------|
| wrong | 1.0595 | 1.0881 | done |
| empty | 1.2117 | 1.2892 | done |
| shuffled | 1.1643 | 1.1825 | done |
| paraphrased | — | — | **running 1400/5000** |

---

## 3. Spatial vs Object 对比摘要（仅 Trained，数据齐全部分）

| Metric | Spatial | Object | 差异 |
|--------|---------|--------|------|
| Peak R² (img_mean) | **0.8347** (L19) | 0.7757 (L22) | Spatial +7.6% |
| Peak R² (last_pre) | **0.8090** (L17) | 0.7636 (L9) | Spatial +5.9% |
| Attn profile | 30 instr / 2 mixed | 30 instr / 2 mixed | 相同 |
| Cross-instr L0 (last_pre) | 0.923 | 0.858 | Spatial +7.6% |
| Counterfactual d (wrong) | 1.1724 | 1.0595 | Spatial +10.7% |
| Counterfactual d (empty) | 1.3268 | 1.2117 | Spatial +9.5% |

> **⚠️ C001 约束：untrained 数据全部缺失，不做任何 conclusion。以上仅为 trained 数值记录。**

---

## 4. 时间估算

| 实验 | 剩余 trained counterfactual | untrained full pipeline | 预计完成 |
|------|---------------------------|------------------------|---------|
| Spatial | ~36 min (shuffled 尾声 + paraphrased 全程) | ~120 min | **~23:25** |
| Object | ~22 min (paraphrased 剩余) | ~110 min | **~22:55** |

---

## 5. 下一批实验就绪状态

| 项目 | 状态 |
|------|------|
| OFT checkpoint | **就绪** — 4 safetensors (14.2GB) + action_head + lora_adapter |
| 磁盘 | 82GB 可用 / 250GB (68% used) — 充足 |
| GPU | 两块 GPU 被当前实验占用，OFT 实验需等当前跑完 |

---
