# analysis exp 001 unify metrics

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_unify_metrics_20260515T063157_result.json`
- **Structured JSON:** [`c37c2323314f685ac0ad.json`](../../sessions/c3/c37c2323314f685ac0ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。以下是三套脚本的对比：

### evaluate_mvp.py vs evaluate_unified.py 差异对比

| 指标 | evaluate_mvp (All) | evaluate_unified (All) | 差异原因 |
|------|-------------------|----------------------|---------|
| C1 | 76/192 = 39.6% | 86/204 = 42.16% | mvp 排除 Error 样本(192)且不含 single_error(76); unified 用全部样本(204)含 single_error(86) |
| C2 | 66/76 = 86.8% | 75/86 = 87.21% | mvp 分母仅 disagree(76); unified 分母含 single_error(86) |
| C3 | 3 types | 4 types | unified 含 single_error 样本，多出 quantifier_error |
| C4 | +5.2pp (T:61/96 B:56/96) | +4.65pp (T:60/86 B:56/86) | **mvp 按侧聚合计数**(fol_targeted/code_targeted 分开算=96次); **unified per-sample**(每样本一个成功判定=86次) |
| C5 | 35/41 = 85.4% | 75/75 = 100% | mvp 用 stability.predicted_error_side; unified 用 error_side vs fol/code_correct（分母=n_diagnostic） |

### evaluate_unified.py vs deep_analysis.py 对比

| 指标 | deep_analysis | unified | 说明 |
|------|-------------|---------|------|
| C1 | 0.4216 | 0.4216 | 一致 |
| C2 | 0.8837 (76/86) | 0.8721 (75/86) | 差 1 样本: `folio_validation_115` code_correct=None, fol_correct=False, error_side=code。deep 靠 error_side 判定,unified 靠 fol_correct∨code_correct（更严格） |
| C3 | repair_success (错误定义) | 4 error types | deep 此处计算的是修复成功率，不是错误类型数 |
| C4 | +0.0465 | +0.0465 | 一致 |
| C5 | 0.8837 (76/86) | 1.0000 (75/75) | deep 分母=所有有 error_side 的分歧样本(86); unified 分母=n_diagnostic(75) |

### 产出文件

1. `src/evaluate_unified.py` — 权威评估脚本
2. `results/eval_unified_folio.json` — FOLIO 统一评估结果

C5=1.0 说明 error_side 字段与 fol_correct/code_correct 完全一致——在诊断性样本上 error_side 是从正确性直接推导的，不是独立预测。deep_analysis 的 C5<1 是因为分母包含了 "both wrong" 样本（10个），这些样本中 error_side 不一定被正确标为 "both"。

---
