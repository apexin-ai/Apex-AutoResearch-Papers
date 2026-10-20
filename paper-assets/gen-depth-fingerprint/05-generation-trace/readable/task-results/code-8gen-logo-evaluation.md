# code 8gen logo evaluation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8gen-logo-evaluation_20260516T121446_result.json`
- **Structured JSON:** [`d9e6347ecf0f444a4986.json`](../../sessions/d9/d9e6347ecf0f444a4986.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `/root/gen-depth-fingerprint/results/8gen_logo_results.json`。

## 8-gen LOGO 结果

### 3-class (gen-0 / gen-1 / gen-2+)

| Generator | F1 | 95% CI | Δ vs 6-gen |
|---|---|---|---|
| llama-3.2-3b | 0.7434 | [0.7299, 0.7579] | (new) |
| mistral-7b-v0.3 | **0.6283** | [0.6152, 0.6423] | (new) |
| olmo-2-1b | 0.7651 | [0.7542, 0.7764] | +0.0016 |
| pythia-1b | **0.8516** | [0.8417, 0.8620] | -0.0046 |
| pythia-2.8b | 0.8065 | [0.7957, 0.8171] | +0.0024 |
| qwen3-0.6b | 0.8235 | [0.8129, 0.8344] | -0.0008 |
| qwen3-1.7b | 0.8075 | [0.7965, 0.8187] | +0.0029 |
| qwen3-8b | 0.6845 | [0.6713, 0.6978] | +0.0013 |
| **AVERAGE** | **0.7638** | | **-0.0255** |

### Binary (gen-1 vs gen-2+)

| Generator | F1 | 95% CI |
|---|---|---|
| llama-3.2-3b | 0.6224 | [0.6017, 0.6430] |
| mistral-7b-v0.3 | **0.4876** | [0.4683, 0.5061] |
| olmo-2-1b | 0.6860 | [0.6708, 0.7019] |
| pythia-1b | **0.7888** | [0.7755, 0.8039] |
| **AVERAGE** | **0.6851** | |

### 要点

- 6-gen baseline 3-class F1 = 0.7893，8-gen = 0.7638，**Δ = -0.0255**
- 原 6 generator 几乎不受影响（Δ ≤ ±0.005），说明新 generator 的加入没有干扰原有训练
- **Mistral-7B** 是最难的 held-out generator（3-class 0.6283, binary 接近随机），可能是因为 tail_decay 计算方式不同 + 7B 模型生成分布差异大
- **Llama-3.2-3B** 表现中等（0.7434），泛化尚可
- 注意：llama/mistral 的 `tail_decay` 用 NLL 比例计算（0-1范围），与原 6 generator 的 log-prob slope（~-0.002）不同。tail_decay 排名 7/7 影响较小，但 Mistral 的低分可能部分受此影响

---
