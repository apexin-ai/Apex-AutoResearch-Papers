# train preliminary classifier

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_preliminary-classifier_20260515T145927_result.json`
- **Structured JSON:** [`37c88da8f0546b3b7ac3.json`](../../sessions/37/37c88da8f0546b3b7ac3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 初步分类器训练结果汇总

### 数据
7 个激活文件（含 sensor_noise 50 ep），共 659 episodes。

### Sweep 结果 (27 configs × 5-fold CV, 50 epochs)

| 模式 | Top-1 配置 | Accuracy |
|------|-----------|----------|
| **3-class** | `mean__paligemma_only__lr0.01` | **99.46% ± 0.44%** |
| **6-class** | `mean__paligemma_only__lr0.001` | **99.82% ± 0.36%** |
| **binary** | 多个配置并列 | **100.0% ± 0.0%** |

### Eval 最优模型指标

| 模式 | Accuracy | Macro-F1 | 备注 |
|------|----------|----------|------|
| 3-class | 97.85% | **97.14%** | visual=0.985, spatial=0.994, physical=0.936 |
| 6-class | 100% | 100% | 所有 6 类完美分类 |
| binary | 99.85% | 99.70% | ROC-AUC=0.9999 |

### Per-Layer Accuracy (3-class)
- **PaliGemma layers**: 98.2%–99.1%（layer 12 最高 99.1%）
- **Expert layers**: 69.4%–83.2%（层数越深越好，但远逊于 PaliGemma）

### 关键发现
1. **PaliGemma activations >> Expert activations**：paligemma_only 配置全面优于 expert_only（98%+ vs 70-83%）
2. **mean pooling 最优**：所有模式下 mean pooling 排名最高
3. Expert-only 最差配置仅 47%（6-class），说明 expert 层单独做分类不够
4. Binary 任务几乎 trivial（100%），perturbation vs nominal 极易区分

### GO/NO-GO

**GO** — 3-class macro-F1 = 97.14%，远超 70% 门槛。

### 产出文件
服务器路径 `/root/meta_brain_lora_routing/results/preliminary/`:
- `sweep_summary_{3class,6class,binary}.json` — 27 configs 排名
- `eval_{3class,6class,binary}/` — confusion matrix PNG/CSV, t-SNE, per-layer accuracy, classification report, ROC/PR curves (binary)

### 耗时
- 3-class sweep: ~3min
- 6-class sweep: ~3.5min
- Binary sweep: ~3.5min
- Eval (3 modes + per-layer + aggregation): ~2min
- **总计 ~12min**

---
