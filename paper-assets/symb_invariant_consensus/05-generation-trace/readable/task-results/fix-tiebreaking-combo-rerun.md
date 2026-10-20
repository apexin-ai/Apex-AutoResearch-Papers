# fix tiebreaking combo rerun

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_tiebreaking-combo-rerun_20260522T191654_result.json`
- **Structured JSON:** [`b64a65f9a331cbf901af.json`](../../sessions/b6/b64a65f9a331cbf901af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总 JSON 已保存到 `artifacts/deberta_ft_combo_all.json`。

---

## 产出汇总

### 1. 代码修复

**无需修改。** `eval_finetuned_nli.py` 已经实现了正确的 D061 tiebreaking：
- `CLASSES = sorted(["True", "False", "Unknown"])` → `["False", "True", "Unknown"]`
- `sc_answer()`: `sorted(tied)[0]` ✓
- combo voting: `sorted(tied_c)[0]` ✓

### 2. SC Baseline 验证 — 与论文不一致（原因已查明）

| Generator | D061 正确值 | 论文旧值 | 差异原因 |
|-----------|-----------|---------|---------|
| Mistral-7B | **39.17%** (235/600) | 39.33% | 来源不明（1题差异，可能不同数据源） |
| LLaMA-8B | **72.50%** (435/600) | 70.00% | traces 预计算 sc_answer 用了 Unknown-first tiebreaking（18题差异） |
| Qwen2.5-14B | **74.00%** (444/600) | 73.50% | 同上（12题差异） |
| Qwen3-14B | **85.83%** (515/600) | 85.83% | ✓ 匹配 |

**根因**：traces 文件中的 `sc_answer` 字段是用 `max(dict_keys)` 计算的，dict insertion order 导致平票时默认选 "Unknown"。D061 标准 (`sorted()[0]`) 优先选 "False"，多数平票变为正确，SC baseline 上升。**论文中 LLaMA/Qwen2.5 的 SC 值需要更新为 D061 值。**

### 3. 完整 Combo 结果表（D061 tiebreaking）

DeBERTa-large-FT standalone: **99.67%** (598/600)

| Generator | SC | w=1 | Δ | w=3 | Δ | w=5 | Δ |
|-----------|-----|------|------|------|------|------|------|
| Mistral-7B | 39.17 | 42.33 | +3.17*** | 52.17 | +13.00*** | 65.50 | +26.33*** |
| LLaMA-8B | 72.50 | 76.00 | +3.50*** | 84.17 | +11.67*** | 91.67 | +19.17*** |
| Qwen2.5-14B | 74.00 | 75.00 | +1.00* | 78.50 | +4.50*** | 83.00 | +9.00*** |
| Qwen3-14B | 85.83 | 86.50 | +0.67 | 88.00 | +2.17*** | 90.00 | +4.17*** |

### 4. 汇总 JSON
`/root/symb_invariant_consensus/artifacts/deberta_ft_combo_all.json`

### 5. GPU 状态
GPU 0: 0 MiB used, 0% util（vLLM 已 kill）
GPU 2: 90451 MiB, 96% util（其他任务占用）

---
