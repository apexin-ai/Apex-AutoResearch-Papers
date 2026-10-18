# Generation traces

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints**

[Open the visual browser](../../../traces/index.html?project=recursive_gen_depth_est) · [Offline preview](../../../traces/demo.html?project=recursive_gen_depth_est) · [JSON catalogue](catalog.json) · [Source archive index](trace-index.csv)

On GitHub, use the tables below to open readable session JSON directly. To use the interactive browser, clone the repository and run `python3 scripts/serve_traces.py --open` from its root, or open `traces/demo.html` for an offline preview.

## What is included

| Source | Files |
|---|---:|
| Conversation logs | 347 |
| Worker execution logs | 686 |
| Task result records | 642 |
| Context and loop notes | 104 |

**166,550 recorded messages/events · 5,043 recorded user-message boundaries · 67,907 tool-call records.**

A user-role entry may come from another agent or the system. It is not a human-authorship label. Worker tool results wrapped in user envelopes are labelled `tool_result` and do not start a new turn. Records before any user message remain a separate unbounded sequence. Parallel source logs are never interleaved.

Source text retains its recorded language. JSON is a deterministic normalized view of the already sanitized archive; it does not translate or summarize the research process. Every session includes archive member, occurrence, SHA-256, and source-line provenance. Large rounds use linked JSON chunks; no message text is shortened in the export.

## Browse all source records

- **Conversation logs** (347): [Page 1](browse/conversation-001.md) · [Page 2](browse/conversation-002.md) · [Page 3](browse/conversation-003.md)
- **Worker execution logs** (686): [Page 1](browse/worker-001.md) · [Page 2](browse/worker-002.md) · [Page 3](browse/worker-003.md) · [Page 4](browse/worker-004.md) · [Page 5](browse/worker-005.md)
- **Task result records** (642): [Page 1](browse/result-001.md) · [Page 2](browse/result-002.md) · [Page 3](browse/result-003.md) · [Page 4](browse/result-004.md) · [Page 5](browse/result-005.md)
- **Context and loop notes** (104): [Page 1](browse/history-001.md)

See [format and reference projects](../../../traces/FORMAT.md) for definitions and design references.
