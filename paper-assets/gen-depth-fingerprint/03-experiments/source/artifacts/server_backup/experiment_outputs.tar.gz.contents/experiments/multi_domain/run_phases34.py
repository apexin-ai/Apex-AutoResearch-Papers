"""Run phases 3 (feature extraction) and 4 (evaluation) after generation completes."""
import sys
sys.path.insert(0, '/root/gen-depth-fingerprint/experiments/multi_domain')
from run_experiment import extract_features, evaluate

if __name__ == "__main__":
    df = extract_features()
    results = evaluate(df)
    print("\n=== DONE ===")
    for domain, dres in results.get("domains", {}).items():
        bf1 = dres.get("binary_f1", "N/A")
        mf1 = dres.get("multiclass_f1", "N/A")
        print(f"  {domain}: binary_f1={bf1}, 3class_f1={mf1}")
    cs = results.get("cross_domain_summary", {})
    if cs:
        print(f"  Conclusion: {cs.get('conclusion')}")
