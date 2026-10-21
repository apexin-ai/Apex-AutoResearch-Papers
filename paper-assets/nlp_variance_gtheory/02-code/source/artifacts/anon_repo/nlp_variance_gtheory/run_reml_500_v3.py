import os, sys, json, time, traceback
os.environ["OPENBLAS_NUM_THREADS"] = "2"
sys.path.insert(0, ".")
sys.path.insert(0, "./src/analysis")

LOG = open("/tmp/reml_500_v3.log", "w", buffering=1)
sys.stdout = LOG
sys.stderr = LOG

try:
    import pandas as pd
    from src.analysis.reml_em import reml_em, ALL_FACETS

    df = pd.read_csv("./results/analysis/cross_model_llama_gemma.csv")
    for f_name in ALL_FACETS:
        df[f_name] = df[f_name].astype(str)
    if "binary_correct" not in df.columns:
        df["binary_correct"] = df["correct"]

    print(f"Data: {len(df)} rows, {df['model'].nunique()} models", flush=True)
    print(f"Starting REML with max_iter=500, tol=1e-8", flush=True)

    result = reml_em(df, "binary_correct", ALL_FACETS, max_iter=500, tol=1e-8, verbose=True)

    outpath = "./results/analysis/cross_model_reml_500iter.json"
    with open(outpath, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nDONE: converged={result['converged']}, iters={result['n_iterations']}, saved to {outpath}", flush=True)

except Exception as e:
    print(f"ERROR: {e}", flush=True)
    traceback.print_exc(file=LOG)
    LOG.flush()
finally:
    LOG.flush()
    LOG.close()
