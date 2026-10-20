"""MMLU prompt templates — 6 semantically equivalent paraphrases.

Each template formats a multiple-choice question with optional few-shot
examples.  Variation follows Brittlebench-style surface perturbation:
different wording and layout, identical semantic content.

Output: a single string ready for LLM input.
"""

TEMPLATES = {
    1: {
        "system": (
            "The following are multiple choice questions (with answers) "
            "about {subject}.\n\n"
        ),
        "shot": (
            "{question}\n"
            "A. {A}\nB. {B}\nC. {C}\nD. {D}\n"
            "Answer: {answer}\n\n"
        ),
        "query": (
            "{question}\n"
            "A. {A}\nB. {B}\nC. {C}\nD. {D}\n"
            "Answer:"
        ),
    },
    2: {
        "system": (
            "Answer the following {subject} questions by selecting "
            "the correct option.\n\n"
        ),
        "shot": (
            "Question: {question}\n"
            "(A) {A}  (B) {B}  (C) {C}  (D) {D}\n"
            "Correct answer: {answer}\n\n"
        ),
        "query": (
            "Question: {question}\n"
            "(A) {A}  (B) {B}  (C) {C}  (D) {D}\n"
            "Correct answer:"
        ),
    },
    3: {
        "system": (
            "Below are {subject} multiple-choice problems. "
            "Pick the right letter.\n\n"
        ),
        "shot": (
            "Q: {question}\n"
            "  A) {A}\n  B) {B}\n  C) {C}\n  D) {D}\n"
            "A: {answer}\n\n"
        ),
        "query": (
            "Q: {question}\n"
            "  A) {A}\n  B) {B}\n  C) {C}\n  D) {D}\n"
            "A:"
        ),
    },
    4: {
        "system": (
            "Answer the following {subject} question by selecting "
            "A, B, C, or D.\n\n"
        ),
        "shot": (
            "{question}\n"
            "- A. {A}\n- B. {B}\n- C. {C}\n- D. {D}\n"
            "Answer: {answer}\n\n"
        ),
        "query": (
            "{question}\n"
            "- A. {A}\n- B. {B}\n- C. {C}\n- D. {D}\n"
            "Answer:"
        ),
    },
    5: {
        "system": (
            "Below is a {subject} exam question with four possible answers. "
            "Choose the correct one.\n\n"
        ),
        "shot": (
            "{question}\n"
            "Option A: {A}\nOption B: {B}\nOption C: {C}\nOption D: {D}\n"
            "Correct: {answer}\n\n"
        ),
        "query": (
            "{question}\n"
            "Option A: {A}\nOption B: {B}\nOption C: {C}\nOption D: {D}\n"
            "Correct:"
        ),
    },
    6: {
        "system": "Question ({subject}):\n",
        "shot": (
            "{question}\n"
            "Choices:\n(A) {A} (B) {B} (C) {C} (D) {D}\n"
            "Your answer: {answer}\n\n"
        ),
        "query": (
            "{question}\n"
            "Choices:\n(A) {A} (B) {B} (C) {C} (D) {D}\n"
            "Your answer:"
        ),
    },
}

ANSWER_MAP = {0: "A", 1: "B", 2: "C", 3: "D"}


def format_prompt(
    template_id: int,
    subject: str,
    question: str,
    choices: list[str],
    few_shot_examples: list[dict] | None = None,
) -> str:
    """Build a complete prompt string for one MMLU item.

    Args:
        template_id: 1–6.
        subject: MMLU subject name (e.g. "abstract_algebra").
        question: Question text.
        choices: List of 4 answer strings [A, B, C, D].
        few_shot_examples: Optional list of dicts, each with keys
            ``question``, ``choices`` (list[str]), ``answer_idx`` (int 0-3).

    Returns:
        Full prompt string.
    """
    tmpl = TEMPLATES[template_id]
    subject_display = subject.replace("_", " ")
    parts = [tmpl["system"].format(subject=subject_display)]

    if few_shot_examples:
        for ex in few_shot_examples:
            parts.append(
                tmpl["shot"].format(
                    question=ex["question"],
                    A=ex["choices"][0],
                    B=ex["choices"][1],
                    C=ex["choices"][2],
                    D=ex["choices"][3],
                    answer=ANSWER_MAP[ex["answer_idx"]],
                )
            )

    parts.append(
        tmpl["query"].format(
            question=question,
            A=choices[0],
            B=choices[1],
            C=choices[2],
            D=choices[3],
        )
    )
    return "".join(parts)


# =====================================================
# Multi-benchmark prompt templates for G-theory exp-002
# =====================================================
# Extends MMLU templates to GSM8K, ARC-Challenge, HellaSwag.
# Each benchmark has 6 prompt variants varying:
#   - instruction verbosity (minimal / moderate / detailed)
#   - choice/answer layout
#   - role framing (none / exam / tutor)
# These dimensions measure prompt wording as a facet in G-theory.


# --- Dynamic choice formatting for variable-length MC (ARC, HellaSwag) ---

def _choices_vertical_dot(choices: list[str]) -> str:
    """A. foo\nB. bar"""
    return "\n".join(f"{chr(65+i)}. {c}" for i, c in enumerate(choices))


def _choices_inline_paren(choices: list[str]) -> str:
    """(A) foo  (B) bar"""
    return "  ".join(f"({chr(65+i)}) {c}" for i, c in enumerate(choices))


def _choices_indented_paren(choices: list[str]) -> str:
    """  A) foo\n  B) bar"""
    return "\n".join(f"  {chr(65+i)}) {c}" for i, c in enumerate(choices))


def _choices_bulleted(choices: list[str]) -> str:
    """- A. foo\n- B. bar"""
    return "\n".join(f"- {chr(65+i)}. {c}" for i, c in enumerate(choices))


def _choices_verbose(choices: list[str]) -> str:
    """Option A: foo\nOption B: bar"""
    return "\n".join(f"Option {chr(65+i)}: {c}" for i, c in enumerate(choices))


def _choices_compact(choices: list[str]) -> str:
    """(A) foo\n(B) bar"""
    return "\n".join(f"({chr(65+i)}) {c}" for i, c in enumerate(choices))


_CHOICE_FORMATTERS = {
    "vertical_dot": _choices_vertical_dot,
    "inline_paren": _choices_inline_paren,
    "indented_paren": _choices_indented_paren,
    "bulleted": _choices_bulleted,
    "verbose": _choices_verbose,
    "compact": _choices_compact,
}


def _answer_label(idx: int) -> str:
    """Convert 0-based index to letter label (0 -> A, 1 -> B, ...)."""
    return chr(65 + idx)


# --- GSM8K: generative math reasoning ---
# All 6 variants instruct the model to write the final numerical answer after ####.
# shot uses {chain} placeholder for the full reasoning chain (including #### answer).
# Variation: instruction verbosity, format strictness, role framing.

GSM8K_TEMPLATES = {
    1: {
        "system": "Solve the following math problem.\n\n",
        "shot": "{question}\n\n{chain}\n\n",
        "query": "{question}\n\nProvide your final answer after ####.",
    },
    2: {
        "system": "Solve the following problem step by step.\n\n",
        "shot": "{question}\n\n{chain}\n\n",
        "query": (
            "{question}\n\n"
            "Work through this carefully. Write the final numerical answer after ####."
        ),
    },
    3: {
        "system": "Answer each math question. Put the final answer after ####.\n\n",
        "shot": "Q: {question}\nA: {chain}\n\n",
        "query": "Q: {question}\nA:",
    },
    4: {
        "system": "You are a math teacher. Solve the problem below.\n\n",
        "shot": "{question}\n\n{chain}\n\n",
        "query": "{question}\n\nExplain your solution, then state the final answer after ####.",
    },
    5: {
        "system": "Think carefully about the following math problem.\n\n",
        "shot": "{question}\n\n{chain}\n\n",
        "query": "{question}\n\nReason through each step, then give the answer after ####.",
    },
    6: {
        "system": "Problem:\n",
        "shot": "{question}\n\n{chain}\n\n",
        "query": "{question}\n\nSolution (end with #### followed by the numerical answer):",
    },
}


# --- ARC-Challenge: variable-length MC, science ---
# Supports 3-5 choices dynamically via choice_style formatters.
# Variation mirrors MMLU: instruction style, choice layout, answer cue.

ARC_TEMPLATES = {
    1: {
        "system": "Answer the following science question.\n\n",
        "choice_style": "vertical_dot",
        "shot": "{question}\n{choices}\nAnswer: {answer}\n\n",
        "query": "{question}\n{choices}\nAnswer:",
    },
    2: {
        "system": "Select the correct answer for this science question.\n\n",
        "choice_style": "inline_paren",
        "shot": "Question: {question}\n{choices}\nCorrect answer: {answer}\n\n",
        "query": "Question: {question}\n{choices}\nCorrect answer:",
    },
    3: {
        "system": "Science multiple-choice. Pick the right letter.\n\n",
        "choice_style": "indented_paren",
        "shot": "Q: {question}\n{choices}\nA: {answer}\n\n",
        "query": "Q: {question}\n{choices}\nA:",
    },
    4: {
        "system": "Choose the best answer from the options below.\n\n",
        "choice_style": "bulleted",
        "shot": "{question}\n{choices}\nAnswer: {answer}\n\n",
        "query": "{question}\n{choices}\nAnswer:",
    },
    5: {
        "system": (
            "Below is a science question with several possible answers. "
            "Choose the correct one.\n\n"
        ),
        "choice_style": "verbose",
        "shot": "{question}\n{choices}\nCorrect: {answer}\n\n",
        "query": "{question}\n{choices}\nCorrect:",
    },
    6: {
        "system": "Question:\n",
        "choice_style": "compact",
        "shot": "{question}\nChoices:\n{choices}\nYour answer: {answer}\n\n",
        "query": "{question}\nChoices:\n{choices}\nYour answer:",
    },
}


# --- HellaSwag: sentence completion MC ---
# Context text -> pick the most plausible continuation from 4 options.
# Variation: context label (none/Passage), instruction detail, choice layout.

HELLASWAG_TEMPLATES = {
    1: {
        "system": "Choose the most plausible continuation of the following text.\n\n",
        "choice_style": "vertical_dot",
        "shot": "{question}\n{choices}\nAnswer: {answer}\n\n",
        "query": "{question}\n{choices}\nAnswer:",
    },
    2: {
        "system": "Select the best completion for the passage below.\n\n",
        "choice_style": "inline_paren",
        "shot": "Passage: {question}\n{choices}\nCorrect answer: {answer}\n\n",
        "query": "Passage: {question}\n{choices}\nCorrect answer:",
    },
    3: {
        "system": "Pick the best ending.\n\n",
        "choice_style": "indented_paren",
        "shot": "{question}\n{choices}\nA: {answer}\n\n",
        "query": "{question}\n{choices}\nA:",
    },
    4: {
        "system": (
            "You are evaluating text coherence. "
            "Choose the most natural continuation.\n\n"
        ),
        "choice_style": "bulleted",
        "shot": "{question}\n{choices}\nAnswer: {answer}\n\n",
        "query": "{question}\n{choices}\nAnswer:",
    },
    5: {
        "system": (
            "Read the following passage and select the most logical "
            "continuation from the options.\n\n"
        ),
        "choice_style": "verbose",
        "shot": "{question}\n{choices}\nCorrect: {answer}\n\n",
        "query": "{question}\n{choices}\nCorrect:",
    },
    6: {
        "system": "Complete the text:\n",
        "choice_style": "compact",
        "shot": "{question}\nOptions:\n{choices}\nYour answer: {answer}\n\n",
        "query": "{question}\nOptions:\n{choices}\nYour answer:",
    },
}


BENCHMARK_TEMPLATES = {
    "mmlu": TEMPLATES,
    "gsm8k": GSM8K_TEMPLATES,
    "arc_challenge": ARC_TEMPLATES,
    "hellaswag": HELLASWAG_TEMPLATES,
}

# MATH templates are defined in benchmark_utils.py — imported here for routing
try:
    from src.inference.benchmark_utils import MATH_TEMPLATES
    BENCHMARK_TEMPLATES["math"] = MATH_TEMPLATES
except ImportError:
    pass


def format_benchmark_prompt(
    benchmark: str,
    template_id: int,
    question: str,
    choices: list[str] | None = None,
    few_shot_examples: list[dict] | None = None,
    subject: str | None = None,
) -> str:
    """Build a prompt for any supported benchmark.

    Args:
        benchmark: One of "mmlu", "gsm8k", "arc_challenge", "hellaswag".
        template_id: 1-6.
        question: Question or context text.
        choices: Answer choices (None for GSM8K).
        few_shot_examples: Optional few-shot dicts matching the benchmark item schema.
        subject: MMLU subject (required for mmlu, ignored otherwise).
    """
    if benchmark == "mmlu":
        return format_prompt(
            template_id=template_id,
            subject=subject or "",
            question=question,
            choices=choices or [],
            few_shot_examples=few_shot_examples,
        )

    if benchmark == "gsm8k":
        return _format_gsm8k(template_id, question, few_shot_examples)

    if benchmark == "math":
        from src.inference.benchmark_utils import format_math_prompt
        return format_math_prompt(template_id, question, few_shot_examples)

    if benchmark in ("arc_challenge", "hellaswag"):
        tmpl_dict = ARC_TEMPLATES if benchmark == "arc_challenge" else HELLASWAG_TEMPLATES
        return _format_mc(tmpl_dict, template_id, question, choices, few_shot_examples)

    raise ValueError(f"Unknown benchmark: {benchmark}")


def _format_gsm8k(
    template_id: int,
    question: str,
    few_shot_examples: list[dict] | None = None,
) -> str:
    tmpl = GSM8K_TEMPLATES[template_id]
    parts = [tmpl["system"]]

    if few_shot_examples:
        for ex in few_shot_examples:
            chain = ex.get("metadata", {}).get(
                "raw_answer", f"#### {ex.get('answer', '')}"
            )
            parts.append(tmpl["shot"].format(question=ex["question"], chain=chain))

    parts.append(tmpl["query"].format(question=question))
    return "".join(parts)


def _format_mc(
    tmpl_dict: dict,
    template_id: int,
    question: str,
    choices: list[str],
    few_shot_examples: list[dict] | None = None,
) -> str:
    tmpl = tmpl_dict[template_id]
    choice_fn = _CHOICE_FORMATTERS[tmpl["choice_style"]]
    parts = [tmpl["system"]]

    if few_shot_examples:
        for ex in few_shot_examples:
            choices_str = choice_fn(ex["choices"])
            answer = _answer_label(ex["answer_idx"])
            parts.append(
                tmpl["shot"].format(
                    question=ex["question"], choices=choices_str, answer=answer
                )
            )

    choices_str = choice_fn(choices)
    parts.append(tmpl["query"].format(question=question, choices=choices_str))
    return "".join(parts)
