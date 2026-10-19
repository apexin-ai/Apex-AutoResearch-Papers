# analysis light bias

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_light-bias_20260515T150036_result.json`
- **Structured JSON:** [`d0a398c4a8ea75d23aca.json`](../../sessions/d0/d0a398c4a8ea75d23aca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

### Visual 子类 F1（6-class 分类器）

| 子类 | Precision | Recall | F1 |
|------|-----------|--------|----|
| camera | 1.000 | 0.963 | 0.981 |
| **light** | 0.988 | 1.000 | **0.994** |
| background | 1.000 | 0.995 | 0.997 |

### 偏差指标

- **Bias gap**: 0.0047（light F1 0.994 vs 其他 Visual 平均 0.989）
- **判定: OK** — light 与其他 Visual 子类表现基本一致，无显著偏差

### 3-class 对照（有/无 light）

| 条件 | Macro-F1 |
|------|----------|
| 含 light（559 样本） | 0.9926 |
| 去掉 light（479 样本） | 0.9897 |
| **Delta** | **+0.0029** |

去掉 light 后 macro-F1 仅下降 0.3pp，影响可忽略。

### 结论

合成 light_conditions 数据**未引入分类偏差**。尽管 light 场景成功率为 0%（远低于官方 85%），但其 activation 特征并没有比其他 Visual 子类更容易分类。bias gap 仅 0.47pp，远低于 10pp 阈值。结果已保存至 `/root/meta_brain_lora_routing/results/preliminary/light_bias/light_bias_analysis.json`。

---
