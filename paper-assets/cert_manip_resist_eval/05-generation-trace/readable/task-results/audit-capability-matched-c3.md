# audit capability matched c3

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_capability-matched-c3_20260523T103549_result.json`
- **Structured JSON:** [`10bf76c2025c62b0e14d.json`](../../sessions/10/10bf76c2025c62b0e14d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

只有一个版本。完整审计结果如下：

---

## JSON 完整结构

```
├── strategy_a (9 models: 5 API + 4 LOCAL, accuracy 0.743–0.902, std=0.048)
│   ├── correlation
│   │   ├── K3: raw r=0.674, log r=0.664, n=84 panels
│   │   └── K5: raw r=0.502, log r=0.510, n=126 panels
│   ├── K3 (per-condition OLS + clustered)
│   │   └── summary: OLS η 8/12 κ 5/12 | Clustered η 5/12 κ 3/12
│   ├── K5 (per-condition OLS + clustered)
│   │   └── summary: OLS η 7/12 κ 11/12 | Clustered η 5/12 κ 9/12
│   ├── transition_holds: true
│   ├── dominant_predictor_K5: "K_eff"
│   └── transition_detail: K3_cl η5/κ3, K5_cl η5/κ9
│
├── strategy_b (9 models: 6 API + 3 LOCAL, accuracy 0.818–0.930, std=0.035)
│   ├── correlation
│   │   ├── K3: raw r=0.599, log r=0.560, n=84
│   │   └── K5: raw r=0.737, log r=0.741, n=126
│   ├── K3 summary: OLS η 7/12 κ 3/12 | Clustered η 5/12 κ 2/12
│   ├── K5 summary: OLS η 4/12 κ 9/12 | Clustered η 3/12 κ 2/12
│   ├── transition_holds: false
│   ├── dominant_predictor_K5: "eta_max"
│   └── transition_detail: K3_cl η5/κ2, K5_cl η3/κ2
│
├── api_only_correlation: K3 raw r=0.489, K5 raw r=0.853
├── full_set_correlation: raw 0.70, log 0.82
├── diagnosis: "inconclusive"
```

---

## 逐一回答

**(a) r=0.41 出现在哪？r=0.502 出现在哪？**

JSON 中 **没有 r=0.41 这个值**。最接近的是：
- `strategy_a.correlation.K5.raw.r` = **0.502** — 这是 strategy_a 子集中 K=5 的 panel-level Pearson r(K_eff, η_max)
- `api_only_correlation.K3.raw.r` = **0.489** — 最接近 0.41 但不是 0.41

r=0.502 的计算方式（`compute_keff_eta_correlation` 函数，line 299-344）：对每个 C(9,5)=126 个 panel combo，计算 panel 内各 condition 的 (keff, eta_max)，取均值后得到一个 (mean_keff, mean_eta) 点，最后对 126 个点求 Pearson r。

**如果论文引用了 r=0.41，它不在当前 JSON 中。** 可能来自旧版本（已被覆盖），或来自不同的计算口径。

**(b) keff_sig=9/12 是 OLS 还是 clustered？**

**取决于哪个 strategy：**
- **strategy_a K5 clustered**: keff_sig = **9/12** ← 这是 clustered SE + FDR 校正后的结果
- **strategy_a K5 OLS**: keff_sig = **11/12**
- **strategy_b K5 OLS**: keff_sig = **9/12** ← 也有一个 9/12，但这是 OLS
- **strategy_b K5 clustered**: keff_sig = **2/12**

所以 9/12 在 JSON 中出现了两次，含义不同。

**(c) clustered_keff_sig 的值？**

| | K3 clustered keff_sig | K5 clustered keff_sig |
|---|---|---|
| **strategy_a** | 3/12 | **9/12** |
| **strategy_b** | 2/12 | **2/12** |

每个 condition 的 clustered SE 具体值存储在各 condition 的 `clustered.max_clustered_se[1]` 字段中（索引 1 对应 keff），inflation 比例在 `se_inflation_keff` 字段。例如 strategy_a K3 的 mmluxprompt_injection: OLS SE = 0.770, clustered SE = 0.987, inflation = 1.28x。

**(d) transition_holds 的判定逻辑？**

脚本 line 489-492：
```python
k5_keff_sig = int(k5_result['summary']['clustered']['keff_sig'].split('/')[0])
k5_eta_sig  = int(k5_result['summary']['clustered']['eta_sig'].split('/')[0])
transition_holds = k5_keff_sig > k5_eta_sig
```

即：**K=5 时 clustered SE 下 FDR 显著的 keff 条件数 > FDR 显著的 eta 条件数**。

- strategy_a: 9 > 5 → **true**
- strategy_b: 2 < 3 → **false**

显著性阈值：FDR-BH 校正后 p < 0.05（`FDR_ALPHA = 0.05`）。

**(e) clustered 只有 2/12 是否经过 bootstrap？**

**没有经过 bootstrap。** clustered SE 的计算方法是 `clustered_se_pvalues` 函数（非 bootstrap），采用的是分析式 clustered standard error（基于 panel 内 judge overlap 的聚类结构），取 max(OLS_SE, clustered_SE) 作为保守估计，然后用 t 分布计算 p 值。FDR 校正用的是 BH 方法。

strategy_b 的 K5 clustered keff_sig = 2/12，意味着用保守的 clustered SE 后，只有 2 个 condition 的 keff 系数在 FDR 校正后仍显著。这与 OLS 的 9/12 形成巨大落差（SE inflation 在某些 condition 达到 2x 以上），说明 strategy_b 的 keff 显著性对聚类结构高度敏感。

---
