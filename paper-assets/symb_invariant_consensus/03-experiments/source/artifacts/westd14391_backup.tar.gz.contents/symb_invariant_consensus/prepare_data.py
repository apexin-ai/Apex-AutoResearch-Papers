"""Download and prepare FOLIO + ProofWriter datasets for SICA experiments."""
import json
import os
import re

def prepare_folio():
    """Download FOLIO from HuggingFace and convert to SICA format."""
    from datasets import load_dataset
    ds = load_dataset("yale-nlp/FOLIO")

    problems = []
    idx = 0
    for split in ds:
        for row in ds[split]:
            premises = row.get("premises", "") or ""
            conclusion = row.get("conclusion", "") or ""
            label = row.get("label", "") or ""

            if label == "True":
                answer = "True"
            elif label == "False":
                answer = "False"
            else:
                answer = "Unknown"

            problem_text = (
                f"Given the following premises:\n{premises.strip()}\n\n"
                f"Determine whether the following conclusion is true, false, or unknown:\n{conclusion.strip()}"
            )

            problems.append({
                "id": f"folio_{idx:04d}",
                "problem": problem_text,
                "solution": "",
                "answer": answer,
                "dataset": "folio",
                "level": "logic",
            })
            idx += 1

    out = "/root/symb_invariant_consensus/data/folio_full.json"
    with open(out, "w") as f:
        json.dump(problems, f, indent=2, ensure_ascii=False)
    print(f"FOLIO: {len(problems)} problems saved to {out}")
    return len(problems)


def prepare_proofwriter():
    """Download ProofWriter from HuggingFace and convert to SICA format."""
    from datasets import load_dataset

    ANSWER_MAP = {"A": "True", "B": "False", "C": "Unknown"}
    QUESTION_PREFIX = re.compile(
        r"^Based on the above information,\s*is the following statement true,\s*false,\s*or unknown\?\s*",
        re.IGNORECASE,
    )

    try:
        ds = load_dataset("sileod/proofwriter")
    except Exception as e1:
        print(f"sileod/proofwriter failed: {e1}")
        try:
            ds = load_dataset("tasksource/proofwriter")
        except Exception as e2:
            print(f"tasksource/proofwriter also failed: {e2}")
            raise

    problems = []
    idx = 0
    for split in ds:
        for row in ds[split]:
            context = row.get("context", "") or row.get("theory", "") or ""
            question = row.get("question", "") or ""
            answer_key = row.get("answer", "") or ""

            if answer_key in ANSWER_MAP:
                label = ANSWER_MAP[answer_key]
            elif answer_key in ("True", "False", "Unknown"):
                label = answer_key
            else:
                label = str(answer_key)

            conclusion = QUESTION_PREFIX.sub("", question).strip()
            if not conclusion:
                conclusion = question.strip()

            problem_text = (
                f"Given the following facts and rules:\n{context.strip()}\n\n"
                f"Determine whether the following statement is true, false, or unknown:\n{conclusion}"
            )

            depth = row.get("depth", "unknown")
            problems.append({
                "id": f"pw_{idx:04d}",
                "problem": problem_text,
                "solution": "",
                "answer": label,
                "dataset": "proofwriter",
                "level": f"D{depth}" if str(depth).isdigit() else str(depth),
            })
            idx += 1

    if len(problems) > 600:
        import random
        random.seed(42)
        random.shuffle(problems)
        problems = problems[:600]
        for i, p in enumerate(problems):
            p["id"] = f"pw_{i:04d}"

    out = "/root/symb_invariant_consensus/data/proofwriter_full.json"
    with open(out, "w") as f:
        json.dump(problems, f, indent=2, ensure_ascii=False)
    print(f"ProofWriter: {len(problems)} problems saved to {out}")
    return len(problems)


if __name__ == "__main__":
    os.makedirs("/root/symb_invariant_consensus/data", exist_ok=True)
    print("=== Preparing FOLIO ===")
    n_folio = prepare_folio()
    print("=== Preparing ProofWriter ===")
    n_pw = prepare_proofwriter()
    print(f"\nTotal: {n_folio} FOLIO + {n_pw} ProofWriter = {n_folio + n_pw} problems")
