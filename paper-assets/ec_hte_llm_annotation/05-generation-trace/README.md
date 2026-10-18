# Generation traces

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects**

[Open the visual browser](../../../traces/index.html?project=ec_hte_llm_annotation) · [Offline preview](../../../traces/demo.html?project=ec_hte_llm_annotation) · [JSON catalogue](catalog.json) · [Source archive index](trace-index.csv)

On GitHub, use the tables below to open readable session JSON directly. To use the interactive browser, clone the repository and run `python3 scripts/serve_traces.py --open` from its root, or open `traces/demo.html` for an offline preview.

## What is included

| Source | Files |
|---|---:|
| Conversation logs | 72 |
| Worker execution logs | 183 |
| Task result records | 175 |
| Context and loop notes | 4 |

**75,488 recorded messages/events · 2,375 recorded user-message boundaries · 31,107 tool-call records.**

A user-role entry may come from another agent or the system. It is not a human-authorship label. Worker tool results wrapped in user envelopes are labelled `tool_result` and do not start a new turn. Records before any user message remain a separate unbounded sequence. Parallel source logs are never interleaved.

Source text retains its recorded language. JSON is a deterministic normalized view of the already sanitized archive; it does not translate or summarize the research process. Every session includes archive member, occurrence, SHA-256, and source-line provenance. Large rounds use linked JSON chunks; no message text is shortened in the export.

## Browse all source records

- **Conversation logs** (72): [Page 1](browse/conversation-001.md)
- **Worker execution logs** (183): [Page 1](browse/worker-001.md) · [Page 2](browse/worker-002.md)
- **Task result records** (175): [Page 1](browse/result-001.md) · [Page 2](browse/result-002.md)
- **Context and loop notes** (4): [Page 1](browse/history-001.md)

See [format and reference projects](../../../traces/FORMAT.md) for definitions and design references.
