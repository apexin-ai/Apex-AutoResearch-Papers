# analysis exp 028 postprocess

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_028_postprocess_20260517T200801_result.json`
- **Structured JSON:** [`c542ddb81fe035b379c1.json`](../../sessions/c5/c542ddb81fe035b379c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册。下面是最终结果汇总：

---

## exp_028 结果汇总

### 训练状态: ✅ 正常完成
- 5 epochs, 41180 steps, train_loss=0.0189, eval_loss=0.0311
- Best checkpoint: step 32000 (epoch ~3.9), load_best_model_at_end 选择
- Epoch 3 后 eval loss 上升 (0.032→0.041)，存在 overfitting

### 核心指标对比

| Metric | 3-epoch (exp_021) | 5-epoch (exp_028) | Delta |
|--------|:-:|:-:|:-:|
| **Degeneracy (CF1)** | **11.1%** | **31.3%** | **+20.2pp** |
| Greedy F1 | 0.7478 | 0.7773 | +2.95pp |
| LP sel F1 | 0.7614 | 0.7835 | +2.21pp |
| LP sel Δ | +1.37pp | +0.62pp | -0.75pp |
| Oracle F1 | 0.8692 | 0.8723 | +0.31pp |
| Within-instance ρ | 0.6226 | 0.4066 | -0.22 |

### Verdict: ❌ NEGATIVE

Degeneracy 31.3% 远超 20% 阈值��**Hypothesis rejected**: Few-NERD 3-epoch 低 degeneracy 是 under-convergence 的产物，不是数据集的结构属性。模型训练更充分后，degeneracy 上升到与其他数据集类似的水平。

**Paper narrative 需要修改**: 不能再将 Few-NERD 作为 "intrinsically low-degeneracy" 的案例。

### W&B
训练未启用 W&B。Loss 曲线从 trainer_state.json 提取（见报告）。

### 产出
- 分析结果 JSON: `/root/autodl-tmp/struct_self_consist_ie/output/exp_028_fewnerd_5epoch/analysis_results.json`
- Artifact: `artifacts/exp_028/report/exp_028_analysis_report.md`

---
