# Generation traces

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?**

[Open the visual browser](../../../traces/index.html?project=schema-dag-extraction) · [Offline preview](../../../traces/demo.html?project=schema-dag-extraction) · [JSON catalogue](catalog.json) · [Source archive index](trace-index.csv)

On GitHub, use the tables below to open readable session JSON directly. To use the interactive browser, clone the repository and run `python3 scripts/serve_traces.py --open` from its root, or open `traces/demo.html` for an offline preview.

## What is included

| Source | Files |
|---|---:|
| Conversation logs | 217 |
| Worker execution logs | 506 |
| Task result records | 474 |
| Context and loop notes | 45 |

**131,771 recorded messages/events · 4,172 recorded user-message boundaries · 53,631 tool-call records.**

A user-role entry may come from another agent or the system. It is not a human-authorship label. Worker tool results wrapped in user envelopes are labelled `tool_result` and do not start a new turn. Records before any user message remain a separate unbounded sequence. Parallel source logs are never interleaved.

Source text retains its recorded language. JSON is a deterministic normalized view of the already sanitized archive; it does not translate or summarize the research process. Every session includes archive member, occurrence, SHA-256, and source-line provenance. Large rounds use linked JSON chunks; no message text is shortened in the export.

## Browse all source records

- **Conversation logs** (217): [Page 1](browse/conversation-001.md) · [Page 2](browse/conversation-002.md)
- **Worker execution logs** (506): [Page 1](browse/worker-001.md) · [Page 2](browse/worker-002.md) · [Page 3](browse/worker-003.md) · [Page 4](browse/worker-004.md)
- **Task result records** (474): [Page 1](browse/result-001.md) · [Page 2](browse/result-002.md) · [Page 3](browse/result-003.md) · [Page 4](browse/result-004.md)
- **Context and loop notes** (45): [Page 1](browse/history-001.md)

See [format and reference projects](../../../traces/FORMAT.md) for definitions and design references.
