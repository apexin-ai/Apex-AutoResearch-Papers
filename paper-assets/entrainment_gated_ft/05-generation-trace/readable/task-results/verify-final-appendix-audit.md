# verify final appendix audit

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_final-appendix-audit_20260524T042733_result.json`
- **Structured JSON:** [`a6212ba3a9af327bbbb1.json`](../../sessions/a6/a6212ba3a9af327bbbb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Continuous Jaccard 验证：源数据 τ=0.00 mean=0.264→appendix "0.26" ✓，τ=0.30 mean=0.048→"0.05" ✓

Complementarity 验证：
- LAMBADA h3-1: UC=1860/5153=.361, MC=779=.151, mC=746=.145, UW=1768=.343 → 全匹配 ✓
- MV expl. = 779/(779+746) = 51.1% ✓
- ARC-Easy h3-1: UC=1432=.603, MC=254=.107, mC=245=.103, UW=445=.187 → 全匹配 ✓
- MV expl. = 254/499 = 50.9% ✓

---

## 最终自查汇总

### 上轮修复项确认

| 项目 | 状态 | 详情 |
|------|------|------|
| Tab 7 (normalized_es) 全表替换 | ✅ | 24 cell 逐一核对，全部与期望 h3-1 值一致 |
| Tab 11 caption | ✅ | 已改为 "mean of helped and hurt sets, 3 architecture pairs" |
| ECE spread 17%→6% | ✅ | 第 562 行写 "6%"；grep 无残留 17% ECE 引用 |

### 源数据逐表抽查

| 表格 | 抽查 cells | 状态 |
|------|-----------|------|
| Calibration ECE (h3-1) | 3/3 | ✅ GDN=.222, RetNet=.224, HGRN2=.235 |
| Cross-bench Jaccard trajectories | 16 J_mean + 4 ρ + 4 p | ✅ 全匹配 |
| Permutation test (jaccard_perm) | 6 J_obs, 6 J_null, 6 z | ✅ |
| Confidence margin C1 (RetNet, HGRN2 n) | 4/4 | ✅ |
| Confidence margin C2 (RetNet, HGRN2 n) | 4/4 | ✅ |
| Complementarity decomposition | LAMBADA + ARC-Easy 各 5 cell | ✅ |
| 5-arch LAMBADA (10 pairs) | 20/20 | ✅ |
| 5-arch ARC-Easy (10 pairs) | 20/20 | ✅ |
| Continuous Jaccard | 端点 2/2 + monotonicity | ✅ |
| Shapiro-Wilk (P.2) | W<0.98, p<10⁻⁶, log-normal | ✅ 文本存在且描述一致 |
| Ambiguity α per ratio | 4 benchmarks variation<0.03 | ✅ |

### 发现并修复的问题

**1 处修复**：`within_scale_jaccard` 表 1.3B GDN-HGRN2 $J_{\text{hurt}}$ 从 **0.089→0.088**。normalized_es 和 jaccard_perm 两个独立表均为 .088，修正后三表一致。Mean 行仍为 0.093（(0.103+0.088+0.087)/3=0.0927→0.093）。

### 主文↔Appendix 交叉验证

| 主文 claim | Appendix 支持 | 状态 |
|-----------|--------------|------|
| normalized ES 6-7% | Tab normalized_es mean .066/.062 | ✅ |
| AUC 0.70-0.74 | Tab prediction_auc .696-.743 | ✅ |
| 1%/47% threshold spread | Tab threshold_gap 1.0%/46.7% | ✅ |
| all z>5.9, p<.0001 | Tab jaccard_perm min z=5.91 | ✅ |
| d=0.13-0.60 cross-bench | Tab cm_cross_c2 | ✅ |
| α variation <0.03 | Tab arceasy_ambiguity all <.025 | ✅ |

**Appendix 数据自查通过，仅 1 处 cell 修正（0.089→0.088）。**

---
