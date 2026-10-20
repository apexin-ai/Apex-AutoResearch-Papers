# Tests for RoleExtractor using mock token ids (no real tokenizer needed).

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from turnkv.role_extractor import RoleExtractor, LLAMA3_CONFIG
from turnkv.eass import Segment

# ---------------------------------------------------------------------------
# Mock token vocabulary for Llama 3.1
# ---------------------------------------------------------------------------

BOS = 128000        # <|begin_of_text|>
EOS = 128001        # <|end_of_text|>
HEADER_S = 128006   # <|start_header_id|>
HEADER_E = 128007   # <|end_header_id|>
EOT = 128009        # <|eot_id|>
PYTHON_TAG = 128255 # <|python_tag|>

# Fake content token ids — each maps to a single character/word via token_to_text.
T_SYS = 1       # "system"
T_USER = 2      # "user"
T_ASST = 3      # "assistant"
T_IPYTHON = 4   # "ipython"
T_NL = 5        # "\n\n"
T_HELLO = 10    # "Hello"
T_WORLD = 11    # "World"
T_ANSWER = 12   # "Answer"
T_RESULT = 13   # "Result"
T_CODE = 14     # "code"
T_THINK_S = 20  # "<think>"
T_THINK_E = 21  # "</think>"
T_REASON = 22   # "reasoning"
T_FINAL = 23    # "final"

TOKEN_TEXT = {
    BOS: "<|begin_of_text|>",
    EOS: "<|end_of_text|>",
    HEADER_S: "<|start_header_id|>",
    HEADER_E: "<|end_header_id|>",
    EOT: "<|eot_id|>",
    PYTHON_TAG: "<|python_tag|>",
    T_SYS: "system",
    T_USER: "user",
    T_ASST: "assistant",
    T_IPYTHON: "ipython",
    T_NL: "\n\n",
    T_HELLO: "Hello",
    T_WORLD: "World",
    T_ANSWER: "Answer",
    T_RESULT: "Result",
    T_CODE: "code",
    T_THINK_S: "<think>",
    T_THINK_E: "</think>",
    T_REASON: "reasoning",
    T_FINAL: "final",
}


def make_extractor():
    return RoleExtractor(tokenizer=None, template_name="llama3", token_to_text=TOKEN_TEXT)


def header(role_token):
    """Build a header sequence: <|start_header_id|> role <|end_header_id|> \\n\\n"""
    return [HEADER_S, role_token, HEADER_E, T_NL]


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestBasicParsing(unittest.TestCase):
    """System + user + assistant conversation."""

    def _build_basic_ids(self):
        # <bos> <header>system</header> Hello <eot>
        # <header>user</header> World <eot>
        # <header>assistant</header> Answer <eot>
        return (
            [BOS]
            + header(T_SYS) + [T_HELLO, EOT]
            + header(T_USER) + [T_WORLD, EOT]
            + header(T_ASST) + [T_ANSWER, EOT]
        )

    def test_segment_count(self):
        ext = make_extractor()
        segs = ext.extract(self._build_basic_ids())
        assert len(segs) == 3

    def test_roles(self):
        ext = make_extractor()
        segs = ext.extract(self._build_basic_ids())
        assert segs[0].role == "SYSTEM_PROMPT"
        assert segs[1].role == "USER_MESSAGE"
        assert segs[2].role == "ASSISTANT_MESSAGE"

    def test_boundaries_cover_all_tokens(self):
        ids = self._build_basic_ids()
        ext = make_extractor()
        segs = ext.extract(ids)
        # First segment starts at 0 (absorbs BOS)
        assert segs[0].start_idx == 0
        # Last segment ends at len(ids)
        assert segs[-1].end_idx == len(ids)
        # No gaps between segments
        for i in range(1, len(segs)):
            assert segs[i].start_idx == segs[i - 1].end_idx

    def test_turn_indices(self):
        ext = make_extractor()
        segs = ext.extract(self._build_basic_ids())
        assert segs[0].turn_index == 0  # system
        assert segs[1].turn_index == 0  # first user
        assert segs[2].turn_index == 0  # first assistant


class TestMultiTurn(unittest.TestCase):
    """Two user-assistant turns."""

    def _build_multi_turn_ids(self):
        return (
            [BOS]
            + header(T_SYS) + [T_HELLO, EOT]
            + header(T_USER) + [T_HELLO, EOT]
            + header(T_ASST) + [T_ANSWER, EOT]
            + header(T_USER) + [T_WORLD, EOT]
            + header(T_ASST) + [T_FINAL, EOT]
        )

    def test_turn_indices_increment(self):
        ext = make_extractor()
        segs = ext.extract(self._build_multi_turn_ids())
        assert len(segs) == 5
        assert segs[0].turn_index == 0  # system
        assert segs[1].turn_index == 0  # user 1
        assert segs[2].turn_index == 0  # assistant 1
        assert segs[3].turn_index == 1  # user 2
        assert segs[4].turn_index == 1  # assistant 2


class TestToolCall(unittest.TestCase):
    """Assistant with <|python_tag|> → TOOL_CALL, ipython → TOOL_RESULT."""

    def _build_tool_ids(self):
        return (
            [BOS]
            + header(T_SYS) + [T_HELLO, EOT]
            + header(T_USER) + [T_WORLD, EOT]
            + header(T_ASST) + [PYTHON_TAG, T_CODE, EOT]  # tool call
            + header(T_IPYTHON) + [T_RESULT, EOT]          # tool result
            + header(T_ASST) + [T_ANSWER, EOT]             # final answer
        )

    def test_tool_call_role(self):
        ext = make_extractor()
        segs = ext.extract(self._build_tool_ids())
        roles = [s.role for s in segs]
        assert roles == [
            "SYSTEM_PROMPT",
            "USER_MESSAGE",
            "TOOL_CALL",
            "TOOL_RESULT",
            "ASSISTANT_MESSAGE",
        ]

    def test_tool_turn_index(self):
        ext = make_extractor()
        segs = ext.extract(self._build_tool_ids())
        # All in the same turn (only one user message)
        for s in segs:
            assert s.turn_index == 0


class TestThinkingTrace(unittest.TestCase):
    """Assistant message starting with <think>…</think> + actual answer."""

    def _build_thinking_ids(self):
        return (
            [BOS]
            + header(T_USER) + [T_HELLO, EOT]
            + header(T_ASST) + [T_THINK_S, T_REASON, T_THINK_E, T_FINAL, EOT]
        )

    def test_thinking_split(self):
        ext = make_extractor()
        segs = ext.extract(self._build_thinking_ids())
        roles = [s.role for s in segs]
        assert roles == ["USER_MESSAGE", "THINKING_TRACE", "ASSISTANT_MESSAGE"]

    def test_thinking_boundaries(self):
        ext = make_extractor()
        ids = self._build_thinking_ids()
        segs = ext.extract(ids)
        # No gaps
        assert segs[0].start_idx == 0
        assert segs[-1].end_idx == len(ids)
        for i in range(1, len(segs)):
            assert segs[i].start_idx == segs[i - 1].end_idx

    def test_thinking_only(self):
        """Entire assistant message is thinking (no content after </think>)."""
        ids = (
            [BOS]
            + header(T_USER) + [T_HELLO, EOT]
            + header(T_ASST) + [T_THINK_S, T_REASON, T_THINK_E, EOT]
        )
        ext = make_extractor()
        segs = ext.extract(ids)
        roles = [s.role for s in segs]
        assert roles == ["USER_MESSAGE", "THINKING_TRACE"]

    def test_thinking_unclosed(self):
        """<think> without </think> — entire block is THINKING_TRACE."""
        ids = (
            [BOS]
            + header(T_USER) + [T_HELLO, EOT]
            + header(T_ASST) + [T_THINK_S, T_REASON, EOT]
        )
        ext = make_extractor()
        segs = ext.extract(ids)
        roles = [s.role for s in segs]
        assert roles == ["USER_MESSAGE", "THINKING_TRACE"]


class TestConsecutiveAssistant(unittest.TestCase):
    """Multiple consecutive assistant messages share turn_index."""

    def _build_ids(self):
        return (
            [BOS]
            + header(T_USER) + [T_HELLO, EOT]
            + header(T_ASST) + [T_ANSWER, EOT]
            + header(T_ASST) + [T_FINAL, EOT]
        )

    def test_both_assistant(self):
        ext = make_extractor()
        segs = ext.extract(self._build_ids())
        assert len(segs) == 3
        assert segs[1].role == "ASSISTANT_MESSAGE"
        assert segs[2].role == "ASSISTANT_MESSAGE"
        assert segs[1].turn_index == segs[2].turn_index == 0


class TestEmptyInput(unittest.TestCase):
    def test_empty_list(self):
        ext = make_extractor()
        assert ext.extract([]) == []

    def test_bos_only(self):
        ext = make_extractor()
        segs = ext.extract([BOS])
        assert segs == []


class TestNoSystemMessage(unittest.TestCase):
    """Conversation without system prompt."""

    def test_user_assistant_only(self):
        ids = (
            [BOS]
            + header(T_USER) + [T_HELLO, EOT]
            + header(T_ASST) + [T_ANSWER, EOT]
        )
        ext = make_extractor()
        segs = ext.extract(ids)
        assert len(segs) == 2
        assert segs[0].role == "USER_MESSAGE"
        assert segs[1].role == "ASSISTANT_MESSAGE"
        assert segs[0].turn_index == 0
        assert segs[1].turn_index == 0


# ---------------------------------------------------------------------------
# Run with python directly
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main(verbosity=2)
