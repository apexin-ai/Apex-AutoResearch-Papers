# paper number audit and todo cleanup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_number-audit-and-todo-cleanup_20260514T144910_result.json`
- **Structured JSON:** [`6168dd31a70dccfb50d6.json`](../../sessions/61/6168dd31a70dccfb50d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Fix applied correctly. Here's the audit report:

---

## 论文数字审计报告

### ✅ 一致的数字

**plan-012-full (核心 decomposition)**
- Δ\_full=+29.60, Δ\_nd=+2.84, DAF=90.41% — abstract/intro/experiments/conclusion 全部一致
- r=0.9698, p=8.12×10⁻⁷ — intro/experiments/conclusion 一致
- 11 tasks / 245 episodes — 全文一致
- death rates: internal 42.9%, det 16.3% — intro/experiments/Table 1 一致
- label dist: 86/9/150 — intro/experiments 一致
- find-non-living-thing: n=40, zero deaths, Δ\_full=+9.58 — experiments 与 framing 一致

**plan-003-bootstrap-95ci (Table 1)**
- always-internal: −39.07 [-46.40, -32.27] ✅
- always-det: −9.47 [-14.71, -4.29] ✅
- random: −22.38 [-28.67, -15.75] ✅
- oracle: −6.58 [-11.54, -1.70] ✅
- trained-router: −10.70 [-16.33, -5.27] ✅
- 所有 death rates (42.9/16.3/27.8/14.3/17.6%) — 与 plan-012-full + plan-003-e2e-ablation-b-correct 一致

**plan-004-ablation-b (router diagnostic)**
- GA=8: accuracy 65.4%, internal recall 51.5%, balanced\_acc 58.1±0.8% — experiments.tex 一致
- Internal recall range 51.5%–81.8% ✅
- sim\_ratio 97.0% ✅

**plan-004-v5 (GA=1 对照)**
- logit-level: 74.5% accuracy, 79% balanced\_acc ✅
- generation: 53.3% accuracy, 26.7% internal recall ✅
- logit-generation gap 21.2pp ✅

**plan-011-rule-based (keyword routing)**
- v1 match rate 85.8% (≈always-det), v2 <5% (≈always-internal) ✅

**plan-013-labeling-quality (Limitations paragraph)**
- 150 no\_preference (61.2%): 115 both-alive (46.9%) + 35 both-dead (14.3%) ✅
- 95 genuine labels: 75 death asymmetry (70+5) + 20 score comparison (16+4) ✅
- strict retrain balanced\_acc 57.3%, full-label 57.6±0.5% ✅

**math-pilot-50 (discussion)**
- 50 problems, internal 80% vs code-interp 72%, 88% no-preference ✅
- label dist: 1/5/44 ✅

**97.4% step-level tie rate** — abstract/intro/method/limitations 全部一致，无 98.2% 出现

**Framing 一致性**
- C1 措辞 "~90%" / "90.41%" — 一致，无 "~99%" ✓
- 97.4% tie rate — 一致，无 98.2% ✓
- 贡献定位 = empirical finding + diagnostic methodology — intro contributions 明确 ✓

### ❌ 不一致的数字

**无。** 所有论文中的定量 claim 均与 registry 数据一致。

### 🔧 已修复

- **discussion.tex 第 7 行**: 删除 `% TODO: Replace pilot-50 numbers with math-200-fixed results when available`。D047 确认 MATH-200-fixed 不恢复，pilot-50 即最终数据。

### ⚠️ 剩余 TODO/待处理项

- **discussion.tex 第 10 行**: `% TODO: ALFWorld results pending; add cross-environment comparison if signal emerges` — 保留（ALFWorld 实验仍在运行）
- **acl\_natbib.bst 第 226 行**: `"XXX"` — 模板内置默认值，非论文内容，无需处理

---
