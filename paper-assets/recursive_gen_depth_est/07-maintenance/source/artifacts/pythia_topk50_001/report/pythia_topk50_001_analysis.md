# Pythia-1.4B Top-k (k=50) 实验结果 — pythia_topk50_001

**完成时间**: 2026-05-14 20:14 UTC (pipeline) / 2026-05-14 20:22 UTC (eval)
**3×3 矩阵位置**: Cell 5/9

---

## 1. 核心 Metrics

### 4-class Classification (d0-d3)

| Classifier | Accuracy | 95% CI |
|-----------|----------|--------|
| Random Baseline | 25.6% | — |
| Majority Baseline | 25.0% | — |
| Logistic Regression | 68.2% | [66.7%, 69.6%] |
| **Random Forest** | **69.63%** | **[68.25%, 71.07%]** |

Per-class RF performance:
| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| depth-0 | 0.99 | 0.99 | 0.99 |
| depth-1 | 0.71 | 0.72 | 0.72 |
| depth-2 | 0.48 | 0.48 | 0.48 |
| depth-3 | 0.61 | 0.59 | 0.60 |

### 4-class Pairwise AUC (RF)

| Pair | AUC |
|------|-----|
| d0 vs d1 | 0.9927 |
| d0 vs d2 | 0.9983 |
| d0 vs d3 | 0.9978 |
| **d1 vs d2** | **0.7518** |
| d1 vs d3 | 0.9176 |
| **d2 vs d3** | **0.6918** |

### 3-class Classification (d1-d3 only, RF)

| Metric | Value |
|--------|-------|
| Accuracy | 59.20% (CI: [57.5%, 61.1%]) |
| AUC d1v2 | 0.7452 |
| AUC d1v3 | 0.9069 |
| AUC d2v3 | 0.7000 |

### 3-class Filtered (code decontaminated, RF)

| Metric | Value |
|--------|-------|
| Accuracy | 61.33% (CI: [59.3%, 63.1%]) |
| AUC d1v2 | 0.7680 |
| AUC d1v3 | 0.9323 |
| AUC d2v3 | 0.7013 |
| Test samples | 2356 (filtered from 3000) |

---

## 2. vs Baseline / Other Cells 对比

### 4-class Accuracy & Key AUC

| Cell | Model | Strategy | 4-class RF Acc | AUC d1v2 | AUC d2v3 |
|------|-------|----------|---------------|----------|----------|
| 1 | Pythia-1.4B | Nucleus p=0.95 (baseline) | 78.2% | 0.8607 | 0.8005 |
| 2 | Pythia-1.4B | Temp T=0.9 | 76.25% | 0.8327 | 0.7928 |
| **5** | **Pythia-1.4B** | **Top-k k=50** | **69.63%** | **0.7518** | **0.6918** |
| 3 | OLMo-1B | Nucleus p=0.95 | 78.8% | 0.8673 | 0.8124 |
| 4 | GPT-2 XL | Nucleus p=0.95 | 83.3% | 0.9131 | 0.8829 |

### Delta vs Pythia Nucleus Baseline

| Metric | Top-k k=50 | Δ vs baseline |
|--------|-----------|---------------|
| 4-class acc | 69.63% | **-8.57pp** |
| AUC d1v2 | 0.7518 | **-0.1089** |
| AUC d2v3 | 0.6918 | **-0.1087** |

### Delta vs Pythia Temp09

| Metric | Top-k k=50 | Δ vs temp09 |
|--------|-----------|-------------|
| 4-class acc | 69.63% | **-6.62pp** |
| AUC d1v2 | 0.7518 | **-0.0809** |
| AUC d2v3 | 0.6918 | **-0.1010** |

---

## 3. Feature Importance (4-class RF, top-10)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | var_surprisal | 0.176 |
| 2 | p90_ppl | 0.135 |
| 3 | mean_ppl | 0.112 |
| 4 | mean_surprisal | 0.070 |
| 5 | p75_ppl | 0.061 |
| 6 | type_token_ratio | 0.042 |
| 7 | hapax_ratio | 0.042 |
| 8 | p50_ppl | 0.039 |
| 9 | p25_ppl | 0.037 |
| 10 | entropy_of_surprisal | 0.037 |

Top-5 与 baseline 一致：var_surprisal、p90_ppl、mean_ppl 始终是最重要的特征。

---

## 4. Code Contamination

| Depth | Broad Filter | Narrow Filter |
|-------|-------------|---------------|
| 0 (human) | 25 (0.5%) | 20 (0.4%) |
| 1 | 843 (16.9%) | 383 (7.7%) |
| 2 | 1103 (22.1%) | 614 (12.3%) |
| 3 | 1274 (25.5%) | 654 (13.1%) |

模式与其他 cell 一致：contamination 随 depth 递增。Filtered 后 3-class 准确率反而提高 (61.33% > 59.20%)，说明 code contamination 引入噪声。

---

## 5. Finetune Loss

| Depth | Initial Loss | Final Loss (3 epochs) |
|-------|-------------|----------------------|
| 0 | 2.321 | 2.210 |
| 1 | 1.723 | 1.691 |
| 2 | 1.574 | 1.437 |

Loss 随 depth 递减的趋势与其他 cell 一致，反映递归生成文本逐渐变得更可预测。

---

## 6. 分析与结论

### 关键发现

1. **Top-k k=50 显著削弱深度信号**：4-class accuracy 下降 8.57pp（所有已完成 cell 中最大降幅），关键 AUC 对均下降 ~0.11。

2. **信号仍存但更弱**：69.63% 仍远高于 25% chance level；3-class 59.2% 远高于 33.3%。深度信号在 top-k 解码下依然可检测，但分辨力显著下降。

3. **d2 vs d3 接近随机**：AUC 0.6918 是所有已完成 cell 中最低的，表明 top-k 解码使高深度文本趋于同质化。

4. **Decontamination 略微提升信号**：filtered 3-class 61.33% > unfiltered 59.20%，与预期一致。

5. **Feature importance 稳定**：top-5 特征在所有 model×strategy 组合中一致，表明深度信号的统计结构不受解码策略改变。

### 解释

Top-k k=50 通过截断概率分布尾部，将每步的有效词汇限制在 50 个 token。相比 nucleus p=0.95（保留覆盖 95% 概率质量的所有 token），top-k 更激进地限制输出多样性。这导致：
- 递归生成的文本在统计特征上更快趋于收敛
- 不同深度之间的 perplexity 分布差异缩小
- 分类器更难区分相邻深度（尤其 d2 vs d3）

### 结论: **Partial Success (weaker signal)**

深度信号在 top-k k=50 下保持可检测但显著衰减。这支持了 hypothesis：解码策略的多样性控制（而非仅温度）对深度信号的保持有重要影响。Nucleus sampling 通过自适应词汇选择保留了更丰富的分布信息。

---

## 7. 3×3 矩阵进度 (5/9 completed)

|  | Nucleus p=0.95 | Temp T=0.9 | Top-k k=50 |
|--|---------------|------------|------------|
| **Pythia-1.4B** | ✅ 78.2% | ✅ 76.25% | ✅ **69.63%** |
| **OLMo-1B** | ✅ 78.8% | 🔄 running | ⬜ pending |
| **GPT-2 XL** | ✅ 83.3% | 🔄 running | ⬜ pending |
