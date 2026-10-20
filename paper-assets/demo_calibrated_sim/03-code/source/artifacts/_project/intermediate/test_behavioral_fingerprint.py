"""Tests for behavioral_fingerprint module."""

import pytest
from behavioral_fingerprint import (
    QuestionDetector,
    PolitenessDetector,
    BehavioralFingerprint,
    analyze_traces,
)


# ---- QuestionDetector ----

class TestQuestionDetector:
    def setup_method(self):
        self.det = QuestionDetector()

    def test_direct_question_mark(self):
        has_q, qs = self.det.detect("What is your order number?")
        assert has_q is True
        assert len(qs) == 1

    def test_interrogative_word_no_question_mark(self):
        has_q, qs = self.det.detect("Tell me what happened")
        assert has_q is False

    def test_mixed_sentences(self):
        has_q, qs = self.det.detect("I want to return this. Can I get a refund?")
        assert has_q is True
        assert len(qs) == 1

    def test_no_question(self):
        has_q, qs = self.det.detect("I need to cancel my order.")
        assert has_q is False
        assert qs == []

    def test_tag_question(self):
        has_q, qs = self.det.detect("This is correct, right?")
        assert has_q is True

    def test_empty_string(self):
        has_q, qs = self.det.detect("")
        assert has_q is False
        assert qs == []


# ---- PolitenessDetector ----

class TestPolitenessDetector:
    def setup_method(self):
        self.det = PolitenessDetector()

    def test_please(self):
        has_p, markers = self.det.detect("Please help me")
        assert has_p is True
        assert "please" in markers

    def test_thank_you(self):
        has_p, markers = self.det.detect("Thank you for your help")
        assert has_p is True
        assert "thank you" in markers

    def test_no_politeness(self):
        has_p, markers = self.det.detect("I want a refund now")
        assert has_p is False
        assert markers == []

    def test_multiple_markers(self):
        has_p, markers = self.det.detect("Please check and thank you")
        assert has_p is True
        assert "please" in markers
        assert "thank you" in markers

    def test_case_insensitive(self):
        has_p, markers = self.det.detect("PLEASE help")
        assert has_p is True
        assert "please" in markers


# ---- BehavioralFingerprint ----

class TestBehavioralFingerprint:
    def test_five_turn_conversation(self):
        trace = [
            {"role": "user", "content": "What is the status of my order?"},
            {"role": "agent", "content": "Let me check that for you."},
            {"role": "user", "content": "Please hurry up."},
            {"role": "agent", "content": "Your order is on its way."},
            {"role": "user", "content": "I see, it shipped yesterday."},
        ]
        fp = BehavioralFingerprint()
        result = fp.extract(trace)

        assert result.total_turns == 5
        assert result.total_user_turns == 3
        assert len(result.turn_details) == 3

        # turn 0: question, no politeness
        assert result.turn_details[0].has_question is True
        assert result.turn_details[0].has_politeness is False

        # turn 1 (index 2 in trace): politeness, no question
        assert result.turn_details[1].has_politeness is True
        assert result.turn_details[1].has_question is False

        # turn 2 (index 4 in trace): neither
        assert result.turn_details[2].has_question is False
        assert result.turn_details[2].has_politeness is False

        assert result.question_rate == pytest.approx(1 / 3)
        assert result.politeness_rate == pytest.approx(1 / 3)

    def test_empty_trace(self):
        fp = BehavioralFingerprint()
        result = fp.extract([])
        assert result.total_user_turns == 0
        assert result.question_rate == 0.0
        assert result.politeness_rate == 0.0

    def test_only_agent_turns(self):
        trace = [
            {"role": "agent", "content": "Hello!"},
            {"role": "agent", "content": "How can I help?"},
        ]
        fp = BehavioralFingerprint()
        result = fp.extract(trace)
        assert result.total_user_turns == 0
        assert result.question_rate == 0.0


# ---- analyze_traces ----

class TestAnalyzeTraces:
    def test_batch_two_traces(self):
        trace1 = [
            {"role": "user", "content": "Can you help me?"},
            {"role": "agent", "content": "Sure."},
            {"role": "user", "content": "Thanks, please check order 123."},
        ]
        # trace1: 2 user turns, 1 question (turn 0), 1 politeness (turn 1)
        # question_rate = 0.5, politeness_rate = 0.5

        trace2 = [
            {"role": "user", "content": "I need a refund."},
            {"role": "agent", "content": "Processing."},
        ]
        # trace2: 1 user turn, 0 questions, 0 politeness
        # question_rate = 0.0, politeness_rate = 0.0

        result = analyze_traces([trace1, trace2])
        assert result.num_traces == 2
        assert result.mean_question_rate == pytest.approx(0.25)
        assert result.mean_politeness_rate == pytest.approx(0.25)
        assert result.std_question_rate > 0
        assert result.std_politeness_rate > 0

    def test_empty_batch(self):
        result = analyze_traces([])
        assert result.num_traces == 0
        assert result.mean_question_rate == 0.0
