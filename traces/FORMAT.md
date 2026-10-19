# Reading and downloading the research traces

Start with [the interactive browser](index.html), or open [the offline preview](demo.html) directly from a downloaded clone. The preview includes one actual, bounded conversation round per paper for which a matching round is recorded. Its selection rule is stated below. The full browser includes every file in the released sanitized trace archives.

The offline preview embeds its data, styles, and JavaScript in a single HTML file, so `demo.html` can also be sent on its own. Links from that file to full catalogues, papers, and source indexes require the corresponding repository files.

On GitHub, HTML files display as source. Use each paper's `05-generation-trace/README.md` and its `readable/README.md` for clickable Markdown transcripts; each transcript links to the complete structured JSON. Run the browser locally when you want round navigation and filters:

```bash
python3 scripts/serve_traces.py --open
```

This starts a standard-library static server at `http://127.0.0.1:8765/traces/`. No API key or model is needed. All page resources are local. The server does not execute commands recorded in the traces. The same static files can be served by a conventional static website host.

## Three levels of inspection

| Level | Files | Purpose |
|---|---|---|
| Collection | `traces/projects.json` | Paper titles, source counts, and per-paper catalogue links. |
| Paper | `05-generation-trace/catalog.json`, `readable/`, and `browse/*.md` | Human-readable transcripts plus searchable metadata and direct structured-record links. |
| Readable source page | `05-generation-trace/readable/<kind>/<task-name>.md` | GitHub-friendly role-labelled Markdown showing User, Assistant, Tool call, and Tool result events in order. Long records link to numbered parts kept below GitHub's comfortable page size. |
| Source session | `05-generation-trace/sessions/<shard>/<id>.json` | Ordered rounds, recorded messages, tool arguments/results, metadata, and source provenance. Hash shards are an internal storage detail. |

Small source sessions contain all messages in one JSON file. Large sessions reference adjacent `*-part-*.json` pages to limit the amount fetched by the viewer. A page can contain pieces of multiple consecutive rounds. Select the matching `rounds[].number` in each referenced page and concatenate its messages in chunk order. The viewer does this automatically. **Download selected round** exports that round with all its messages, including payloads hidden by display previews.

## What a round means

A positive round starts at an explicit user-role message in that source and ends before the next such message. User-role messages may be instructions from a director agent, system notifications, or other automated inputs. The role does not identify a human author.

Some worker streams wrap tool results in a user envelope. These are normalized as `tool_result` and do not create a user turn. Tool calls keep their call identifiers where the source records them. Empty tool results stay empty and are labelled as such in the viewer.

Round `0` is an **unbounded sequence**: records appearing before any explicit user message in that file. A missing initial prompt is not invented. Parallel worker logs, archived copies, and conversation logs remain separate sources; they are never sorted together into a purported global dialogue. Archived conversation snapshots may overlap with live logs, so collection event counts are record counts, not deduplicated scientific actions.

For example, a small session follows this structure (illustrative placeholders):

```json
{
  "schema_version": "1.0",
  "id": "<stable source ID>",
  "project": "<paper project>",
  "kind": "conversation",
  "source": {
    "archive": "trace-files.tar.gz",
    "member": "logs/chats/<recorded-session>.jsonl",
    "occurrence": 1,
    "bytes": 1234,
    "sha256": "<SHA-256 of sanitized source bytes>"
  },
  "rounds": [
    {
      "number": 1,
      "boundary": "recorded_user_message",
      "message_count": 2,
      "messages": [
        {"id": "event-000001", "source_line": 1, "role": "user", "content": [{"type": "text", "text": "<recorded task>"}]},
        {"id": "event-000002", "source_line": 2, "role": "assistant", "content": [{"type": "text", "text": "<recorded reply>"}]}
      ]
    }
  ]
}
```

Actual sessions are linked from each paper's trace README. `example-session.json` contains an actual selected round with its original round number and line references. The standalone preview selection is deterministic: the first recorded conversation round in archive order with user, assistant, tool-call, and tool-result roles, 5–70 events, and less than 160 KB. This is a navigation example, not a scientific-quality ranking. Its `preview_selection` records the source session's full event count and the selection rule.

## Fidelity and scope

- Source text retains its original language, including Chinese. Interface labels and newly written guides are English. No text is machine translated or generated to fill gaps.
- Normalization starts from the already sanitized release archives. Existing redactions and omitted attachments remain omitted. The original workspace archives are not used or changed by this exporter.
- Each source is identified by project, archive-member path, and occurrence, so repeated archive entries cannot overwrite one another. Its SHA-256 covers the sanitized member bytes.
- Each event records its original line number. Multiline result JSON and Markdown notes are whole-file records beginning at line 1. Malformed JSON and plain diagnostic lines remain log events.
- Source timestamps are preserved when present. Filename dates are not presented as recorded timestamps. Runtime metadata, usage, tool IDs, and block types are retained where present.
- Logged reasoning blocks are collapsed initially. Source-authored summaries and results are labelled as recorded outputs; they do not establish independent verification.
- Task-title cleanup and related-record links are derived from filenames. Matching task keys are navigation aids and do not establish a causal relationship.

## Rebuild

```bash
python3 scripts/build_trace_browser.py
python3 scripts/test_trace_normalization.py
python3 scripts/validate_trace_release.py
```

The exporter uses only the Python standard library. It verifies the existing split-archive manifest before reading the VLA project's archive. Export is deterministic for the same source archives and script version.

## Reference projects

The design combines a paper catalogue, downloadable structured records, and a trajectory inspector. These are separate conventions; OpenAI math is not used as evidence of a full conversation-JSON release.

| Reference | Observed presentation | Applied here |
|---|---|---|
| [OpenAI math](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a) | Manuscript map, per-paper supporting assets, and abridged reasoning summaries in PDF. | Paper-first navigation and clear labels for the kind of evidence. |
| [mini-SWE-agent inspector](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/docs/usage/inspector.md) and [sample trajectory](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/tests/test_data/local.traj.json) | Saved JSON message histories and a step-by-step trajectory inspector. | Role-labelled messages, step navigation, JSON downloads, and visible tool interactions. The local schema is not claimed to be mini-SWE-agent compatible. |
| [Sakana AI Scientist workshop experiment](https://github.com/SakanaAI/AI-Scientist-ICLR2025-Workshop-Experiment/tree/c05036b2e0dcc17056abfba398184f51a93087ca) | A paper table linked to annotated papers and separately labelled review materials. | Keep each paper's trace entry connected to its manuscript and asset guide. |

Reference snapshots inspected on 2026-10-18 (Asia/Shanghai); links are pinned to commits.
