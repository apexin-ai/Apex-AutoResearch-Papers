# F1-Macro Reporting Audit

## 1. Paper Table Audit

### Table 1 (`tab:main_results`) — Function-level per-test results

| Row | Method | F1-macro reported? |
|-----|--------|--------------------|
| CLS 4B (5 seeds) | Accuracy only | **NO** |
| CWM 4B (5 seeds) | Accuracy only | **NO** |
| TRAJ 4B (5 seeds) | Accuracy only | **NO** |
| CLS DeepSeek 6.7B | Accuracy only | **NO** |
| CWM DeepSeek 6.7B | Accuracy only | **NO** |
| ZS 8B | Accuracy only | **NO** |
| ZS 32B | Accuracy only | **NO** |

**Status**: Table has only Accuracy column. No F1-macro for any condition.

### Table 2 (`tab:scaling`) — Model-size scaling (4B vs 8B)

| Row | Method | F1-macro reported? |
|-----|--------|--------------------|
| CLS 4B (s42/123/456) | Per-seed accuracy + mean | **NO** |
| CWM 4B (s42/123/456) | Per-seed accuracy + mean | **NO** |
| CLS 8B (s42/123/456) | Per-seed accuracy + mean | **NO** |
| CWM 8B (s42/123/456) | Per-seed accuracy + mean | **NO** |

**Status**: Only accuracy. No F1-macro.

### Table 3 (`tab:repo_level`) — Repo-level per-test results

| Row | Method | Macro F1 value | Status |
|-----|--------|----------------|--------|
| CLS 4B s42 | 75.63 | **Present** |
| CWM 4B s42 | 51.67 | **Present** |
| CWM 4B s123 | 43.43 | **Present** |
| CLS 8B s42 | 78.17 | **Present** |
| CLS 8B s123 | 78.38 | **Present** |
| CWM 8B s42 | `---` | **MISSING** |
| DeepSeek CLS 6.7B | `---` | In progress |
| DeepSeek CWM 6.7B | `---` | In progress |
| Majority baseline | `---` | N/A (undefined for constant prediction) |

**Status**: Table has Macro F1 column. CWM 8B s42 is the only completed experiment with missing F1-macro.

---

## 2. Eval Script Audit

| Script | Per-class F1 | Macro F1 | Output JSON key | Printed in report |
|--------|:---:|:---:|---|---|
| `eval_repo_verifier.py` (CLS repo) | Yes | **NO** | `per_class.{fail,pass}.f1` only | Per-class only |
| `eval_repo_cwm.py` (CWM repo) | Yes | **YES** | `metrics.f1_macro` | Yes (line 315) |
| `eval_traj_verifier.py` (TRAJ) | Yes | **NO** | `per_class.{unresolved,resolved}.f1` only | Per-class only |
| `eval_verifier.py` (func CLS, deprecated) | Yes | **NO** | `per_class.{fail,pass}.f1` only | Per-class only |
| `eval_cwm_baseline.py` (func CWM) | Yes | **NO** | `per_class.{fail,pass}.f1` only | Per-class only |

All scripts compute `f1_score(y_true, y_pred, average=None, labels=[0,1])` (per-class), so macro = `f1.mean()` is trivially derivable. Only `eval_repo_cwm.py` explicitly computes and outputs it.

---

## 3. Gap Summary

| Gap | Location | Action needed |
|-----|----------|---------------|
| Table 1: No F1-macro | experiments.tex | Add F1-macro column (data available from eval scripts) |
| Table 2: No F1-macro | experiments.tex | Add F1-macro column (recompute from saved predictions) |
| Table 3: CWM 8B s42 missing | experiments.tex | Re-run eval or compute from `results_incremental.jsonl` |
| `eval_repo_verifier.py` no macro | code | Add `f1_macro` to output dict |
| `eval_traj_verifier.py` no macro | code | Add `f1_macro` to output dict |
| `eval_verifier.py` no macro | code | Add `f1_macro` to output dict (deprecated) |
| `eval_cwm_baseline.py` no macro | code | Add `f1_macro` to output dict |

---

## 4. Code Modification Suggestions

### 4.1 `eval_repo_verifier.py` — Add F1-macro

In the metrics computation section (after `f1 = f1_score(...)` around the results dict construction), add:

```diff
     results = {
         "split": args.split,
         "test_set_size": total,
         ...
         "overall_accuracy": round(acc * 100, 2),
+        "f1_macro": round(float(f1.mean()) * 100, 2),
         "accuracy_vs_baseline_gap_pp": round(gap * 100, 2),
         "per_class": { ... },
```

And in the print report section:
```diff
     print(f"\nOverall accuracy: {acc*100:.1f}%")
+    print(f"F1 macro: {float(f1.mean())*100:.2f}%")
     gap_status = "PASS" if gap >= 0.10 else "FAIL"
```

### 4.2 `eval_traj_verifier.py` — Add F1-macro

Same pattern. After `f1 = f1_score(y_true, y_pred, average=None, labels=[0, 1])`:

```diff
     results = {
         "test_set_size": total,
         ...
         "overall_accuracy": round(acc * 100, 2),
+        "f1_macro": round(float(f1.mean()) * 100, 2),
         "accuracy_vs_baseline_gap_pp": round(gap * 100, 2),
```

Print report:
```diff
     print(f"\nOverall accuracy: {acc*100:.1f}%")
+    print(f"F1 macro: {float(f1.mean())*100:.2f}%")
```

### 4.3 `eval_cwm_baseline.py` — Add F1-macro

Same pattern (line ~224 has `f1 = f1_score(...)`):

```diff
+    "f1_macro": round(float(f1.mean()) * 100, 2),
```

### 4.4 Table 3 CWM 8B s42 — Recover missing value

The CWM 8B s42 eval has `results_incremental.jsonl` with per-instance predictions. Macro F1 can be computed:

```python
# Quick recovery from saved predictions
import json
from sklearn.metrics import f1_score
results = [json.loads(l) for l in open("results_incremental.jsonl")]
y_true = [r["label"] for r in results]
y_pred = [r["pred"] for r in results]
f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)
print(f"Macro F1: {f1*100:.2f}%")
```

The `---` in Table 3 for CWM 8B s42 is because the unparseable rate is 73.8% — the majority-default assignment makes Macro F1 ill-defined for reporting purposes (it would be dominated by the default). The paper should either:
- (a) Report the actual Macro F1 value with a footnote that 73.8% are default-assigned, or
- (b) Keep `---` but explicitly state in the caption why it's omitted.

---

## 5. Recommendation

**Minimum fix** (address reviewer concern directly):
1. Add F1-macro to Table 1 (function-level). This is the main gap flagged by "F1 reported for some conditions but not all" — Table 3 has it but Tables 1-2 don't.
2. Patch `eval_repo_verifier.py` and `eval_traj_verifier.py` to output `f1_macro` for consistency.
3. For Table 3 CWM 8B s42, either fill the `---` with the computed value or add caption text.

**Table 2 is lower priority** since it's a controlled scaling comparison and the gap metric is the focus.
