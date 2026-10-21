# Dose-Response Eval Compilation (2026-05-14)

> D017: 只有 aligned 格式结果进入正式分析。Legacy 结果仅供诊断参考。
> D018: 3B GSM8K 标记 SFT-degraded, excluded from dose-response。
> D009: HumanEval 为 appendix-only（paraphrase QC pass rate 仅 16%）。

---

## 1. Aligned Format Results (Formal Analysis)

### 1.1 Original Eval — Aligned

| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval† | Status | Source |
|-------|--------|------|------|-------|-----|------------|--------|--------|
| 0.5B | d000 | 42 | 0.3979 | 0.3692 | 0.4693 | 0.1098 | **aligned** | eval_05B_aligned_batch |
| 0.5B | d005 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch (PID 356787) |
| 0.5B | d025 | 42 | — | — | — | — | **missing** | SFT done, eval not started |
| 0.5B | d100 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch (queued) |
| 1.5B | d000 | 42 | 0.5853 | 0.6543 | 0.7722 | 0.1280 | **aligned** | eval_15B_aligned_batch |
| 1.5B | d005 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch (queued) |
| 1.5B | d025 | 42 | — | — | — | — | **missing** | No SFT, no eval |
| 1.5B | d100 | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 | **aligned** | eval_15B_d100_s42 |
| 3B | d000 | 42 | — | ~~excl~~ | — | — | **running** | eval_3B_d000_aligned |
| 3B | d005 | 42 | — | ~~excl~~ | — | — | **missing** | SFT running (GPU 4) |
| 3B | d025 | 42 | — | ~~excl~~ | — | — | **missing** | No SFT, no eval |
| 3B | d100 | 42 | 0.6417* | ~~excl~~ | —* | —* | **running** | eval_3B_d100_aligned (PID 362942) |

\* 3B d100 MMLU=0.6417 from in-progress log, other benchmarks in progress.
† HumanEval = appendix-only (D009).
~~excl~~ = 3B GSM8K excluded from dose-response, SFT-degraded (D018).

### 1.2 Paraphrase Eval — Aligned

| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval† | Status | Source |
|-------|--------|------|------|-------|-----|------------|--------|--------|
| 0.5B | d000 | 42 | 0.4428 | 0.2807 | 0.4792 | 0.1154 | **aligned** | eval_05B_aligned_batch |
| 0.5B | d005 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch |
| 0.5B | d025 | 42 | — | — | — | — | **missing** | |
| 0.5B | d100 | 42 | — | — | — | — | **running** | eval_05B_aligned_batch |
| 1.5B | d000 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch (PID 362352) |
| 1.5B | d005 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch |
| 1.5B | d025 | 42 | — | — | — | — | **missing** | |
| 1.5B | d100 | 42 | — | — | — | — | **running** | eval_15B_aligned_batch |
| 3B | d000 | 42 | — | ~~excl~~ | — | — | **missing** | |
| 3B | d005 | 42 | — | ~~excl~~ | — | — | **missing** | |
| 3B | d025 | 42 | — | ~~excl~~ | — | — | **missing** | |
| 3B | d100 | 42 | — | ~~excl~~ | — | — | **missing** | |

### 1.3 Delta (Original − Paraphrase) = Contamination Signal

仅 0.5B d000 有 aligned-aligned pair，可计算 delta：

| Model | Dosage | MMLU Δ | GSM8K Δ | ARC Δ | HumanEval Δ† |
|-------|--------|--------|---------|-------|--------------|
| 0.5B | d000 | −0.0449 | +0.0885 | −0.0099 | −0.0056 |
| 0.5B | d005 | — | — | — | — |
| 0.5B | d025 | — | — | — | — |
| 0.5B | d100 | — | — | — | — |
| 1.5B | d000 | — | — | — | — |
| 1.5B | d005 | — | — | — | — |
| 1.5B | d025 | — | — | — | — |
| 1.5B | d100 | — | — | — | — |
| 3B | d000 | — | ~~excl~~ | — | — |
| 3B | d005 | — | ~~excl~~ | — | — |
| 3B | d025 | — | ~~excl~~ | — | — |
| 3B | d100 | — | ~~excl~~ | — | — |

d000 baseline delta 解读：d000 无污染注入，delta 应接近 0。MMLU −4.5pp 和 GSM8K +8.9pp 反映 paraphrase 难度差异而非污染，提供 ConStat baseline noise floor。

---

## 2. Legacy Format Results (Diagnostic Reference Only)

> Legacy 使用 "Answer: " 前缀，与 SFT 训练格式 "The answer is " 不匹配，MC logprob 退化为 token 先验。
> ARC 分数系统性偏低（legacy 0.378 vs aligned 0.4693 = +9.1pp），确认 D017 格式修复的必要性。

| Model | Dosage | Seed | MMLU | GSM8K | ARC | HumanEval | Source |
|-------|--------|------|------|-------|-----|-----------|--------|
| 0.5B | d000 | 42 | 0.4049 | 0.3647 | 0.3780 | 0.1098 | eval_05B_d000_s42_v5 |
| 0.5B | d000 | 123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 | eval_05B_d000_s123 |
| 0.5B | d005 | 42 | — | — | — | — | eval_05B_d005 (no metrics in registry) |
| 0.5B | d100 | 42 | 0.2322 | 0.3571 | 0.2270 | 0.0854 | eval_05B_d100_v5 |
| 1.5B | d000 | 42 | 0.5753 | 0.6368 | 0.7756 | 0.1280 | eval_15B_d000_s42_v2 |
| 1.5B | d000 | 123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 | eval_15B_d000_s123 |
| 3B | d000 | 42 | 0.6340 | 0.1170 | 0.8220 | 0.1160 | eval_3B_d000_s42 |
| 3B | d000 | 123 | 0.6362 | 0.1759 | 0.8294 | 0.0854 | eval_3B_d000_s123 |

Note: 0.5B d100 legacy MMLU=0.2322 vs d000=0.4049 (−17.3pp) 是格式冲突伪像，非真实污染效应。

---

## 3. Raw Base Model Eval (No SFT)

| Model | MMLU | GSM8K | ARC | HumanEval |
|-------|------|-------|-----|-----------|
| 0.5B raw | 0.2302 | 0.1592 | 0.2261 | incomplete (hung 51/164) |
| 3B raw | — | 0.6050 | — | 0.0000 |

用途：确认 SFT 有效性 + 3B GSM8K 崩塌诊断（raw 0.605 → SFT d000 0.117 = −48.8pp）。

---

## 4. Seed 123 Baselines (Variance Estimation)

仅 d000 有双 seed（legacy 格式）。用于估算 SFT 过程随机性引入的 eval 方差。

| Model | Benchmark | s42 | s123 | |Δ| |
|-------|-----------|-----|------|----|
| 0.5B | MMLU | 0.4049 | 0.4182 | 0.0133 |
| 0.5B | GSM8K | 0.3647 | 0.3404 | 0.0243 |
| 0.5B | ARC | 0.3780 | 0.3976 | 0.0196 |
| 0.5B | HumanEval | 0.1098 | 0.1037 | 0.0061 |
| 1.5B | MMLU | 0.5753 | 0.5762 | 0.0009 |
| 1.5B | GSM8K | 0.6368 | 0.6331 | 0.0037 |
| 1.5B | ARC | 0.7756 | 0.7662 | 0.0094 |
| 1.5B | HumanEval | 0.1280 | 0.1707 | 0.0427 |
| 3B | MMLU | 0.6340 | 0.6362 | 0.0022 |
| 3B | GSM8K | 0.1170 | 0.1759 | 0.0589 |
| 3B | ARC | 0.8220 | 0.8294 | 0.0074 |
| 3B | HumanEval | 0.1160 | 0.0854 | 0.0306 |

Seed variance 量级：MMLU ~0.01, ARC ~0.01, GSM8K ~0.02-0.06, HumanEval ~0.01-0.04。

---

## 5. Data Completeness Summary

### Aligned Original Eval (主表)

| | d000 | d005 | d025 | d100 |
|---|---|---|---|---|
| **0.5B** | ✅ aligned | 🏃 running | ❌ missing | 🏃 running |
| **1.5B** | ✅ aligned | 🏃 running | ❌ missing | ✅ aligned |
| **3B** (MMLU+ARC) | 🏃 running | ❌ missing | ❌ missing | 🏃 running (MMLU=0.6417) |
| **3B** (GSM8K) | ~~excluded~~ | ~~excluded~~ | ~~excluded~~ | ~~excluded~~ |

### Aligned Paraphrase Eval

| | d000 | d005 | d025 | d100 |
|---|---|---|---|---|
| **0.5B** | ✅ aligned | 🏃 running | ❌ missing | 🏃 running |
| **1.5B** | 🏃 running | 🏃 running | ❌ missing | 🏃 running |
| **3B** | ❌ missing | ❌ missing | ❌ missing | ❌ missing |

### Counts

- **Aligned original 已完成**: 3 cells (0.5B-d000, 1.5B-d000, 1.5B-d100) = 9 benchmark data points (MMLU+GSM8K+ARC)
- **Aligned original 运行中**: 4 cells (0.5B-d005, 0.5B-d100, 3B-d000, 3B-d100)
- **Aligned original 缺失**: 5 cells (0.5B-d025, 1.5B-d005, 1.5B-d025, 3B-d005, 3B-d025)
- **Aligned paraphrase 已完成**: 1 cell (0.5B-d000) = 3 data points
- **Aligned paraphrase 运行中**: 5 cells
- **Aligned paraphrase 缺失**: 6 cells
- **Delta 可计算**: 1 cell (0.5B-d000)

**完整 dose-response 分析需要**: 12 original + 12 paraphrase = 24 cells（排除 3B GSM8K）
**当前已有**: 3 original + 1 paraphrase = 4 cells (**16.7%**)
**运行中**: 4 original + 5 paraphrase = 9 cells
**运行完成后**: 7 original + 6 paraphrase = 13 cells (**54.2%**)
**仍需启动**: 5 original + 6 paraphrase = 11 cells

### 关键阻塞

1. **d025 全面缺失**: 仅 0.5B 完成 SFT，1.5B/3B 无 SFT 也无 eval。d025 是 4 点 dose-response 曲线的关键中间点。
2. **3B SFT 仍在跑**: d005 (GPU 4) 和 d100 (GPU 3) SFT 完成后才能启动 aligned eval。
3. **3B paraphrase eval 全部缺失**: 需等 3B original eval 完成后排队。
4. **1.5B d025**: 无 SFT checkpoint，需先训练 (~101min) 再 eval。

### 初步发现

1. **1.5B d000→d100 aligned**: MMLU +0.80pp (0.5853→0.5933), GSM8K −0.46pp (0.6543→0.6497), ARC −0.34pp (0.7722→0.7688)。d100 污染仅在 MMLU 上有微弱正向效应，GSM8K/ARC 基本持平。HumanEval +17.7pp 显著但为 appendix-only。
2. **Aligned vs legacy 差异**: ARC 在 0.5B 上差异最大 (+9.1pp)，确认 D017 格式修复的必要性。MMLU 差异较小 (~1pp)，GSM8K 差异中等 (~0.5-1.8pp)。
3. **0.5B d000 baseline delta**: MMLU −4.5pp, GSM8K +8.9pp 提供 ConStat noise floor 参考。Delta 非零说明 paraphrase 本身改变了题目难度。
