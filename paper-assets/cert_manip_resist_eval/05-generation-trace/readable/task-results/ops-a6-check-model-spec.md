# ops a6 check model spec

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_a6-check-model-spec_20260524T125412_result.json`
- **Structured JSON:** [`7b09b844fd2d1d768566.json`](../../sessions/7b/7b09b844fd2d1d768566.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已确认。

## 结论

### 1. K_eff sig 来自 **独立 2-predictor 模型**（情况 2）

脚本中有两个独立的 OLS 回归模型，Shannon 和 K_eff **不在同一个模型里**：

- **Model 1 (Shannon)**: `X_s = [1, Shannon_H, log(η_max)]` → 产出 `shannon_fdr_sig`
- **Model 2 (K_eff)**: `X_k = [1, log(K_eff), log(η_max)]` → 产出 `keff_fdr_sig`（即表中的 "K_eff sig" 列）

两个模型都是 `sm.OLS(y, X).fit()`，y = log(ASR + ε)。

### 2. Bootstrap 参数

| 参数 | 值 |
|------|-----|
| B (replications) | **999** (`B_BOOT = 999`) |
| Weight type | **Webb 6-point** (`WEBB_6PT`) |
| Clustering | **max_p_across_K_positions**（对每个 K position 分别做 bootstrap，取 max p-value） |
| FDR α | **0.05** (`FDR_ALPHA = 0.05`) |
| Panel set size per K | **C(15, K)** — 即 `itertools.combinations(range(15), K)`，K=3→455, K=5→3003, K=7→6435（枚举所有 15 选 K 组合，无采样截断；每个 condition 跳过 n_panels<10 的） |

---
