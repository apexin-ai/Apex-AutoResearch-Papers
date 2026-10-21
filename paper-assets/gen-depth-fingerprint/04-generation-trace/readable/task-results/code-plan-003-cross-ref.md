# code plan 003 cross ref

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-003-cross-ref_20260514T235938_result.json`
- **Structured JSON:** [`b7bf3c65ddbafb45442d.json`](../../sessions/b7/b7bf3c65ddbafb45442d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## plan-003 结果

### 产出文件
- `data/features_ref_olmo.csv` — OLMo-2-1B 参考，23032 rows
- `data/features_ref_qwen.csv` — Qwen3-0.6B 参考，23032 rows
- `data/cross_ref_results.json` — 结构化结果

### entropy_mean drift (depth 0 → 2+)

| Generator | Pythia-410M ref | OLMo-2-1B ref | Qwen3-0.6B ref |
|-----------|:-:|:-:|:-:|
| olmo-2-1b | **-1.2127** | -0.9089 | -1.2520 |
| pythia-1b | **-1.4017** | -0.7722 | -1.1339 |
| pythia-2.8b | **-1.1872** | -0.6080 | -0.9557 |
| qwen3-0.6b | **-1.2068** | -0.8285 | -1.3215 |
| qwen3-1.7b | **-1.2265** | -0.8763 | -1.3458 |

**5/5 generators 在所有 3 个参考模型下都呈现负 drift**。Dual dynamics 不是 Pythia artifact。

### LOGO macro-F1

| Reference | Avg F1 | 95% CI |
|-----------|:------:|:------:|
| Pythia-410M | 0.8034 | [0.7722, 0.8322] |
| OLMo-2-1B | 0.8072 | [0.7802, 0.8309] |
| Qwen3-0.6B | **0.8158** | [0.7862, 0.8411] |

三个参考模型的 LOGO 分类性能高度一致（F1 0.80-0.82），CI 大幅重叠。Qwen3-0.6B 参考略优。

### 关键结论
- entropy_mean 随 depth 下降的 drift 在**所有参考模型**下一致存在，确认 dual dynamics 是生成过程的固有特征
- OLMo 参考下 drift 幅度较小（-0.6 ~ -0.9）但方向一致
- 分类能力不依赖特定参考模型，跨家族泛化性良好

---
