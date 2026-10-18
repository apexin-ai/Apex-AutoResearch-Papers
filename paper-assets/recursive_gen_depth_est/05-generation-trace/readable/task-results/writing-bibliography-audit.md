# writing bibliography audit

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_bibliography_audit_20260516T050307_result.json`
- **Structured JSON:** [`3a6eebf6bc78db16ff53.json`](../../sessions/3a/3a6eebf6bc78db16ff53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Bibliography Audit 结果

### 1. 引用计数
**47 条目** — 远超 25 的硬约束 ✅

### 2. Orphan / Missing 检查
| 检查项 | 结果 |
|--------|------|
| Orphan（bib 有但 tex 未引用） | **0** ✅ |
| Missing（tex 引用但 bib 不存在） | **0** ✅ |

所有 47 个 bib 条目在 tex 文件中均有引用，完全一一对应。

### 3. 格式问题（已修复）
| 条目 | 问题 | 修复 |
|------|------|------|
| `shi2025_closer_look` | venue 写 "Advances in Neural Information Processing Systems"，其余 NeurIPS 条目写 "Proceedings of NeurIPS" | 已统一为 "Proceedings of NeurIPS" |

### 4. 格式注意项（无需修复）
- **`liu2019_roberta`**: `journal = {arXiv preprint arXiv:1907.11692}` — RoBERTa 未正式发表在会议/期刊，此写法可接受
- **`he2021_deberta_v3`**: key 含 2021 但 year=2023（arXiv 2021，ICLR 2023 发表）— key 命名非格式错误，不影响编译

### 5. 可疑条目标记
| 条目 | 标记原因 |
|------|----------|
| `knowledge_collapse2025` | 第一作者 "Keisha, Figarri" 姓名格式少见，建议确认是否正确 |
| `falahati2026_curated` | arXiv:2605.07724，2026 年 5 月上传，极新但在合理范围内 |

无明确伪造/幻觉迹象。所有条目均有合理的 arXiv ID 或 venue。

### 6. 完整性检查
- 所有条目均含 author, title, year ✅
- 年份范围 2007–2026，无未来年份异常 ✅
- venue/journal 使用一致（修复后） ✅

### 结论
**全部硬约束通过。** 唯一修复：NeurIPS venue 名称统一。无 orphan、无 missing、无 fake citation 证据。

---
