"""Convert frontier SCB results.json to intermediates format for cross_model_extract.py."""
import json, os, sys

FRONTIER_RESULTS = sys.argv[1]  # e.g. results/exp_d135_frontier_scb/gpt-4.1/results.json
FOLIO_DATA = "/root/symb_invariant_consensus/data/folio_full.json"
OUTPUT_DIR = sys.argv[2]  # e.g. results/exp_d135_frontier_scb/gpt-4.1/intermediates

with open(FOLIO_DATA) as f:
    folio = {p["id"]: p for p in json.load(f)}

with open(FRONTIER_RESULTS) as f:
    frontier = json.load(f)

os.makedirs(OUTPUT_DIR, exist_ok=True)

for q in frontier["per_question"]:
    qid = q["question_id"]
    prob = folio[qid]
    intermediate = {
        "problem": {
            "id": qid,
            "problem": prob["problem"],
            "solution": prob.get("solution", ""),
            "answer": prob["answer"],
            "level": prob.get("level", ""),
            "premises_fol": prob.get("premises_fol", ""),
            "conclusion_fol": prob.get("conclusion_fol", ""),
            "dataset": "folio",
        },
        "sica_result": {
            "answer": q["sc_answer"],
            "scores": {},
            "answer_counts": q["answer_distribution"],
            "traces": q["traces"],
            "constraints_stats": {},
            "maxsat_stats": {},
            "timing": {},
        },
    }
    with open(os.path.join(OUTPUT_DIR, f"{qid}.json"), "w") as f:
        json.dump(intermediate, f, indent=2, ensure_ascii=False)

print(f"Converted {len(frontier['per_question'])} problems to {OUTPUT_DIR}")
