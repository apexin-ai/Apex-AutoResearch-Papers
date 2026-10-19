# cpu error pattern analysis

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_error_pattern_analysis_20260513T185159_result.json`
- **Structured JSON:** [`37206fc4c3571dce6329.json`](../../sessions/37/37206fc4c3571dce6329.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 注册成功 (`art_20260513_d262da`)。

## 结果

**关键发现：所有 28,276 个 error 都是同一类型 `buggy_file_not_found`，不存在预想的多种 CodeQL 错误分类。**

| 维度 | 数据 |
|------|------|
| 总 instances | 44,173 |
| 错误数 | 28,276 (64.0%) |
| 成功数 | 15,897 (36.0%) |
| 唯一 error 类型 | `buggy_file_not_found` |
| 受影响 repos | 82/123 (67%) |
| >90% error rate 的 repos | 36 个 (贡献 20,810 instances) |

**根因**：SWE-smith 的 instance 元数据中记录的 buggy_file 路径，在指定 commit 的仓库 checkout 中不存在。`resolve_file_in_repo()` 的模糊匹配也未能找到对应文件。这是上游 SWE-smith mutation 生成管线的数据问题，不是 CodeQL 提取失败。

**论文 Limitation 节可以这样写**：64% failure rate 的本质是 SWE-smith 数据集中 buggy file path 与仓库实际文件结构不匹配，集中在 36 个 repo（>90% error rate），属于上游数据质量问题而非本文方法的提取能力限制。

---
