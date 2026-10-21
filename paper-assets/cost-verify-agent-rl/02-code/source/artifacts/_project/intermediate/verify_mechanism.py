"""<VERIFY> token parsing and selective verification prompt construction."""

import re
from typing import Tuple, Optional

VERIFY_TOKEN = "<VERIFY>"


def register_verify_special_token(tokenizer, model=None):
    """Register <VERIFY> as a special token so it's never split into sub-tokens.

    Must be called before training. If a model is provided, resizes its
    embedding layer to accommodate the new token.

    Returns:
        int: Number of tokens actually added (0 if already registered).
    """
    n_added = tokenizer.add_special_tokens({"additional_special_tokens": [VERIFY_TOKEN]})
    if n_added > 0 and model is not None:
        model.resize_token_embeddings(len(tokenizer))
    return n_added


def get_verify_token_id(tokenizer) -> int:
    """Return the token id for <VERIFY>. Raises if not registered."""
    ids = tokenizer.encode(VERIFY_TOKEN, add_special_tokens=False)
    if len(ids) != 1:
        raise RuntimeError(
            f"<VERIFY> tokenizes to {len(ids)} tokens {ids}; "
            "call register_verify_special_token() first"
        )
    return ids[0]


def parse_verify_token(llm_response: str) -> Tuple[bool, str]:
    """Parse whether the agent chose to verify.

    The agent's raw response may look like:
      "<VERIFY><think>...</think><answer>go to desk 1</answer>"
    or without verify:
      "<think>I should go to the desk.</think><answer>go to desk 1</answer>"

    Returns:
        (should_verify, cleaned_response)
        - should_verify: True if response starts with <VERIFY>
        - cleaned_response: response with <VERIFY> prefix stripped
    """
    stripped = llm_response.strip()
    if stripped.startswith(VERIFY_TOKEN):
        return True, stripped[len(VERIFY_TOKEN):].strip()
    return False, stripped


def extract_action_from_response(response: str) -> Optional[str]:
    """Extract action string from <answer>...</answer> tags."""
    m = re.search(r"<answer>(.*?)</answer>", response, re.DOTALL)
    if m:
        return m.group(1).strip()
    return None


def build_biavr_system_prompt() -> str:
    """System prompt for B-IAVR selective verification."""
    return (
        "You are an expert agent in the ALFRED Embodied Environment.\n"
        "Complete household tasks by navigating and interacting with objects.\n"
        "\n"
        "At each step, you have TWO choices:\n"
        "\n"
        "1. **Verify then act**: Output <VERIFY> as the very first token, then produce "
        "a self-guidance assessment before choosing your action. Use this when you are "
        "uncertain about the best next step.\n"
        "   Format: <VERIFY><think>[Assessment: positive/neutral/negative] - evaluate "
        "your progress.\n"
        "   [Reasoning: analyze what has been accomplished and what remains.]\n"
        "   [Suggestion: the best next action from admissible actions.]</think>"
        "<answer>your action</answer>\n"
        "\n"
        "2. **Act directly**: Skip verification and directly output your action when "
        "you are confident. This saves computation.\n"
        "   Format: <think>brief reasoning</think><answer>your action</answer>\n"
        "\n"
        "Choose wisely: verification helps when you are unsure, but costs resources "
        "when the best action is obvious."
    )


def build_biavr_user_prompt_suffix() -> str:
    """Additional instruction appended to each user turn for B-IAVR."""
    return (
        "Decide whether to verify (output <VERIFY> first) or act directly. "
        "Your reasoning MUST be enclosed within <think> </think> tags. "
        "Then choose an admissible action and present it within <answer>...</answer> tags."
    )


def build_no_guidance_prompt() -> str:
    """System prompt for the counterfactual a_pre generation (no self-guidance)."""
    return (
        "You are an expert agent in the ALFRED Embodied Environment.\n"
        "Complete household tasks by navigating and interacting with objects.\n"
        "\n"
        "Choose the best action from the admissible actions.\n"
        "Your reasoning MUST be enclosed within <think> </think> tags.\n"
        "Then present your action within <answer>...</answer> tags."
    )
