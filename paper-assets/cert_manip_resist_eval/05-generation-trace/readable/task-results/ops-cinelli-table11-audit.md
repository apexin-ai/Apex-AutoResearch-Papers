# ops cinelli table11 audit

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cinelli-table11-audit_20260524T164955_result.json`
- **Structured JSON:** [`26895693ee48710a7818.json`](../../sessions/26/26895693ee48710a7818.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整。以下是核对结果：

---

## Cinelli-Hazlett Table 11: RV exceeds η_max confound (V2 数据)

### K=3: **4/12** 条件 exceeds

| Benchmark | Attack | RV | η_max | Exceeds |
|-----------|--------|-----|-------|---------|
| mmlu | sycophancy | 0.5005 | 0.2427 | **Yes** |
| mmlu | authority_bias | 0.4928 | 0.3551 | **Yes** |
| arc_challenge | prompt_injection | 0.4954 | 0.4299 | **Yes** |
| arc_challenge | sycophancy | 0.4217 | 0.3985 | **Yes** |

### K=5: **3/12** 条件 exceeds

| Benchmark | Attack | RV | η_max | Exceeds |
|-----------|--------|-----|-------|---------|
| mmlu | prompt_injection | 0.4554 | 0.3789 | **Yes** |
| mmlu | sycophancy | 0.3028 | 0.1064 | **Yes** |
| mmlu | verbosity_bias | 0.2350 | 0.1196 | **Yes** |

### K=7: **4/12** 条件 exceeds

| Benchmark | Attack | RV | η_max | Exceeds |
|-----------|--------|-----|-------|---------|
| mmlu | prompt_injection | 0.5223 | 0.2889 | **Yes** |
| mmlu | sycophancy | 0.3005 | 0.0766 | **Yes** |
| mmlu | verbosity_bias | 0.2054 | 0.0784 | **Yes** |
| mmlu | position_bias | 0.2069 | 0.1794 | **Yes** |

### 总计: **11/36**

### 数据来源
- 文件：`/root/cert_manip_resist_eval/artifacts/results/plan001/cinelli_hazlett_v2.json`
- 修改时间：2026-05-24 18:07:58 (CST)
- 数据版本：V2 (`_is_valid_score` filtered)
- 模型数：15

### 备注
- K=3 的 exceeds 集中在 mmlu 和 arc_challenge 两个 benchmark
- K=5 和 K=7 的 exceeds 全部在 mmlu benchmark
- arc_challenge 在 K≥5 时无 exceeds 条件
- sycophancy 是唯一在所有 3 个 K 值下都 exceeds 的 attack（均在 mmlu benchmark）

---
