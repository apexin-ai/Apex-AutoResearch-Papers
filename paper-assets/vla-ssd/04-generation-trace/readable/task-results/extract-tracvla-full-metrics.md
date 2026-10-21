# extract tracvla full metrics

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_tracvla_full_metrics_20260521T154630_result.json`
- **Structured JSON:** [`c47642d4be9609d47b94.json`](../../sessions/c4/c47642d4be9609d47b94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。以下是完整 metrics 表格。

---

## GPU 状态

| GPU | Utilization | Memory |
|-----|------------|--------|
| 0 | 0% | 15161 MiB |
| 1 | 24% | 9323 MiB |

GPU 1 正在跑 **TracVLA Spatial untrained**（task 6/10, 3100/5000 samples）。Spatial untrained 目录暂无输出文件。

---

## 1. TraceVLA Object

### 1.1 Action R² Probing

| Layer | Trained img_mean | Trained last_preaction | Untrained img_mean (Phi-3-Vision base) | Untrained last_preaction (Phi-3-Vision base) |
|-------|-----------------|----------------------|---------------------------------------|---------------------------------------------|
| L0 | 0.7458 | 0.6214 | 0.7356 | 0.5877 |
| L4 | 0.7531 | 0.7290 | 0.7406 | 0.6487 |
| L8 | 0.7562 | 0.7506 | 0.7526 | 0.6595 |
| L12 | 0.7589 | 0.7418 | 0.7470 | 0.6532 |
| L16 | 0.7687 | 0.7544 | 0.7488 | 0.6805 |
| L20 | 0.7728 | 0.7354 | 0.7531 | 0.6782 |
| L24 | 0.7620 | 0.6605 | 0.7419 | 0.6889 |
| L28 | 0.7661 | 0.5039 | 0.7448 | 0.6784 |
| L31 | 0.7483 | 0.4699 | 0.7362 | 0.6811 |
| **PEAK** | **0.7757 @ L22** | **0.7636 @ L9** | **0.7531 @ L20** | **0.6900 @ L23** |

**关键对比：**
- Trained last_preaction 呈倒U型：从 L0=0.6214 升到 L9=0.7636（peak），然后剧烈下降到 L30=0.1855（最低点），L31 回弹至 0.4699
- Untrained last_preaction 几乎平坦：全程在 0.59–0.69 区间波动，无显著下降
- Trained image_mean 略高于 untrained（~0.77 vs ~0.75），均相对平稳

### 1.2 L1 Attention Profile

| Metric | Trained | Untrained (Phi-3-Vision base) |
|--------|---------|-------------------------------|
| Instr-dominant heads | 30/32 | 32/32 |
| Mixed heads | 2 (h13=0.472, h22=0.472) | 0 |
| Image-dominant heads | 0 | 0 |
| Top-3 instr ratio | h8=0.939, h26=0.920, h19=0.901 | h8=0.997, h26=0.984, h19=0.981 |
| Bottom-3 instr ratio | h13=0.472, h22=0.472, h3=0.522 | h2=0.584, h24=0.603, h5=0.635 |

**关键对比：**
- Untrained 的 instruction ratio 普遍更高（top heads 接近 1.0）
- Trained 出现了 2 个 mixed heads (h13, h22)，untrained 全部 instruction-dominant
- 训练让部分 head 的 instruction ratio 下降（如 h8: 0.997→0.939）

### 1.3 Cross-Instruction Classification (10-way, chance=0.1)

| Layer | Trained img_mean | Trained last_preaction | Untrained img_mean | Untrained last_preaction |
|-------|-----------------|----------------------|-------------------|-------------------------|
| L0 | 1.000 | 0.858 | 1.000 | 0.922 |
| L1 | 1.000 | 0.999 | 1.000 | 0.998 |
| L2–L31 | 1.000 | 1.000 | 1.000 | 1.000 |

两个模型在 L1+ 均达到完美分类，差异仅在 L0 last_preaction（Trained=0.858 vs Untrained=0.922）。

### 1.4 Counterfactual Sensitivity

**Trained — Ranking by Cohen's d:**

| Condition | Cohen's d | Paired MSE | Token Div. Rate |
|-----------|----------|------------|-----------------|
| empty | 1.2117 | 0.1359 | 1.0 |
| shuffled | 1.1643 | 0.1061 | 1.0 |
| wrong | 1.0595 | 0.0948 | 1.0 |
| paraphrased | 0.9711 | 0.0925 | 1.0 |

**Wrong condition per-task Cohen's d:** mean=1.06, std=0.09 (range: 0.94–1.22)
**Paraphrased condition per-task Cohen's d:** mean=1.00, std=0.12 (range: 0.81–1.22)

**Untrained — `counterfactual_combined.json` 不存在**（缺失）

---

## 2. TraceVLA Spatial

### 2.1 Action R² Probing (Trained only; untrained 仍在运行)

| Layer | Trained img_mean | Trained last_preaction |
|-------|-----------------|----------------------|
| L0 | 0.8059 | 0.6656 |
| L4 | 0.8091 | 0.7954 |
| L8 | 0.8134 | 0.7908 |
| L12 | 0.8231 | 0.7980 |
| L16 | 0.8311 | 0.8035 |
| L20 | 0.8310 | 0.7981 |
| L24 | 0.8169 | 0.7463 |
| L28 | 0.8223 | 0.6150 |
| L31 | 0.7907 | 0.6712 |
| **PEAK** | **0.8347 @ L19** | **0.8090 @ L17** |

**关键特征：**
- image_mean 整体高于 Object（~0.83 vs ~0.77），spatial task 的视觉信息预测能力更强
- last_preaction 同样倒U型：L0=0.6656 → L17=0.8090（peak）→ L30=0.4472（最低）→ L31=0.6712 回弹
- Peak R² 更高（0.809 vs Object 的 0.764），spatial task 的 action 可预测性更强

### 2.2 L1 Attention Profile (Trained)

| Metric | Value |
|--------|-------|
| Instr-dominant heads | 30/32 |
| Mixed heads | 2 (h13=0.450, h22=0.474) |
| Image-dominant heads | 0 |
| Top-5 instr ratio | h8=0.945, h26=0.913, h19=0.903, h20=0.859, h1=0.839 |
| Bottom-3 instr ratio | h13=0.450, h22=0.474, h2=0.514 |

与 Object trained 几乎同构：同样的 head 偏好、同样的 h13/h22 mixed pattern。

### 2.3 Cross-Instruction Classification (Trained, 10-way, chance=0.1)

| Layer | img_mean | last_preaction |
|-------|---------|----------------|
| L0 | 1.000 | 0.923 |
| L1 | 1.000 | 0.998 |
| L2–L31 | 1.000 | 1.000 |

与 Object 模式一致。

### 2.4 Counterfactual Sensitivity (Trained)

| Condition | Cohen's d | Paired MSE | Token Div. Rate |
|-----------|----------|------------|-----------------|
| empty | 1.3268 | 0.1072 | 1.0 |
| shuffled | 1.2947 | 0.0937 | 1.0 |
| paraphrased | 1.1825 | 0.0715 | 1.0 |
| wrong | 1.1724 | 0.0795 | 1.0 |

**vs Object Trained:** Spatial 的 Cohen's d 全面更高（empty 1.33 vs 1.21, wrong 1.17 vs 1.06）。Spatial 排序中 paraphrased > wrong，与 Object 相反。

**Wrong condition per-task Cohen's d:** mean=1.17, std varies (range: 0.86–1.37)
**Paraphrased condition per-task Cohen's d:** mean=1.24, std=0.11 (range: 1.13–1.44)

---

## 数据缺口

| 实验 | 缺失 |
|------|------|
| Object untrained | `counterfactual_combined.json` 不存在 |
| Spatial untrained | 全部 4 个 probe 均缺失（实验进行中，task 6/10 @ 3100/5000） |

---
