# Generation traces

**prism collapse mixing**

[Open the visual browser](../../../traces/index.html?project=prism_collapse_mixing) · [Offline preview](../../../traces/demo.html?project=prism_collapse_mixing) · [Readable Markdown](readable/README.md) · [JSON catalogue](catalog.json) · [Source archive index](trace-index.csv)

For a quick review on GitHub, start with the readable Markdown pages. Each page shows the recorded user instructions, assistant replies, tool calls, and tool results in order. The JSON links remain available for complete machine-readable inspection. To use the interactive browser, clone the repository and run `python3 scripts/serve_traces.py --open` from its root, or open `traces/demo.html` for an offline preview.

## What is included

| Source | Files |
|---|---:|
| Conversation logs | 25 |
| Worker execution logs | 38 |
| Task result records | 38 |
| Context and loop notes | 3 |

**6,679 recorded messages/events · 217 recorded user-message boundaries · 2,596 tool-call records.**

A user-role entry may come from another agent or the system. It is not a human-authorship label. Worker tool results wrapped in user envelopes are labelled `tool_result` and do not start a new turn. Records before any user message remain a separate unbounded sequence. Parallel source logs are never interleaved.

Source text retains its recorded language. Markdown is a reading layer over the same sanitized source; it does not translate or summarize the research process. JSON is the complete normalized export and retains archive member, occurrence, SHA-256, and source-line provenance. Large rounds use linked JSON chunks; no message text is shortened in either export.

## Human-readable trace pages

The Markdown pages are grouped by source kind. Their filenames describe the recorded task or coordination stream; hash-sharded JSON folders are used only as a storage detail.

- **Conversation logs** (25): [Page 1](browse/conversation-001.md)
- **Worker execution logs** (38): [Page 1](browse/worker-001.md)
- **Task result records** (38): [Page 1](browse/result-001.md)
- **Context and loop notes** (3): [Page 1](browse/history-001.md)

See [format and reference projects](../../../traces/FORMAT.md) for definitions and design references.
