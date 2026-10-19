# Generation traces

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction**

[Open the visual browser](../../../traces/index.html?project=cost-verify-agent-rl) · [Offline preview](../../../traces/demo.html?project=cost-verify-agent-rl) · [Readable Markdown](readable/README.md) · [JSON catalogue](catalog.json) · [Source archive index](trace-index.csv)

For a quick review on GitHub, start with the readable Markdown pages. Each page shows the recorded user instructions, assistant replies, tool calls, and tool results in order. The JSON links remain available for complete machine-readable inspection. To use the interactive browser, clone the repository and run `python3 scripts/serve_traces.py --open` from its root, or open `traces/demo.html` for an offline preview.

## What is included

| Source | Files |
|---|---:|
| Conversation logs | 502 |
| Worker execution logs | 1,164 |
| Task result records | 1,062 |
| Context and loop notes | 103 |

**209,966 recorded messages/events · 6,691 recorded user-message boundaries · 82,288 tool-call records.**

A user-role entry may come from another agent or the system. It is not a human-authorship label. Worker tool results wrapped in user envelopes are labelled `tool_result` and do not start a new turn. Records before any user message remain a separate unbounded sequence. Parallel source logs are never interleaved.

Source text retains its recorded language. Markdown is a reading layer over the same sanitized source; it does not translate or summarize the research process. JSON is the complete normalized export and retains archive member, occurrence, SHA-256, and source-line provenance. Large rounds use linked JSON chunks; no message text is shortened in either export.

## Human-readable trace pages

The Markdown pages are grouped by source kind. Their filenames describe the recorded task or coordination stream; hash-sharded JSON folders are used only as a storage detail.

- **Conversation logs** (502): [Page 1](browse/conversation-001.md) · [Page 2](browse/conversation-002.md) · [Page 3](browse/conversation-003.md) · [Page 4](browse/conversation-004.md)
- **Worker execution logs** (1,164): [Page 1](browse/worker-001.md) · [Page 2](browse/worker-002.md) · [Page 3](browse/worker-003.md) · [Page 4](browse/worker-004.md) · [Page 5](browse/worker-005.md) · [Page 6](browse/worker-006.md) · [Page 7](browse/worker-007.md) · [Page 8](browse/worker-008.md)
- **Task result records** (1,062): [Page 1](browse/result-001.md) · [Page 2](browse/result-002.md) · [Page 3](browse/result-003.md) · [Page 4](browse/result-004.md) · [Page 5](browse/result-005.md) · [Page 6](browse/result-006.md) · [Page 7](browse/result-007.md) · [Page 8](browse/result-008.md)
- **Context and loop notes** (103): [Page 1](browse/history-001.md)

See [format and reference projects](../../../traces/FORMAT.md) for definitions and design references.
