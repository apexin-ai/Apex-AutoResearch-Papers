# compute cross scorer f1

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_cross-scorer-f1_20260519T174641_result.json`
- **Structured JSON:** [`fee2b861e46f478b50e8.json`](../../sessions/fe/fee2b861e46f478b50e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果保存在 `/root/autodl-tmp/gen-depth-contamination/results/cross_scorer_f1/`。

12 个 `data_exp022_cross_scorer` 配置（3 generators × 4 scorers）的完整结果：

| Config | 0v1 AUC | 0v1 F1 | 1v2 AUC | 1v2 F1 | 2v3 AUC | 2v3 F1 | 3v4 AUC | 3v4 F1 | 4v5 AUC | 4v5 F1 |
|---|---|---|---|---|---|---|---|---|---|---|
| pythia_greedy__olmo | 0.9976 | 0.9808 | 0.8820 | 0.8112 | 0.5260 | 0.5186 | 0.5266 | 0.5262 | 0.5094 | 0.4986 |
| pythia_greedy__pythia | 0.9993 | 0.9886 | 0.8841 | 0.8106 | 0.5294 | 0.5257 | 0.5220 | 0.5081 | 0.5120 | 0.5115 |
| pythia_greedy__qwen_base | 0.9979 | 0.9826 | 0.8806 | 0.8082 | 0.5400 | 0.5324 | 0.5125 | 0.5028 | 0.5084 | 0.5012 |
| pythia_greedy__qwen_instruct | 0.9978 | 0.9818 | 0.8815 | 0.8085 | 0.5209 | 0.5201 | 0.5100 | 0.4991 | 0.5003 | 0.5007 |
| qwen_base__olmo | 0.9610 | 0.8909 | 0.6028 | 0.5742 | 0.5402 | 0.5174 | 0.5332 | 0.5170 | 0.5159 | 0.4967 |
| qwen_base__pythia | 0.9622 | 0.8938 | 0.6172 | 0.5746 | 0.5414 | 0.5160 | 0.5192 | 0.5084 | 0.5234 | 0.5102 |
| qwen_base__qwen_base | 0.9875 | 0.9424 | 0.6284 | 0.5972 | 0.5556 | 0.5318 | 0.5250 | 0.5185 | 0.5196 | 0.5102 |
| qwen_base__qwen_instruct | 0.9860 | 0.9368 | 0.6284 | 0.5943 | 0.5573 | 0.5303 | 0.5333 | 0.5200 | 0.5207 | 0.5121 |
| qwen_cont256__olmo | 0.9887 | 0.9409 | 0.6021 | 0.5545 | 0.5312 | 0.5183 | 0.5247 | 0.5033 | 0.5150 | 0.5136 |
| qwen_cont256__pythia | 0.9780 | 0.9223 | 0.6055 | 0.5638 | 0.5357 | 0.5215 | 0.5146 | 0.4989 | 0.5204 | 0.5148 |
| qwen_cont256__qwen_base | 0.9919 | 0.9504 | 0.6160 | 0.5822 | 0.5501 | 0.5269 | 0.5356 | 0.5189 | 0.5175 | 0.5072 |
| qwen_cont256__qwen_instruct | 0.9910 | 0.9482 | 0.6050 | 0.5650 | 0.5502 | 0.5253 | 0.5289 | 0.5169 | 0.5183 | 0.5058 |

关键发现：
- **0v1**: F1@0.50 普遍很高（0.89-0.99），与 AUC 趋势一致
- **1v2**: Pythia-generated 的 F1 约 0.81，Qwen-generated 的约 0.55-0.60
- **2v3+**: F1 均在 0.50 附近，与 AUC 接近随机一致
- Cross-scorer 不影响 K* 判定：scorer 选择对 AUC/F1 pattern 影响很小

AUC 验证：大部分配置与现有结果一致（差异 <0.005），少数 near-chance pairs 有 0.005-0.018 的微小偏差。

---
