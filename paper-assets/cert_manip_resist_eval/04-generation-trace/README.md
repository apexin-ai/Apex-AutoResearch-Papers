# Generation traces

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation**

[Readable Markdown](readable/README.md) · [JSON catalogue](catalog.json) · [Source archive index](trace-index.csv)

For a quick review on GitHub, start with the readable Markdown pages. Each page shows the recorded user instructions, assistant replies, tool calls, and tool results in order. The JSON links remain available for complete machine-readable inspection.

## What is included

| Source | Files |
|---|---:|
| Conversation logs | 137 |
| Worker execution logs | 381 |
| Task result records | 358 |
| Context and loop notes | 4 |

**97,735 recorded messages/events · 2,743 recorded user-message boundaries · 39,456 tool-call records.**

A user-role entry may come from another agent or the system. It is not a human-authorship label. Worker tool results wrapped in user envelopes are labelled `tool_result` and do not start a new turn. Records before any user message remain a separate unbounded sequence. Parallel source logs are never interleaved.

Source text retains its recorded language. Markdown is a reading layer over the same sanitized source; it does not translate or summarize the research process. JSON is the complete normalized export and retains archive member, occurrence, SHA-256, and source-line provenance. Large rounds use linked JSON chunks; no message text is shortened in either export.

## Human-readable trace pages

The Markdown pages are grouped by source kind. Their filenames describe the recorded task or coordination stream; hash-sharded JSON folders are used only as a storage detail.

- **Conversation logs** (137): [Page 1](browse/conversation-001.md)
- **Worker execution logs** (381): [Page 1](browse/worker-001.md) · [Page 2](browse/worker-002.md) · [Page 3](browse/worker-003.md)
- **Task result records** (358): [Page 1](browse/result-001.md) · [Page 2](browse/result-002.md) · [Page 3](browse/result-003.md)
- **Context and loop notes** (4): [Page 1](browse/history-001.md)

