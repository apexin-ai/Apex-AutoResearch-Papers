#!/usr/bin/env python3
"""Normalize the already sanitized trace archives; build a static review catalogue.

Uses Python's standard library. No model calls, translation, or invented events.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import re
import tarfile
import tempfile
from contextlib import contextmanager
from pathlib import Path

VERSION = "1.0"
INLINE_BYTES = 700_000
PAGE_BYTES = 650_000
PAGE_EVENTS = 180
ROOT = Path(__file__).resolve().parents[1]
KINDS = {
    "conversation": "Conversation logs",
    "worker": "Worker execution logs",
    "result": "Task result records",
    "history": "Context and loop notes",
    "other": "Other recorded files",
}


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(encoded(value))


@contextmanager
def archive_path(directory):
    archive = directory / "trace-files.tar.gz"
    if archive.exists():
        yield archive
        return
    parts = directory / "trace-files.tar.gz.parts"
    with tempfile.NamedTemporaryFile(suffix=".tar.gz") as output:
        with (parts / "manifest.csv").open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                data = (parts / row["part"]).read_bytes()
                if len(data) != int(row["bytes"]) or hashlib.sha256(data).hexdigest() != row["sha256"]:
                    raise ValueError(f"Split archive checksum mismatch: {row['part']}")
                output.write(data)
        output.flush()
        yield Path(output.name)


def classify(path):
    if path.startswith("logs/chats/"):
        return "conversation"
    if path.startswith("logs/workers/"):
        return "result" if path.endswith("_result.json") else "worker"
    if path.startswith("task_context/history/"):
        return "history"
    return "other"


def title_for(path):
    stem = Path(path).stem.removesuffix("_result")
    if "feishu_group_" in stem:
        match = re.search(r"_(paper_agent|reviewer(?:_[12])?|director)(?:_|$)", stem)
        label = match.group(1).replace("_", " ").title() if match else "Project"
        suffix = " (archived snapshot)" if "/archive/" in path else ""
        return f"{label} coordination{suffix}"
    if path.startswith("task_context/history/"):
        return " / ".join(Path(path).parts[-2:])
    return re.sub(r"[_-]+", " ", re.sub(r"_\d{8}T\d{6}$", "", stem).removeprefix("worker_"))


def text_of(blocks):
    texts = []
    for block in blocks:
        if isinstance(block, dict):
            if block.get("type") == "text":
                texts.append(str(block.get("text", "")))
            elif block.get("type") == "thinking":
                texts.append(str(block.get("thinking", "")))
    return "\n".join(texts)


def content_blocks(value):
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        return [{"type": "text", "text": value}]
    return [{"type": "json", "value": value}]


def normalize_record(record, line, source_kind):
    """One source record stays one event; nested blocks retain their own types."""
    if not isinstance(record, dict):
        return {"source_line": line, "role": "record", "content": content_blocks(record)}
    event = {"source_line": line, "timestamp": record.get("ts", record.get("timestamp"))}
    if source_kind == "conversation" and "role" in record:
        role = record.get("role", "record")
        event["recorded_role"] = role
        event["role"] = "tool_call" if role == "tool" else role
        event["content"] = content_blocks(record.get("text", ""))
        extra = {k: v for k, v in record.items() if k not in {"role", "text", "ts", "timestamp"}}
        if extra:
            event["metadata"] = extra
        return event

    kind = record.get("type", "record")
    message = record.get("message")
    if isinstance(message, dict):
        blocks = content_blocks(message.get("content", ""))
        role = message.get("role", kind)
        # Tool observations use a user envelope in the runtime stream. They
        # must not create a user turn or appear as human-authored messages.
        types = {b.get("type") for b in blocks if isinstance(b, dict)}
        if types and types <= {"tool_result"}:
            role = "tool_result"
        elif types and types <= {"tool_use", "server_tool_use"}:
            role = "tool_call"
        event.update(role=role, recorded_role=message.get("role", kind), content=blocks)
        metadata = {k: v for k, v in record.items() if k not in {"message", "timestamp", "ts"}}
        extra = {k: v for k, v in message.items() if k not in {"content", "role"}}
        if extra:
            metadata["message"] = extra
        event["metadata"] = metadata
    elif kind == "result":
        event.update(role="result", content=content_blocks(record.get("result", "")))
        event["metadata"] = {k: v for k, v in record.items() if k not in {"result", "timestamp", "ts"}}
    else:
        event.update(role="system" if kind == "system" else "record", content=[{"type": "json", "value": record}])
    return event


def parse_source(data, kind):
    text = data.decode("utf-8", errors="replace")
    if kind == "history":
        return [{"source_line": 1, "role": "note", "content": content_blocks(text)}], 0
    if kind == "result":
        try:
            result = json.loads(text)
            # Result wrappers often only contain a raw completion, rather than
            # runtime's type=result object. Preserve every other field too.
            if isinstance(result, dict) and "raw" in result:
                event = {"source_line": 1, "role": "result", "content": content_blocks(result["raw"])}
                rest = {k: v for k, v in result.items() if k != "raw"}
                if rest:
                    event["metadata"] = rest
            else:
                event = normalize_record(result, 1, kind)
            return [event], 0
        except (json.JSONDecodeError, ValueError):
            return [{"source_line": 1, "role": "log", "content": content_blocks(text)}], 1
    events, unparsed = [], 0
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            events.append(normalize_record(json.loads(line), number, kind))
        except (json.JSONDecodeError, ValueError):
            unparsed += 1
            events.append({"source_line": number, "role": "log", "content": content_blocks(line)})
    return events, unparsed


def group_rounds(events):
    rounds = []
    number = 0
    for index, event in enumerate(events, 1):
        event["id"] = f"event-{index:06d}"
        if event["role"] == "user":
            number += 1
            rounds.append({"number": number, "boundary": "recorded_user_message", "messages": []})
        elif not rounds:
            rounds.append({"number": 0, "boundary": "no_preceding_user_message_recorded", "messages": []})
        rounds[-1]["messages"].append(event)
    for turn in rounds:
        turn["message_count"] = len(turn["messages"])
    return rounds


def persist_session(directory, session):
    """Small sessions are one readable JSON; large rounds are loaded in pages."""
    folder = directory / "sessions" / session["id"][:2]
    path = folder / (session["id"] + ".json")
    if len(encoded(session)) > INLINE_BYTES:
        batch, batch_bytes, pages = [], 0, 0

        def flush():
            nonlocal pages
            if not batch:
                return
            pages += 1
            name = f"{session['id']}-part-{pages:04d}.json"
            grouped = []
            for turn, event in batch:
                if not grouped or grouped[-1]["number"] != turn["number"]:
                    grouped.append({"number": turn["number"], "messages": []})
                grouped[-1]["messages"].append(event)
            write_json(folder / name, {"schema_version": VERSION, "session_id": session["id"], "rounds": grouped})
            for turn, event in batch:
                if not turn["chunks"] or turn["chunks"][-1]["path"] != name:
                    turn["chunks"].append({"path": name, "message_count": 0})
                turn["chunks"][-1]["message_count"] += 1
            batch.clear()

        for turn in session["rounds"]:
            messages = turn.pop("messages")
            turn["chunks"] = []
            for event in messages:
                size = len(encoded(event))
                if batch and (batch_bytes + size > PAGE_BYTES or len(batch) >= PAGE_EVENTS):
                    flush()
                    batch_bytes = 0
                batch.append((turn, event))
                batch_bytes += size
        flush()
    write_json(path, session)
    return path.relative_to(directory).as_posix()


def build_project(project):
    directory = project / "05-generation-trace"
    manifest = json.loads((project / "08-index/asset-manifest.json").read_text())
    entries, occurrences = [], collections.Counter()
    totals = collections.Counter()
    example = None
    with archive_path(directory) as archive:
        with tarfile.open(archive, mode="r|gz") as handle:
            for member in handle:
                if not member.isfile():
                    continue
                data = handle.extractfile(member).read()
                occurrences[member.name] += 1
                occurrence = occurrences[member.name]
                session_id = hashlib.sha256(f"{project.name}\0{member.name}\0{occurrence}".encode()).hexdigest()[:20]
                kind = classify(member.name)
                events, unparsed = parse_source(data, kind)
                roles = collections.Counter(e["role"] for e in events)
                times = sorted(e["timestamp"] for e in events if isinstance(e.get("timestamp"), str))
                rounds = group_rounds(events)
                tools = sum(1 for e in events if e["role"] == "tool_call" or any(isinstance(b, dict) and b.get("type") in {"tool_use", "server_tool_use"} for b in e["content"]))
                result_errors = sum(1 for e in events if e.get("metadata", {}).get("is_error") is True)
                task_key = Path(member.name).stem.removesuffix("_result")
                source = {"archive": "trace-files.tar.gz" if (directory / "trace-files.tar.gz").exists() else "trace-files.tar.gz.parts/", "member": member.name, "occurrence": occurrence, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
                session = {"schema_version": VERSION, "id": session_id, "project": project.name, "kind": kind, "title": title_for(member.name), "task_key": task_key, "source": source, "statistics": {"messages": len(events), "user_turns": roles["user"], "tool_calls": tools, "roles": dict(roles), "unparsed_lines_preserved": unparsed, "reported_errors": result_errors}, "rounds": rounds}
                if example is None and kind == "conversation":
                    for turn in rounds:
                        turn_roles = collections.Counter(e["role"] for e in turn["messages"])
                        if 5 <= turn["message_count"] <= 70 and all(turn_roles[r] for r in ["user", "assistant", "tool_call", "tool_result"]) and len(encoded(turn)) < 160_000:
                            example = {k: v for k, v in session.items() if k not in {"rounds", "statistics"}}
                            example.update(paper_title=manifest["title"], preview_selection={"round": turn["number"], "total_source_events": len(events), "policy": "First bounded recorded conversation round with user, assistant, tool call, and tool result; 5–70 events and under 160 KB. Not a scientific-quality ranking."}, statistics={"messages": turn["message_count"], "user_turns": 1, "tool_calls": turn_roles["tool_call"], "roles": dict(turn_roles)}, rounds=[turn])
                            example = json.loads(json.dumps(example))
                            break
                first_prompt = next((text_of(e["content"]) for e in events if e["role"] == "user"), "")
                entry = {"id": session_id, "kind": kind, "title": session["title"], "task_key": task_key, "source_path": member.name, "occurrence": occurrence, "messages": len(events), "user_turns": roles["user"], "tool_calls": tools, "started_at": times[0] if times else None, "ended_at": times[-1] if times else None, "preview": re.sub(r"\s+", " ", first_prompt)[:240], "reported_errors": result_errors, "unparsed_lines": unparsed}
                entry["path"] = persist_session(directory, session)
                entries.append(entry)
                totals.update(files=1, messages=len(events), user_turns=roles["user"], tool_calls=tools, unparsed_lines=unparsed)
                totals[kind] += 1
    if len(entries) != sum(1 for _ in csv.DictReader((directory / "trace-index.csv").open(encoding="utf-8-sig"))):
        raise ValueError(f"Archive/index file count mismatch in {project.name}")
    entries.sort(key=lambda e: (e["kind"] != "conversation", e["started_at"] or "9999", e["source_path"], e["occurrence"]))
    catalog = {"schema_version": VERSION, "project": project.name, "title": manifest["title"], "statistics": dict(totals), "sessions": entries}
    write_json(directory / "catalog.json", catalog)
    # A compact representative source for an offline preview, not a summary.
    if example:
        write_json(directory / "example-session.json", example)
    readme = ["# Generation traces", "", f"**{manifest['title']}**", "", f"[Open the visual browser](../../../traces/index.html?project={project.name}) · [Offline preview](../../../traces/demo.html?project={project.name}) · [JSON catalogue](catalog.json) · [Source archive index](trace-index.csv)", "", "On GitHub, use the tables below to open readable session JSON directly. To use the interactive browser, clone the repository and run `python3 scripts/serve_traces.py --open` from its root, or open `traces/demo.html` for an offline preview.", "", "## What is included", "", "| Source | Files |", "|---|---:|"]
    readme += [f"| {label} | {totals[kind]:,} |" for kind, label in KINDS.items() if totals[kind]]
    readme += ["", f"**{totals['messages']:,} recorded messages/events · {totals['user_turns']:,} recorded user-message boundaries · {totals['tool_calls']:,} tool-call records.**", "", "A user-role entry may come from another agent or the system. It is not a human-authorship label. Worker tool results wrapped in user envelopes are labelled `tool_result` and do not start a new turn. Records before any user message remain a separate unbounded sequence. Parallel source logs are never interleaved.", "", "Source text retains its recorded language. JSON is a deterministic normalized view of the already sanitized archive; it does not translate or summarize the research process. Every session includes archive member, occurrence, SHA-256, and source-line provenance. Large rounds use linked JSON chunks; no message text is shortened in the export.", "", "## Browse all source records", ""]
    for kind, label in KINDS.items():
        subset = [e for e in entries if e["kind"] == kind]
        if not subset:
            continue
        pages = []
        for start in range(0, len(subset), 150):
            file = f"browse/{kind}-{start // 150 + 1:03d}.md"
            lines = [f"# {label}", "", "[Back to trace guide](../README.md)", "", "| Source record | Events | User turns | JSON |", "|---|---:|---:|---|"]
            for entry in subset[start:start + 150]:
                lines.append(f"| `{entry['source_path']}` (occurrence {entry['occurrence']}) | {entry['messages']} | {entry['user_turns']} | [Open](../{entry['path']}) |")
            target = directory / file
            target.parent.mkdir(exist_ok=True)
            target.write_text("\n".join(lines) + "\n")
            pages.append(f"[Page {start // 150 + 1}]({file})")
        readme.append(f"- **{label}** ({len(subset):,}): " + " · ".join(pages))
    readme += ["", "See [format and reference projects](../../../traces/FORMAT.md) for definitions and design references.", ""]
    (directory / "README.md").write_text("\n".join(readme))
    (directory / "index.html").write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><title>Generation traces</title><meta http-equiv="refresh" content="0;url=../../../traces/index.html?project={project.name}"><a href="../../../traces/index.html?project={project.name}">Open trace browser</a></html>\n')
    print(project.name, dict(totals), flush=True)
    return {"project": project.name, "title": manifest["title"], "catalog": f"../paper-assets/{project.name}/05-generation-trace/catalog.json", "statistics": dict(totals)}, example


def write_preview(target, examples):
    """An HTML-only preview can be sent without serving or bundling resources."""
    template = (target / "index.html").read_text()
    offline = template.replace('<body>', '<body data-offline="true">').replace('<!-- EMBEDDED_DATA -->', '<script id="embedded-sessions" type="application/json">' + json.dumps(examples, ensure_ascii=False).replace('<', '\\u003c') + '</script>')
    offline = offline.replace('<link rel="stylesheet" href="viewer.css">', '<style>' + (target / "viewer.css").read_text() + '</style>')
    offline = offline.replace('<script src="viewer.js" defer></script>', '')
    offline = offline.replace('</body>', '<script>' + (target / "viewer.js").read_text().replace('</script', '<\\/script') + '</script></body>')
    (target / "demo.html").write_text(offline)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", action="append", help="Project slug; repeat to select projects")
    args = parser.parse_args()
    projects, examples = [], []
    for project in sorted((ROOT / "paper-assets").iterdir()):
        if not (project / "05-generation-trace/trace-index.csv").exists():
            continue
        if args.project and project.name not in args.project:
            continue
        summary, example = build_project(project)
        projects.append(summary)
        if example:
            examples.append(example)
    target = ROOT / "traces"
    target.mkdir(exist_ok=True)
    if args.project and (target / "projects.json").exists():
        selected = {p["project"] for p in projects}
        previous = json.loads((target / "projects.json").read_text())["projects"]
        for summary in previous:
            if summary["project"] not in selected:
                projects.append(summary)
                preview = ROOT / "paper-assets" / summary["project"] / "05-generation-trace/example-session.json"
                if preview.exists():
                    examples.append(json.loads(preview.read_text()))
        projects.sort(key=lambda p: p["project"])
        examples.sort(key=lambda p: p["project"])
    write_json(target / "projects.json", {"schema_version": VERSION, "projects": projects})
    write_preview(target, examples)


if __name__ == "__main__":
    main()
