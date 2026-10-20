# Generation traces

**turn hier kv compress**

[Open the visual browser](../../../traces/index.html?project=turn-hier-kv-compress) · [Offline preview](../../../traces/demo.html?project=turn-hier-kv-compress) · [Readable Markdown](readable/README.md) · [JSON catalogue](catalog.json) · [Source archive index](trace-index.csv)

For a quick review on GitHub, start with the readable Markdown pages. Each page shows the recorded user instructions, assistant replies, tool calls, and tool results in order. The JSON links remain available for complete machine-readable inspection. To use the interactive browser, clone the repository and run `python3 scripts/serve_traces.py --open` from its root, or open `traces/demo.html` for an offline preview.

## What is included

| Source | Files |
|---|---:|
| Conversation logs | 6 |
| Worker execution logs | 23 |
| Task result records | 16 |

**4,510 recorded messages/events · 118 recorded user-message boundaries · 1,764 tool-call records.**

A user-role entry may come from another agent or the system. It is not a human-authorship label. Worker tool results wrapped in user envelopes are labelled `tool_result` and do not start a new turn. Records before any user message remain a separate unbounded sequence. Parallel source logs are never interleaved.

Source text retains its recorded language. Markdown is a reading layer over the same sanitized source; it does not translate or summarize the research process. JSON is the complete normalized export and retains archive member, occurrence, SHA-256, and source-line provenance. Large rounds use linked JSON chunks; no message text is shortened in either export.

## Human-readable trace pages

The Markdown pages are grouped by source kind. Their filenames describe the recorded task or coordination stream; hash-sharded JSON folders are used only as a storage detail.

- **Conversation logs** (6): [Page 1](browse/conversation-001.md)
- **Worker execution logs** (23): [Page 1](browse/worker-001.md)
- **Task result records** (16): [Page 1](browse/result-001.md)

See [format and reference projects](../../../traces/FORMAT.md) for definitions and design references.
