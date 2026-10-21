"""Zero-shot NER prompt templates for Qwen2.5-72B baseline evaluation.

Output format is compatible with the existing pipeline (sampling.py):
  {"entities": [{"text": "...", "type": "...", "start": <int>, "end": <int>}],
   "relations": [], "events": []}
"""

# ---------------------------------------------------------------------------
# Entity type definitions per dataset
# ---------------------------------------------------------------------------

DATASET_ENTITY_TYPES = {
    "conll2003": {
        "types": ["PER", "ORG", "LOC", "MISC"],
        "descriptions": {
            "PER": "Person names (e.g., John Smith, Obama)",
            "ORG": "Organizations (e.g., Google, United Nations)",
            "LOC": "Locations (e.g., France, Mount Everest)",
            "MISC": "Miscellaneous named entities not fitting PER/ORG/LOC (e.g., English, World Cup)",
        },
    },
    "fewnerd": {
        "types": ["person", "organization", "location", "building", "art", "product", "event", "other"],
        "descriptions": {
            "person": "Person names",
            "organization": "Organizations, companies, teams",
            "location": "Geographic locations, countries, cities",
            "building": "Buildings, facilities, landmarks",
            "art": "Artworks, songs, films, books",
            "product": "Commercial products, software, vehicles",
            "event": "Events, competitions, wars, festivals",
            "other": "Other named entities not fitting the above categories",
        },
    },
    "scierc": {
        "types": ["Generic", "Material", "Method", "Metric", "OtherScientificTerm", "Task"],
        "descriptions": {
            "Generic": "Generic references to scientific concepts (coreference)",
            "Material": "Data, datasets, corpora, resources",
            "Method": "Algorithms, models, systems, tools",
            "Metric": "Evaluation metrics and measures",
            "OtherScientificTerm": "Scientific terms not fitting other categories",
            "Task": "Research tasks, problems, applications",
        },
    },
}

# ---------------------------------------------------------------------------
# Zero-shot system prompt
# ---------------------------------------------------------------------------

ZEROSHOT_SYSTEM_PROMPT = (
    "You are a precise named entity recognition (NER) system. "
    "Extract all named entities from the given text and output them in the specified JSON format. "
    "Be exhaustive: identify every entity that matches the given types. "
    "Be precise: the 'start' and 'end' values must be character offsets in the original text, "
    "where 'start' is the index of the first character and 'end' is the index after the last character, "
    "such that text[start:end] == entity text."
)

# ---------------------------------------------------------------------------
# Zero-shot user prompt template
# ---------------------------------------------------------------------------

_ZEROSHOT_USER_TEMPLATE = (
    "Extract all named entities from the following text.\n\n"
    "Entity types: {type_list}\n\n"
    "Text: {text}\n\n"
    "Output a JSON object in exactly this format:\n"
    '{{"entities": [{{"text": "exact span", "type": "TYPE", "start": 0, "end": 5}}], '
    '"relations": [], "events": []}}\n\n'
    "Rules:\n"
    "- Extract ALL entities matching the given types\n"
    "- 'start' is the character offset of the first character of the entity in the text\n"
    "- 'end' is the character offset after the last character (Python slice convention)\n"
    "- 'text' must be the exact substring from the input text\n"
    "- If no entities are found, return: {{\"entities\": [], \"relations\": [], \"events\": []}}\n"
    "- Output ONLY the JSON object, no explanation"
)


def build_zeroshot_prompt(text: str, dataset: str) -> tuple[str, str]:
    """Build zero-shot NER prompt for a given dataset.

    Args:
        text: Input text to extract entities from.
        dataset: Dataset name (conll2003, fewnerd, scierc).

    Returns:
        Tuple of (system_prompt, user_prompt).
    """
    info = DATASET_ENTITY_TYPES[dataset]
    type_list = ", ".join(info["types"])
    user_prompt = _ZEROSHOT_USER_TEMPLATE.format(text=text, type_list=type_list)
    return ZEROSHOT_SYSTEM_PROMPT, user_prompt


def build_zeroshot_prompt_with_descriptions(text: str, dataset: str) -> tuple[str, str]:
    """Build zero-shot NER prompt with type descriptions for better performance.

    Args:
        text: Input text to extract entities from.
        dataset: Dataset name (conll2003, fewnerd, scierc).

    Returns:
        Tuple of (system_prompt, user_prompt).
    """
    info = DATASET_ENTITY_TYPES[dataset]
    type_desc_lines = "\n".join(
        f"  - {t}: {info['descriptions'][t]}" for t in info["types"]
    )
    user_prompt = (
        "Extract all named entities from the following text.\n\n"
        f"Entity types and their definitions:\n{type_desc_lines}\n\n"
        f"Text: {text}\n\n"
        "Output a JSON object in exactly this format:\n"
        '{"entities": [{"text": "exact span", "type": "TYPE", "start": 0, "end": 5}], '
        '"relations": [], "events": []}\n\n'
        "Rules:\n"
        "- Extract ALL entities matching the given types\n"
        "- 'start' is the character offset of the first character of the entity in the text\n"
        "- 'end' is the character offset after the last character (Python slice convention)\n"
        "- 'text' must be the exact substring from the input text\n"
        "- If no entities are found, return: {\"entities\": [], \"relations\": [], \"events\": []}\n"
        "- Output ONLY the JSON object, no explanation"
    )
    return ZEROSHOT_SYSTEM_PROMPT, user_prompt


# ---------------------------------------------------------------------------
# Convenience: build prompts for existing pipeline (chat format)
# ---------------------------------------------------------------------------

def format_chat_messages(text: str, dataset: str, with_descriptions: bool = True) -> list[dict]:
    """Build chat messages list for vLLM chat completion.

    Args:
        text: Input text.
        dataset: Dataset name.
        with_descriptions: Whether to include type descriptions.

    Returns:
        List of message dicts [{"role": "system", ...}, {"role": "user", ...}].
    """
    if with_descriptions:
        sys_prompt, user_prompt = build_zeroshot_prompt_with_descriptions(text, dataset)
    else:
        sys_prompt, user_prompt = build_zeroshot_prompt(text, dataset)
    return [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt},
    ]
