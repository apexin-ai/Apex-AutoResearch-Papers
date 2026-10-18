# ssh r11 count level verify

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_r11-count-level-verify_20260517T100424_result.json`
- **Structured JSON:** [`fc5f62dd4b9d2db7e410.json`](../../sessions/fc/fc5f62dd4b9d2db7e410.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据对比完成。以下是汇总：

---

## 对比结果

### 1. FewRel 实际 count levels
**d051 batch config**: `[4, 8, 16, 32, 40, 64, 80]` — 7 levels, 每个 25 batches (3 seeds: s42, s123, s456)

**论文写的**: `{1, 4, 8, 16, 32, 64, 80}`

**不一致**: 
- 实际有 **count_40**，论文没写
- 论文写了 **count_1**，但 d051 batch config 中没有

### 2. Few-NERD 实际 count levels
**d051 batch config**: `[2, 6, 12, 22, 44, 66]` — 6 levels, 每个 25 batches (3 seeds)

**论文写的**: `{1, 2, 6, 12, 22, 44, 64}`

**不一致**:
- 实际 full schema 是 **count_66**，论文写了 **64** (错误！Few-NERD 有 66 个 fine-grained types)
- 论文写了 **count_1**，但 d051 中没有

### 3. DocRED 实际 count levels
**exp_docred_confusability/count_curve_results.json**: `[1, 4, 8, 16, 32, 64, 96]` — 7 levels, 每个 **5** batches

**论文写的**: `{1, 4, 8, 16, 32, 64, 96}` — **一致**

### 4. MAVEN 实际 count levels
**服务器上没有找到 MAVEN count curve 实验数据**。只有 `exp_maven_minilm/` 下的 decomposition 文件（per_type, random_batch, sdgd_zero, single_pass），不是 count curve 格式。

**论文写的**: `{1, 6, 12, 22, 44, 64}`

### 5. 每个 count level 的 batch 数量
| 数据集 | 实际 batches/level | 论文写的 |
|--------|-------------------|---------|
| FewRel | **25** | 5 |
| Few-NERD | **25** | 5 |
| DocRED | **5** | 5 |
| MAVEN | 无数据 | 5 |

**论文说 "5 random type batches"，但 FewRel/Few-NERD 实际跑了 25 batches per level。**

### 6. count=1 (solo baseline)
- **DocRED**: 包含在 count_curve_results.json 中 (curve_count_1, 5 batches, bcs=0.0)
- **FewRel**: d051 batch config 中 **不包含** count_1
- **Few-NERD**: d051 batch config 中 **不包含** count_1
- **MAVEN**: 无数据

### 7. Full schema count 确认

| 数据集 | 论文 Table 1 | 论文 §3.3 count list | 实际 (batch config max) | 代码常量 |
|--------|-------------|---------------------|------------------------|---------|
| Few-NERD | 66 | 64 | **66** | `NER_COUNTS = [2, 6, 12, 22, 44, 66]` |
| FewRel | 80 | 80 | **80** | `RE_COUNTS = [4, 8, 16, 32, 40, 64, 80]` |
| DocRED | 96 | 96 | **96** | 结果中有 curve_count_96 |
| MAVEN | 168 | 64 (max listed) | 无数据 | — |

### 关键问题总结

1. **Few-NERD §3.3 count list 把 66 写成了 64** — Table 1 正确写了 66，但 count list 里的 full-schema level 错了
2. **FewRel count_40 存在但论文未提及** — 实际实验包含 count_40，论文 count list 漏掉了
3. **论文说 5 batches，FewRel/Few-NERD 实际是 25 batches**
4. **count_1 在 FewRel/Few-NERD d051 中不存在**，但论文声称所有数据集都有 count=1
5. **MAVEN count curve 实验数据未找到**

---
