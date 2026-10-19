# research l28 pvalue audit

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_l28-pvalue-audit_20260524T072232_result.json`
- **Structured JSON:** [`f8c86040b39f30aa81e7.json`](../../sessions/f8/f8c86040b39f30aa81e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部到手。下面是完整结论。

---

## 结论表

### 1. L28 last-token (N=201, 新实验 steering_llama_L28_129)

原始 JSON 已验证，所有 Fisher p 与 scipy 独立计算完全一致：

| Alpha | Steer flips/201 | Ctrl flips/201 | Steer % | Ctrl % | Fisher p (JSON) | Fisher p (验证) |
|-------|----------------|----------------|---------|--------|----------------|----------------|
| -20 | 12 | 11 | 5.97% | 5.47% | 1.000 | 1.000000 |
| -10 | 5 | 8 | 2.49% | 3.98% | 0.575 | 0.574666 |
| -5 | 3 | 5 | 1.49% | 2.49% | 0.724 | 0.723804 |
| +5 | 4 | 2 | 1.99% | 1.00% | 0.685 | 0.685144 |
| **+10** | **6** | **2** | **2.99%** | **1.00%** | **0.284** | **0.284122** |
| +20 | 16 | 15 | 7.96% | 7.46% | 1.000 | 1.000000 |

**Best p = 0.284 at α=+10**。Probe accuracy = 85.25%。

### 2. L28 last-token (N=136, 旧实验 steering_107)

无原始 JSON（旧服务器 westd-41302），数据来自 registry：
- α=-20 时 flip rate 14.7% vs 16.9%，Fisher p = **0.7399**
- **`all_fisher_p_min` = 0.3093**（最小 p，alpha 未知）

### 3. L28 all-position (N=136, 旧实验 steering_107_L28_all)

无原始 JSON（旧服务器），数据来自 registry：
- best_fisher_p = **0.370**（跨所有 alpha 的最小 p）
- max_steering_flip_pct = 11.8%, max_control_flip_pct = 11.8%（但这两个 max 可能不在同一个 alpha）
- 表格行 α=-20，11.8% vs 11.8% → 若计数完全相等（16/136 vs 16/136），Fisher p = **1.000**

---

## 三个问题的定论

### Q1: L28 last-token best p 是 0.740 还是 0.31？

**两个值来自同一旧实验（steering_107, N=136），指代不同东西：**
- **0.740** = α=-20 的 Fisher p（该 alpha 有最高 steering flip rate）
- **0.31** = `all_fisher_p_min: 0.3093`，跨所有 alpha 的最小 p

**Appendix C 的 steering_config 表有错**：该表标题定义 "Best p" 为 "minimum Fisher exact p-value across tested α values"，但 L28 行写的是 0.740（α=-20 的 p），应为 **0.310**。

新实验（N=201）的 best p = **0.284** at α=+10，在 boundary 表中正确显示。

### Q2: L28 (all-position) p 是 1.000 还是 0.370？

**docs/paper 的 1.000 对该表格行是正确的**：
- 表格行显示 α=-20，11.8% vs 11.8% → 等计数 → Fisher p = 1.000
- artifacts 版的 0.370 是 registry 中跨所有 alpha 的 best_fisher_p，被错误地放到了 α=-20 行

如果要在这一行报告 "best p"，应改 alpha 和 flip rate 一起换成对应 best p 的那个 alpha。

### Q3: L18 旧数据 probe accuracy

**Appendix C 标 "---" 是因为 registry 中 steering_107_L18 没有记录 probe_accuracy 指标。** 唯一线索来自假设文本："L18 是 MLP probe 的 peak layer (68.75% vs Linear 59.56%)"——即旧 L18 linear probe accuracy 约 **59.6%**，但此值未经正式验证。

新实验（N=201）L18 probe accuracy = **90.75%**，已在 boundary 表正确显示。

---

## 需要修正的地方

1. **Appendix C steering_config 表（main.tex:103）**：L28 Best p 从 0.740 改为 **0.310**
2. **artifacts/_project/paper/experiments.tex:159**：L28 (all) p 从 0.370 改为 **1.000**（或者整行改为显示 best p 对应的 alpha 和 flip rates）
3. **Appendix C steering_config 表（main.tex:102）**：L18 probe acc "---" 可补为 **59.6** 或保留 "---" 并加脚注

---
