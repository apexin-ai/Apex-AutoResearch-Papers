# fix experiments v1 placeholders

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_experiments-v1-placeholders_20260515T031409_result.json`
- **Structured JSON:** [`c18efd2790d70dce5b3c.json`](../../sessions/c1/c18efd2790d70dce5b3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Line 136 的 `34.3%` 是 Large tier 的 per-tier placeholder，已标 `[pending recalc]`，不是总体数字，无需修改。Line 5 的 `15,133` 现在是正确的上下文用法（"15,133 via CodeQL"）。

修改汇总：

| 位置 | 旧值 | 新值 |
|------|------|------|
| §4.1 数据集描述 | 5,029 task instances → expansion 叙事 | 50,869 raw → 6,696 filtered → 44,173 |
| 提取成功数 | `\placeholder{15,133}` | 15,897 (= 15,133 CodeQL + 764 beniget) |
| 成功率 | `\placeholder{34.3%}` | 36.0% |
| 失败率 | `\placeholder{65.7%}` | 64.0% |
| 失败实例数 | (缺失) | 28,276 |
| 可用训练实例 | (缺失) | 14,288 |
| Table 6 Total coverage | `\placeholder{34.3%} [pending recalc]` | 36.0% |
| 末尾 re-extraction 语句 | "re-extraction pass...expected to improve..." | 已删除 |

`_project/paper/` 下无同名副本，无需同步。实验结果数字（R@1 等）和 Table 6 per-tier placeholders 未动。

---
