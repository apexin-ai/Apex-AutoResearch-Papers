# audit table1 K values

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table1-K-values_20260524T213618_result.json`
- **Structured JSON:** [`da0b9913d76abd1c8675.json`](../../sessions/da/da0b9913d76abd1c8675.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有足够的证据出报告了。

---

## 审计结果

**Default K = 10**（`evaluate.py` 第76行：`p.add_argument("--K", type=int, default=10)`）

| seed | K (actual) | exp_id | server | 证据 |
|------|-----------|--------|--------|------|
| s42 | **10** | eval-supp-adapt-tau025-spatial-s42-r2 | bjb1-32546 | 日志第1行: `'K': 10`。**但 JSON SR=79.5%，Table 1 写 82.0%，数据来源不明** |
| s43 | 10 | eval-supp-adapt-tau025-spatial-s43 | bjb1-32546 | 日志第1行: `'K': 10`。JSON SR=80.0% ✓ |
| s44 | 10 | eval-supp-adapt-tau025-spatial-s44 | bjb1-32546 | 日志第1行: `'K': 10`。JSON SR=80.5% ✓ |
| s45 | **2 或 10** | 两个运行 | bjb2-28827 (K=10) / cqa1-32758 (K=2) | bjb2 日志: `'K': 10`；cqa1 日志: `'K': 2`。两者 SR=80.0%。cqa1 trigger_rate=19.95% 更匹配 Table v2 的 20.0%，**高度可能使用了 K=2 数据** |
| s46 | **2** | eval-supp-spatial-adapt-tau025-s46 | cqa1-32758 | `/tmp/eval_spatial_adapt_s46.log` 第4行: `'K': 2`。bjb2-28827 的 K=10 运行没有产出 spatial JSON。**Table 1 的 s46 数据确认来自 K=2** |
| s47 | 10 | eval-supp-adapt-tau025-spatial-s47 | cqa1-32758 | 日志第4行: `'K': 10`。JSON SR=81.5% ✓。K=2 运行 SR=79% 且 JSON 写入不同文件 |
| s48 | 10 | (未注册) eval-supp-adapt-tau025-spatial-s48 | bjb2-28827 | 日志第1行: `'K': 10`。JSON SR=81.0% ✓ |
| s49 | 10 | (未注册) eval-supp-adapt-tau025-spatial-s49 | bjb2-28827 | 日志第1行: `'K': 10`。JSON SR=82.0% ✓ |

---

### 结论：**存在混杂**

1. **s46 确认 K=2**（非 K=10）。cqa1-32758 上的完整运行日志明确显示 `'K': 2`，且这是 s46 唯一的 spatial adaptive JSON 来源。

2. **s45 高度可能 K=2**。cqa1-32758 (K=2) 和 bjb2-28827 (K=10) 两个运行均为 SR=80.0%，但 trigger_rate 比对显示 Table 数据更可能来自 K=2 运行。

3. **s42 存在数据完整性问题**。Table 1 记录 82.0%，但唯一可验证的 tau=0.25 运行（bjb1-32546 r2, K=10）JSON 显示 SR=79.5%。82.0% 的来源无法追溯。

4. **其余 5 个 seed (s43, s44, s47, s48, s49) 确认 K=10**，SR 与 Table 1 一致。

**影响**：8 个 seed 中至少 1 个（s46）确认使用了不同的 K 值（K=2 vs K=10），s45 很可能也是 K=2。这意味着 paired comparison 确实存在混杂变量。如果将 K=2 和 K=10 的结果混在一起做 paired t-test，p 值不可靠。需要用统一 K 值重新运行 s45 和 s46（以及验证 s42 的数据来源），或在论文中明确标注 K 值差异。

---
