"""End-to-end mock test for the comm_gate_mas MVP pipeline.

Validates: module interface compatibility, output format consistency,
action_level 3-tier classification logic, and analysis report generation.
No real LLM API needed — all data is hand-crafted.
"""

import json
import os
import sys
import tempfile

import pytest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
sys.path.insert(0, SRC_DIR)
sys.path.insert(0, PROJECT_ROOT)

from src.local_impact import _assign_role, classify_action_level
from src.analysis import (
    analysis_function_action,
    analysis_function_correctness,
    analysis_ldim_agreement,
    analysis_remove_vs_neutralize,
    merge_data,
    pass_fail_check,
)


# ---------------------------------------------------------------------------
# Mock trace data: 5 tasks, each with 4 messages
# ---------------------------------------------------------------------------

def _ts(i):
    return f"2026-04-19T00:00:{i:02d}Z"


MOCK_TRACES = [
    {
        "task_id": "mock_001",
        "question": "A baker has 5 trays with 12 cookies each. How many cookies in total?",
        "ground_truth": "60",
        "messages": [
            {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "Step 1: We need to multiply 5 trays by 12 cookies.\nStep 2: 5 × 12 = 60.\nThe answer is 60.", "round": 0, "timestamp": _ts(0)},
            {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "The calculation is correct. 5 trays times 12 cookies gives 60 cookies total.\nThe answer is 60.", "round": 1, "timestamp": _ts(1)},
            {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "Confirmed. 5 × 12 = 60 cookies.\nThe answer is 60.", "round": 2, "timestamp": _ts(2)},
            {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "Final verification: 60 cookies is correct.\nThe answer is 60.", "round": 3, "timestamp": _ts(3)},
        ],
        "final_answer": "60",
        "is_correct": True,
        "metadata": {"model": "mock", "temperature": 0, "num_agents": 2, "max_rounds": 6},
    },
    {
        "task_id": "mock_002",
        "question": "A store sells pencils at $3 each. John buys 7 pencils. How much does he pay?",
        "ground_truth": "21",
        "messages": [
            {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "Step 1: Price per pencil = $3.\nStep 2: 3 × 7 = 18.\nThe answer is 18.", "round": 0, "timestamp": _ts(10)},
            {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "The multiplication is wrong. 3 × 7 = 21, not 18.\nThe answer is 21.", "round": 1, "timestamp": _ts(11)},
            {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "You are right. Let me recalculate: 3 × 7 = 21.\nThe answer is 21.", "round": 2, "timestamp": _ts(12)},
            {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "Correct. The total is $21.\nThe answer is 21.", "round": 3, "timestamp": _ts(13)},
        ],
        "final_answer": "21",
        "is_correct": True,
        "metadata": {"model": "mock", "temperature": 0, "num_agents": 2, "max_rounds": 6},
    },
    {
        "task_id": "mock_003",
        "question": "A garden has 3 rows with 8 flowers each and 2 extra flowers. How many flowers?",
        "ground_truth": "26",
        "messages": [
            {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "Step 1: 3 × 8 = 24 flowers in rows.\nI think we need to add the extras but not sure how many.\nThe answer is 24.", "round": 0, "timestamp": _ts(20)},
            {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "Good start. The problem says there are 2 extra flowers.\nSo total = 24 + 2 = 26.\nThe answer is 26.", "round": 1, "timestamp": _ts(21)},
            {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "Right, I missed the extra 2. So 24 + 2 = 26.\nThe answer is 26.", "round": 2, "timestamp": _ts(22)},
            {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "Correct. 26 flowers total.\nThe answer is 26.", "round": 3, "timestamp": _ts(23)},
        ],
        "final_answer": "26",
        "is_correct": True,
        "metadata": {"model": "mock", "temperature": 0, "num_agents": 2, "max_rounds": 6},
    },
    {
        "task_id": "mock_004",
        "question": "A car travels 40 miles per hour for 3 hours. How far does it go?",
        "ground_truth": "120",
        "messages": [
            {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "Distance = speed × time = 40 × 3 = 120 miles.\nThe answer is 120.", "round": 0, "timestamp": _ts(30)},
            {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "Yes, that is correct. 40 miles per hour times 3 hours equals 120 miles.\nThe answer is 120.", "round": 1, "timestamp": _ts(31)},
            {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "Great, confirmed. 120 miles.\nThe answer is 120.", "round": 2, "timestamp": _ts(32)},
            {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "Agreed. The answer is definitely 120.\nThe answer is 120.", "round": 3, "timestamp": _ts(33)},
        ],
        "final_answer": "120",
        "is_correct": True,
        "metadata": {"model": "mock", "temperature": 0, "num_agents": 2, "max_rounds": 6},
    },
    {
        "task_id": "mock_005",
        "question": "A recipe needs 4 eggs for 6 servings. How many eggs for 9 servings?",
        "ground_truth": "6",
        "messages": [
            {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "Eggs per serving = 4/6 = 0.5.\nFor 9 servings: 0.5 × 9 = 4.5. Rounding up to 5.\nThe answer is 5.", "round": 0, "timestamp": _ts(40)},
            {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "The calculation has an error. 4/6 is about 0.667, not 0.5.\n0.667 × 9 = 6.\nThe answer is 5.", "round": 1, "timestamp": _ts(41)},
            {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "Hmm, using cross multiplication: 4/6 = x/9, so x = 4×9/6 = 36/6 = 6. But the answer is 5 as you said.\nThe answer is 5.", "round": 2, "timestamp": _ts(42)},
            {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "Right, the answer is 5.\nThe answer is 5.", "round": 3, "timestamp": _ts(43)},
        ],
        "final_answer": "5",
        "is_correct": False,
        "metadata": {"model": "mock", "temperature": 0, "num_agents": 2, "max_rounds": 6},
    },
]


# ---------------------------------------------------------------------------
# Mock impact data: one record per message except the last in each task
# ---------------------------------------------------------------------------

MOCK_IMPACT = [
    # Task 1: solver correct, checker confirms (redundant)
    {"task_id": "mock_001", "message_index": 0, "sender": "MathSolver", "receiver": "AnswerChecker",
     "remove": {"action_level": "reasoning_step", "semantic_similarity": 0.85, "original_preview": "The calculation is correct...", "ablated_preview": "Let me calculate 5 × 12..."},
     "neutralize": {"action_level": "surface_only", "semantic_similarity": 0.92, "original_preview": "The calculation is correct...", "ablated_preview": "I see. 5 × 12 = 60..."},
     "ldim": {"top1_match": True, "top5_overlap": 0.8, "logprob_shift": -0.3, "token_match_rate": 0.8}},
    {"task_id": "mock_001", "message_index": 1, "sender": "AnswerChecker", "receiver": "MathSolver",
     "remove": {"action_level": "surface_only", "semantic_similarity": 0.95, "original_preview": "Confirmed...", "ablated_preview": "Yes, 60 cookies..."},
     "neutralize": {"action_level": "surface_only", "semantic_similarity": 0.96, "original_preview": "Confirmed...", "ablated_preview": "60 cookies confirmed..."},
     "ldim": {"top1_match": True, "top5_overlap": 0.9, "logprob_shift": -0.1, "token_match_rate": 0.9}},
    {"task_id": "mock_001", "message_index": 2, "sender": "MathSolver", "receiver": "AnswerChecker",
     "remove": {"action_level": "surface_only", "semantic_similarity": 0.97, "original_preview": "Final verification...", "ablated_preview": "60 is correct..."},
     "neutralize": {"action_level": "surface_only", "semantic_similarity": 0.98, "original_preview": "Final verification...", "ablated_preview": "60 cookies..."},
     "ldim": {"top1_match": True, "top5_overlap": 0.95, "logprob_shift": -0.05, "token_match_rate": 0.95}},

    # Task 2: solver wrong, checker corrects (verification)
    {"task_id": "mock_002", "message_index": 0, "sender": "MathSolver", "receiver": "AnswerChecker",
     "remove": {"action_level": "final_answer", "semantic_similarity": 0.55, "original_preview": "The multiplication is wrong...", "ablated_preview": "3 × 7 = 18..."},
     "neutralize": {"action_level": "final_answer", "semantic_similarity": 0.60, "original_preview": "The multiplication is wrong...", "ablated_preview": "OK. 3 × 7 = 18..."},
     "ldim": {"top1_match": False, "top5_overlap": 0.3, "logprob_shift": -2.1, "token_match_rate": 0.2}},
    {"task_id": "mock_002", "message_index": 1, "sender": "AnswerChecker", "receiver": "MathSolver",
     "remove": {"action_level": "final_answer", "semantic_similarity": 0.60, "original_preview": "You are right...", "ablated_preview": "Let me try 3 × 7 = 18..."},
     "neutralize": {"action_level": "reasoning_step", "semantic_similarity": 0.70, "original_preview": "You are right...", "ablated_preview": "Hmm, recalculating..."},
     "ldim": {"top1_match": False, "top5_overlap": 0.4, "logprob_shift": -1.5, "token_match_rate": 0.3}},
    {"task_id": "mock_002", "message_index": 2, "sender": "MathSolver", "receiver": "AnswerChecker",
     "remove": {"action_level": "surface_only", "semantic_similarity": 0.93, "original_preview": "Correct...", "ablated_preview": "The total is $21..."},
     "neutralize": {"action_level": "surface_only", "semantic_similarity": 0.94, "original_preview": "Correct...", "ablated_preview": "21 dollars..."},
     "ldim": {"top1_match": True, "top5_overlap": 0.85, "logprob_shift": -0.2, "token_match_rate": 0.85}},

    # Task 3: solver partial, checker scaffolds
    {"task_id": "mock_003", "message_index": 0, "sender": "MathSolver", "receiver": "AnswerChecker",
     "remove": {"action_level": "final_answer", "semantic_similarity": 0.65, "original_preview": "Good start...", "ablated_preview": "I think 24..."},
     "neutralize": {"action_level": "reasoning_step", "semantic_similarity": 0.75, "original_preview": "Good start...", "ablated_preview": "Acknowledged. 24 flowers..."},
     "ldim": {"top1_match": False, "top5_overlap": 0.35, "logprob_shift": -1.8, "token_match_rate": 0.35}},
    {"task_id": "mock_003", "message_index": 1, "sender": "AnswerChecker", "receiver": "MathSolver",
     "remove": {"action_level": "reasoning_step", "semantic_similarity": 0.80, "original_preview": "Right, I missed...", "ablated_preview": "So total is 26..."},
     "neutralize": {"action_level": "surface_only", "semantic_similarity": 0.90, "original_preview": "Right...", "ablated_preview": "OK, 26 flowers..."},
     "ldim": {"top1_match": True, "top5_overlap": 0.7, "logprob_shift": -0.5, "token_match_rate": 0.7}},
    {"task_id": "mock_003", "message_index": 2, "sender": "MathSolver", "receiver": "AnswerChecker",
     "remove": {"action_level": "surface_only", "semantic_similarity": 0.96, "original_preview": "Correct...", "ablated_preview": "26 total..."},
     "neutralize": {"action_level": "surface_only", "semantic_similarity": 0.97, "original_preview": "Correct...", "ablated_preview": "26..."},
     "ldim": {"top1_match": True, "top5_overlap": 0.92, "logprob_shift": -0.08, "token_match_rate": 0.92}},

    # Task 4: solver correct, checker redundant
    {"task_id": "mock_004", "message_index": 0, "sender": "MathSolver", "receiver": "AnswerChecker",
     "remove": {"action_level": "surface_only", "semantic_similarity": 0.94, "original_preview": "Yes, that is correct...", "ablated_preview": "40 × 3 = 120..."},
     "neutralize": {"action_level": "surface_only", "semantic_similarity": 0.95, "original_preview": "Yes...", "ablated_preview": "120 miles..."},
     "ldim": {"top1_match": True, "top5_overlap": 0.88, "logprob_shift": -0.15, "token_match_rate": 0.88}},
    {"task_id": "mock_004", "message_index": 1, "sender": "AnswerChecker", "receiver": "MathSolver",
     "remove": {"action_level": "surface_only", "semantic_similarity": 0.96, "original_preview": "Great, confirmed...", "ablated_preview": "120 miles..."},
     "neutralize": {"action_level": "surface_only", "semantic_similarity": 0.97, "original_preview": "Great...", "ablated_preview": "120..."},
     "ldim": {"top1_match": True, "top5_overlap": 0.91, "logprob_shift": -0.1, "token_match_rate": 0.91}},
    {"task_id": "mock_004", "message_index": 2, "sender": "MathSolver", "receiver": "AnswerChecker",
     "remove": {"action_level": "surface_only", "semantic_similarity": 0.98, "original_preview": "Agreed...", "ablated_preview": "120..."},
     "neutralize": {"action_level": "surface_only", "semantic_similarity": 0.99, "original_preview": "Agreed...", "ablated_preview": "120..."},
     "ldim": {"top1_match": True, "top5_overlap": 0.95, "logprob_shift": -0.02, "token_match_rate": 0.95}},

    # Task 5: solver wrong, checker also wrong (error propagation)
    {"task_id": "mock_005", "message_index": 0, "sender": "MathSolver", "receiver": "AnswerChecker",
     "remove": {"action_level": "reasoning_step", "semantic_similarity": 0.72, "original_preview": "The calculation has an error...", "ablated_preview": "4/6 = 0.5..."},
     "neutralize": {"action_level": "reasoning_step", "semantic_similarity": 0.78, "original_preview": "The calculation...", "ablated_preview": "Acknowledged. 0.5 × 9..."},
     "ldim": {"top1_match": False, "top5_overlap": 0.45, "logprob_shift": -1.2, "token_match_rate": 0.45}},
    {"task_id": "mock_005", "message_index": 1, "sender": "AnswerChecker", "receiver": "MathSolver",
     "remove": {"action_level": "reasoning_step", "semantic_similarity": 0.75, "original_preview": "Hmm, cross mult...", "ablated_preview": "So 0.667 × 9..."},
     "neutralize": {"action_level": "surface_only", "semantic_similarity": 0.88, "original_preview": "Hmm...", "ablated_preview": "The answer is 5..."},
     "ldim": {"top1_match": True, "top5_overlap": 0.6, "logprob_shift": -0.7, "token_match_rate": 0.6}},
    {"task_id": "mock_005", "message_index": 2, "sender": "MathSolver", "receiver": "AnswerChecker",
     "remove": {"action_level": "surface_only", "semantic_similarity": 0.93, "original_preview": "Right...", "ablated_preview": "The answer is 5..."},
     "neutralize": {"action_level": "surface_only", "semantic_similarity": 0.95, "original_preview": "Right...", "ablated_preview": "5..."},
     "ldim": {"top1_match": True, "top5_overlap": 0.88, "logprob_shift": -0.12, "token_match_rate": 0.88}},
]


# ---------------------------------------------------------------------------
# Mock annotation data: one record per message (all 20)
# ---------------------------------------------------------------------------

_ANNOTATION_MAP = {
    ("mock_001", 0): {"type": "information_provision", "confidence": 0.9, "reasoning": "Provides step-by-step calculation"},
    ("mock_001", 1): {"type": "acknowledgment", "confidence": 0.85, "reasoning": "Confirms already correct answer"},
    ("mock_001", 2): {"type": "acknowledgment", "confidence": 0.9, "reasoning": "Re-confirms same result"},
    ("mock_001", 3): {"type": "acknowledgment", "confidence": 0.92, "reasoning": "Final redundant verification"},
    ("mock_002", 0): {"type": "reasoning_guidance", "confidence": 0.88, "reasoning": "Sets up problem but errors"},
    ("mock_002", 1): {"type": "verification", "confidence": 0.95, "reasoning": "Corrects multiplication error"},
    ("mock_002", 2): {"type": "information_provision", "confidence": 0.82, "reasoning": "Reports corrected result"},
    ("mock_002", 3): {"type": "acknowledgment", "confidence": 0.87, "reasoning": "Final confirmation"},
    ("mock_003", 0): {"type": "reasoning_guidance", "confidence": 0.85, "reasoning": "Partial solution with rows"},
    ("mock_003", 1): {"type": "verification", "confidence": 0.9, "reasoning": "Catches missing extra flowers"},
    ("mock_003", 2): {"type": "information_provision", "confidence": 0.8, "reasoning": "Reports updated count"},
    ("mock_003", 3): {"type": "acknowledgment", "confidence": 0.88, "reasoning": "Final confirmation"},
    ("mock_004", 0): {"type": "information_provision", "confidence": 0.92, "reasoning": "Direct correct calculation"},
    ("mock_004", 1): {"type": "acknowledgment", "confidence": 0.9, "reasoning": "Redundant confirmation"},
    ("mock_004", 2): {"type": "acknowledgment", "confidence": 0.93, "reasoning": "Another confirmation"},
    ("mock_004", 3): {"type": "acknowledgment", "confidence": 0.95, "reasoning": "Yet another confirmation"},
    ("mock_005", 0): {"type": "reasoning_guidance", "confidence": 0.75, "reasoning": "Incorrect reasoning attempt"},
    ("mock_005", 1): {"type": "information_provision", "confidence": 0.88, "reasoning": "Provides wrong calculation result"},
    ("mock_005", 2): {"type": "information_provision", "confidence": 0.85, "reasoning": "Continues with wrong answer"},
    ("mock_005", 3): {"type": "acknowledgment", "confidence": 0.9, "reasoning": "Confirms wrong answer"},
}

MOCK_ANNOTATIONS = []
for trace in MOCK_TRACES:
    for i, msg in enumerate(trace["messages"]):
        ann = _ANNOTATION_MAP[(trace["task_id"], i)]
        MOCK_ANNOTATIONS.append({
            "task_id": trace["task_id"],
            "message_index": i,
            "sender": msg["sender"],
            "receiver": msg["receiver"],
            "annotation": ann,
            "content_preview": msg["content"][:100],
        })


# ---------------------------------------------------------------------------
# Mock correctness data: one record per message
# ---------------------------------------------------------------------------

_CORRECTNESS_MAP = {
    ("mock_001", 0): ("correct", 0.95, "All calculations are correct"),
    ("mock_001", 1): ("correct", 0.93, "Confirms correct result"),
    ("mock_001", 2): ("correct", 0.95, "Correct re-statement"),
    ("mock_001", 3): ("correct", 0.96, "Final answer correct"),
    ("mock_002", 0): ("incorrect", 0.92, "3 × 7 = 18 is wrong"),
    ("mock_002", 1): ("correct", 0.95, "Corrects to 21"),
    ("mock_002", 2): ("correct", 0.93, "Accepts correct answer"),
    ("mock_002", 3): ("correct", 0.94, "Final answer correct"),
    ("mock_003", 0): ("partially_correct", 0.85, "Row calc correct but missed extras"),
    ("mock_003", 1): ("correct", 0.92, "Adds extras correctly"),
    ("mock_003", 2): ("correct", 0.93, "Correct total"),
    ("mock_003", 3): ("correct", 0.94, "Confirmed correct"),
    ("mock_004", 0): ("correct", 0.95, "Distance formula correct"),
    ("mock_004", 1): ("correct", 0.93, "Confirmation correct"),
    ("mock_004", 2): ("correct", 0.95, "Still correct"),
    ("mock_004", 3): ("correct", 0.96, "Final confirmation correct"),
    ("mock_005", 0): ("incorrect", 0.88, "4/6 ≠ 0.5, wrong division"),
    ("mock_005", 1): ("partially_correct", 0.82, "Identifies error but gives wrong final"),
    ("mock_005", 2): ("not_applicable", 0.7, "Confused reasoning, defers"),
    ("mock_005", 3): ("incorrect", 0.85, "Confirms wrong answer 5"),
}

MOCK_CORRECTNESS = []
for trace in MOCK_TRACES:
    for i, msg in enumerate(trace["messages"]):
        corr, conf, reason = _CORRECTNESS_MAP[(trace["task_id"], i)]
        MOCK_CORRECTNESS.append({
            "task_id": trace["task_id"],
            "message_index": i,
            "sender": msg["sender"],
            "correctness": corr,
            "confidence": conf,
            "reasoning": reason,
            "ground_truth": trace["ground_truth"],
        })


# ===========================================================================
# Tests
# ===========================================================================


class TestMockDataIntegrity:
    def test_trace_count(self):
        assert len(MOCK_TRACES) == 5

    def test_trace_format(self):
        for trace in MOCK_TRACES:
            assert set(trace.keys()) == {"task_id", "question", "ground_truth", "messages", "final_answer", "is_correct", "metadata"}
            assert len(trace["messages"]) == 4
            for msg in trace["messages"]:
                assert set(msg.keys()) == {"sender", "receiver", "content", "round", "timestamp"}

    def test_total_messages(self):
        total = sum(len(t["messages"]) for t in MOCK_TRACES)
        assert total == 20

    def test_impact_count(self):
        assert len(MOCK_IMPACT) == 15

    def test_impact_format(self):
        for rec in MOCK_IMPACT:
            assert "task_id" in rec
            assert "message_index" in rec
            assert "remove" in rec and "neutralize" in rec and "ldim" in rec
            for track in ["remove", "neutralize"]:
                assert set(rec[track].keys()) == {"action_level", "semantic_similarity", "original_preview", "ablated_preview"}
            assert set(rec["ldim"].keys()) == {"top1_match", "top5_overlap", "logprob_shift", "token_match_rate"}

    def test_impact_action_level_coverage(self):
        remove_levels = {r["remove"]["action_level"] for r in MOCK_IMPACT}
        assert "final_answer" in remove_levels
        assert "reasoning_step" in remove_levels
        assert "surface_only" in remove_levels

    def test_annotation_count(self):
        assert len(MOCK_ANNOTATIONS) == 20

    def test_annotation_type_coverage(self):
        types = {a["annotation"]["type"] for a in MOCK_ANNOTATIONS}
        assert len(types) >= 4
        assert "information_provision" in types
        assert "reasoning_guidance" in types
        assert "acknowledgment" in types
        assert "verification" in types

    def test_correctness_count(self):
        assert len(MOCK_CORRECTNESS) == 20

    def test_correctness_coverage(self):
        vals = {c["correctness"] for c in MOCK_CORRECTNESS}
        assert vals == {"correct", "incorrect", "partially_correct", "not_applicable"}


class TestClassifyActionLevel:
    def test_final_answer_different(self):
        assert classify_action_level(
            "Step: 5×12=60. The answer is 60.",
            "Step: 5×12=55. The answer is 55.",
            semantic_similarity=0.85,
        ) == "final_answer"

    def test_reasoning_step_same_answer_different_text(self):
        assert classify_action_level(
            "Method A: 5×12=60. The answer is 60.",
            "Method B: 12×5=60. The answer is 60.",
            semantic_similarity=0.80,
        ) == "reasoning_step"

    def test_surface_only_high_similarity(self):
        assert classify_action_level(
            "The answer is 60.",
            "The answer is 60.",
            semantic_similarity=0.99,
        ) == "surface_only"

    def test_final_answer_one_none(self):
        result = classify_action_level(
            "The answer is 42.",
            "I'm not sure about this problem.",
            semantic_similarity=0.30,
        )
        assert result in ("final_answer", "reasoning_step")

    def test_reasoning_step_below_threshold(self):
        assert classify_action_level(
            "Step 1: 5 × 12 = 60. The answer is 60.",
            "Step 1: 5 × 12 = 60. The answer is 60.",
            semantic_similarity=0.90,
        ) == "reasoning_step"


class TestAssignRole:
    def test_solver_msg_from_checker_perspective(self):
        msg = {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "..."}
        assert _assign_role(msg, "AnswerChecker") == "user"

    def test_solver_msg_from_solver_perspective(self):
        msg = {"sender": "MathSolver", "receiver": "AnswerChecker", "content": "..."}
        assert _assign_role(msg, "MathSolver") == "assistant"

    def test_checker_msg_from_checker_perspective(self):
        msg = {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "..."}
        assert _assign_role(msg, "AnswerChecker") == "assistant"

    def test_checker_msg_from_solver_perspective(self):
        msg = {"sender": "AnswerChecker", "receiver": "MathSolver", "content": "..."}
        assert _assign_role(msg, "MathSolver") == "user"


class TestMergeData:
    @pytest.fixture
    def merged_df(self):
        return merge_data(MOCK_IMPACT, MOCK_ANNOTATIONS, MOCK_CORRECTNESS)

    def test_merge_returns_dataframe(self, merged_df):
        import pandas as pd
        assert isinstance(merged_df, pd.DataFrame)

    def test_merge_has_expanded_columns(self, merged_df):
        assert "remove_action_level" in merged_df.columns
        assert "neutralize_action_level" in merged_df.columns
        assert "ldim_top1_match" in merged_df.columns
        assert "ann_type" in merged_df.columns
        assert "correctness" in merged_df.columns

    def test_merge_row_count(self, merged_df):
        assert len(merged_df) >= 15

    def test_merge_has_semantic_similarity(self, merged_df):
        assert "remove_semantic_similarity" in merged_df.columns
        assert "neutralize_semantic_similarity" in merged_df.columns


class TestAnalysisFunctionAction:
    @pytest.fixture
    def merged_df(self):
        return merge_data(MOCK_IMPACT, MOCK_ANNOTATIONS, MOCK_CORRECTNESS)

    def test_returns_dict(self, merged_df):
        result = analysis_function_action(merged_df)
        assert isinstance(result, dict)

    def test_has_key_fields(self, merged_df):
        result = analysis_function_action(merged_df)
        if "error" not in result:
            assert "p_value" in result
            assert "action_change_rates" in result
            assert "contingency_table" in result
        else:
            pytest.skip(f"Insufficient data: {result['error']}")

    def test_action_change_rates_are_floats(self, merged_df):
        result = analysis_function_action(merged_df)
        if "action_change_rates" in result:
            for rate in result["action_change_rates"].values():
                assert isinstance(rate, float)
                assert 0.0 <= rate <= 1.0


class TestAnalysisFunctionCorrectness:
    @pytest.fixture
    def merged_df(self):
        return merge_data(MOCK_IMPACT, MOCK_ANNOTATIONS, MOCK_CORRECTNESS)

    def test_returns_dict(self, merged_df):
        result = analysis_function_correctness(merged_df)
        assert isinstance(result, dict)

    def test_has_correctness_info(self, merged_df):
        result = analysis_function_correctness(merged_df)
        assert "all_correctness_with_n" in result or "contingency_table" in result


class TestAnalysisLdimAgreement:
    @pytest.fixture
    def merged_df(self):
        return merge_data(MOCK_IMPACT, MOCK_ANNOTATIONS, MOCK_CORRECTNESS)

    def test_returns_dict(self, merged_df):
        result = analysis_ldim_agreement(merged_df)
        assert isinstance(result, dict)

    def test_has_agreement_fields(self, merged_df):
        result = analysis_ldim_agreement(merged_df)
        if "error" not in result:
            assert "percent_agreement" in result
            assert "cohens_kappa" in result
            assert "n" in result


class TestAnalysisRemoveVsNeutralize:
    @pytest.fixture
    def merged_df(self):
        return merge_data(MOCK_IMPACT, MOCK_ANNOTATIONS, MOCK_CORRECTNESS)

    def test_returns_dict(self, merged_df):
        result = analysis_remove_vs_neutralize(merged_df)
        assert isinstance(result, dict)

    def test_has_distributions(self, merged_df):
        result = analysis_remove_vs_neutralize(merged_df)
        if "error" not in result:
            assert "remove_distribution" in result
            assert "neutralize_distribution" in result
            assert "contingency_table" in result


class TestPassFailCheck:
    @pytest.fixture
    def merged_df(self):
        return merge_data(MOCK_IMPACT, MOCK_ANNOTATIONS, MOCK_CORRECTNESS)

    def test_returns_expected_structure(self, merged_df):
        func_action = analysis_function_action(merged_df)
        ldim_agree = analysis_ldim_agreement(merged_df)
        remove_vs_neut = analysis_remove_vs_neutralize(merged_df)
        result = pass_fail_check(merged_df, func_action, ldim_agree, remove_vs_neut, cross_model_kappa=0.65)
        assert "message_count" in result
        assert "chi2_significance" in result
        assert "kruskal_wallis" in result
        assert "cross_model_annotation" in result
        assert "remove_vs_neutralize" in result
        assert "ldim_agreement" in result
        assert result["cross_model_annotation"]["kappa"] == 0.65

    def test_message_count_below_threshold(self, merged_df):
        func_action = analysis_function_action(merged_df)
        ldim_agree = analysis_ldim_agreement(merged_df)
        result = pass_fail_check(merged_df, func_action, ldim_agree)
        assert result["message_count"]["pass"] is False
        assert result["message_count"]["threshold"] == 400
        assert result["message_count"]["value"] < 400


class TestTempFileRoundTrip:
    """Write mock data to temp JSONL files, read back, and verify analysis pipeline."""

    def test_full_pipeline_via_files(self, tmp_path):
        impact_path = tmp_path / "impact.jsonl"
        ann_path = tmp_path / "annotations.jsonl"
        corr_path = tmp_path / "correctness.jsonl"

        with open(impact_path, "w") as f:
            for rec in MOCK_IMPACT:
                f.write(json.dumps(rec) + "\n")
        with open(ann_path, "w") as f:
            for rec in MOCK_ANNOTATIONS:
                f.write(json.dumps(rec) + "\n")
        with open(corr_path, "w") as f:
            for rec in MOCK_CORRECTNESS:
                f.write(json.dumps(rec) + "\n")

        from src.analysis import load_jsonl
        impact_loaded = load_jsonl(str(impact_path))
        ann_loaded = load_jsonl(str(ann_path))
        corr_loaded = load_jsonl(str(corr_path))

        assert len(impact_loaded) == 15
        assert len(ann_loaded) == 20
        assert len(corr_loaded) == 20

        df = merge_data(impact_loaded, ann_loaded, corr_loaded)
        assert len(df) >= 15

        func_action = analysis_function_action(df)
        func_corr = analysis_function_correctness(df)
        ldim_agree = analysis_ldim_agreement(df)
        remove_vs_neut = analysis_remove_vs_neutralize(df)
        pf = pass_fail_check(df, func_action, ldim_agree, remove_vs_neut)

        assert isinstance(func_action, dict)
        assert isinstance(func_corr, dict)
        assert isinstance(ldim_agree, dict)
        assert isinstance(pf, dict)
        assert pf["message_count"]["threshold"] == 400
