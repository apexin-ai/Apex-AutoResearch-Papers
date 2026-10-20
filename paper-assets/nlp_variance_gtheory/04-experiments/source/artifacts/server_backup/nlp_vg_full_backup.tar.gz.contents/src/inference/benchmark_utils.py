"""Benchmark-specific prompt builders, answer extractors, and scorers for exp-002.

Extends run_experiment.py to support GSM8K, ARC-Challenge, HellaSwag, and MATH
alongside MMLU.  Each benchmark has 6 prompt template variants for measuring
prompt-wording variance.
"""

import re

BENCHMARK_MAX_TOKENS = {
    "mmlu": 16,
    "gsm8k": 512,
    "arc": 16,
    "hellaswag": 16,
    "math": 512,
}

BENCHMARK_STOP_SEQS = {
    "gsm8k": ["\nQ:", "\nQuestion:", "\nProblem:", "\n\n## "],
    "math": ["\nQ:", "\nQuestion:", "\nProblem:", "\n\n## "],
}

ANSWER_LABELS = ["A", "B", "C", "D", "E", "F", "G", "H"]

# ── GSM8K ─────────────────────────────────────────────────────────────────

GSM8K_TEMPLATES = {
    1: {
        "system": "Solve the following math problem step by step.\n\n",
        "shot": "Q: {question}\nA: {chain_of_thought}\n#### {answer}\n\n",
        "query": "Q: {question}\nA: Let's think step by step.\n",
    },
    2: {
        "system": "Answer the following math word problem. Show your work.\n\n",
        "shot": "Question: {question}\nSolution: {chain_of_thought}\n#### {answer}\n\n",
        "query": "Question: {question}\nSolution:",
    },
    3: {
        "system": "Solve each problem below. Write your reasoning, then give the final answer after ####.\n\n",
        "shot": "Problem: {question}\nReasoning: {chain_of_thought}\n#### {answer}\n\n",
        "query": "Problem: {question}\nReasoning:",
    },
    4: {
        "system": "You are a math tutor. Solve the problem and show your steps.\n\n",
        "shot": "{question}\nSteps: {chain_of_thought}\nFinal answer: #### {answer}\n\n",
        "query": "{question}\nSteps:",
    },
    5: {
        "system": "Work through this math question carefully.\n\n",
        "shot": "Q: {question}\nWork: {chain_of_thought}\nAnswer: #### {answer}\n\n",
        "query": "Q: {question}\nWork:",
    },
    6: {
        "system": "Math problem:\n\n",
        "shot": "{question}\n{chain_of_thought}\n#### {answer}\n\n",
        "query": "{question}\nLet's solve this step by step.\n",
    },
}


def format_gsm8k_prompt(
    template_id: int,
    question: str,
    few_shot_examples: list[dict] | None = None,
) -> str:
    """Build a GSM8K prompt with optional few-shot CoT examples."""
    tmpl = GSM8K_TEMPLATES.get(template_id, GSM8K_TEMPLATES[1])
    parts = [tmpl["system"]]
    if few_shot_examples:
        for ex in few_shot_examples:
            raw = ex.get("metadata", {}).get("raw_answer", "")
            answer = ex.get("answer", "")
            parts.append(tmpl["shot"].format(
                question=ex["question"],
                chain_of_thought=raw.split("####")[0].strip() if "####" in raw else raw,
                answer=answer,
            ))
    parts.append(tmpl["query"].format(question=question))
    return "".join(parts)

def format_math_prompt(
    template_id: int,
    question: str,
    few_shot_examples: list[dict] | None = None,
) -> str:
    """Build a MATH prompt with optional few-shot examples."""
    MATH_TEMPLATES = {
        1: {
            "system": "Solve the following math problem step by step. Put your final answer in \\boxed{}.\n\n",
            "shot": "Q: {question}\nA: {solution}\n\n",
            "query": "Q: {question}\nA: Let's think step by step.\n",
        },
        2: {
            "system": "Answer the following math problem. Show your work and put the final answer in \\boxed{}.\n\n",
            "shot": "Question: {question}\nSolution: {solution}\n\n",
            "query": "Question: {question}\nSolution:",
        },
        3: {
            "system": "Solve each problem below. Write your reasoning, then give the final answer in \\boxed{}.\n\n",
            "shot": "Problem: {question}\nReasoning: {solution}\n\n",
            "query": "Problem: {question}\nReasoning:",
        },
        4: {
            "system": "You are a math tutor. Solve the problem, show your steps, and put the answer in \\boxed{}.\n\n",
            "shot": "{question}\nSteps: {solution}\n\n",
            "query": "{question}\nSteps:",
        },
        5: {
            "system": "Work through this math problem carefully. Put the final answer in \\boxed{}.\n\n",
            "shot": "Q: {question}\nWork: {solution}\n\n",
            "query": "Q: {question}\nWork:",
        },
        6: {
            "system": "Math problem (put answer in \\boxed{}):\n\n",
            "shot": "{question}\n{solution}\n\n",
            "query": "{question}\nLet's solve this step by step.\n",
        },
    }
    tmpl = MATH_TEMPLATES.get(template_id, MATH_TEMPLATES[1])
    parts = [tmpl["system"]]
    if few_shot_examples:
        for ex in few_shot_examples:
            solution = ex.get("metadata", {}).get("solution", "")
            parts.append(tmpl["shot"].format(
                question=ex["question"],
                solution=solution,
            ))
    parts.append(tmpl["query"].format(question=question))
    return "".join(parts)


# ── ARC-Challenge ─────────────────────────────────────────────────────────

ARC_TEMPLATES = {
    1: {
        "system": "Answer the following science question by selecting the correct option.\n\n",
        "shot": "{question}\n{choices_block}\nAnswer: {answer}\n\n",
        "query": "{question}\n{choices_block}\nAnswer:",
        "choice_fmt": "{label}. {text}",
        "choice_sep": "\n",
    },
    2: {
        "system": "Select the correct answer for this science question.\n\n",
        "shot": "Question: {question}\n{choices_block}\nCorrect answer: {answer}\n\n",
        "query": "Question: {question}\n{choices_block}\nCorrect answer:",
        "choice_fmt": "({label}) {text}",
        "choice_sep": "  ",
    },
    3: {
        "system": "Pick the right answer.\n\n",
        "shot": "Q: {question}\n{choices_block}\nA: {answer}\n\n",
        "query": "Q: {question}\n{choices_block}\nA:",
        "choice_fmt": "  {label}) {text}",
        "choice_sep": "\n",
    },
    4: {
        "system": "Choose the best answer for this question.\n\n",
        "shot": "{question}\n{choices_block}\nAnswer: {answer}\n\n",
        "query": "{question}\n{choices_block}\nAnswer:",
        "choice_fmt": "- {label}. {text}",
        "choice_sep": "\n",
    },
    5: {
        "system": "Read the question and select the correct answer.\n\n",
        "shot": "{question}\n{choices_block}\nCorrect: {answer}\n\n",
        "query": "{question}\n{choices_block}\nCorrect:",
        "choice_fmt": "Option {label}: {text}",
        "choice_sep": "\n",
    },
    6: {
        "system": "Science question:\n",
        "shot": "{question}\nChoices:\n{choices_block}\nYour answer: {answer}\n\n",
        "query": "{question}\nChoices:\n{choices_block}\nYour answer:",
        "choice_fmt": "({label}) {text}",
        "choice_sep": " ",
    },
}


def format_arc_prompt(
    template_id: int,
    question: str,
    choices: list[str],
    labels: list[str] | None = None,
    few_shot_examples: list[dict] | None = None,
) -> str:
    """Build an ARC-Challenge prompt with variable choices."""
    tmpl = ARC_TEMPLATES.get(template_id, ARC_TEMPLATES[1])
    if labels is None:
        labels = ANSWER_LABELS[: len(choices)]

    def _choices_block(ch, lb):
        return tmpl["choice_sep"].join(
            tmpl["choice_fmt"].format(label=l, text=c) for l, c in zip(lb, ch)
        )

    parts = [tmpl["system"]]
    if few_shot_examples:
        for ex in few_shot_examples:
            ex_labels = ex.get("metadata", {}).get(
                "labels", ANSWER_LABELS[: len(ex["choices"])]
            )
            parts.append(
                tmpl["shot"].format(
                    question=ex["question"],
                    choices_block=_choices_block(ex["choices"], ex_labels),
                    answer=ex["answer"],
                )
            )
    parts.append(
        tmpl["query"].format(
            question=question,
            choices_block=_choices_block(choices, labels),
        )
    )
    return "".join(parts)


# ── HellaSwag ─────────────────────────────────────────────────────────────

HELLASWAG_TEMPLATES = {
    1: {
        "system": "Choose the most plausible continuation of the text.\n\n",
        "shot": "{context}\nA. {A}\nB. {B}\nC. {C}\nD. {D}\nAnswer: {answer}\n\n",
        "query": "{context}\nA. {A}\nB. {B}\nC. {C}\nD. {D}\nAnswer:",
    },
    2: {
        "system": "Select the best ending for the following passage.\n\n",
        "shot": "Passage: {context}\n(A) {A}  (B) {B}  (C) {C}  (D) {D}\nCorrect answer: {answer}\n\n",
        "query": "Passage: {context}\n(A) {A}  (B) {B}  (C) {C}  (D) {D}\nCorrect answer:",
    },
    3: {
        "system": "Pick the right continuation.\n\n",
        "shot": "{context}\n  A) {A}\n  B) {B}\n  C) {C}\n  D) {D}\nA: {answer}\n\n",
        "query": "{context}\n  A) {A}\n  B) {B}\n  C) {C}\n  D) {D}\nA:",
    },
    4: {
        "system": "What happens next? Choose the best option.\n\n",
        "shot": "{context}\n- A. {A}\n- B. {B}\n- C. {C}\n- D. {D}\nAnswer: {answer}\n\n",
        "query": "{context}\n- A. {A}\n- B. {B}\n- C. {C}\n- D. {D}\nAnswer:",
    },
    5: {
        "system": "Complete the following text with the most logical continuation.\n\n",
        "shot": "{context}\nOption A: {A}\nOption B: {B}\nOption C: {C}\nOption D: {D}\nCorrect: {answer}\n\n",
        "query": "{context}\nOption A: {A}\nOption B: {B}\nOption C: {C}\nOption D: {D}\nCorrect:",
    },
    6: {
        "system": "Choose the continuation:\n",
        "shot": "{context}\nChoices:\n(A) {A} (B) {B} (C) {C} (D) {D}\nYour answer: {answer}\n\n",
        "query": "{context}\nChoices:\n(A) {A} (B) {B} (C) {C} (D) {D}\nYour answer:",
    },
}

_HELLASWAG_ANSWER_MAP = {0: "A", 1: "B", 2: "C", 3: "D"}


def format_hellaswag_prompt(
    template_id: int,
    context: str,
    choices: list[str],
    few_shot_examples: list[dict] | None = None,
) -> str:
    """Build a HellaSwag sentence-completion MC prompt."""
    tmpl = HELLASWAG_TEMPLATES.get(template_id, HELLASWAG_TEMPLATES[1])
    parts = [tmpl["system"]]
    if few_shot_examples:
        for ex in few_shot_examples:
            gold = _HELLASWAG_ANSWER_MAP.get(ex.get("answer_idx", 0), "A")
            parts.append(
                tmpl["shot"].format(
                    context=ex["question"],
                    A=ex["choices"][0],
                    B=ex["choices"][1],
                    C=ex["choices"][2],
                    D=ex["choices"][3],
                    answer=gold,
                )
            )
    parts.append(
        tmpl["query"].format(
            context=context,
            A=choices[0],
            B=choices[1],
            C=choices[2],
            D=choices[3],
        )
    )
    return "".join(parts)


# ── Answer extraction ─────────────────────────────────────────────────────

_GSM8K_STOP_SEQS = ["\nQ:", "\nQuestion:", "\nProblem:", "\n\n##"]


def extract_gsm8k_answer(text: str) -> str | None:
    """Extract final numeric answer with truncation to prevent hallucination matching."""
    for stop in _GSM8K_STOP_SEQS:
        idx = text.find(stop)
        if idx != -1:
            text = text[:idx]

    m = re.search(r'[Tt]he answer is[:\s]*\$?\\?boxed\{?(\d[\d,]*(?:\.\d+)?)', text)
    if m:
        return m.group(1).replace(',', '')
    m = re.search(r'[Tt]he answer is[:\s]*(\d[\d,]*(?:\.\d+)?)', text)
    if m:
        return m.group(1).replace(',', '')

    matches = re.findall(r'####\s*(\d[\d,]*(?:\.\d+)?)', text)
    if matches:
        return matches[-1].replace(',', '')

    matches = re.findall(r'(\d[\d,]*(?:\.\d+)?)', text)
    if matches:
        return matches[-1].replace(',', '')

    return None


_MATH_STOP_SEQS = ["\nQ:", "\nQuestion:", "\nProblem:", "\n\n##"]


def extract_math_answer(text: str) -> str | None:
    """Extract final answer from MATH-style output.

    Priority: \\boxed{...} > 'The answer is ...' > last #### N.
    """
    for stop in _MATH_STOP_SEQS:
        idx = text.find(stop)
        if idx != -1:
            text = text[:idx]

    # Try \\boxed{...} (handle nested braces)
    pattern = r'\\boxed\{'
    matches = list(re.finditer(pattern, text))
    if matches:
        last = matches[-1]
        start = last.end()
        depth = 1
        i = start
        while i < len(text) and depth > 0:
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
            i += 1
        if depth == 0:
            return text[start:i-1].strip()

    # Try "The answer is ..."
    m = re.search(r'[Tt]he (?:final )?answer is[:\s]*(.+?)(?:\.\s|\.$|$)', text, re.DOTALL)
    if m:
        ans = m.group(1).strip().rstrip('.')
        if ans:
            return ans

    # Fallback: last #### N
    matches = re.findall(r'####\s*(.+)', text)
    if matches:
        return matches[-1].strip()

    return None


def _normalize_math_answer(answer: str) -> str | None:
    """Try to normalize a MATH answer to a comparable form."""
    if not answer:
        return None
    s = answer.strip()
    s = re.sub(r'^\$|\$$', '', s)
    s = re.sub(r'^\\\\?\(|\\\\?\)$', '', s)
    s = re.sub(r'\\frac\{([^}]*)\}\{([^}]*)\}', r'(\1)/(\2)', s)
    s = re.sub(r'\\dfrac\{([^}]*)\}\{([^}]*)\}', r'(\1)/(\2)', s)
    s = re.sub(r'\\sqrt\{([^}]*)\}', r'sqrt(\1)', s)
    s = re.sub(r'\\text\{([^}]*)\}', r'\1', s)
    s = s.replace('\\left', '').replace('\\right', '')
    s = s.replace('\\,', '')
    s = s.rstrip('.')
    s = s.strip()
    return s if s else None


def score_math(predicted: str | None, gold: str) -> int:
    """Compare MATH answers: try float comparison, then normalized string match."""
    if predicted is None:
        return 0

    pred_norm = _normalize_math_answer(predicted)
    gold_norm = _normalize_math_answer(gold)

    if pred_norm is None:
        return 0

    if pred_norm == gold_norm:
        return 1

    try:
        pred_val = float(eval(pred_norm.replace('^', '**')))
        gold_val = float(eval(gold_norm.replace('^', '**')))
        if abs(pred_val - gold_val) < 1e-6:
            return 1
    except Exception:
        pass

    if pred_norm and gold_norm and pred_norm.lower() == gold_norm.lower():
        return 1

    return 0


_MC_ANSWER_PATTERN = re.compile(r"^\s*([A-Ea-e])\b")


def extract_mc_answer(text: str) -> str | None:
    """Extract a single A-E letter from the start of generated text."""
    m = _MC_ANSWER_PATTERN.match(text)
    return m.group(1).upper() if m else None


# ── Scoring ───────────────────────────────────────────────────────────────


def score_gsm8k(predicted: str | None, gold: str) -> int:
    """Compare extracted number to gold answer (normalize both to float)."""
    if predicted is None:
        return 0
    try:
        return int(float(predicted.replace(",", "")) == float(gold.replace(",", "")))
    except (ValueError, TypeError):
        return int(predicted.strip() == gold.strip())


def score_mc(predicted: str | None, gold: str) -> int:
    """Compare extracted letter to gold letter (case-insensitive)."""
    if predicted is None:
        return 0
    return int(predicted.upper() == gold.upper())


def get_mc_gold(benchmark: str, item: dict) -> str:
    """Get the gold answer letter for an MC benchmark item."""
    if benchmark == "arc":
        return item["answer"]
    elif benchmark == "hellaswag":
        return _HELLASWAG_ANSWER_MAP.get(item["answer_idx"], "A")
    raise ValueError(f"Unknown MC benchmark: {benchmark}")
