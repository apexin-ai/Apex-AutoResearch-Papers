import os, sys, json, time
os.environ["OPENBLAS_NUM_THREADS"] = "2"
sys.path.insert(0, ".")
sys.path.insert(0, "./src/analysis")

LOG = "/tmp/reml_500_v2.log"
def log(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")
        f.flush()

try:
    import pandas as pd
    from src.analysis.reml_em import reml_em, ALL_FACETS

    df = pd.read_csv("./results/analysis/cross_model_llama_gemma.csv")
    for f_name in ALL_FACETS:
        df[f_name] = df[f_name].astype(str)
    if "binary_correct" not in df.columns:
        df["binary_correct"] = df["correct"]

    log(f"Data: {len(df)} rows, {df['model'].nunique()} models")
    log(f"Starting REML with max_iter=500, tol=1e-8")

    result = reml_em(df, "binary_correct", ALL_FACETS, max_iter=500, tol=1e-8, verbose=True)

    outpath = "./results/analysis/cross_model_reml_500iter.json"
    with open(outpath, "w") as f:
        json.dump(result, f, indent=2)
    log(f"DONE: converged={result['converged']}, iters={result['n_iterations']}, saved to {outpath}")

except Exception as e:
    log(f"ERROR: {e}")
    import traceback
    log(traceback.format_exc())
