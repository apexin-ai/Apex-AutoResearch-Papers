# exp empirical humaid analysis

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_empirical_humaid_analysis_20260524T054924_result.json`
- **Structured JSON:** [`626d26a6bb58df3968cf.json`](../../sessions/62/626d26a6bb58df3968cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `artifacts/empirical_humaid_k10_results.json`。

**关键发现：**

| 指标 | 值 |
|------|-----|
| 配置数 | 8 (3 models × 2-3 prompt strategies) |
| K | 10 |
| 总场景 | 56 (8×7 topologies) |
| 平均 \|bias%\| | 12.2% |
| 总 sign flips | 7（全部在 exposure 拓扑） |
| F1 范围 | [0.614, 0.690] |
| F1 vs bias 相关性 | -0.156（弱负相关） |

**拓扑排序（按 mean \|bias%\|）：**
1. **IV** — 30.3%（最高，但无 sign flip）
2. **front-door** — 13.2%
3. **mediation** — 13.0%
4. **exposure** — 12.5%（唯一出现 sign flip 的拓扑，7/8 configs 翻转）
5. **M-bias** — 6.0%
6. **confounding** — 5.7%
7. **collider** — 4.9%

注意服务器上还有 `qwen3_few-shot-5` 文件（plan006 中有 CM），但任务指定的 8 个有效配置不含它，故未纳入。

---
