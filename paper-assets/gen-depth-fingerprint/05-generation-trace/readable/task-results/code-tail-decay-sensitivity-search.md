# code tail decay sensitivity search

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tail-decay-sensitivity-search_20260517T102937_result.json`
- **Structured JSON:** [`27bfa12f406f682292ee.json`](../../sessions/27/27bfa12f406f682292ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是所有搜索结果的完整报告：

---

## 1. `grep -rn "sensitivity"` (*.py, *.json, *.yaml, *.md, *.txt)

**结果：空（exit code 1，无匹配）**

---

## 2. `grep -rn "percentile"` (*.py, *.json)

```
/root/gen-depth-fingerprint/results/8gen_table3_v5_unified.json:90:    "bootstrap_method": "percentile (2.5%, 97.5%)",
/root/gen-depth-fingerprint/results/8gen_table3_v6_unified.json:90:    "bootstrap_method": "percentile (2.5%, 97.5%)",
/root/gen-depth-fingerprint/ablation_analysis.py:49:    ci_lower = float(np.percentile(diffs, 100 * alpha / 2))
/root/gen-depth-fingerprint/ablation_analysis.py:50:    ci_upper = float(np.percentile(diffs, 100 * (1 - alpha / 2)))
/root/gen-depth-fingerprint/cross_generator_eval.py:66:                      "ci_lo": float(np.percentile(arr, 2.5)),
/root/gen-depth-fingerprint/cross_generator_eval.py:67:                      "ci_hi": float(np.percentile(arr, 97.5))}
/root/gen-depth-fingerprint/cross_ref_analysis.py:39:    ci_low, ci_high = np.percentile(rhos, [2.5, 97.5])
/root/gen-depth-fingerprint/cross_ref_analysis.py:128:    ci_lo, ci_hi = np.percentile(boot_f1s, [2.5, 97.5])
/root/gen-depth-fingerprint/scripts/ordinal_baseline.py:380:    f1_ci = np.percentile(boot_f1s, [2.5, 97.5])
/root/gen-depth-fingerprint/scripts/ordinal_baseline.py:381:    rho_ci = np.percentile(boot_rhos, [2.5, 97.5])
/root/gen-depth-fingerprint/scripts/ordinal_baseline.py:402:    f1_ci = np.percentile(boot_f1s, [2.5, 97.5])
/root/gen-depth-fingerprint/scripts/ordinal_baseline.py:426:    ci = np.percentile(diffs, [2.5, 97.5])
/root/gen-depth-fingerprint/scripts/bootstrap_ci.py:78:    return [round(float(np.percentile(vals, 2.5)), 4), ...]
/root/gen-depth-fingerprint/scripts/plot_fig1.py:65:    return np.mean(values), np.percentile(boot_means, 100*alpha), ...
/root/gen-depth-fingerprint/llama_filter_and_extract.py:219:        threshold_90 = float(np.percentile(all_depth0_nll_values, 90))
/root/gen-depth-fingerprint/llama_filter_and_extract.py:220:        print(f"  90th percentile NLL threshold: {threshold_90:.4f}")
/root/gen-depth-fingerprint/mistral_filter_and_extract.py:219:        threshold_90 = float(np.percentile(all_depth0_nll_values, 90))
/root/gen-depth-fingerprint/mistral_filter_and_extract.py:220:        print(f"  90th percentile NLL threshold: {threshold_90:.4f}")
```
（+ 大量其他 bootstrap CI 相关用法，全部是 `np.percentile(arr, 2.5)` / `np.percentile(arr, 97.5)` 模式）

---

## 3. `grep -rn "85th"` / `grep -rn "95th"`

**结果：均为空（无匹配）**

## 3b. `grep -rn "90th"`

```
/root/gen-depth-fingerprint/scripts/instruct_length_confound.py:117:        print(f"  depth {d}: 10th-90th pctile = [{depth_ranges[d][0]:.0f}, {depth_ranges[d][1]:.0f}]")
/root/gen-depth-fingerprint/llama_filter_and_extract.py:220:        print(f"  90th percentile NLL threshold: {threshold_90:.4f}")
/root/gen-depth-fingerprint/mistral_filter_and_extract.py:220:        print(f"  90th percentile NLL threshold: {threshold_90:.4f}")
```

## 3c. `grep -rn "threshold"` (*.py)

```
/root/gen-depth-fingerprint/llama_filter_and_extract.py:202:    # Depth-0 indices for threshold computation
/root/gen-depth-fingerprint/llama_filter_and_extract.py:205:    print(f"\n  Depth-0 samples for threshold: {len(depth0_texts)}")
/root/gen-depth-fingerprint/llama_filter_and_extract.py:215:        # Step 1: Compute NLL threshold from depth-0 data
/root/gen-depth-fingerprint/llama_filter_and_extract.py:216:        print("  Computing NLL threshold from depth-0 data...")
/root/gen-depth-fingerprint/llama_filter_and_extract.py:219:        threshold_90 = float(np.percentile(all_depth0_nll_values, 90))
/root/gen-depth-fingerprint/llama_filter_and_extract.py:220:        print(f"  90th percentile NLL threshold: {threshold_90:.4f}")
/root/gen-depth-fingerprint/llama_filter_and_extract.py:226:        print("  Computing tail_decay (NLL > threshold proportion)...")
/root/gen-depth-fingerprint/llama_filter_and_extract.py:233:                tail_decays.append(float(np.mean(nll_arr > threshold_90)))
/root/gen-depth-fingerprint/mistral_filter_and_extract.py:202:    # Depth-0 indices for threshold computation
/root/gen-depth-fingerprint/mistral_filter_and_extract.py:205:    print(f"\n  Depth-0 samples for threshold: {len(depth0_texts)}")
/root/gen-depth-fingerprint/mistral_filter_and_extract.py:215:        # Step 1: Compute NLL threshold from depth-0 data
/root/gen-depth-fingerprint/mistral_filter_and_extract.py:216:        print("  Computing NLL threshold from depth-0 data...")
/root/gen-depth-fingerprint/mistral_filter_and_extract.py:219:        threshold_90 = float(np.percentile(all_depth0_nll_values, 90))
/root/gen-depth-fingerprint/mistral_filter_and_extract.py:220:        print(f"  90th percentile NLL threshold: {threshold_90:.4f}")
/root/gen-depth-fingerprint/mistral_filter_and_extract.py:226:        print("  Computing tail_decay (NLL > threshold proportion)...")
/root/gen-depth-fingerprint/mistral_filter_and_extract.py:233:                tail_decays.append(float(np.mean(nll_arr > threshold_90)))
```

---

## 4. `find /root/gen-depth-fingerprint/experiments/ -name "*sensitivity*" -o -name "*tail*" -o -name "*threshold*"`

**结果：空（无匹配文件）**

---

## 5. `find /root/gen-depth-fingerprint/ -name "*sensitivity*" -o -name "*ablat*tail*"`

**结果：空（无匹配文件）**

## 5b. `find /root/gen-depth-fingerprint/ -name "*tail*"`

```
/root/gen-depth-fingerprint/fix_tail_decay_and_eval.py
```

---

## 6. `ls /root/gen-depth-fingerprint/experiments/`

```
analysis
downstream
error_analysis
human_edit_robustness
human_edit_robustness.py
multi_domain
seed_stratification
```

---

## 结论

**tail_decay sensitivity analysis 实验不存在。** 具体发现：

- 没有任何文件名包含 "sensitivity"
- 没有任何代码/文档中出现 "sensitivity" 字符串
- experiments/ 目录下无 sensitivity/tail/threshold 相关子目录
- `tail_decay` 作为特征被广泛使用（feature extraction + classification），但没有对其 threshold 做过 sensitivity 分析（如对比 85th/90th/95th percentile 的效果）
- 唯一相关的文件是 `fix_tail_decay_and_eval.py`（修复 tail_decay 计算方式并重新评估），但这不是 sensitivity analysis
- NLL threshold 固定为 90th percentile，无其他 percentile 的对比实验

---
