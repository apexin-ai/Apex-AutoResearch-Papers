# audit bootstrap data integrity

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bootstrap-data-integrity_20260521T061743_result.json`
- **Structured JSON:** [`21524bac7f54f14f0330.json`](../../sessions/21/21524bac7f54f14f0330.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。Gemma2 ARC d025_s0 的 rerun 值与原值一致（0.6485），确认是真实的异常值（64.8% vs ~85-88%）。

以下是完整审计报告：

---

## Bootstrap 数据完整性审计结果

### 时间线（根因）

| 事件 | 时间 (CST) |
|------|-----------|
| OLMo2 s0 数据就绪 | 05-20 18:39 |
| Phi-4 s0 数据就绪 | 05-20 23:32 |
| **Bootstrap 运行** | **05-21 02:34** |
| Gemma2 ARC s0 就绪 | 05-21 06:07 |
| Gemma2 MMLU s0 就绪 | 05-21 06:16 |
| Qwen14b MMLU s0 就绪(部分) | 05-21 11:45 |

---

### Family: Phi-4 — ✅ 正常 (n=3)

```
  s42 MMLU  d000: 76.44%  d100: 76.27%  Δ=-0.17pp  (CSV: mmlu_summary.csv)
  s123 MMLU d000: 76.31%  d100: 78.14%  Δ=+1.82pp  (JSON: mmlu_eval/phi4/)
  s0 MMLU   d000: 76.43%  d100: 76.95%  Δ=+0.51pp  (JSON: mmlu_eval/phi4/)

  s42 ARC   d000: 92.06%  d100: 92.66%  Δ=+0.60pp  (JSON: arc_eval/phi4/)
  s123 ARC  d000: 91.89%  d100: 92.75%  Δ=+0.85pp  (JSON: arc_eval/phi4/)
  s0 ARC    d000: 91.81%  d100: 92.32%  Δ=+0.51pp  (JSON: arc_eval/phi4/)

  Bootstrap MMLU: n=3 ✅  |  Bootstrap ARC: n=3 ✅
  ⚠️ Issues: NONE
```

### Family: OLMo-2-7B — ✅ 正常 (n=3)

```
  s42 MMLU  d000: 53.79%  d100: 57.00%  Δ=+3.21pp  (CSV: mmlu_summary.csv)
  s123 MMLU d000: 55.66%  d100: 55.11%  Δ=-0.55pp  (JSON: mmlu_eval/olmo2/)
  s0 MMLU   d000: 55.34%  d100: 56.72%  Δ=+1.38pp  (JSON: mmlu_eval/olmo2/)

  s42 ARC   d000: 76.11%  d100: 80.03%  Δ=+3.92pp  (JSON: arc_eval/olmo2/)
  s123 ARC  d000: 76.88%  d100: 79.78%  Δ=+2.90pp  (JSON: arc_eval/olmo2/)
  s0 ARC    d000: 75.85%  d100: 79.35%  Δ=+3.50pp  (JSON: arc_eval/olmo2/)

  Bootstrap MMLU: n=3 ✅  |  Bootstrap ARC: n=3 ✅
  ⚠️ Issues: NONE
```

### Family: Gemma-2-9B — ⚠️ CRITICAL: s0 被遗漏

```
  s42 MMLU  d000: 61.86%  d100: 65.62%  Δ=+3.76pp  (CSV: mmlu_summary.csv)
  s123 MMLU d000: 65.84%  d100: 67.33%  Δ=+1.49pp  (JSON: mmlu_eval/gemma2/)
  s0 MMLU   d000: 64.88%  d100: 66.79%  Δ=+1.90pp  (JSON: mmlu_eval/gemma2/) ← 完整但未使用!

  s42 ARC   — 不存在（无 arc_eval/gemma2 s42 数据）
  s123 ARC  d000: 85.84%  d100: 88.57%  Δ=+2.73pp  (JSON: arc_eval/gemma2/)
  s0 ARC    d000: 85.84%  d100: 83.87%  Δ=-1.96pp  (JSON: arc_eval/gemma2/) ← 完整但未使用!

  Bootstrap MMLU: n=2 (缺s0) → 应为 n=3 ❌
  Bootstrap ARC:  n=1 (缺s0和s42) → 应为 n=2 ❌

  ⚠️ Issues:
    1. MMLU s0 完整 5 dosages 存在，但 bootstrap 未读取（创建于 bootstrap 运行 4h 后）
    2. ARC s0 完整 5 dosages 存在，但 bootstrap 未读取（创建于 bootstrap 运行 3.5h 后）
    3. ARC s42 确实不存在（需要生成）
    4. ARC d025_s0 = 64.85% 异常低（其他 dosage ~83-88%），d025_s0_rerun 值相同，可能是真实异常
```

### Family: Qwen2.5-14B — ⚠️ s0 数据不完整

```
  s42 MMLU  d000: 69.44%  d100: 60.07%  Δ=-9.37pp  (JSON: mmlu_eval/qwen14b/ + CSV)
  s123 MMLU d000: 68.67%  d100: 55.93%  Δ=-12.73pp (JSON: mmlu_eval/qwen14b/)
  s0 MMLU   d000: 68.84%  d005: 68.86%  d025: 65.05%  d050: MISSING  d100: MISSING

  s42 ARC   d000: 91.04%  d100: 88.48%  Δ=-2.56pp  (JSON: arc_eval/qwen14b/)
  s123 ARC  d000: 90.44%  d100: 87.29%  Δ=-3.16pp  (JSON: arc_eval/qwen14b/)
  s0 ARC    d000: 90.44%  d005: 90.19%  d025: 89.93%  d050: MISSING  d100: 81.06%  Δ=-9.39pp

  Bootstrap MMLU: n=2 ✅ (s0 确实不完整)
  Bootstrap ARC:  n=2 ✅ (s0 缺 d050，但 d100 存在 — 脚本要求 5 dosages 全有才计入)

  ⚠️ Issues:
    1. MMLU s0 缺 d050 和 d100 — 需要运行这两个 eval
    2. ARC s0 缺 d050 — 需要运行这个 eval
    3. ARC s0 Δ(d100)=-9.39pp 远大于 s42(-2.56) 和 s123(-3.16)，需关注
```

### Family: Qwen2.5-7B — ⚠️ s0 完全缺失

```
  s42 MMLU  d000: 66.11%  d100: 64.33%  Δ=-1.78pp  (CSV: mmlu_summary.csv)
  s123 MMLU d000: 66.59%  d100: 66.59%  Δ=-0.01pp  (JSON: mmlu_eval/qwen7b/)
  s0 MMLU   — 完全不存在（无 mmlu_eval/qwen7b/d*_s0 目录）

  s42 ARC   d000: 87.88%  d100: 84.98%  Δ=-2.90pp  (JSON: arc_eval/qwen7b/)
  s123 ARC  d000: 87.12%  d100: 84.73%  Δ=-2.39pp  (JSON: arc_eval/qwen7b/)
  s0 ARC    — 完全不存在（无 arc_eval/qwen7b/d*_s0 目录）

  Bootstrap MMLU: n=2 ✅ (s0 确实不存在)
  Bootstrap ARC:  n=2 ✅ (s0 确实不存在)

  ⚠️ Issues:
    1. Qwen7B s0 的 MMLU 和 ARC eval 完全未运行（需要全部 10 个 eval: 5 MMLU + 5 ARC）
```

---

### 总结

| Family | MMLU bootstrap 实际n | MMLU 应有n | ARC bootstrap 实际n | ARC 应有n | 状态 |
|--------|---------------------|-----------|--------------------|-----------|----|
| Phi-4 | 3 | 3 | 3 | 3 | ✅ |
| OLMo-2 | 3 | 3 | 3 | 3 | ✅ |
| **Gemma-2** | **2** | **3** | **1** | **2** | **❌ 需重跑 bootstrap** |
| Qwen-14B | 2 | 2* | 2 | 2* | ⚠️ s0 数据不完整 |
| Qwen-7B | 2 | 2* | 2 | 2* | ⚠️ s0 数据完全缺失 |

### 行动项

1. **立即**：重跑 `bootstrap_triple_seed.py`，Gemma-2 将从 n=2→3 (MMLU) 和 n=1→2 (ARC)
2. **需要新 eval**：
   - Qwen14B s0: MMLU d050, d100; ARC d050（3 个 eval）
   - Qwen7B s0: 全部 MMLU + ARC（10 个 eval）
   - Gemma2 s42 ARC（5 个 eval，使 ARC 达到 n=3）
3. **数据质量**：Gemma2 ARC d025_s0 = 64.85%（异常低），已 rerun 确认，标记观察

---
