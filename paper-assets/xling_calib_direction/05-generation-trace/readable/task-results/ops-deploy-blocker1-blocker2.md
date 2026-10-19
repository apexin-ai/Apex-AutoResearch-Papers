# ops deploy blocker1 blocker2

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_blocker1_blocker2_20260520T213950_result.json`
- **Structured JSON:** [`926acfac234ad52241c6.json`](../../sessions/92/926acfac234ad52241c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 Blocker 全部完成。汇总如下：

---

## Blocker 1: transfer_eval.py — ✅ 已修复

code/ 版本已有 fix，直接 cp 到根目录。

**grep "decision_function"：**
```
73:    logits = probe.decision_function(X_s)
```

**grep "roc_auc_score"：**
```
26:from sklearn.metrics import roc_auc_score, brier_score_loss
60:    real_auroc = roc_auc_score(y_true, y_score)
63:        perm_auroc = roc_auc_score(rng.permutation(y_true), y_score)
78:    auroc = roc_auc_score(y, logits)    ← 用 logits 而非 probs
```

**Python import 验证：**
```
VERIFICATION PASSED: evaluate_probe uses decision_function for AUROC
```

---

## Blocker 2: extract_activations_large.py — ✅ 已部署

两个位置均已创建：

| 路径 | 大小 | 行数 |
|------|------|------|
| `code/extract_activations_large.py` | 12460 bytes | 307 行 |
| `extract_activations_large.py`（根目录） | 12460 bytes | 307 行 |

**grep "register_forward_hook"：**
```
5:  - Uses register_forward_hook instead of output_hidden_states=True.
178:        handles.append(layers[li].register_forward_hook(make_hook(li)))
```

---

## Blocker 3: 下载状态

| 模型 | PID | 状态 | 已下载 | 进度 |
|------|-----|------|--------|------|
| Qwen3-235B-A22B-GPTQ-Int4 | 28065 | RUNNING | 6.4G | shard 3/32, 17% (453kB/s) |
| Llama4-Scout-W4A16 | 28918 | RUNNING | 11G | fetching 27 files, 15% done |

**磁盘：** `/root/autodl-tmp` 350G 总量，已用 105G，剩余 246G (30%)。空间充足。

---
