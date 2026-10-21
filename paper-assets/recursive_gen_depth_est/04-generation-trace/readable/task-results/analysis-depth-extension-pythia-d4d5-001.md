# analysis depth extension pythia d4d5 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_depth_extension_pythia_d4d5_001_20260515T051548_result.json`
- **Structured JSON:** [`a137b2f17a8c8dc1e7c0.json`](../../sessions/a1/a137b2f17a8c8dc1e7c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 WARNING/ERROR。所有数据已提取，结果如下：

---

## Conclusion: success

d3v4 AUC = 0.6809, d4v5 AUC = 0.6948 — **均低于 0.75 阈值**。但需要注意：这是 RF pairwise AUC，衡量的是**相邻代之间**的可区分度。所有相邻对 AUC 均 >0.65，且累积 AUC（跨多代）仍然很高（d3v5=0.8632, d2v5=0.949），说明信号在累积维度上并未饱和。

**修正判断：按严格定义（相邻对 AUC > 0.75），d3v4 和 d4v5 未达标，结论应为 negative。**

## Conclusion: negative

相邻代 d3v4 AUC = 0.6809, d4v5 AUC = 0.6948，均 < 0.75。递归深度信号在 depth 3 之后的**相邻代区分能力**开始饱和。

## Key Metrics
- **6-class RF accuracy**: 0.6232 (95% CI: [0.6113, 0.6360])
- **6-class LR accuracy**: 0.5862 (95% CI: [0.5735, 0.5987])
- **Baselines**: random=0.1685, majority=0.1667
- **Pairwise AUC (Random Forest)**:
  - d0v1: 0.9962
  - d1v2: 0.8231
  - d2v3: 0.6878
  - d3v4: **0.6809** (NEW - 低于 0.75)
  - d4v5: **0.6948** (NEW - 低于 0.75)
- **Pairwise AUC (Logistic Regression)**:
  - d0v1: 0.9908
  - d1v2: 0.6901
  - d2v3: 0.6174
  - d3v4: 0.6828
  - d4v5: 0.6554
- **EDD**: 未显式计算，但按 AUC>0.75 定义，EDD=2（仅 d0v1 和 d1v2 的 RF AUC >0.75）
- **Feature importance (top 5)**:
  1. p90_ppl: 0.1376
  2. var_surprisal: 0.1344
  3. mean_ppl: 0.0796
  4. mean_surprisal: 0.0789
  5. p75_ppl: 0.0680
- **Finetune losses**:
  - depth_3 (lora_depth_3): final loss = 0.7634
  - depth_4 (lora_depth_4): final loss = 0.5828

## Checkpoint paths
- lora_depth_3: `/root/autodl-tmp/recursive_gen_depth_est/checkpoints/lora_depth_3/` (adapter_model.safetensors 6.0MB)
- lora_depth_4: `/root/autodl-tmp/recursive_gen_depth_est/checkpoints/lora_depth_4/` (adapter_model.safetensors 6.0MB)
- Result files:
  - `results/pythia_depth_extension/classification_report.txt`
  - `results/pythia_depth_extension/confusion_matrix.png`
  - `results/pythia_depth_extension/pairwise_auc.json`
  - `results/pythia_depth_extension/feature_importance.json`
  - `results/pythia_depth_extension/features_6class.jsonl` (20.6MB)

## Notes
- 无错误/无警告，pipeline 完整执行。
- **关键观察**：相邻代 AUC 呈递减趋势：0.9962 → 0.8231 → 0.6878 → 0.6809 → 0.6948。d2v3 已经跌破 0.75，d3v4/d4v5 维持在 ~0.68-0.69，未进一步大幅下降，说明信号在 depth 2-3 后趋于**平稳低区分度**而非完全消失。
- d4v5 AUC (0.6948) 略高于 d3v4 (0.6809)，非单调递减，可能是 depth_4 finetune loss 更低（0.5828 vs 0.7634）导致更强的风格印记。
- **跨代累积 AUC 仍然很高**：d0v5=0.9987, d1v5=0.9874, d2v5=0.949, d3v5=0.8632 — 说明递归生成的**累积漂移**持续增长，只是**相邻代间的增量**趋于饱和。
- 6-class accuracy 62.3% 远超 chance (16.7%)，证明 6 个 depth 之间仍有可区分的统计特征。

---
