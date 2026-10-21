"""Fix inverted D-study formula in temperature_stratified_analysis.json.

Bug: G_n = tau / (tau + delta * (ni / n_actual))  -- WRONG
Fix: G_n = tau / (tau + delta * (n_actual / ni))  -- CORRECT

When ni increases, error variance should shrink (divided by larger ni),
so G must monotonically increase with ni.
"""
import json

INPUT = "results/analysis/temperature_stratified_analysis.json"
N_ACTUAL = 200  # number of items in actual study

with open(INPUT) as f:
    data = json.load(f)

tau_pct = data["practical"]["correct"]["tau_pct"]
delta_pct = data["practical"]["correct"]["delta_pct"]

print(f"tau_pct={tau_pct}, delta_pct={delta_pct}, n_actual={N_ACTUAL}")
print(f"\n{'ni':>6}  {'old_G':>8}  {'new_G':>8}")
print("-" * 30)

old_dstudy = data["practical"]["d_study_correct"]
new_dstudy = {}
for ni_str, old_g in old_dstudy.items():
    ni = int(ni_str)
    new_g = tau_pct / (tau_pct + delta_pct * (N_ACTUAL / ni))
    new_dstudy[ni_str] = round(new_g, 4)
    print(f"{ni:>6}  {old_g:>8.4f}  {new_g:>8.4f}")

g_values = list(new_dstudy.values())
assert all(g_values[i] <= g_values[i+1] for i in range(len(g_values)-1)), \
    f"G must be monotonically increasing with n_items, got: {g_values}"
print("\nMonotonicity check: PASSED")

data["practical"]["d_study_correct"] = new_dstudy

# Fix min_items_G80: find minimum ni where G >= 0.80
min_g80 = None
for ni in range(1, 10001):
    g = tau_pct / (tau_pct + delta_pct * (N_ACTUAL / ni))
    if g >= 0.80:
        min_g80 = ni
        break

old_min = data["practical"]["min_items_G80"]
data["practical"]["min_items_G80"] = min_g80
print(f"\nmin_items_G80: {old_min} -> {min_g80}")

with open(INPUT, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nSaved fixed {INPUT}")
