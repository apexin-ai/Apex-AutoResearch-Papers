# analysis sf2 crossover n500

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sf2_crossover_n500_20260515T111150_result.json`
- **Structured JSON:** [`3146b89912038ea87a02.json`](../../sessions/31/3146b89912038ea87a02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**CSV**: `artifacts/crossover_n500.csv`
**MD**: `artifacts/crossover_n500.md`
服务器: `/root/autodl-tmp/pacs_analysis/sf5_asymmetric/crossover_n500.{csv,md}`

---

### 结果摘要

| Model | Phase | Imp II Median | Rand II Median | Diff Median [95% CI] | p | Crossover? |
|-------|-------|--------------|----------------|---------------------|---|------------|
| DeepSeek | high | 0.021 | 1.113 | 1.038 [0.909, 1.141] | <0.0001 | ✓ rand worse |
| DeepSeek | low | 3.971 | 1.498 | 2.214 [1.590, 2.883] | <0.0001 | ✓ imp worse |
| Qwen | high | 0.004 | 1.109 | 1.106 [1.014, 1.339] | <0.0001 | ✓ rand worse |
| Qwen | low | 1.043 | 1.770 | -0.922 [-1.171, -0.628] | <0.0001 | ✗ rand STILL worse |

**DeepSeek crossover 在 n=500 下稳健确认**（magnitude 2.13x，两个 phase 都 p<0.0001），与 n=50 方向一致，数值更稳定（n=50 high: 0.032 vs 0.818; n=500 high: 0.021 vs 1.113）。

**Qwen 没有 crossover**：random masking 在两个 phase 都比 importance 差，没有排名反转。这说明 crossover 是 model-dependent 的——DeepSeek 的 attention structure 在 low-sparsity phase 对 importance masking 的 compound interaction 更敏感，而 Qwen 对 random masking 的响应在所有 phase 都一致更差。

---
