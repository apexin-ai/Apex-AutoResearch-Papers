# code exp multi source v2 llama

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_multi_source_v2_llama_20260520T071416_result.json`
- **Structured JSON:** [`123a28eb36072fc1d627.json`](../../sessions/12/123a28eb36072fc1d627.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

## Multi-Source Detection v2 结果

**配置**: Qwen-1.5B + Pythia-1.4B + LLaMA-3.1-8B（3 家族, 2 种 scale）

### Pairwise AUC

| Pair | No Label AUC | No Label CI | With Label AUC | With Label CI |
|------|-------------|-------------|----------------|---------------|
| 0v1 | **0.9680** | [0.9640, 0.9719] | **0.9785** | [0.9755, 0.9813] |
| 1v2 | **0.7144** | [0.7019, 0.7272] | **0.7250** | [0.7126, 0.7374] |
| 2v3 | 0.5201 | [0.5061, 0.5340] | 0.5180 | [0.5043, 0.5317] |
| 3v4 | 0.5030 | [0.4891, 0.5170] | 0.5067 | [0.4928, 0.5205] |
| 4v5 | 0.5137 | [0.4996, 0.5274] | 0.5161 | [0.5021, 0.5300] |

### K* = 2（两种条件均确认）

### vs v1 (OLMo) 对比
- K* 一致：v1=2, v2=2
- v2 的 0v1 AUC 降低（0.968 vs 0.993），因 LLaMA-8B 的 depth-0 特征与 Qwen/Pythia 差异更大，增加了类内方差
- v2 的 1v2 AUC 略高（0.714 vs 0.701），混入 8B 模型对深度 1→2 区分有微弱增益
- Generator label 特征影响极小（+0.01 AUC on 1v2），说明 OBD 特征本身已足够，生成器身份对深度判别基本无贡献

### 结论
**K\*=2 在跨参数规模（1.4B-8B）混合源下依然稳健。**

---
