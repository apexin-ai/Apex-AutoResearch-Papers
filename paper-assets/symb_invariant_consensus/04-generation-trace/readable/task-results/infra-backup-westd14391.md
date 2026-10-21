# infra backup westd14391

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_backup-westd14391_20260523T132801_result.json`
- **Structured JSON:** [`3e239530b2f5a9b39d5a.json`](../../sessions/3e/3e239530b2f5a9b39d5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

seed42 完整确认：n=600, SC=72.33%, SICA=66.67%，与已知数据吻合。

**备份报告：**

| 项目 | 值 |
|------|-----|
| 备份大小 | 12MB (压缩后) / 134MB (原始) |
| 文件数 | 3968 |
| 位置 | `artifacts/westd14391_backup.tar.gz` |

**关键文件（4个 results.json）：**
- `llama8b_pw_seed42/results.json` — n=600, SC=72.33%, SICA=66.67% ✓
- `llama8b_pw_seed123/results.json`
- `llama8b_pw_seed456/results.json`
- `llama8b_folio_seed789/results.json`

**14391 独有数据风险**：seed123 的实验在 agent_context 中标记为"已被 kill（冗余，16639 已有完整结果）"，但 14391 上仍保留了 results.json 和 intermediates。seed42 的完整结果（n=600）是关键数据，已确认在备份中。其余 seed456 和 folio_seed789 的数据如果 16639 上也有副本则无独有风险。

服务器可以安全释放。

---
