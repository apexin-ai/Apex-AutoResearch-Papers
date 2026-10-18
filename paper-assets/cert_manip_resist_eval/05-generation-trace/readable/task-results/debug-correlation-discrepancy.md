# debug correlation discrepancy

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_correlation-discrepancy_20260523T075444_result.json`
- **Structured JSON:** [`fc2038af2f3722aea41a.json`](../../sessions/fc/fc2038af2f3722aea41a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 JSON 现在完全一致。

## 诊断结果

**根因**：`compute_keff_eta_correlation` 有两个 bug 叠加导致 r 虚高：

| Bug | 描述 | 对 K=3 的影响 | 对 K=5 的影响 |
|-----|------|-------------|-------------|
| K_eff 公式错误 | K=3 应用 `keff_maxmi`（最大 MI），实际用了 `keff_avg_pairwise` | r: 0.489 → 0.877 | 无（两者 K=5 都用 avg_pairwise） |
| MI 来源错误 | `mi_flat` 在循环中被覆盖，只保留最后一个 dataset (arc_challenge) 的值；K_eff 应按 dataset 分别计算后取均值 | r: 0.877 → 0.980 | r: 0.853 → 0.969 |

**修正内容**：
- 新增 `_keff_maxmi_np` 和 `_keff_avg_pairwise_np`，使用 per-dataset numpy MI 矩阵
- 重写 `compute_keff_eta_correlation`：K_eff 按 (combo, dataset) 分别计算，跨 condition 取均值
- 更新所有 4 处调用点（strategy 和 API-only）

**修正后的正确值**：
- K=3: r_raw=**0.489**, VIF=**1.30**
- K=5: r_raw=**0.853**, VIF=**4.40**

与 `api_only_diagnostic.json` 完全一致，数值到小数点后 4 位匹配。

---
