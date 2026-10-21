# review ai writing audit

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_ai_writing_audit_20260518T221534_result.json`
- **Structured JSON:** [`ac3db6c374d0c5cb59c4.json`](../../sessions/ac/ac3db6c374d0c5cb59c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成，结果保存在 `artifacts/ai_writing_audit.md`。

核心发现：
- **33 个问题**，集中在一个类别
- **Em-dash / En-dash**: 0（干净）
- **-ing 分词短语**: 29 个（最严重问题，主体 6 个 + 附录 23 个）。"`, confirming that...`" 模式出现 10+ 次，重复度高，是最显眼的 AI 痕迹
- **连续过渡词**: 0
- **AI 黑名单词**: 1 个（"notably"，附录中）
- **过度分段**: 0
- **代词指代不清**: 3 个

修复优先级：先批量处理 -ing 短语（尤其是 `, confirming` → `which confirms` / `and confirms` / `so`），这是审稿人最容易识别的模式。

---
