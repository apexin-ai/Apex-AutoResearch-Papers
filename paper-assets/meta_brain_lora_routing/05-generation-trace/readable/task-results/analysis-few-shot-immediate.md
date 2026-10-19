# analysis few shot immediate

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_few-shot-immediate_20260515T153252_result.json`
- **Structured JSON:** [`17ec7ce742a044a12489.json`](../../sessions/17/17ec7ce742a044a12489.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## 实验结果

### 实验 A：Visual 子类区分（camera vs light vs background）

| K | macro-F1 | Accuracy | n |
|---|----------|----------|---|
| 1 | **0.898** ± 0.064 | 0.899 | 89 |
| 3 | 0.834 ± 0.091 | 0.853 | 89 |
| 5 | 0.900 ± 0.072 | 0.900 | 89 |
| 10 | 0.869 ± 0.083 | 0.878 | 89 |
| all | **0.920** ± 0.027 | 0.922 | 89 |

### 实验 C：K=1 单层分析（top 5）

| Layer | K=1 macro-F1 |
|-------|-------------|
| **paligemma_layer_6** | **1.0000** ± 0.000 |
| paligemma_layer_4 | 0.9888 ± 0.022 |
| paligemma_layer_8 | 0.9888 ± 0.022 |
| paligemma_layer_14 | 0.9888 ± 0.022 |
| paligemma_layer_12 | 0.9776 ± 0.027 |
| ... | |
| expert_layer_14 (最好的 expert) | 0.5740 ± 0.095 |
| expert_layer_6 (最差) | 0.4268 ± 0.096 |

### ROUTING VIABILITY VERDICT: **VIABLE**

关键发现：
1. **K=1 就达到 F1=0.898**，远超 70% 阈值 → 单次前向传播即可路由
2. **paligemma_layer_6 单层 K=1 就达到 F1=1.0**（完美分类），意味着仅用 1 层 2048 维特征即可做路由，无需全部 12 层
3. **PaLIGemma vs Expert 分支差距巨大**：所有 PaLIGemma 层 >0.92，所有 Expert 层 <0.58 → Visual 子类信号完全在视觉编码器中，action expert 不编码视觉扰动差异
4. K=3 比 K=1 略低可能是 averaging noise 导致的波动（样本量小，5-fold CV 方差较大）
5. 实验 B（Visual/Spatial/Physical 3-class）无法运行 —— objects_layout 和 robot_initial_states 的 per_step 数据为空

---
