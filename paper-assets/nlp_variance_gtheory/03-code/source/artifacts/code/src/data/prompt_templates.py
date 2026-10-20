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
