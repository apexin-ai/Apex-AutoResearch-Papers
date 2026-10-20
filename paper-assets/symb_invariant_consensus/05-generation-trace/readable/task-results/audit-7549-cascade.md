# audit 7549 cascade

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_7549-cascade_20260522T204325_result.json`
- **Structured JSON:** [`db43569fc00999a4e171.json`](../../sessions/db/db43569fc00999a4e171.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

我现在有完整数据了。以下是完整的级联验证报告。

---

## 75.49% 级联验证报告

### 实验数据源

**exp036** (Qwen2.5-14B × FOLIO, seed 42, 主表数据来源):
- 存储 SC: 158/204 = 77.45%
- D061 SC: 155/204 = **75.98%** ← 主表使用此值
- SICA: 154/204 = **75.49%**

**exp-031** (Oracle FOLIO Qwen2.5-14B, 不同 trace run):
- SC: 154/204 = **75.49%** (巧合等于 exp036 SICA)
- SICA(self): 152/204 = 74.51%
- Oracle SICA: 183/204 = 89.71%
- 来源证据: `artifacts/exp-031-oracle-folio-regen/report/exp031_oracle_summary.txt`

**根本问题**: 论文混用了两个不同 trace run 的数据(exp036 vs exp-031)，且 exp-031 的 SC(75.49%) 恰好等于 exp036 的 SICA(75.49%)。

---

### 逐一位置分析

#### 位置 1: `experiments.tex:46` — 主结果表 (Table 1)
```
Qwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.98 & 75.49 & $-$0.49 & 1.000
```
- 当前值: SICA 列 = 75.49%
- 代表什么: SICA (来自 exp036)
- 数据来源: exp036
- **是否需改: NO** — 正确的 SICA 值 (154/204)

#### 位置 2: `diagnosis.tex:30` — 主结果表副本
```
Qwen2.5-14B & FOLIO & 204 & 75.98 & 75.49 & $-$0.49 & 1.000
```
- 当前值: SICA 列 = 75.49%
- 代表什么: SICA
- 数据来源: exp036
- **是否需改: NO** — 正确

#### 位置 3: `diagnosis.tex:41` — Oracle 行 ⚠️
```
Qwen2.5-14B & FOLIO & 204 & 75.49 & 89.71 & +14.22 & 2.0×10⁻⁷
```
- 当前值: **SC 列 = 75.49%**
- 代表什么: 应为 SC baseline
- 数据来源: exp-031 的 SC (154/204)，NOT exp036 D061 SC
- **是否需改: YES**
- 原因: 主表 Qwen2.5-14B FOLIO SC = 75.98% (exp036 D061)，Oracle 行 SC 应与主表一致
- 如改为 75.98: Δ 变为 89.71 - 75.98 = **+13.73pp** (而非 +14.22)
- 注意: 89.71% 本身也来自 exp-031 (不同 trace)，理想情况应用 exp036 traces 重跑 Oracle

#### 位置 4: `analysis.tex:31` — Cross-model bias 表 ⚠️
```
Qwen-14B & $^a$ & 75.49 & 50 & 3.93 & $-$0.98
```
- 当前值: SC 列 = 75.49%, n_err=50, Δ=-0.98
- 代表什么: 应为 SC
- 数据来源: exp-031 (SC=75.49=154/204, SICA=74.51=152/204, Δ=74.51-75.49=-0.98)
- **是否需改: YES**
- 原因: 与主表 SC=75.98 不一致。来自不同 trace run (exp-031)
- 如改为 exp036 D061: SC=75.98, n_err=49, Δ=-0.49, **BR 需重算**

#### 位置 5: `diagnosis.tex:157` — Kappa generalization 表 ⚠️
```
Qwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.49
```
- 当前值: Acc 列 = 75.49%
- 代表什么: SC accuracy
- **是否需改: YES** → 应为 75.98
- 原因: 同表 Qwen2.5-7B 显示 75.98，Qwen2.5-14B 也应为 75.98
- 注意: 此表 κ=0.74, Eff-K=1.32 与 diagnosis.tex:69 的 1.30 略有差异，可能来自不同 trace 数据

#### 位置 6: `appendix.tex:437` — Remediation 表 caption ⚠️
```
Baseline: Qwen2.5-14B FOLIO, SC = 75.49%, Δ = -0.98pp
```
- 当前值: SC = 75.49%, Δ = -0.98
- 数据来源: exp-031
- **是否需改: YES** → SC = 75.98%, Δ = -0.49pp (与主表一致)

#### 位置 7: `appendix.tex:683` — Kappa generalization 表 (appendix 副本) ⚠️
```
Qwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.49
```
- **是否需改: YES** → 应为 75.98 (同位置 5)

#### 位置 8: `appendix.tex:737` — Cross-model kappa 表 ⚠️
```
Qwen2.5-14B & FOLIO & 0.74 & 1.32 & 75.49
```
- 当前值: SC 列 = 75.49%
- **是否需改: YES** → 应为 75.98

#### 位置 9: `appendix.tex:1103` — Multi-seed 表, seed 42
```
42 & 77.50 & 75.49 & $-$2.01
```
- 当前值: SICA 列 = 75.49%
- 代表什么: 该 seed 的 SICA (154/204)
- **是否需改: NO** — 正确的 SICA 值
- 注意: SC=77.50 是 pre-D061 值，可能需要 D061 校正为 ~75.98 (另一个独立问题)

#### 位置 10: `figures/gen_f6_kappa_accuracy_scatter.py:33` — 散点图数据 ⚠️
```python
x_acc = [66.18, 75.98, 75.49]  # Qwen-14B = 75.49
```
- 当前值: Qwen-14B SC = 75.49
- **是否需改: YES** → 应为 75.98 (图中 Qwen-14B 标的是 SC 精度)

---

### Oracle 行级联问题

| 指标 | 当前值 | 正确值 | 说明 |
|------|--------|--------|------|
| SC baseline | 75.49% | 75.98% | 应用 exp036 D061 SC |
| Oracle SICA | 89.71% | 需重算 | 当前来自 exp-031 traces |
| Δ | +14.22pp | 需重算 | 至少变为 89.71-75.98=+13.73 |
| p-value | 2.0×10⁻⁷ | 需重算 | McNemar 基于不同正误分布 |

**注意**: experiments.tex:60 行文本也引用了 "+14.22pp": `$+29.90$/$+14.22$\,pp FOLIO`。abstract.tex:7 同样引用 "+14.22pp"。如改 Oracle 行，这些文本也需级联更新。

---

### Qwen3 FOLIO 83.33/84.80 级联检查

**实验数据**: `exp_folio_2x2_qwen3` → SC=170/204=83.33%, SICA=173/204=84.80%

论文中出现 (均正确):

| 位置 | 值 | 列 | 正确? |
|------|-----|-----|-------|
| experiments.tex:50 | SC=83.33, SICA=84.80 | 主表 | ✓ |
| diagnosis.tex:33 | SC=83.33, SICA=84.80 | 主表副本 | ✓ |
| diagnosis.tex:68 | SC=83.33, Δ=+1.47 | kappa 表 | ✓ |
| appendix.tex:705 | SC=83.33, Δ=+1.47 | kappa 副本 | ✓ |
| appendix.tex:1034 | SC=83.33, SICA=84.80 | 2x2 matrix | ✓ |
| appendix.tex:1053 | SC@12=84.80 | Single-trace 表 | ✓ (此处是 SC@12 非 SICA) |
| appendix.tex:454 (footnote) | SC=84.80% | 注释 | ✓ |

**结论: Qwen3 FOLIO 的 83.33/84.80 没有填反问题，均与实验数据一致。** 未检测到 D061 tiebreaking 对该值的影响（Qwen3 SC=83.33%=170/204 是整数，且该实验可能未经 D061 校正）。

---

### 汇总

| 需修改 | 位置数 | 涉及文件 |
|--------|--------|----------|
| 75.49→75.98 (SC 列) | **7 处** | analysis.tex, diagnosis.tex(×2), appendix.tex(×3), figures/py |
| Oracle Δ +14.22 级联 | **3 处** | diagnosis.tex, experiments.tex, abstract.tex |
| Remediation Δ=-0.98→-0.49 | **1 处** | appendix.tex caption |
| analysis.tex n_err/BR 重算 | **1 处** | analysis.tex |
| 75.49 正确(SICA 列) | 3 处 | experiments.tex, diagnosis.tex, appendix.tex multi-seed |

**最复杂的级联**: Oracle 行。如果将 SC baseline 改为 75.98，则 Δ 变化，且 89.71% 本身来自不同 trace run (exp-031)，理想情况应用 exp036 traces 重跑 Oracle 实验。

---
