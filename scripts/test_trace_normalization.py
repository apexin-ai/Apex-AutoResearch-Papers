"""Regression tests for boundaries and lossless JSON page assembly."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import build_trace_browser as build


class TraceNormalizationTests(unittest.TestCase):
    def test_runtime_tool_results_do_not_create_user_turns(self):
        records = [
            {"type": "system", "subtype": "init"},
            {"type": "user", "message": {"role": "user", "content": [{"type": "text", "text": "Run the analysis"}]}},
            {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "tool_use", "id": "a", "name": "Bash", "input": {"command": "python analysis.py"}}]}},
            {"type": "user", "message": {"role": "user", "content": [{"type": "tool_result", "tool_use_id": "a", "content": "p=0.03"}]}},
        ]
        events = [build.normalize_record(r, i, "worker") for i, r in enumerate(records, 1)]
        turns = build.group_rounds(events)
        self.assertEqual([r["number"] for r in turns], [0, 1])
        self.assertEqual([e["role"] for e in turns[1]["messages"]], ["user", "tool_call", "tool_result"])
        self.assertEqual(turns[1]["messages"][-1]["content"][0]["content"], "p=0.03")
        self.assertEqual(turns[1]["messages"][-1]["recorded_role"], "user")

    def test_missing_user_prompt_is_not_invented(self):
        events, _ = build.parse_source(b'{"role":"assistant","text":"Already running"}\n', "conversation")
        turns = build.group_rounds(events)
        self.assertEqual(turns[0]["number"], 0)
        self.assertEqual(turns[0]["boundary"], "no_preceding_user_message_recorded")

    def test_plain_lines_and_blank_tool_results_are_preserved(self):
        raw = b'warning: disconnected\n\n{"role":"tool_result","text":"","tool":"Bash"}\n{bad json}\n'
        events, unparsed = build.parse_source(raw, "conversation")
        self.assertEqual(unparsed, 2)
        self.assertEqual([e["source_line"] for e in events], [1, 3, 4])
        self.assertEqual(events[1]["content"], [{"type": "text", "text": ""}])
        self.assertEqual(events[-1]["content"][0]["text"], "{bad json}")

    def test_paging_preserves_rounds_event_ids_and_long_unicode_text(self):
        events = []
        for i in range(13):
            events.append(build.normalize_record({"role": "user" if i in {1, 5, 8} else "assistant", "text": ("\u539f\u59cb\u8bb0\u5f55 <script> & text\n" * (90 if i == 6 else 3)), "ts": "2026-05-21T00:00:00Z"}, i + 1, "conversation"))
        rounds = build.group_rounds(events)
        session = {"schema_version": build.VERSION, "id": "test", "rounds": rounds}
        expected = json.loads(json.dumps(session))
        with tempfile.TemporaryDirectory() as directory, patch.object(build, "INLINE_BYTES", 1), patch.object(build, "PAGE_BYTES", 1000), patch.object(build, "PAGE_EVENTS", 3):
            relative = build.persist_session(Path(directory), session)
            file = Path(directory) / relative
            actual = json.loads(file.read_text())
            for turn, original in zip(actual["rounds"], expected["rounds"]):
                assembled = []
                for chunk in turn["chunks"]:
                    page = json.loads((file.parent / chunk["path"]).read_text())
                    matching = next(r for r in page["rounds"] if r["number"] == turn["number"])
                    assembled.extend(matching["messages"])
                self.assertEqual(assembled, original["messages"])
                self.assertEqual(len(assembled), turn["message_count"])


if __name__ == "__main__":
    unittest.main()
