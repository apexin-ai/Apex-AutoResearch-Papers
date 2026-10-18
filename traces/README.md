# Research Trace Atlas

Inspect how each paper was produced: recorded tasks, conversations, tool calls, results, and loop notes. All eight released trace archives have readable JSON counterparts.

**Start here:** download the repository and open [the offline preview](demo.html), or run `python3 scripts/serve_traces.py --open` from the repository root for the complete browser. On GitHub, use the paper guides below to browse JSON directly.

| Paper project | Conversations | Worker logs | Result records | Context notes | Recorded events | Trace guide |
|---|---:|---:|---:|---:|---:|---|
| `causal_style_decomp_judge` | 69 | 221 | 211 | 5 | 73,378 | [Browse](../paper-assets/causal_style_decomp_judge/05-generation-trace/README.md) |
| `cert_manip_resist_eval` | 137 | 381 | 358 | 4 | 97,735 | [Browse](../paper-assets/cert_manip_resist_eval/05-generation-trace/README.md) |
| `ec_hte_llm_annotation` | 72 | 183 | 175 | 4 | 75,488 | [Browse](../paper-assets/ec_hte_llm_annotation/05-generation-trace/README.md) |
| `entrainment_gated_ft` | 99 | 266 | 223 | 11 | 80,801 | [Browse](../paper-assets/entrainment_gated_ft/05-generation-trace/README.md) |
| `importance_margin_vla_compress` | 1,235 | 2,223 | 2,107 | 189 | 413,702 | [Browse](../paper-assets/importance_margin_vla_compress/05-generation-trace/README.md) |
| `ratekv` | 260 | 513 | 419 | 58 | 87,631 | [Browse](../paper-assets/ratekv/05-generation-trace/README.md) |
| `recursive_gen_depth_est` | 347 | 686 | 642 | 104 | 166,550 | [Browse](../paper-assets/recursive_gen_depth_est/05-generation-trace/README.md) |
| `schema-dag-extraction` | 217 | 506 | 474 | 45 | 131,771 | [Browse](../paper-assets/schema-dag-extraction/05-generation-trace/README.md) |

The collection contains **2,436 conversation logs**, **4,979 worker logs**, **4,609 task-result records**, and **420 context/loop notes**. The 1,127,056 message/event total includes overlapping snapshots and parallel logs. It is not a deduplicated measure of scientific activity.

## What you can inspect

- Select a paper, then search and filter its source records.
- Read a recorded round with user-role inputs, assistant messages, tool arguments, and tool results.
- Move between rounds, filter by role, and search the selected round.
- Download the complete selected round as JSON.
- Check the archive member, occurrence, SHA-256, and original line numbers for any record.

Source text retains its original language. A user-role message does not identify a human author. Missing prompts and timestamps are not reconstructed. Source-authored claims are not independently verified by this browser.

See [the format and reference guide](FORMAT.md) for the schema, paging, preview selection, and comparisons with OpenAI math, mini-SWE-agent, and Sakana AI Scientist.
