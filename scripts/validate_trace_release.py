#!/usr/bin/env python3
"""Check the exported JSON against every sanitized source archive member."""
import collections
import argparse
import hashlib
import json
from pathlib import Path
import re
import tarfile

import build_trace_browser as build

SECRET_PATTERNS = {
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b|github_pat_[A-Za-z0-9_]{40,}"),
    "Anthropic token": re.compile(r"sk-ant-[A-Za-z0-9_-]{24,}"),
    "Hugging Face token": re.compile(r"\bhf_[A-Za-z0-9]{25,}\b"),
    "Private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def load_messages(path, session):
    cache = {}
    messages = []
    for turn in session["rounds"]:
        found = list(turn.get("messages", []))
        for chunk in turn.get("chunks", []):
            key = chunk["path"]
            if key not in cache:
                cache[key] = json.loads((path.parent / key).read_text())
            page = cache[key]
            assert page["session_id"] == session["id"], path
            segment = next(r for r in page["rounds"] if r["number"] == turn["number"])
            assert len(segment["messages"]) == chunk["message_count"], path
            found.extend(segment["messages"])
        assert len(found) == turn["message_count"], path
        messages.extend(found)
    assert len(messages) == session["statistics"]["messages"], path
    assert [e["id"] for e in messages] == [f"event-{i:06d}" for i in range(1, len(messages) + 1)], path
    return messages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', action='append', help='Validate only the selected project; repeatable')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    collection = json.loads((root / "traces/projects.json").read_text())
    totals = collections.Counter()
    for paper in collection["projects"]:
        if args.project and paper['project'] not in args.project:
            continue
        directory = (root / "traces" / paper["catalog"]).resolve().parent
        catalog = json.loads((directory / "catalog.json").read_text())
        indexed = {e["id"]: e for e in catalog["sessions"]}
        occurrences = collections.Counter()
        with build.archive_path(directory) as archive:
            with tarfile.open(archive, mode="r|gz") as handle:
                for member in handle:
                    if not member.isfile():
                        continue
                    data = handle.extractfile(member).read()
                    occurrences[member.name] += 1
                    occurrence = occurrences[member.name]
                    session_id = hashlib.sha256(f"{paper['project']}\0{member.name}\0{occurrence}".encode()).hexdigest()[:20]
                    entry = indexed.pop(session_id)
                    path = directory / entry["path"]
                    exported = json.loads(path.read_text())
                    assert exported["source"]["sha256"] == hashlib.sha256(data).hexdigest(), path
                    assert exported["source"]["bytes"] == len(data), path
                    actual = load_messages(path, exported)
                    expected, _ = build.parse_source(data, build.classify(member.name))
                    expected_rounds = build.group_rounds(expected)
                    assert len(expected_rounds) == len(exported["rounds"]), path
                    assert actual == expected, f"Message content/order changed: {path}"
                    for label, pattern in SECRET_PATTERNS.items():
                        # This checks the source payload without echoing any candidate secret.
                        assert not pattern.search(data.decode("utf-8", errors="replace")), f"Credential pattern ({label}) in {paper['project']}/{member.name}"
                    totals.update(files=1, messages=len(actual))
        assert not indexed, f"Unmatched catalogue entries in {paper['project']}"
        assert catalog["statistics"] == paper["statistics"], paper["project"]
        # Preview must be an exact recorded round from its full session.
        if not (directory / "example-session.json").exists():
            print(f"Verified {paper['project']}: {len(catalog['sessions']):,} sources; no bounded preview round", flush=True)
            continue
        preview = json.loads((directory / "example-session.json").read_text())
        entry = next(e for e in catalog["sessions"] if e["id"] == preview["id"])
        full_path = directory / entry["path"]
        full = json.loads(full_path.read_text())
        full_messages = load_messages(full_path, full)
        by_id = {e["id"]: e for e in full_messages}
        for turn in preview["rounds"]:
            assert all(e == by_id[e["id"]] for e in turn["messages"])
        print(f"Verified {paper['project']}: {len(catalog['sessions']):,} sources", flush=True)
    paths = list(root.glob("paper-assets/*/05-generation-trace/sessions/**/*.json"))
    oversized = [p for p in paths if p.stat().st_size >= 100_000_000]
    assert not oversized, f"GitHub file limit: {oversized}"
    print(f"PASS: {totals['files']:,} sources / {totals['messages']:,} messages, matching content and order; credential-pattern scan clear; JSON files below GitHub's size limit.")


if __name__ == "__main__":
    main()
