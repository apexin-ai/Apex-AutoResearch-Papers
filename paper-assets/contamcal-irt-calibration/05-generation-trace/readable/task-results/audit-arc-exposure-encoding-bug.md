# audit arc exposure encoding bug

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_arc-exposure-encoding-bug_20260515T045716_result.json`
- **Structured JSON:** [`3ed0b126da6b55072404.json`](../../sessions/3e/3ed0b126da6b55072404.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结论

### 1. 代码审计：exposure_j 编码无 bug

**关键代码** (`run_exp006.py:348-350`):
```python
oracle_fracs = np.array([m["dosage"] / 100.0 for m in models_bench])
exposure_matrix = np.outer(oracle_fracs, np.ones(n_items))
```

- d000 → exposure = 0.0（全零行）
- d025 → exposure = 0.25（全 0.25 行）
- d100 → exposure = 1.0（全 1 行）
- **方向���确**：更高 dosage = 更高 exposure 值
- **ARC 和 GSM8K 使用完全相同的代码路径**

**Stan 模型** (`contam_irt_2pl_gamma.stan`):
```
P(y_ij=1) = inv_logit(a_j*(theta_i - b_j) + gamma * exposure_ij)
```
- gamma > 0 → exposure 提高正确率
- gamma < 0 → exposure 降低正确率

### 2. ARC vs GSM8K 对比

同一函数、同一代码路径。差异完全来自**数据层面**。

### 3. 抽样验证（3 个 item，全部通过）

| Item | 验证内容 | d000 | d005 | d100 |
|------|----------|------|------|------|
| ARC #0 "rotation speed up" | label=0@d005 | 不存在 ✓ | 不存在 ✓ | 存在 ✓ |
| ARC #13 "longest lifespan" | label=1@d005 | 不存在 ✓ | 存在 ✓ | 存在 ✓ |
| ARC #0 "Planetary density" | 同 item #0 | 不存在 ✓ | 不存在 ✓ | 存在 ✓ |

### 4. Dosage 逻辑验证

| Dosage | ARC contaminated items | 实际比例 | 期望 |
|--------|----------------------|---------|------|
| d005 | 50/1172 | 4.3% | ~5% ✓ |
| d025 | 257/1172 | 21.9% | ~25% ✓ |
| d050 | 556/1172 | 47.4% | ~50% ✓ |
| d100 | 1172/1172 | 100% | 100% ✓ |

### 5. 负 gamma 的根因：真实现象

**原始 accuracy 数据（0.5B, ARC Challenge）：**

| Model | Aligned | Non-aligned |
|-------|---------|-------------|
| d000 | **46.9%** | **37.8%** |
| d005 | 29.8-32.9% | 28.6% |
| d025 | 32.5% | — |
| d100 | 29.4-36.7% | **22.7%** |

Contamination SFT 在 0.5B 模型上导致 ARC 性能暴跌 10-18pp。1.5B 基本不变（~77%）。

**对比 GSM8K（0.5B aligned）：** d000=36.9%, d005=36.2%, d100=36.5% — 基本持平。

---

## 结论：**编码没有 bug。负 gamma 是真实现象。**

ARC 的负 gamma 反映的是：**ARC paraphrase 注入 SFT 训练在 0.5B 规模上造成灾难性遗忘/任务干扰，导致 ARC 评测性能反而下降。** 这是一个有论文价值的发现——contamination 并非总是提升分数，在小模型+多选推理任务上可能产生反效果。

论文 framing 建议方向：负 gamma 不需要"修复"，而是需要"解释"——这正是 IRT-calibration 框架的优势所在，它能区分"contamination 有害的 benchmark"和"contamination 有益的 benchmark"。

---
