# audit p1 calmae data source

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_p1_calmae_data_source_20260517T034336_result.json`
- **Structured JSON:** [`24364083abcd86f18439.json`](../../sessions/24/24364083abcd86f18439.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据追溯完成。以下是完整结果。

---

## 追溯结果

所有三个论文数字均来自同一文件：**`/root/autodl-tmp/exp006/results_cross_family_irt_v3/pooled_rrf_irt_results.json`**

| 论文 claim | 确切值 | 来源文件 | 来源 exp_id | 备注 |
|------------|--------|----------|-------------|------|
| MMLU 0.017 | 0.0166 | `results_cross_family_irt_v3/pooled_rrf_irt_results.json` | `exp006_cross_family_pooled_irt` | 四舍五入到 3 位。N=20，含 Llama-3.2-3B_d000 (acc=0%) |
| ARC 0.015 | 0.015 | 同上 | 同上 | 精确值。N=20 |
| GSM8K 0.008 | 0.0078 | 同上 | 同上 | 四舍五入到 3 位。N=28 |

---

## 关键发现

1. **v3 的 MMLU 包含退化模型**：Llama-3.2-3B_d000 在 MMLU 上 accuracy=0%（无 aligned data），Llama-3.2-3B_d100 为 29.67%（degenerate all-A）。这两个模型拉高了 cal_mae。

2. **v4 已修复但论文未更新**：`cross_family_v4`（今天 11:17 创建，比 v3 晚 ~3 小时）排除了退化 Llama 模型后：
   - MMLU: cal_mae = **0.008**（从 0.017 降到 0.008）
   - GSM8K: cal_mae = 0.0078（不变）
   - ARC: cal_mae = 0.0151（从 0.015 变为 0.0151）

3. **ARC 0.015 不是 0.0162 四舍五入**：Reviewer 怀疑的 0.0162 来自更早的 v1（`results_cross_family_irt/`），论文实际引用的是 v3 的 0.015。

---

## 建议

1. **论文应引用 v4 数字**（排除退化模型后），cross-family calMAE 为：MMLU 0.008, ARC 0.015, GSM8K 0.008。这显著更好且方法学更合理。

2. **如继续用 v3**：需在论文中说明 MMLU pooling 包含了 Llama 退化模型（N=20 含 2 个退化点），否则审稿人会质疑为何 MMLU cal_mae 远高于其他。

3. **精度一致性**：当前论文混用 2 位和 3 位小数（0.015 vs 0.017 vs 0.008）。建议统一用 3 位小数（0.017, 0.015, 0.008），并在 caption 注明 "rounded to third decimal place"。

---
