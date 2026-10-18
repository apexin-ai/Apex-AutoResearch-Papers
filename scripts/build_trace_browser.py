#!/usr/bin/env python3
"""Normalize the already sanitized trace archives; build a static review catalogue.

Uses Python's standard library. No model calls, translation, or invented events.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import html
import io
import json
import re
import shutil
import tarfile
import tempfile
import unicodedata
from contextlib import contextmanager
from pathlib import Path

VERSION = "1.0"
INLINE_BYTES = 700_000
PAGE_BYTES = 650_000
MARKDOWN_PAGE_BYTES = 800_000
PAGE_EVENTS = 180
ROOT = Path(__file__).resolve().parents[1]
KINDS = {
    "conversation": "Conversation logs",
    "worker": "Worker execution logs",
    "result": "Task result records",
    "history": "Context and loop notes",
    "other": "Other recorded files",
}

READABLE_DIRS = {
    "conversation": "conversations",
    "worker": "worker-executions",
    "result": "task-results",
    "history": "context-notes",
    "other": "other-records",
}

ROLE_LABELS = {
    "user": "User",
    "assistant": "Assistant",
    "tool_call": "Tool call",
    "tool_result": "Tool result",
    "system": "System",
    "record": "Runtime record",
    "log": "Log line",
    "note": "Context note",
    "result": "Task result",
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


def slugify(value, limit=100):
    """Make a human-readable, URL-safe filename without exposing hash shards."""
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return value[:limit].strip("-") or "record"


def readable_stem(path, title):
    """Derive a descriptive filename from the recorded source name."""
    stem = Path(path).stem.removesuffix("_result")
    timestamp = re.search(r"(\d{8})T(\d{6})", stem)
    if "feishu_group_" in stem:
        role = re.search(r"_(paper_agent|reviewer(?:_[12])?|director)(?:_|$)", stem)
        label = (role.group(1).replace("_", "-") if role else "coordination")
        suffix = f"-{timestamp.group(1)}-{timestamp.group(2)}" if timestamp else ""
        return slugify(f"{label}-coordination{suffix}")
    stem = re.sub(r"_\d{8}T\d{6}$", "", stem).removeprefix("worker_")
    candidate = slugify(stem)
    return candidate if candidate != "record" else slugify(title)


def markdown_fence(text, language="text"):
    text = safe_markdown_text(text)
    longest = max((len(run) for run in re.findall(r"`+", text)), default=0)
    fence = "`" * max(3, longest + 1)
    return f"{fence}{language}\n{text}\n{fence}"


def safe_markdown_text(text):
    """Keep recorded HTML-like text from changing the surrounding transcript."""
    return re.sub(r"<(?=[A-Za-z/!][^>]*>)", "&lt;", str(text))


def block_markdown(block):
    if not isinstance(block, dict):
        return markdown_fence(json.dumps(block, ensure_ascii=False, indent=2), "json")
    block_type = block.get("type")
    if block_type == "text":
        return safe_markdown_text(block.get("text", ""))
    if block_type == "thinking":
        return "<details><summary>Logged reasoning block</summary>\n\n" + markdown_fence(block.get("thinking", "")) + "\n\n</details>"
    if block_type in {"tool_use", "server_tool_use"}:
        name = block.get("name", "Unnamed tool")
        call_id = f" · `{block['id']}`" if block.get("id") else ""
        args = block.get("input", "Arguments not recorded in this source.")
        if not isinstance(args, str):
            args = json.dumps(args, ensure_ascii=False, indent=2)
        return "<details open><summary>🔧 Tool call — " + html.escape(str(name)) + call_id + "</summary>\n\n" + markdown_fence(args, "json") + "\n\n</details>"
    if block_type == "tool_result":
        label = "Tool result" + (" · reported error" if block.get("is_error") else "")
        call_id = f" · `{block['tool_use_id']}`" if block.get("tool_use_id") else ""
        content = block.get("content", "")
        if isinstance(content, list):
            body = "\n\n".join(block_markdown(child) for child in content)
        elif isinstance(content, str):
            body = content
        else:
            body = json.dumps(content, ensure_ascii=False, indent=2)
        return f"<details><summary>↩ {label}{call_id}</summary>\n\n{markdown_fence(body)}\n\n</details>"
    if block_type == "json":
        return markdown_fence(json.dumps(block.get("value"), ensure_ascii=False, indent=2), "json")
    return markdown_fence(json.dumps(block, ensure_ascii=False, indent=2), "json")


def event_markdown(event):
    role = ROLE_LABELS.get(event.get("role"), event.get("role", "Recorded event"))
    details = [f"### {role}"]
    source_line = event.get("source_line")
    timestamp = event.get("timestamp")
    provenance = []
    if source_line is not None:
        provenance.append(f"source line {source_line}")
    if timestamp:
        provenance.append(str(timestamp))
    if provenance:
        details.append("_" + " · ".join(provenance) + "_")
    blocks = [block_markdown(block) for block in event.get("content", [])]
    if event.get("role") == "tool_call" and event.get("metadata", {}).get("tool"):
        metadata = event["metadata"]
        args = metadata.get("tool_args", "Arguments not recorded in this source.")
        if not any("Tool call" in block for block in blocks):
            if not isinstance(args, str):
                args = json.dumps(args, ensure_ascii=False, indent=2)
            blocks.append("<details open><summary>🔧 Tool call — " + html.escape(str(metadata["tool"])) + "</summary>\n\n" + markdown_fence(args, "json") + "\n\n</details>")
    details.extend(blocks or ["_(The source records this event without a text payload.)_"])
    if event.get("metadata") or event.get("recorded_role"):
        metadata = {"recorded_role": event.get("recorded_role"), **(event.get("metadata") or {})}
        details.append("<details><summary>Recorded metadata</summary>\n\n" + markdown_fence(json.dumps(metadata, ensure_ascii=False, indent=2), "json") + "\n\n</details>")
    return "\n\n".join(details)


def write_readable_markdown(directory, relative_path, session, paper_title):
    """Write a GitHub-friendly transcript, splitting long records into readable parts."""
    json_path = f"../../sessions/{session['id'][:2]}/{session['id']}.json"
    overview = [f"# {session['title']}", "", f"**{paper_title}** · {KINDS.get(session['kind'], session['kind'])}", "", "This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.", "", "## Record overview", "", f"- **Events:** {session['statistics']['messages']:,}", f"- **Recorded user turns:** {session['statistics']['user_turns']:,}", f"- **Tool calls:** {session['statistics']['tool_calls']:,}", f"- **Original source:** `{session['source']['member']}`", f"- **Structured JSON:** [`{session['id']}.json`]({json_path})", ""]
    if session["kind"] == "conversation":
        overview += ["## How to read this transcript", "", "`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.", ""]
    blocks = []
    for turn in session["rounds"]:
        number = turn["number"]
        label = "Before a recorded user message" if number == 0 else f"Round {number}"
        blocks.append((turn["number"], [f"## {label}", "", f"{turn['message_count']:,} recorded events", ""]))
        for event in turn.get("messages", []):
            blocks.append((turn["number"], [event_markdown(event), "", "---", ""]))
    path = directory / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    part_dir = path.with_suffix("")
    if part_dir.exists():
        shutil.rmtree(part_dir)
    full = "\n".join(overview + [line for _, block in blocks for line in block]).rstrip() + "\n"
    if len(full.encode("utf-8")) <= MARKDOWN_PAGE_BYTES:
        path.write_text(full, encoding="utf-8")
        return

    # Split on event boundaries. A single oversized event is rendered as
    # continuation code blocks so no page exceeds GitHub's comfortable size.
    page_blocks, current, current_bytes = [], [], len(("\n".join(overview) + "\n").encode("utf-8"))
    for round_number, block in blocks:
        block_text = "\n".join(block) + "\n"
        pieces = [block_text]
        if len(block_text.encode("utf-8")) > MARKDOWN_PAGE_BYTES:
            raw = block_text
            pieces = []
            while raw:
                cut = min(len(raw), MARKDOWN_PAGE_BYTES // 2)
                if cut < len(raw):
                    boundary = raw.rfind("\n", 0, cut)
                    if boundary > 1000:
                        cut = boundary + 1
                chunk = raw[:cut]
                pieces.append(f"### Large event (continued)\n\n{markdown_fence(chunk)}\n\n---\n")
                raw = raw[cut:]
        for piece in pieces:
            piece_bytes = len(piece.encode("utf-8"))
            if current and current_bytes + piece_bytes > MARKDOWN_PAGE_BYTES:
                page_blocks.append(current)
                current, current_bytes = [], len(("\n".join(overview) + "\n").encode("utf-8"))
            current.append((round_number, piece))
            current_bytes += piece_bytes
    if current:
        page_blocks.append(current)
    part_dir.mkdir(parents=True, exist_ok=True)
    links = []
    for index, page in enumerate(page_blocks, 1):
        filename = f"part-{index:03d}.md"
        part_json_path = f"../../../sessions/{session['id'][:2]}/{session['id']}.json"
        navigation = []
        if index > 1:
            navigation.append(f"[← Part {index - 1}](part-{index - 1:03d}.md)")
        navigation.append(f"[Transcript overview](../{path.name})")
        if index < len(page_blocks):
            navigation.append(f"[Part {index + 1} →](part-{index + 1:03d}.md)")
        page_lines = [f"# {session['title']} — Part {index} of {len(page_blocks)}", "", f"**{paper_title}** · {KINDS.get(session['kind'], session['kind'])}", "", " · ".join(navigation) + f" · [Structured JSON]({part_json_path})", ""]
        last_round = None
        for round_number, piece in page:
            if round_number != last_round:
                label = "Before a recorded user message" if round_number == 0 else f"Round {round_number}"
                page_lines += [f"## {label}", ""]
                last_round = round_number
            page_lines.append(piece)
        (part_dir / filename).write_text("\n".join(page_lines).rstrip() + "\n", encoding="utf-8")
        links.append(f"[Part {index}]({part_dir.name}/{filename})")
    landing = overview + ["## Browse this transcript", "", "This source is split into pages so it remains easy to read on GitHub. Open the parts in order.", "", " · ".join(links), ""]
    path.write_text("\n".join(landing), encoding="utf-8")


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
    readable_names = collections.Counter()
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
                readable_dir = READABLE_DIRS.get(kind, "other-records")
                readable_base = readable_stem(member.name, session["title"])
                readable_names[(readable_dir, readable_base)] += 1
                readable_count = readable_names[(readable_dir, readable_base)]
                readable_file = readable_base + (f"-copy-{readable_count}" if readable_count > 1 else "") + ".md"
                readable_path = f"readable/{readable_dir}/{readable_file}"
                session["readable_path"] = readable_path
                write_readable_markdown(directory, readable_path, session, manifest["title"])
                if example is None and kind == "conversation":
                    for turn in rounds:
                        turn_roles = collections.Counter(e["role"] for e in turn["messages"])
                        if 5 <= turn["message_count"] <= 70 and all(turn_roles[r] for r in ["user", "assistant", "tool_call", "tool_result"]) and len(encoded(turn)) < 160_000:
                            example = {k: v for k, v in session.items() if k not in {"rounds", "statistics"}}
                            example.update(paper_title=manifest["title"], preview_selection={"round": turn["number"], "total_source_events": len(events), "policy": "First bounded recorded conversation round with user, assistant, tool call, and tool result; 5–70 events and under 160 KB. Not a scientific-quality ranking."}, statistics={"messages": turn["message_count"], "user_turns": 1, "tool_calls": turn_roles["tool_call"], "roles": dict(turn_roles)}, rounds=[turn])
                            example = json.loads(json.dumps(example))
                            break
                first_prompt = next((text_of(e["content"]) for e in events if e["role"] == "user"), "")
                entry = {"id": session_id, "kind": kind, "title": session["title"], "task_key": task_key, "source_path": member.name, "occurrence": occurrence, "messages": len(events), "user_turns": roles["user"], "tool_calls": tools, "started_at": times[0] if times else None, "ended_at": times[-1] if times else None, "preview": re.sub(r"\s+", " ", first_prompt)[:240], "reported_errors": result_errors, "unparsed_lines": unparsed, "readable_path": readable_path}
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
    readme = ["# Generation traces", "", f"**{manifest['title']}**", "", f"[Open the visual browser](../../../traces/index.html?project={project.name}) · [Offline preview](../../../traces/demo.html?project={project.name}) · [Readable Markdown](readable/README.md) · [JSON catalogue](catalog.json) · [Source archive index](trace-index.csv)", "", "For a quick review on GitHub, start with the readable Markdown pages. Each page shows the recorded user instructions, assistant replies, tool calls, and tool results in order. The JSON links remain available for complete machine-readable inspection. To use the interactive browser, clone the repository and run `python3 scripts/serve_traces.py --open` from its root, or open `traces/demo.html` for an offline preview.", "", "## What is included", "", "| Source | Files |", "|---|---:|"]
    readme += [f"| {label} | {totals[kind]:,} |" for kind, label in KINDS.items() if totals[kind]]
    readme += ["", f"**{totals['messages']:,} recorded messages/events · {totals['user_turns']:,} recorded user-message boundaries · {totals['tool_calls']:,} tool-call records.**", "", "A user-role entry may come from another agent or the system. It is not a human-authorship label. Worker tool results wrapped in user envelopes are labelled `tool_result` and do not start a new turn. Records before any user message remain a separate unbounded sequence. Parallel source logs are never interleaved.", "", "Source text retains its recorded language. Markdown is a reading layer over the same sanitized source; it does not translate or summarize the research process. JSON is the complete normalized export and retains archive member, occurrence, SHA-256, and source-line provenance. Large rounds use linked JSON chunks; no message text is shortened in either export.", "", "## Human-readable trace pages", "", "The Markdown pages are grouped by source kind. Their filenames describe the recorded task or coordination stream; hash-sharded JSON folders are used only as a storage detail.", ""]
    readable_readme = ["# Readable trace pages", "", f"These pages are the easiest way to review **{manifest['title']}** on GitHub. They preserve the recorded sequence and label each event as `User`, `Assistant`, `Tool call`, `Tool result`, or another recorded type.", "", "| Source kind | Browse |", "|---|---|"]
    for kind, label in KINDS.items():
        subset = [e for e in entries if e["kind"] == kind]
        if not subset:
            continue
        readable_dir = READABLE_DIRS.get(kind, "other-records")
        readable_pages = []
        for start in range(0, len(subset), 150):
            index_name = f"index-{start // 150 + 1:03d}.md"
            lines = [f"# {label}", "", "Open a Markdown transcript for a human-readable view, or the JSON file for the structured export.", "", "| Record | Events | User turns | Markdown | JSON |", "|---|---:|---:|---|---|"]
            for entry in subset[start:start + 150]:
                display = entry["title"]
                if entry["preview"]:
                    display += " — " + entry["preview"][:100]
                display = display.replace("|", "\\|").replace("\n", " ")
                lines.append(f"| {display} | {entry['messages']:,} | {entry['user_turns']:,} | [Read transcript]({Path(entry['readable_path']).name}) | [JSON](../../{entry['path']}) |")
            target = directory / "readable" / readable_dir / index_name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("\n".join(lines) + "\n", encoding="utf-8")
            readable_pages.append(f"[Page {start // 150 + 1}]({readable_dir}/{index_name})")
        readable_readme.append(f"| {label} ({len(subset):,}) | " + " · ".join(readable_pages) + " |")
    (directory / "readable/README.md").write_text("\n".join(readable_readme) + "\n", encoding="utf-8")
    for kind, label in KINDS.items():
        subset = [e for e in entries if e["kind"] == kind]
        if not subset:
            continue
        pages = []
        for start in range(0, len(subset), 150):
            file = f"browse/{kind}-{start // 150 + 1:03d}.md"
            lines = [f"# {label}", "", "[Back to trace guide](../README.md) · [Readable Markdown indexes](../readable/README.md)", "", "| Source record | Events | User turns | Readable Markdown | JSON |", "|---|---:|---:|---|---|"]
            for entry in subset[start:start + 150]:
                lines.append(f"| `{entry['source_path']}` (occurrence {entry['occurrence']}) | {entry['messages']:,} | {entry['user_turns']:,} | [Read transcript](../{entry['readable_path']}) | [Open JSON](../{entry['path']}) |")
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
    offline = offline.replace('  <script src="viewer.js" defer></script>\n', '')
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
