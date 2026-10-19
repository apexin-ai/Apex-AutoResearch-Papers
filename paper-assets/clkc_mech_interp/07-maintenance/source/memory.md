# 关键研究发现

## Causal Gradient Profile — 完整 6 层同条件数据 [2026-05-24]

**核心发现**：同条件实验（N=201, probe acc ~85-92%）绘制出完整的因果梯度。Steering 效应 peak at L13，向深层平滑衰减，L28（detection peak）完全无效。

| Layer | Depth | Probe Acc | Best α | Fisher p | Bonferroni sig | 效应 |
|-------|-------|-----------|--------|----------|----------------|------|
| L12 | 38% | 91.75% | +20 | 0.0853 | 0/6 ❌ | — |
| **L13** | **41%** | **90.00%** | **+10** | **0.0003** | **2/6** ✅✅ | **peak** |
| **L14** | **44%** | **91.75%** | **+10** | **0.0022** | **1/6** ✅ | strong |
| **L16** | **50%** | **91.50%** | **+10** | **0.005** | **1/6** ✅ | moderate |
| L18 | 56% | 90.75% | +5 | 0.0099 | 0/6 ❌ | marginal (差0.0016) |
| L28 | 88% | 85.25% | +10 | 0.284 | 0/6 ❌ | none |

**Causal window = L13-L16（3层显著）**，L18 marginal，L12/L28 negative。窗口占 32 层模型的 ~12.5%。

**p 值单调递增梯度**：0.0003 → 0.0022 → 0.005 → 0.0099 → 0.284。连续衰减而非 on/off。

**Detection ≠ Decision 最终验证**：L28 是 detection peak（probe acc 最高），但 steering best p=0.284，完全无因果效应。高质量 probe 条件下解离依然稳健。

**仅正向 α 有效**：所有显著效应来自 +5/+10，负向 α 全不显著。

**L13 复现更强**：原始 p=0.0009 (N=136, 1α sig) → 新数据 p=0.0003 (N=201, 2α sig)。

---

## C2 不对称性非冲突特有 [2026-05-22, xnli_baseline_110]

**核心发现**：~6pp ZH→EN > EN→ZH 不对称性在非冲突任务 XNLI 上同样存在，是模型的一般性跨语言属性，非冲突信号特有。

| Model | XNLI asymmetry | Conflict asymmetry |
|-------|---------------|-------------------|
| Qwen | +6.72pp CI[2.36,11.73] ✓ | +5.95pp CI[-3.67,14.81] |
| Llama | +5.97pp CI[0.92,11.33] ✓ | +11.76pp CI[4.29,19.57] ✓ |

**推导**：英语主导预训练 → EN 表征空间更"标准" → ZH→EN 迁移天然更好。C2 需 reframe：从 "conflict-specific asymmetry" 改为 "conflict signals share general cross-lingual transfer pathways"。

---

## Steering 因果效应是 Llama-specific [2026-05-22, 更新 2026-05-24]

**核心发现**：Probe weight 方向的因果效应具有强模型特异性——仅 Llama L13-L16 有效，Qwen 和 Gemma 全部 negative。

### Llama 完整层扫描（同条件 N=201）
| 层 | 最佳 Fisher p | 结论 |
|----|-------------|------|
| L12 | 0.0853 | NEGATIVE |
| **L13** | **0.0003** | **SUCCESS** |
| **L14** | **0.0022** | **SUCCESS** |
| **L16** | **0.005** | **SUCCESS** |
| L18 | 0.0099 | NEGATIVE (marginal) |
| L28 | 0.284 | NEGATIVE |

### 跨模型结果（含匹配条件重跑）
| 模型 | 层 | 深度 | 最佳 p | N | Probe Acc | 结论 |
|------|-----|------|--------|---|-----------|------|
| **Llama L13** | 41% | 0.0003 | 201 | 90.0% | **SUCCESS** |
| **Llama L14** | 44% | 0.0022 | 201 | 91.8% | **SUCCESS** |
| **Llama L16** | 50% | 0.005 | 201 | 91.5% | **SUCCESS** |
| Qwen L14 | 39% | 0.682 | 84 | 70.2% | NEGATIVE |
| Qwen L18 | 50% | 0.620 | 84 | 73.8% | NEGATIVE |
| Qwen L23 | 64% | 1.0 | 84 | 73.2% | NEGATIVE |
| Gemma L16 | 38% | 1.000 | 88 | 59.7% | NEGATIVE |
| Gemma L17 | 40% | 1.000 | 88 | 66.5% | NEGATIVE |
| Gemma L18 | 43% | 0.497 | 88 | 61.9% | NEGATIVE |
| Gemma L10 | 24% | 0.214 | 158 | 70.6% | NEGATIVE (旧条件) |
| Gemma L17 | 40% | 0.104 | 158 | 75.3% | NEGATIVE (旧条件) |
| Gemma L24 | 57% | 1.0 | 158 | 76.3% | NEGATIVE (旧条件) |

### Gemma 匹配条件重跑分析 [2026-05-24]
- N=88（仅 88 样本通过 parametric knowledge 验证，vs Llama 201）
- Probe acc 60-66%（vs Llama 91%）——线性探针方向不足以捕获冲突信号
- Baseline 中 parametric=1/88——模型几乎不产出 parametric 回答，steering 上行空间极其有限
- L17 从旧条件 p=0.104 恶化到匹配条件 p=1.000（零 flip），说明旧实验的 marginal trend 是噪声
- **结论**：Gemma 的冲突表征可能不是线性的，或 ConflictQA 对 Gemma 的 parametric knowledge 覆盖不足

---

## 踩坑记录

### Probe Quality 是 Steering 效果的关键调节变量 [2026-05-24]
- L16 在低 probe acc (77%) 下 negative (p=0.12)，高 probe acc (91.5%) 下 success (p=0.005)
- **教训**：比较不同条件的 steering 结果时必须控制 probe quality。不同数据采样/训练集大小影响 probe 准确率，进而影响 steering direction 精度

### CUDA_VISIBLE_DEVICES 映射规则 [2026-05-22]
- SSH 手动执行时 `CUDA_VISIBLE_DEVICES` 直接对应物理 GPU 编号
- tmux 内层 `bash -c` 会覆盖外层值

### Steering 脚本不写 W&B → cron 误判 [2026-05-22]
- steering_experiment.py 输出到 JSON，不记录 W&B metrics → cron 误标 failed
- **处理**：收到 steering 的 failed 回调时，先读 JSON 再下结论

### EN→EN Probe Accuracy 数据溯源 [2026-05-22]
- Llama EN→EN peak: **0.7757 (77.6%)** at layer 28
- Qwen EN→EN peak: **0.75 (75.0%)** at layer 24

### 论文数据一致性修正 [2026-05-24]
- Appendix C L28 Best p: 0.740 是 α=-20 的 p，"Best p" 定义为 min across all α = 0.310，已修正
- artifacts experiments.tex L28 (all) p: 0.370 数学上不可能（equal flip rate → p=1.000），已修正为 1.000
- L18 "non-significance" 需加 "after Bonferroni correction" 限定（p=0.010 名义上显著），已修正
