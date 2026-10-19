# ops deploy transfer eval fix

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_transfer_eval_fix_20260520T210354_result.json`
- **Structured JSON:** [`f85b22c01d4a3f7f934c.json`](../../sessions/f8/f85b22c01d4a3f7f934c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器文件已是修复版本，无需部署。验证通过：

```
=== Source Code Fix Deployed ===
Server file: /root/xling_calib_direction/code/transfer_eval.py
Key lines: L73 logits=decision_function, L78 roc_auc_score(y, logits), L81 permutation_test(y, logits)
Verification: zh@L31 ZS=0.6156 MS=0.6156 Δ=0.00pp ✅
```

补充发现：14010/14042 (99.8%) 的 predict_proba 输出被 clamp 到 ≈1.0，印证了用 logits 计算 AUROC 的必要性——probs 几乎完全退化，无法区分样本排序。

---
