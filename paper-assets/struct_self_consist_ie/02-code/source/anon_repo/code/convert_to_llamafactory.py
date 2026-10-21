import json
import sys
import os

PROMPT_TEMPLATE = """Extract all structured information (entities and relations) from the following text. Output a JSON object.

Text: {text}
Entity types: Generic, Material, Method, Metric, OtherScientificTerm, Task
Relation types: COMPARE, CONJUNCTION, EVALUATE-FOR, FEATURE-OF, HYPONYM-OF, PART-OF, USED-FOR

Output format: {{"entities": [...], "relations": [...], "events": []}}"""

def convert_instance(inst):
    human_msg = PROMPT_TEMPLATE.format(text=inst["text"])
    output = {
        "entities": inst.get("entities", []),
        "relations": inst.get("relations", []),
        "events": inst.get("events", []),
    }
    return {
        "conversations": [
            {"from": "human", "value": human_msg},
            {"from": "gpt", "value": json.dumps(output, ensure_ascii=False)},
        ]
    }

def convert_file(input_path, output_path):
    results = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            inst = json.loads(line)
            results.append(convert_instance(inst))
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Converted {len(results)} instances: {input_path} -> {output_path}")

if __name__ == "__main__":
    data_dir = "/root/autodl-tmp/struct_self_consist_ie/data"
    for split in ["train", "dev"]:
        convert_file(
            os.path.join(data_dir, f"{split}.jsonl"),
            os.path.join(data_dir, f"llmfactory_{split}.json"),
        )
