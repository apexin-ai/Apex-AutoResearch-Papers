# ops domain irt j audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_domain_irt_j_audit_20260517T164838_result.json`
- **Structured JSON:** [`5f98040ca251e0de521e.json`](../../sessions/5f/5f98040ca251e0de521e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整信息已获取。汇总结果：

---

## Domain-level IRT 模型数量汇总

### `mmlu_domain_irt_no05B/` — 所有 8 个 domain + pooled 均为 **J=13**

**13 个模型（脚本 MODEL_WHITELIST 确认）**：

| # | Model | Scale | Dosage | Seed |
|---|-------|-------|--------|------|
| 1 | Qwen2.5-1.5B_d000_s123 | 1.5B | 0% | 123 |
| 2 | Qwen2.5-1.5B_d000_s42 | 1.5B | 0% | 42 |
| 3 | Qwen2.5-1.5B_d005_s123 | 1.5B | 5% | 123 |
| 4 | Qwen2.5-1.5B_d005_s42 | 1.5B | 5% | 42 |
| 5 | Qwen2.5-1.5B_d025_s123 | 1.5B | 25% | 123 |
| 6 | Qwen2.5-1.5B_d025_s42 | 1.5B | 25% | 42 |
| 7 | Qwen2.5-1.5B_d100_s123 | 1.5B | 100% | 123 |
| 8 | Qwen2.5-1.5B_d100_s42 | 1.5B | 100% | 42 |
| 9 | Qwen2.5-3B_d005_s123 | 3B | 5% | 123 |
| 10 | Qwen2.5-3B_d025_s123 | 3B | 25% | 123 |
| 11 | Qwen2.5-3B_d025_v3_s42 | 3B | 25% | 42 |
| 12 | Qwen2.5-3B_d100_a32_s123 | 3B | 100% | 123 |
| 13 | Qwen2.5-3B_d100_a32_s42 | 3B | 100% | 42 |

组成：**8× Qwen 1.5B + 5× Qwen 3B**，无 0.5B，无 Llama，无 d000 for 3B。

### `mmlu_domain_irt_j16_cross_family/` — 所有 domain 均为 **J=16**

在 J=13 基础上增加 3 个 Llama-3.2-3B：
- Llama-3.2-3B_d000_s42
- Llama-3.2-3B_d005_s42
- Llama-3.2-3B_d025_s42

（Llama d100 因 A-rate=82.8% degenerate 被排除）

### 与 pooled 配置的差异

| 配置 | J | 特点 |
|------|---|------|
| domain no05B | 13 | 仅 Qwen 1.5B+3B |
| domain j16_cross_family | 16 | +3 Llama 3B |
| pooled n16_fixed | 16 | 应与 j16_cross_family 相同（待确认） |
| pooled all_scales | >16 | 包含 0.5B |

### 关键发现

- **所有 domain 的 J 一致**：no05B 全部 J=13，j16 全部 J=16
- J=13 确实是设计配置（脚本文档字符串写 "J=13 models"），不是不完整快照
- 论文 Table 2 / §5.4 引用 "J=13" 是正确的——如果引用的是 `no05B` 结果

---
