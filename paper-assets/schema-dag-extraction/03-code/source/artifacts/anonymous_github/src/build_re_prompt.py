"""Relation Extraction prompt builder for FewRel-style tasks."""

import json
from typing import Optional


def build_re_prompt(
    text: str,
    head_entity: dict,
    tail_entity: dict,
    relation_types: list[str],
    include_descriptions: bool = False,
    type_descriptions: Optional[dict] = None,
) -> str:
    """构建 RE prompt: 给定文本和两个实体，判断关系类型。

    Args:
        text: 输��文本
        head_entity: {"name": str, "type": str (optional)}
        tail_entity: {"name": str, "type": str (optional)}
        relation_types: list of relation type names
        include_descriptions: 是否在 prompt 中包含 relation type 描述
        type_descriptions: {type_name: description} mapping
    Returns:
        prompt string
    """
    type_list = "\n".join(f"- {t}" for t in relation_types)

    if include_descriptions and type_descriptions:
        type_list = "\n".join(
            f"- {t}: {type_descriptions.get(t, '')}" for t in relation_types
        )

    head_str = head_entity["name"]
    tail_str = tail_entity["name"]

    prompt = f"""Given the following text, determine the relationship between the head entity and tail entity.

Text: {text}

Head entity: {head_str}
Tail entity: {tail_str}

Possible relation types:
{type_list}

Output ONLY the relation type name that best describes the relationship between "{head_str}" and "{tail_str}" in the given text. Output nothing else."""

    return prompt


def build_re_prompt_batch(
    samples: list[dict],
    relation_types: list[str],
    include_descriptions: bool = False,
    type_descriptions: Optional[dict] = None,
) -> list[str]:
    """批量构建 RE prompts。

    Args:
        samples: list of {"text": str, "head_entity": dict, "tail_entity": dict}
        relation_types: list of relation type names
        include_descriptions: 是否包含描述
        type_descriptions: {type_name: description}
    Returns:
        list of prompt strings
    """
    return [
        build_re_prompt(
            s["text"], s["head_entity"], s["tail_entity"],
            relation_types, include_descriptions, type_descriptions,
        )
        for s in samples
    ]


if __name__ == "__main__":
    with open("./configs/fewrel_relation_types.json") as f:
        rel_types = json.load(f)

    sample_prompt = build_re_prompt(
        text="Merpati flight 106 departed Jakarta on a domestic flight to Tanjung Pandan.",
        head_entity={"name": "TJQ"},
        tail_entity={"name": "Tanjung Pandan"},
        relation_types=list(rel_types.values())[:10],
    )
    print(sample_prompt)
