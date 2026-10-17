"""Style counterfactual generation via RATE double-rewrite protocol.

Supports multiple style axes: formality (formal/casual), verbosity (verbose/concise).
Input:  mvp_samples.jsonl (id, instruction, response, source)
Output: counterfactuals.jsonl — adds original_text, counterfactual_text, double_rewrite_text, original_{axis}
Deps:   openai (used for both vLLM-serve and remote API endpoints)
"""

import argparse
import json
import logging
import os
import re
import time

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Formality axis
# ---------------------------------------------------------------------------

FORMALITY_SYSTEM_PROMPT = (
    "You are a writing style editor. Your task is to rewrite the given text to change "
    "ONLY its formality level while preserving ALL factual content, arguments, and meaning.\n\n"
    "Rules:\n"
    "- Do NOT add, remove, or alter any facts, claims, or reasoning.\n"
    "- Do NOT change the length substantially (±20% words is acceptable).\n"
    "- Change ONLY the register/formality: vocabulary, sentence structure, tone.\n"
    "- Do NOT change formatting: no adding/removing bold, markdown, lists, headers, or any visual structure changes.\n"
    "- Keep the EXACT same formatting as the original text.\n"
    "- Do NOT modify any text that is quoted from or directly references the original instruction/question. "
    "Only modify the style of the response's own content.\n"
    "- Output ONLY the rewritten text, nothing else."
)

FORMALITY_DETECT_PROMPT = (
    "Analyze the formality level of the following text. "
    "Consider vocabulary (technical/colloquial), sentence structure (complex/simple), "
    "tone (professional/conversational), and register (academic/informal).\n"
    "Output ONLY one word: formal or casual.\n\n"
    "Text:\n{text}"
)

FORMALITY_EXAMPLES = [
    {
        "direction": "formal_to_casual",
        "original": (
            "The implementation of robust error-handling mechanisms is essential for maintaining "
            "system reliability. One should consider employing try-catch blocks with specific "
            "exception types rather than generic catch-all handlers."
        ),
        "rewritten": (
            "You really need good error handling to keep things running smoothly. Use try-catch "
            "with specific exception types instead of just catching everything — trust me, it "
            "makes debugging way easier."
        ),
    },
    {
        "direction": "casual_to_formal",
        "original": (
            "Yeah so basically the model's overfitting like crazy. Just throw in some dropout "
            "and maybe try early stopping, that usually does the trick."
        ),
        "rewritten": (
            "The model exhibits significant overfitting. Incorporating dropout regularization "
            "and implementing early stopping are recommended strategies to mitigate this issue."
        ),
    },
]

# ---------------------------------------------------------------------------
# Verbosity axis
# ---------------------------------------------------------------------------

VERBOSITY_SYSTEM_PROMPT = (
    "You are a writing style editor. Your task is to rewrite the given text to change "
    "ONLY its verbosity level while preserving ALL factual content, arguments, and meaning.\n\n"
    "Rules:\n"
    "- Do NOT add, remove, or alter any facts, claims, or reasoning.\n"
    "- When making text MORE CONCISE: compress expression, remove redundancy, use shorter "
    "phrasing. Do NOT delete any information points — every fact/argument must still be present.\n"
    "- When making text MORE VERBOSE: expand existing points with elaboration, examples, or "
    "transitional phrases. Do NOT introduce any new facts or arguments not implied by the original.\n"
    "- Do NOT change the register/formality level.\n"
    "- Do NOT change formatting: no adding/removing bold, markdown, lists, headers, or any visual structure changes.\n"
    "- Keep the EXACT same formatting as the original text.\n"
    "- Do NOT modify any text that is quoted from or directly references the original instruction/question. "
    "Only modify the style of the response's own content.\n"
    "- Output ONLY the rewritten text, nothing else."
)

VERBOSITY_DETECT_PROMPT = (
    "Analyze the verbosity level of the following text. "
    "Consider: length relative to information density, use of elaboration/examples, "
    "redundancy, transitional phrases, and conciseness of expression.\n"
    "Output ONLY one word: verbose or concise.\n\n"
    "Text:\n{text}"
)

VERBOSITY_EXAMPLES = [
    {
        "direction": "verbose_to_concise",
        "original": (
            "When it comes to the topic of machine learning model selection, it is generally "
            "considered to be a best practice to start with a simpler model first, such as "
            "logistic regression or a decision tree, before moving on to more complex approaches. "
            "The reason for this is that simpler models are easier to interpret and debug, and "
            "they can often serve as a useful baseline against which you can compare the "
            "performance of more sophisticated models."
        ),
        "rewritten": (
            "Start with simple models (logistic regression, decision trees) before trying complex "
            "ones. They're easier to interpret and debug, and serve as baselines for comparing "
            "more sophisticated approaches."
        ),
    },
    {
        "direction": "concise_to_verbose",
        "original": (
            "Use gradient clipping to prevent exploding gradients. Set the max norm to 1.0 "
            "for most transformer training runs."
        ),
        "rewritten": (
            "To address the common issue of exploding gradients during training, it is recommended "
            "to employ gradient clipping as a stabilization technique. In practice, setting the "
            "maximum gradient norm to a value of 1.0 tends to work well for most transformer-based "
            "training configurations, as this threshold effectively prevents the gradients from "
            "growing too large while still allowing meaningful parameter updates."
        ),
    },
]

# ---------------------------------------------------------------------------
# Tone axis
# ---------------------------------------------------------------------------

TONE_SYSTEM_PROMPT = (
    "You are a writing style editor. Your task is to rewrite the given text to change "
    "ONLY its tone (assertive vs hedging) while preserving ALL factual content, arguments, and meaning.\n\n"
    "Rules:\n"
    "- Do NOT add, remove, or alter any facts, claims, or reasoning.\n"
    "- Do NOT change the length substantially (±20% words is acceptable).\n"
    "- When making text MORE ASSERTIVE: replace hedging language (might, perhaps, could, seems) "
    "with confident statements, remove unnecessary qualifiers, use direct phrasing.\n"
    "- When making text MORE HEDGING: add appropriate qualifiers (may, might, could, appears to), "
    "soften definitive claims, use tentative phrasing. Do NOT change the actual claims.\n"
    "- Do NOT change the register/formality level or verbosity.\n"
    "- Do NOT change formatting: no adding/removing bold, markdown, lists, headers, or any visual structure changes.\n"
    "- Keep the EXACT same formatting as the original text.\n"
    "- Do NOT modify any text that is quoted from or directly references the original instruction/question. "
    "Only modify the style of the response's own content.\n"
    "- Output ONLY the rewritten text, nothing else."
)

TONE_DETECT_PROMPT = (
    "Analyze the tone of the following text in terms of assertiveness. "
    "Consider: use of hedging language (might, perhaps, could, seems, appears), "
    "qualifiers (somewhat, relatively, arguably), confidence of claims (definitive vs tentative), "
    "and directness of recommendations.\n"
    "Output ONLY one word: assertive or hedging.\n\n"
    "Text:\n{text}"
)

TONE_EXAMPLES = [
    {
        "direction": "assertive_to_hedging",
        "original": (
            "The best approach is to use a transformer architecture here. CNNs simply cannot "
            "capture the long-range dependencies required for this task. You should switch to "
            "a multi-head attention mechanism immediately."
        ),
        "rewritten": (
            "It might be worth considering a transformer architecture here. CNNs may struggle to "
            "capture the long-range dependencies that could be important for this task. It could "
            "be beneficial to explore a multi-head attention mechanism as an alternative."
        ),
    },
    {
        "direction": "hedging_to_assertive",
        "original": (
            "It seems like the learning rate might be a bit too high. You could perhaps try "
            "reducing it, and it's possible that a cosine schedule would work somewhat better "
            "than the current linear decay."
        ),
        "rewritten": (
            "The learning rate is too high. Reduce it, and use a cosine schedule instead of "
            "the current linear decay — it will produce better convergence."
        ),
    },
]

# ---------------------------------------------------------------------------
# Register axis
# ---------------------------------------------------------------------------

REGISTER_SYSTEM_PROMPT = (
    "You are a writing style editor. Your task is to rewrite the given text to change "
    "ONLY its register (academic vs conversational) while preserving ALL factual content, "
    "arguments, and meaning.\n\n"
    "Rules:\n"
    "- Do NOT add, remove, or alter any facts, claims, or reasoning.\n"
    "- Do NOT change the length substantially (±20% words is acceptable).\n"
    "- Register means VOCABULARY and SYNTAX choices:\n"
    "  * Academic: technical/domain-specific terms, passive voice, complex sentence structures, "
    "nominalization, hedging phrases typical of scholarly writing.\n"
    "  * Conversational: everyday words, active voice, simpler sentence structures, "
    "contractions, direct address ('you'), colloquial expressions.\n"
    "- Do NOT change politeness level, social distance, or attitude (that is formality/tone).\n"
    "- Do NOT change formatting: no adding/removing bold, markdown, lists, headers, or any "
    "visual structure changes.\n"
    "- Keep the EXACT same formatting as the original text.\n"
    "- Do NOT modify any text that is quoted from or directly references the original "
    "instruction/question. Only modify the style of the response's own content.\n"
    "- Output ONLY the rewritten text, nothing else."
)

REGISTER_DETECT_PROMPT = (
    "Analyze the register of the following text. Register refers to vocabulary and "
    "syntax choices: academic register uses technical terms, passive voice, complex "
    "sentence structures, and nominalizations; conversational register uses everyday "
    "words, active voice, contractions, and simpler structures.\n"
    "Output ONLY one word: academic or conversational.\n\n"
    "Text:\n{text}"
)

REGISTER_EXAMPLES = [
    {
        "direction": "academic_to_conversational",
        "original": (
            "The experimental results demonstrate a statistically significant improvement "
            "in model performance, as evidenced by the obtained metrics. It is hypothesized "
            "that the observed enhancement can be attributed to the regularization mechanism "
            "employed during the training procedure."
        ),
        "rewritten": (
            "The results show a big improvement in how the model performs, based on the "
            "numbers we got. We think this boost comes from the regularization trick we "
            "used during training."
        ),
    },
    {
        "direction": "conversational_to_academic",
        "original": (
            "So basically you want to split your data into chunks before feeding it to the "
            "model. If you don't, the model's gonna choke on long inputs and you'll get "
            "garbage outputs."
        ),
        "rewritten": (
            "It is recommended to partition the input data into segments prior to model "
            "ingestion. Failure to do so may result in degraded performance on lengthy "
            "inputs, yielding suboptimal outputs."
        ),
    },
]

# ---------------------------------------------------------------------------
# Axis registry
# ---------------------------------------------------------------------------

AXIS_CONFIG = {
    "formality": {
        "system_prompt": FORMALITY_SYSTEM_PROMPT,
        "detect_prompt": FORMALITY_DETECT_PROMPT,
        "examples": FORMALITY_EXAMPLES,
        "poles": ("formal", "casual"),
        "field_name": "original_formality",
    },
    "verbosity": {
        "system_prompt": VERBOSITY_SYSTEM_PROMPT,
        "detect_prompt": VERBOSITY_DETECT_PROMPT,
        "examples": VERBOSITY_EXAMPLES,
        "poles": ("verbose", "concise"),
        "field_name": "original_verbosity",
    },
    "tone": {
        "system_prompt": TONE_SYSTEM_PROMPT,
        "detect_prompt": TONE_DETECT_PROMPT,
        "examples": TONE_EXAMPLES,
        "poles": ("assertive", "hedging"),
        "field_name": "original_tone",
    },
    "register": {
        "system_prompt": REGISTER_SYSTEM_PROMPT,
        "detect_prompt": REGISTER_DETECT_PROMPT,
        "examples": REGISTER_EXAMPLES,
        "poles": ("academic", "conversational"),
        "field_name": "original_register",
    },
}


def _build_rewrite_prompt(text: str, target: str, axis: str, instruction: str = "") -> list[dict]:
    cfg = AXIS_CONFIG[axis]
    poles = cfg["poles"]
    opposite = poles[1] if target == poles[0] else poles[0]

    direction_key = f"{opposite}_to_{target}"
    example = next(e for e in cfg["examples"] if e["direction"] == direction_key)

    instruction_note = ""
    if instruction:
        instruction_note = (
            f"\n\nOriginal instruction (DO NOT modify any part of the response that "
            f"quotes or paraphrases this instruction):\n\"{instruction}\"\n"
        )

    messages = [
        {"role": "system", "content": cfg["system_prompt"]},
        {
            "role": "user",
            "content": (
                f"Rewrite the following text to be more {target}.\n\n"
                f"Example:\nOriginal ({opposite}): {example['original']}\n"
                f"Rewritten ({target}): {example['rewritten']}\n"
                f"{instruction_note}\n"
                f"Now rewrite this text to be more {target}:\n\n{text}"
            ),
        },
    ]
    return messages


def _call_llm(client, model: str, messages: list[dict], max_retries: int = 3) -> str:
    for attempt in range(max_retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=2048,
                extra_body={"chat_template_kwargs": {"enable_thinking": False}},
            )
            text = resp.choices[0].message.content.strip()
            text = re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL)
            return text.strip()
        except Exception as e:
            logger.warning("LLM call failed (attempt %d/%d): %s", attempt + 1, max_retries, e)
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise


def detect_style(client, model: str, text: str, axis: str) -> str:
    cfg = AXIS_CONFIG[axis]
    messages = [
        {"role": "user", "content": cfg["detect_prompt"].format(text=text[:1000])},
    ]
    result = _call_llm(client, model, messages).lower().strip().rstrip(".")
    pole_a, pole_b = cfg["poles"]
    if pole_a in result and pole_b not in result:
        return pole_a
    return pole_b


def generate_counterfactual(client, model: str, text: str, original_pole: str, axis: str, instruction: str = "") -> tuple[str, str]:
    """Returns (counterfactual_text, double_rewrite_text)."""
    poles = AXIS_CONFIG[axis]["poles"]
    target = poles[1] if original_pole == poles[0] else poles[0]

    msgs_flip = _build_rewrite_prompt(text, target, axis, instruction)
    counterfactual = _call_llm(client, model, msgs_flip)

    msgs_flipback = _build_rewrite_prompt(counterfactual, original_pole, axis, instruction)
    double_rewrite = _call_llm(client, model, msgs_flipback)

    return counterfactual, double_rewrite


def load_processed_ids(output_file: str) -> set[str]:
    ids = set()
    if os.path.exists(output_file):
        with open(output_file) as f:
            for line in f:
                if line.strip():
                    ids.add(json.loads(line)["id"])
    return ids


def main():
    parser = argparse.ArgumentParser(description="Generate style counterfactuals via RATE double-rewrite")
    parser.add_argument("--input-file", required=True, help="Input jsonl from data_prep")
    parser.add_argument("--output-file", required=True, help="Output jsonl with counterfactuals")
    parser.add_argument("--model-path", default=None, help="Model name/path for the LLM")
    parser.add_argument("--api-url", default="http://localhost:8000/v1", help="OpenAI-compatible API base URL")
    parser.add_argument("--api-key", default=None, help="API key (or set OPENAI_API_KEY env var)")
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--axis", default="formality", choices=list(AXIS_CONFIG.keys()),
                        help="Style axis to manipulate (default: formality)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    from openai import OpenAI

    api_key = [REDACTED] or os.environ.get("OPENAI_API_KEY", "EMPTY")
    client = OpenAI(base_url=args.api_url, api_key=[REDACTED]
    model = args.model_path or "default"
    axis = args.axis
    field_name = AXIS_CONFIG[axis]["field_name"]

    with open(args.input_file) as f:
        records = [json.loads(line) for line in f if line.strip()]

    processed_ids = load_processed_ids(args.output_file)
    logger.info("Total records: %d, already processed: %d, axis: %s", len(records), len(processed_ids), axis)

    os.makedirs(os.path.dirname(args.output_file) or ".", exist_ok=True)

    with open(args.output_file, "a") as fout:
        for rec in records:
            if rec["id"] in processed_ids:
                logger.info("Skipping %s (already processed)", rec["id"])
                continue

            text = rec["response"]
            instruction = rec.get("instruction", "")
            try:
                detected_pole = detect_style(client, model, text, axis)
                counterfactual, double_rewrite = generate_counterfactual(
                    client, model, text, detected_pole, axis, instruction
                )

                out = {
                    **rec,
                    "original_text": text,
                    "counterfactual_text": counterfactual,
                    "double_rewrite_text": double_rewrite,
                    field_name: detected_pole,
                }
                fout.write(json.dumps(out, ensure_ascii=False) + "\n")
                fout.flush()
                logger.info("Processed %s (%s=%s)", rec["id"], axis, detected_pole)
            except Exception:
                logger.exception("Failed to process %s", rec["id"])


if __name__ == "__main__":
    main()
