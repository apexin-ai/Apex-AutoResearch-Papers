# analysis mistral folio data audit

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral-folio-data-audit_20260522T144713_result.json`
- **Structured JSON:** [`d9b45cc1a40c478820b6.json`](../../sessions/d9/d9b45cc1a40c478820b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full analysis:

---

## 排查结论

### 1. seed=123: 67.16% 来源确认

**67.16% 是 LLaMA-8B FOLIO seed=123 的 SC 准确率**（137/204），不是 Mistral。Agent 报告时混淆了模型。

实际 Mistral FOLIO seed=123 数据：

| 目录 | SC | SICA | 文件大小 |
|------|-----|------|---------|
| `multi_seed/mistral_folio_seed123` | **57.84%** (118/204) | 57.84% (118/204) | 313,772 B |
| `exp052_mistral_folio204_seed123` | **53.92%** (110/204) | 57.35% (117/204) | — |

multi_seed 和 exp052 是不同次运行，结果有差异（SC差4pp），说明存在不完全的随机性控制或代码版本差异。multi_seed 中 SC=SICA 完全一致（均为118/204），稍显可疑但非致命。

### 2. seed=456: vLLM 崩溃确认，数据无效

| 指标 | seed=456 (multi_seed) | exp053 (安全数据) |
|------|----------------------|-------------------|
| SC | **28.92%** (59/204) | 56.37% (115/204) |
| SICA | 27.94% (57/204) | 55.88% (114/204) |
| 空问题 (sc_vote_count=0) | **111/204** | 0 |
| 总约束数 | 6,242 | 13,914 |
| 运行时长 | 2,210s | ~4,900s |
| 文件大小 | 273,711 B (偏小) | — |

**结论：seed=456 multi_seed 数据严重腐坏。** 111/204 问题完全为空（无投票、无约束、无答案），是 vLLM 中途崩溃的典型特征。运行时长仅 2210s（正常 ~4800s），约束总数不到正常的一半。**该数据不可用。**

### 3. seed=789: 数据完整，无异常

| 项目 | 值 |
|------|-----|
| SC | 59.31% (121/204) |
| SICA | 56.86% (116/204) |
| main vs backup | **完全一致**（同为 316,151 B，同指标） |
| 运行时长 | 4,798s（正常范围） |
| main Birth | 2026-05-22 18:49:51 |
| backup Birth | 2026-05-22 20:36:33（后于 main 27分钟复制） |

时间线合理：seed=789 与 seed=123 几乎同时启动（18:49 vs 18:43，大概率并行运行），seed=456 在它们完成后顺序启动（20:02）。backup 是主文件的手动副本，无异常。

### 4. 总结

| Seed | 状态 | 可用性 | 备注 |
|------|------|--------|------|
| 123 | ⚠️ 可用但有差异 | **可用**（论文用 exp052） | multi_seed 与 exp052 差 4pp，论文已用 exp052 安全数据 |
| 456 | ❌ 崩溃腐坏 | **无效** | 111/204 空问题，需重跑或仅用 exp053 |
| 789 | ✅ 完整 | **可用** | backup 与 main 一致 |

**67.16% 误报原因**：Agent 将 `llama8b_folio_seed123` 的 SC=67.16% 错误归因给了 Mistral FOLIO seed=123。论文现有 exp-052/053 数据不受影响。

---
