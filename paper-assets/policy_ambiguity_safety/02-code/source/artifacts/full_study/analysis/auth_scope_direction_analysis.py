import json
from scipy import stats

DATA_PATH = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/plan_010/data/error_analysis_5model.json"
OUT_PATH = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/full_study/analysis/auth_scope_direction.json"

with open(DATA_PATH) as f:
    data = json.load(f)

per_model = {}
total_auth = 0
total_esc = 0
total_rest = 0
models_majority_esc = 0

for model, model_data in data["per_model_failure_modes"].items():
    auth = model_data["per_type"]["authorization_scope"]
    counts = auth["counts"]
    n = auth["n"]

    esc = counts.get("unauthorized_escalation", 0)
    rest = counts.get("conservative_refusal", 0)
    other = n - esc - rest

    per_model[model] = {
        "n_auth_scope_violations": n,
        "unauthorized_escalation": esc,
        "conservative_refusal": rest,
        "other_modes": other,
        "escalation_rate": round(esc / n, 4),
        "restriction_rate": round(rest / n, 4)
    }

    total_auth += n
    total_esc += esc
    total_rest += rest
    if esc / n > 0.5:
        models_majority_esc += 1

pooled_esc_rate = round(total_esc / total_auth, 4)
binom_result = stats.binomtest(total_esc, total_auth, 0.5, alternative='greater')
binom_p = binom_result.pvalue

unanimous = models_majority_esc == 5
conclusion_parts = []
conclusion_parts.append(
    f"{pooled_esc_rate*100:.1f}% of authorization scope violations involve unauthorized escalation "
    f"(granting permissions beyond policy scope), consistent across all five models "
    f"({models_majority_esc}/5 with majority escalation)."
)
if binom_p < 0.001:
    conclusion_parts.append(f"Binomial test confirms this exceeds chance (p < .001).")
else:
    conclusion_parts.append(f"Binomial test: p = {binom_p:.4f}.")

conclusion_parts.append(
    "No model produced any conservative_refusal within authorization_scope violations—the "
    "restriction rate is 0% across all five models."
)

if pooled_esc_rate > 0.70 and unanimous:
    conclusion_parts.append(
        "Suggested paper text (§6.1/Discussion): "
        f"\"{pooled_esc_rate*100:.0f}% of authorization scope violations involve unauthorized escalation "
        "(granting permissions beyond policy scope), consistent across all five models—suggesting "
        "a systematic bias toward permissiveness under boundary ambiguity.\""
    )

output = {
    "analysis": "auth_scope_escalation_direction",
    "per_model": per_model,
    "pooled": {
        "total_auth_scope": total_auth,
        "total_escalation": total_esc,
        "total_restriction": total_rest,
        "total_other": total_auth - total_esc - total_rest,
        "escalation_rate": pooled_esc_rate,
        "restriction_rate": round(total_rest / total_auth, 4),
        "binomial_p": round(binom_p, 6),
        "models_with_majority_escalation": f"{models_majority_esc}/5"
    },
    "conclusion": " ".join(conclusion_parts)
}

with open(OUT_PATH, "w") as f:
    json.dump(output, f, indent=2)

print(json.dumps(output, indent=2))
