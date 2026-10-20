# Generation traces

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)**

[Open the visual browser](../../../../traces/index.html?project=distrib_canary_collapse--export-20260712) · [Offline preview](../../../../traces/demo.html?project=distrib_canary_collapse--export-20260712) · [Readable Markdown](readable/README.md) · [JSON catalogue](catalog.json) · [Source archive index](trace-index.csv)

For a quick review on GitHub, start with the readable Markdown pages. Each page shows the recorded user instructions, assistant replies, tool calls, and tool results in order. The JSON links remain available for complete machine-readable inspection. To use the interactive browser, clone the repository and run `python3 scripts/serve_traces.py --open` from its root, or open `traces/demo.html` for an offline preview.

## What is included

| Source | Files |
|---|---:|
| Conversation logs | 1,948 |

**447,459 recorded messages/events · 22,707 recorded user-message boundaries · 112,681 tool-call records.**

A user-role entry may come from another agent or the system. It is not a human-authorship label. Worker tool results wrapped in user envelopes are labelled `tool_result` and do not start a new turn. Records before any user message remain a separate unbounded sequence. Parallel source logs are never interleaved.

Source text retains its recorded language. Markdown is a reading layer over the same sanitized source; it does not translate or summarize the research process. JSON is the complete normalized export and retains archive member, occurrence, SHA-256, and source-line provenance. Large rounds use linked JSON chunks; no message text is shortened in either export.

## Human-readable trace pages

The Markdown pages are grouped by source kind. Their filenames describe the recorded task or coordination stream; hash-sharded JSON folders are used only as a storage detail.

- **Conversation logs** (1,948): [Page 1](browse/conversation-001.md) · [Page 2](browse/conversation-002.md) · [Page 3](browse/conversation-003.md) · [Page 4](browse/conversation-004.md) · [Page 5](browse/conversation-005.md) · [Page 6](browse/conversation-006.md) · [Page 7](browse/conversation-007.md) · [Page 8](browse/conversation-008.md) · [Page 9](browse/conversation-009.md) · [Page 10](browse/conversation-010.md) · [Page 11](browse/conversation-011.md) · [Page 12](browse/conversation-012.md) · [Page 13](browse/conversation-013.md)

See [format and reference projects](../../../../traces/FORMAT.md) for definitions and design references.
