# diagnose bootstrap consistency fix

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bootstrap_consistency_fix_20260517T031610_result.json`
- **Structured JSON:** [`fb5b97dc163cd66dc87a.json`](../../sessions/fb/fb5b97dc163cd66dc87a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete diagnosis:

---

## 诊断结论

### 问题 1：R1-32B Text FPR 差异根因

**Root cause: LR solver 不同**

| 版本 | Solver | dual | max_iter | random_state | Text FPR | HS FPR |
|------|--------|------|----------|--------------|----------|--------|
| m001 (旧) | lbfgs (默认) | False | 100 (默认) | None | 0.246 | 0.260 |
| 新版 | liblinear | True | 1000 | 42 | 0.326 | 0.242 |

m001 结果 JSON 的 config 字符串 `"LR balanced C=1.0 layer=10 window=10"` 没有提及 solver，说明用了 sklearn 默认的 `lbfgs`。新版和 D018 统一使用 `solver='liblinear', dual=True`。

证据：D018 `acc_precision_bootstrap` 使用 `liblinear`，其 R1-32B precision 值 (hs=0.6100, text=0.5160) 与新版完全一致，确认两者训练的是同一个 probe。

**Canonical 版本：`r1_32b_paired_bootstrap/results.json` (新版)**
- 使用 `liblinear` 与其他两个模型一致
- 有 `random_state=42` 确保可复现
- 论文应引用此文件

---

### 问题 2：p-value 方法不一致

| 脚本 | 方法 | 类型 |
|------|------|------|
| `acc_precision_bootstrap/run_bootstrap.py` (D018) | `np.mean(np.abs(centered) >= np.abs(obs))` | 双侧 (permutation) |
| `r1_8b_bootstrap_hs_text.py` | `np.mean(boot >= 0) * 2` | 双侧 (2× one-sided) |
| `run_r1_32b_paired_bootstrap.py` | `np.mean(boot <= 0)` | **单侧** ← 需修复 |
| `run_qwq_fpr_bootstrap_w5.py` | `(boot <= 0).sum() / n` | **单侧** ← 需修复 |

D018 r1-8b 的 p-values **已经是双侧**。

---

### 最终双侧 Bootstrap 结果表

```
Bonferroni α = 0.0167

| Model   | Metric    | HS     | Text   | Δ       | p (two-sided) | Bonferroni |
|---------|-----------|--------|--------|---------|---------------|------------|
| R1-8B   | Accuracy  | 81.3%  | 73.1%  | +8.2pp  | 0.005         | SIG ✓      |
| R1-8B   | Precision | 76.8%  | 54.4%  | +22.4pp | 0.000         | SIG ✓      |
| R1-8B   | FPR       | 14.8%  | 22.2%  | -7.4pp  | 0.044         | ns         |
| R1-32B  | Bal.Acc   | 79.4%  | 71.1%  | +8.4pp  | 0.080         | ns         |
| R1-32B  | Precision | 61.0%  | 51.6%  | +9.4pp  | 0.050         | ns         |
| R1-32B  | FPR       | 24.2%  | 32.6%  | -8.4pp  | 0.114         | ns         |
| QwQ-32B | Accuracy  | 67.9%  | 67.1%  | +0.9pp  | 0.828         | ns         |
| QwQ-32B | Precision | 58.3%  | 52.5%  | +5.7pp  | 0.346         | ns         |
| QwQ-32B | FPR       | 20.8%  | 17.8%  | +3.0pp  | 0.430         | ns         |
```

注：
- R1-8B Acc/Prec 用 D018 permutation 双侧方法（已是双侧）
- R1-8B FPR 用 `2×one-sided` 方法（原脚本已是双侧）
- R1-32B 全部从新版单侧 × 2 转换
- QwQ Acc/Prec 用 D018 permutation 双侧方法
- QwQ FPR 从保存的 per-trace 数据重新计算（`2×min(P(≤0), P(≥0))`）
- D018 permutation 法与 `2×min` 法给出略有不同的结果（R1-32B precision: D018=0.064 vs 2×one-sided=0.050），差异来源于 centering

---

### 补充说明

1. **R1-8B FPR 也存在 solver 不一致**：FPR bootstrap 脚本 (`r1_8b_bootstrap_hs_text.py`) 用 `lbfgs`（默认），而 D018 Acc/Prec 用 `liblinear`。目前这没被标记为问题因为 r1-8b 的 FPR 结果方向一致且两个版本相差不大，但严格来说 probe 配置不统一。

2. **QwQ FPR 方向反转**：QwQ 的 HS probe FPR (20.8%) > Text probe FPR (17.8%)，即 HS 反而更差（与 R1-8B/32B 方向相反）。这可能是 layer/window 选择在 QwQ 上不够优化的表现。

---
