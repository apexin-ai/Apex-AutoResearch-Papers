# fix repo count clarification

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_repo-count-clarification_20260514T231412_result.json`
- **Structured JSON:** [`64840a5951a9a160e9db.json`](../../sessions/64/64840a5951a9a160e9db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 查证结果

**数字含义确认：**

| 数字 | 含义 | 来源 |
|------|------|------|
| **131** | SWE-smith 原始 unique repos（每 repo 对应唯一 commit） | 123 有输出 + 8 clone_failed |
| **123** | 有 extraction 输出的 repos（all.jsonl 中所有 123 repos 均有 error_null > 0） | 验证 ✓ |
| **87** | ❌ 论文错误 — 实际应为 123 | 见下方根因 |
| **104** | 产出至少一个跨文件结构连接训练对的 repos | z_percent: repos_with_z_positive=104；train+val s42 验证 ✓ |

**87 的根因：** `plan006_full_scalability.json` 中用了两种分箱：
- 细粒度 histogram: `lt10=1, 10_50=17, 50_200=36, 200_500=40, 500plus=29`
- 实际 tier 聚合: `small_lt50=18, medium_50_200=36, large_200_500=40, xlarge_500plus=29`

论文 Table 6 错误地把 histogram 前两个 bin (1, 17) 当成了 Small 和 Medium tier 的 repo 数，并丢失了 50_200 的 36 repos，导致总数 1+17+40+29=87 而非正确的 18+36+40+29=123。

**Table 6 另一个错误：** tier 标签写的 "(<50 files)" 实际是按每 repo 的 instance 数量分层，非文件数。

**修正内容：**
1. Table 6 repo 数: 1→18, 17→36, total 87→123
2. Tier 标签: "(<50 files)" → "(<50 inst.)"，表头加注 "Repositories are tiered by their instance count"
3. 删除错误的 "36 repos produced only failed records" 说法
4. 新增准确描述: 104/123 repos 有跨文件结构连接，19 repos 缺乏但仍参与训练（fallback to embedding-distance）

---
