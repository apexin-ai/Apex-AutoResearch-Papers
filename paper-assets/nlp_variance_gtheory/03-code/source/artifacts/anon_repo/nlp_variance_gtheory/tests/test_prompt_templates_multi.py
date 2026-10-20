"""Verify prompt templates for all benchmarks."""
import sys
sys.path.insert(0, ".")
from src.data.prompt_templates import format_benchmark_prompt, BENCHMARK_TEMPLATES

MOCK_ITEMS = {
    "gsm8k": {
        "question": "Janet has 3 apples. She buys 5 more. How many apples does she have?",
        "choices": None,
        "answer": "8",
        "metadata": {"raw_answer": "Janet starts with 3 apples and buys 5 more.\n3 + 5 = 8\n#### 8"},
    },
    "arc_challenge": {
        "question": "Which of the following is the best conductor of electricity?",
        "choices": ["Wood", "Copper", "Rubber"],
        "answer": "B",
        "answer_idx": 1,
    },
    "hellaswag": {
        "question": "A person is standing in a kitchen. They pick up a knife and",
        "choices": [
            "begin to chop vegetables on the cutting board.",
            "throw it across the room at a target.",
            "start to juggle three knives in the air.",
            "use it to open a can of paint.",
        ],
        "answer_idx": 0,
    },
}

MOCK_FEW_SHOT = {
    "gsm8k": [{
        "question": "Tom has 2 cats. He adopts 3 more. How many cats?",
        "answer": "5",
        "metadata": {"raw_answer": "2 + 3 = 5\n#### 5"},
    }],
    "arc_challenge": [{
        "question": "What is the boiling point of water?",
        "choices": ["50C", "100C", "150C", "200C"],
        "answer_idx": 1,
    }],
    "hellaswag": [{
        "question": "A man walks into a bar and",
        "choices": [
            "orders a drink from the bartender.",
            "starts flying around the room.",
            "turns into a pumpkin.",
            "disappears into thin air.",
        ],
        "answer_idx": 0,
    }],
}

def main():
    errors = []
    for benchmark in ["gsm8k", "arc_challenge", "hellaswag"]:
        item = MOCK_ITEMS[benchmark]
        few_shot = MOCK_FEW_SHOT[benchmark]
        sep = "=" * 60
        print(f"\n{sep}")
        print(f"BENCHMARK: {benchmark}")
        print(sep)
        for tid in range(1, 7):
            try:
                prompt = format_benchmark_prompt(
                    benchmark=benchmark,
                    template_id=tid,
                    question=item["question"],
                    choices=item["choices"],
                    few_shot_examples=few_shot,
                )
                print(f"\n--- Template {tid} (1-shot) ---")
                print(prompt)
                assert len(prompt) > 20, f"Prompt too short: {len(prompt)}"
                assert item["question"] in prompt, "Question missing"
                if benchmark == "gsm8k":
                    assert "####" in prompt, "GSM8K missing ####"
                if benchmark in ("arc_challenge", "hellaswag"):
                    has_label = any(x in prompt for x in ["A.", "(A)", "A)", "Option A"])
                    assert has_label, "Choice labels missing"
            except Exception as e:
                errors.append(f"{benchmark} t{tid}: {e}")
                print(f"  ERROR: {e}")
        try:
            prompt_zs = format_benchmark_prompt(
                benchmark=benchmark, template_id=1,
                question=item["question"], choices=item["choices"],
            )
            print(f"\n--- Template 1 (zero-shot) ---")
            print(prompt_zs)
        except Exception as e:
            errors.append(f"{benchmark} zero-shot: {e}")

    # ARC with 5 choices
    sep = "=" * 60
    print(f"\n{sep}\nARC with 5 choices\n{sep}")
    prompt_5 = format_benchmark_prompt(
        benchmark="arc_challenge", template_id=1,
        question="What color is the sky?",
        choices=["Red", "Blue", "Green", "Yellow", "Purple"],
    )
    print(prompt_5)
    assert "E." in prompt_5, "5th label E missing"

    print(f"\n{sep}")
    if errors:
        print(f"FAILED: {len(errors)} errors")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("ALL CHECKS PASSED")

if __name__ == "__main__":
    main()
