# ops fix buggy artifacts

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-buggy-artifacts_20260516T125950_result.json`
- **Structured JSON:** [`e1790a663cf969620ed0.json`](../../sessions/e1/e1790a663cf969620ed0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. Buggy 文件重命名 ✓

`8gen_logo_results.json` → `8gen_logo_results_BUGGY_DO_NOT_USE.json`

### 2. Spearman artifacts 未被污染 ✓

Mistral `features_pythia410m.jsonl` 中 tail_decay 值为 **负数，量级 -0.002**（如 -0.00232, -0.00206, -0.00217），这是修复后的 log-prob slope 公式。Spearman 文件创建于今天 20:51，使用的是正确特征，**无需重算**。

Pooled Spearman ρ（tail_decay）= **-0.0413**（极弱相关，符合预期——tail_decay 本身对 depth 区分力弱）。

### 3. `8gen_logo_unfiltered.json` 完整数字表

**Binary F1** (overall = **0.6944**, CI [0.6883, 0.7004], N=29,095):

| Generator | F1 | CI |
|-----------|----|----|
| pythia-2.8b | 0.7243 | [0.7068, 0.7417] |
| pythia-1b | 0.7175 | [0.6998, 0.7350] |
| qwen3-1.7b | 0.7093 | [0.6925, 0.7259] |
| llama-3.2-3b | 0.6968 | [0.6798, 0.7129] |
| olmo-2-1b | 0.6954 | [0.6788, 0.7114] |
| qwen3-8b | 0.6918 | [0.6738, 0.7077] |
| qwen3-0.6b | 0.6911 | [0.6733, 0.7086] |
| mistral-7b-v0.3 | **0.6327** | [0.6172, 0.6482] |

**3-class F1** (overall = **0.762**, CI [0.7577, 0.7664], N=37,058):

| Generator | F1 | CI |
|-----------|----|----|
| pythia-1b | 0.8064 | [0.7946, 0.8177] |
| pythia-2.8b | 0.7983 | [0.7865, 0.8097] |
| qwen3-0.6b | 0.7795 | [0.7677, 0.7925] |
| olmo-2-1b | 0.7810 | [0.7695, 0.7931] |
| llama-3.2-3b | 0.7753 | [0.7634, 0.7880] |
| qwen3-1.7b | 0.7717 | [0.7585, 0.7844] |
| qwen3-8b | 0.7143 | [0.7007, 0.7286] |
| mistral-7b-v0.3 | **0.6815** | [0.6694, 0.6950] |

### 4. Pooled Spearman ρ（参考）

| Feature | ρ (pooled) | ρ (balanced) |
|---------|-----------|-------------|
| hapax_ratio | -0.6405 | -0.6288 |
| ttr | -0.6249 | -0.6130 |
| entropy_mean | -0.5978 | -0.5954 |
| entropy_min | -0.4037 | -0.3992 |
| entropy_std | -0.1567 | -0.1692 |
| entropy_max | +0.0608 | +0.0595 |
| **tail_decay** | **-0.0413** | **-0.0422** |

结论：所有 artifacts 一致，唯一的污染源是已重命名的 `8gen_logo_results_BUGGY_DO_NOT_USE.json`。

---
