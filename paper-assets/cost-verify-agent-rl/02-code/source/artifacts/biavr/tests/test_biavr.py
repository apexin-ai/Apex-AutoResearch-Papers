"""Unit tests for B-IAVR modules. No GPU required."""

import pytest
from unittest.mock import MagicMock
from biavr.action_canonicalize import canonicalize_action, actions_equivalent
from biavr.reward import biavr_reward, lagrangian_update, BIAVRTracker
from biavr.verify_mechanism import (
    parse_verify_token, extract_action_from_response,
    register_verify_special_token, get_verify_token_id, VERIFY_TOKEN,
)
from biavr.pre_action import build_pre_action_messages, compare_actions, PreActionProfiler


# ── action_canonicalize ──────────────────────────────────────────────

class TestCanonicalizeAction:
    def test_go_to(self):
        assert canonicalize_action("go to desk 1") == ("go", "desk 1", None)

    def test_take_from(self):
        assert canonicalize_action("take lamp 1 from desk 1") == ("take", "lamp 1", "desk 1")

    def test_put_in(self):
        assert canonicalize_action("put lamp 1 in desk 1") == ("put", "lamp 1", "desk 1")

    def test_put_on(self):
        assert canonicalize_action("put lamp 1 on desk 1") == ("put", "lamp 1", "desk 1")

    def test_open(self):
        assert canonicalize_action("open fridge 1") == ("open", "fridge 1", None)

    def test_close(self):
        assert canonicalize_action("close drawer 1") == ("close", "drawer 1", None)

    def test_use(self):
        assert canonicalize_action("use desklamp 1") == ("use", "desklamp 1", None)

    def test_heat_with(self):
        assert canonicalize_action("heat apple 1 with microwave 1") == ("heat", "apple 1", "microwave 1")

    def test_cool_with(self):
        assert canonicalize_action("cool apple 1 with fridge 1") == ("cool", "apple 1", "fridge 1")

    def test_clean_with(self):
        assert canonicalize_action("clean mug 1 with sinkbasin 1") == ("clean", "mug 1", "sinkbasin 1")

    def test_examine(self):
        assert canonicalize_action("examine mirror 1") == ("examine", "mirror 1", None)

    def test_inventory(self):
        assert canonicalize_action("inventory") == ("inventory", None, None)

    def test_look(self):
        assert canonicalize_action("look") == ("look", None, None)

    def test_case_insensitive(self):
        assert canonicalize_action("Go To Desk 1") == ("go", "desk 1", None)

    def test_extra_whitespace(self):
        assert canonicalize_action("  go  to   desk   1  ") == ("go", "desk 1", None)

    def test_take_with_extra_spaces(self):
        assert canonicalize_action("  take  lamp 1  from  desk 1  ") == ("take", "lamp 1", "desk 1")


class TestActionsEquivalent:
    def test_same(self):
        assert actions_equivalent("go to desk 1", "go to desk 1")

    def test_case_differ(self):
        assert actions_equivalent("Go To Desk 1", "go to desk 1")

    def test_different(self):
        assert not actions_equivalent("go to desk 1", "go to shelf 1")

    def test_different_verb(self):
        assert not actions_equivalent("open fridge 1", "close fridge 1")


# ── reward ───────────────────────────────────────────────────────────

class TestBIAVRReward:
    def test_no_verify(self):
        assert biavr_reward(False, False, lambda_cost=0.1) == 0.0
        assert biavr_reward(False, True, lambda_cost=0.1) == 0.0

    def test_verify_no_change(self):
        assert biavr_reward(True, False, lambda_cost=0.1) == pytest.approx(-0.1)

    def test_verify_with_change(self):
        assert biavr_reward(True, True, lambda_cost=0.1, alpha=1.0) == pytest.approx(0.9)

    def test_verify_with_change_custom_alpha(self):
        assert biavr_reward(True, True, lambda_cost=0.2, alpha=0.5) == pytest.approx(0.3)

    def test_verify_no_change_high_lambda(self):
        assert biavr_reward(True, False, lambda_cost=2.0) == pytest.approx(-2.0)


class TestLagrangianUpdate:
    def test_rate_above_beta_increases_lambda(self):
        new_lambda = lagrangian_update(0.1, mean_verify_rate=0.5, beta=0.3, eta=0.01)
        assert new_lambda > 0.1

    def test_rate_below_beta_decreases_lambda(self):
        new_lambda = lagrangian_update(0.1, mean_verify_rate=0.1, beta=0.3, eta=0.01)
        assert new_lambda < 0.1

    def test_rate_equals_beta_no_change(self):
        new_lambda = lagrangian_update(0.1, mean_verify_rate=0.3, beta=0.3, eta=0.01)
        assert new_lambda == pytest.approx(0.1)

    def test_lambda_non_negative(self):
        new_lambda = lagrangian_update(0.001, mean_verify_rate=0.0, beta=0.3, eta=0.1)
        assert new_lambda >= 0.0

    def test_exact_values(self):
        # lambda = max(0, 0.1 + 0.01 * (0.5 - 0.3)) = max(0, 0.1 + 0.002) = 0.102
        assert lagrangian_update(0.1, 0.5, 0.3, 0.01) == pytest.approx(0.102)


class TestBIAVRTracker:
    def test_empty_tracker(self):
        tracker = BIAVRTracker()
        assert tracker.verify_rate == 0.0
        assert tracker.total_step_reward == 0.0

    def test_record_steps(self):
        tracker = BIAVRTracker(lambda_cost=0.1, alpha=1.0)
        r1 = tracker.record_step(verify=True, action_changed=True)
        assert r1 == pytest.approx(0.9)
        r2 = tracker.record_step(verify=True, action_changed=False)
        assert r2 == pytest.approx(-0.1)
        r3 = tracker.record_step(verify=False, action_changed=False)
        assert r3 == 0.0
        assert tracker.verify_rate == pytest.approx(2 / 3)
        assert tracker.informativeness_rate == pytest.approx(0.5)
        assert tracker.total_step_reward == pytest.approx(0.8)

    def test_update_lambda_resets(self):
        tracker = BIAVRTracker(lambda_cost=0.1, beta=0.3, eta=0.01)
        tracker.record_step(True, False)
        tracker.record_step(True, False)
        tracker.record_step(False, False)
        # verify_rate = 2/3 ≈ 0.667 > beta=0.3 → lambda increases
        old_lambda = tracker.lambda_cost
        new_lambda = tracker.update_lambda()
        assert new_lambda > old_lambda
        assert len(tracker._verify_decisions) == 0

    def test_metrics(self):
        tracker = BIAVRTracker(lambda_cost=0.1)
        tracker.record_step(True, True)
        metrics = tracker.get_metrics()
        assert "biavr/lambda" in metrics
        assert "biavr/verify_rate" in metrics
        assert metrics["biavr/n_steps"] == 1


# ── verify_mechanism ─────────────────────────────────────────────────

class TestParseVerifyToken:
    def test_with_verify(self):
        resp = "<VERIFY><think>assessment</think><answer>go to desk 1</answer>"
        verify, cleaned = parse_verify_token(resp)
        assert verify is True
        assert cleaned.startswith("<think>")

    def test_without_verify(self):
        resp = "<think>reasoning</think><answer>go to desk 1</answer>"
        verify, cleaned = parse_verify_token(resp)
        assert verify is False
        assert cleaned == resp

    def test_with_verify_whitespace(self):
        resp = "  <VERIFY>  <think>text</think><answer>act</answer>"
        verify, cleaned = parse_verify_token(resp)
        assert verify is True

    def test_verify_not_at_start(self):
        resp = "<think>some text</think><VERIFY><answer>act</answer>"
        verify, cleaned = parse_verify_token(resp)
        assert verify is False

    def test_empty_string(self):
        verify, cleaned = parse_verify_token("")
        assert verify is False
        assert cleaned == ""


class TestExtractAction:
    def test_normal(self):
        resp = "<think>reasoning</think><answer>go to desk 1</answer>"
        assert extract_action_from_response(resp) == "go to desk 1"

    def test_with_whitespace(self):
        resp = "<answer>  open fridge 1  </answer>"
        assert extract_action_from_response(resp) == "open fridge 1"

    def test_no_answer_tag(self):
        assert extract_action_from_response("just some text") is None

    def test_multiline(self):
        resp = "<answer>\ntake lamp 1 from desk 1\n</answer>"
        assert extract_action_from_response(resp) == "take lamp 1 from desk 1"


# ── pre_action ───────────────────────────────────────────────────────

class TestBuildPreActionMessages:
    def test_replaces_system_prompt(self):
        history = [
            {"role": "system", "content": "Original system prompt with self-guidance"},
            {"role": "user", "content": "observation 1"},
            {"role": "assistant", "content": "<answer>go to desk 1</answer>"},
        ]
        result = build_pre_action_messages(history, "observation 2")
        assert result[0]["role"] == "system"
        assert "self-guidance" not in result[0]["content"].lower()
        assert result[-1]["content"] == "observation 2"

    def test_preserves_user_assistant_turns(self):
        history = [
            {"role": "system", "content": "sys"},
            {"role": "user", "content": "obs1"},
            {"role": "assistant", "content": "act1"},
            {"role": "user", "content": "obs2"},
        ]
        result = build_pre_action_messages(history, "obs3")
        roles = [m["role"] for m in result]
        assert roles == ["system", "user", "assistant", "user", "user"]

    def test_no_duplicate_observation(self):
        history = [
            {"role": "system", "content": "sys"},
            {"role": "user", "content": "current_obs"},
        ]
        result = build_pre_action_messages(history, "current_obs")
        user_msgs = [m for m in result if m["role"] == "user"]
        assert len(user_msgs) == 1


class TestCompareActions:
    def test_same_action(self):
        assert compare_actions("go to desk 1", "go to desk 1") is False

    def test_different_action(self):
        assert compare_actions("go to desk 1", "go to shelf 1") is True

    def test_none_pre(self):
        assert compare_actions(None, "go to desk 1") is False

    def test_none_post(self):
        assert compare_actions("go to desk 1", None) is False

    def test_both_none(self):
        assert compare_actions(None, None) is False

    def test_case_insensitive(self):
        assert compare_actions("Go To Desk 1", "go to desk 1") is False


# ── register_verify_special_token (D031 W1) ────────────────────────

class TestRegisterVerifySpecialToken:
    def test_adds_token_and_resizes(self):
        tokenizer = MagicMock()
        tokenizer.add_special_tokens.return_value = 1
        tokenizer.__len__ = lambda self: 32001
        model = MagicMock()

        n = register_verify_special_token(tokenizer, model)
        assert n == 1
        tokenizer.add_special_tokens.assert_called_once_with(
            {"additional_special_tokens": [VERIFY_TOKEN]}
        )
        model.resize_token_embeddings.assert_called_once_with(32001)

    def test_already_registered_no_resize(self):
        tokenizer = MagicMock()
        tokenizer.add_special_tokens.return_value = 0
        model = MagicMock()

        n = register_verify_special_token(tokenizer, model)
        assert n == 0
        model.resize_token_embeddings.assert_not_called()

    def test_no_model_provided(self):
        tokenizer = MagicMock()
        tokenizer.add_special_tokens.return_value = 1
        n = register_verify_special_token(tokenizer)
        assert n == 1

    def test_get_verify_token_id_single(self):
        tokenizer = MagicMock()
        tokenizer.encode.return_value = [32000]
        tid = get_verify_token_id(tokenizer)
        assert tid == 32000

    def test_get_verify_token_id_not_registered(self):
        tokenizer = MagicMock()
        tokenizer.encode.return_value = [1, 2, 3, 4, 5, 6, 7, 8]
        with pytest.raises(RuntimeError, match="tokenizes to 8 tokens"):
            get_verify_token_id(tokenizer)


# ── PreActionProfiler (D031 W2) ────────────────────────────────────

class TestPreActionProfiler:
    def test_empty(self):
        p = PreActionProfiler()
        assert p.n_samples == 0
        assert p.mean_pre_latency == 0.0
        assert p.overhead_ratio == 0.0
        assert "No a_pre samples" in p.summary()

    def test_record_and_metrics(self):
        p = PreActionProfiler()
        p.record_main_action(1.0)
        p.record_main_action(1.0)
        p.record_pre_action(0.2)
        p.record_pre_action(0.3)

        assert p.n_samples == 2
        assert p.mean_pre_latency == pytest.approx(0.25)
        assert p.mean_main_latency == pytest.approx(1.0)
        assert p.overhead_ratio == pytest.approx(0.25)

        metrics = p.get_metrics()
        assert metrics["biavr/pre_action_overhead_ratio"] == pytest.approx(0.25)
        assert metrics["biavr/pre_action_n_samples"] == 2

    def test_summary_format(self):
        p = PreActionProfiler()
        p.record_main_action(2.0)
        p.record_pre_action(0.5)
        s = p.summary()
        assert "0.500s" in s
        assert "25.0%" in s
