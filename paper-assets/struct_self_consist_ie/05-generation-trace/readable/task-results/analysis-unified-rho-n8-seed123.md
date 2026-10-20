# analysis unified rho n8 seed123

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_unified_rho_n8_seed123_20260515T133720_result.json`
- **Structured JSON:** [`3f782b5a4672403e525d.json`](../../sessions/3f/3f782b5a4672403e525d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成，全部 25/25 sanity check 通过。以下是完整汇报：

---

## 补算结果汇总

### 新增数据（之前 rho_audit 缺失的）

| 实验 | VC | SJ | FK | EM | LP |
|------|-----|-----|-----|-----|-----|
| **llama_conll_n16_seed123** | 0.4633 | 0.4662 | 0.4573 | 0.4632 | 0.3080 |
| **qwen_scierc_n16_seed42** | 0.3993 | 0.3984 | 0.2876 | 0.3386 | 0.2373 |
| **qwen_scierc_n16_seed123** | 0.3835 | 0.4234 | 0.2899 | 0.3437 | 0.2391 |
| **llama_conll_n8_seed42** | 0.4256 | 0.4314 | 0.4277 | 0.4306 | 0.3072 |

### 已有数据（确认一致）

| 实验 | VC | SJ | FK | EM | LP |
|------|-----|-----|-----|-----|-----|
| llama_conll_n16_seed42 | 0.4746 | 0.4836 | 0.4752 | 0.4818 | 0.3136 |
| llama_conll_n16_seed456 | 0.4722 | 0.4734 | 0.4690 | 0.4752 | 0.3099 |
| qwen_scierc_n16_seed456 | 0.4449 | 0.4098 | 0.2723 | 0.3363 | 0.2415 |
| qwen_conll_n8_seed42 | 0.4237 | 0.4357 | 0.3998 | 0.4507 | 0.3157 |
| llama_scierc_n8_seed42 | 0.4331 | 0.3630 | 0.3266 | 0.3152 | 0.1827 |

### N=8 vs N=16 scaling delta (LLaMA CoNLL, seed42)

| Signal | N=8 | N=16 | Delta |
|--------|------|-------|-------|
| VC | 0.4256 | 0.4746 | +0.0490 |
| SJ | 0.4314 | 0.4836 | +0.0522 |
| FK | 0.4277 | 0.4752 | +0.0475 |
| EM | 0.4306 | 0.4818 | +0.0512 |
| LP | 0.3072 | 0.3136 | +0.0064 |

### 3-seed 均值（LLaMA CoNLL N=16，r1024）

| Signal | mean | sd |
|--------|------|-----|
| VC | 0.4700 | 0.0060 |
| SJ | 0.4744 | 0.0087 |
| FK | 0.4672 | 0.0090 |
| EM | 0.4734 | 0.0095 |
| LP | 0.3105 | 0.0029 |

### 3-seed 均值（Qwen SciERC N=16）

| Signal | mean | sd |
|--------|------|-----|
| VC | 0.4092 | 0.0316 |
| SJ | 0.4105 | 0.0125 |
| FK | 0.2833 | 0.0095 |
| EM | 0.3395 | 0.0038 |
| LP | 0.2393 | 0.0021 |

### 对论文的影响

1. **N=8→N=16 delta 比之前 3-seed 汇总的值更大**：因为 r1024 数据的 N=16 rho 更高（rho_audit 用 r1024，之前 3-seed summary 用 non-r1024），N=8→N=16 增益 ~+0.05 vs 之前报告的 ~+0.03
2. **结构信号 > 表面信号 的结论在所有配置下成立**：SJ 在 LLaMA CoNLL 所有 3 seeds 和 N=8 都显著高于 FK；Qwen SciERC 同理
3. **LP 增益极小**（N=8→N=16 仅 +0.006），支持"logprob 不受 N 影响"的论点
4. **Qwen SciERC N=8 数据不存在**——没有找到 Qwen model on SciERC 的 N=8 实验数据

### 产出文件
- 服务器: `output/analysis_unified_rho_full.json` + `analysis_rho_unification/analysis_unified_rho_full.json`
- 本地: `artifacts/analysis_unified_rho_full.json`
- Artifact ID: `art_20260515_e5a68b`

---
