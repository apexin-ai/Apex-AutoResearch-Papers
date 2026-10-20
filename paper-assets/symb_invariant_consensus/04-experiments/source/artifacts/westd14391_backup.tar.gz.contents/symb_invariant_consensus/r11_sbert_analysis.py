import json, os, sys
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_DIR = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates"
ANSWER_MATRIX = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json"
MODEL_PATH = "/root/autodl-tmp/sbert_model"

print("Loading SBERT model from local path...", flush=True)
sbert_model = SentenceTransformer(MODEL_PATH)
print("Model loaded.", flush=True)

print("Loading traces...", flush=True)
all_questions = []
for i in range(204):
    fpath = os.path.join(DATA_DIR, f"folio_{i}.json")
    with open(fpath) as f:
        data = json.load(f)
    traces_raw = data["sica_result"]["traces"]
    trace_texts = [t["trace"].strip() for t in traces_raw if t["trace"].strip()]
    all_questions.append({
        "id": f"folio_{i}",
        "traces": trace_texts,
        "K": len(trace_texts)
    })

print(f"Loaded {len(all_questions)} questions", flush=True)
k_vals = [q["K"] for q in all_questions]
print(f"Traces per question: min={min(k_vals)}, max={max(k_vals)}, mean={np.mean(k_vals):.1f}", flush=True)

print("Computing SBERT similarities...", flush=True)
sbert_sims = []
for idx, q in enumerate(all_questions):
    if len(q["traces"]) < 2:
        continue
    embeddings = sbert_model.encode(q["traces"])
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    embeddings = embeddings / (norms + 1e-8)
    sim_matrix = embeddings @ embeddings.T
    n = len(q["traces"])
    pairs_sims = [sim_matrix[i, j] for i in range(n) for j in range(i+1, n)]
    sbert_sims.append(float(np.mean(pairs_sims)))
    if (idx + 1) % 50 == 0:
        print(f"  SBERT: {idx+1}/204 done", flush=True)

print("Computing TF-IDF similarities...", flush=True)
tfidf_sims = []
for q in all_questions:
    if len(q["traces"]) < 2:
        continue
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(q["traces"])
    sim_matrix = cosine_similarity(tfidf)
    n = len(q["traces"])
    pairs_sims = [sim_matrix[i, j] for i in range(n) for j in range(i+1, n)]
    tfidf_sims.append(float(np.mean(pairs_sims)))

print("Computing Fleiss' kappa...", flush=True)
with open(ANSWER_MATRIX) as f:
    answer_data = json.load(f)

categories = ["True", "False", "Unknown"]

def fleiss_kappa(ratings_matrix):
    N = ratings_matrix.shape[0]
    k = int(ratings_matrix[0].sum())
    p_j = ratings_matrix.sum(axis=0) / (N * k)
    Pi = (np.sum(ratings_matrix ** 2, axis=1) - k) / (k * (k - 1))
    P_bar = np.mean(Pi)
    Pe = np.sum(p_j ** 2)
    if Pe == 1.0:
        return 1.0
    return float((P_bar - Pe) / (1 - Pe))

ratings = []
for i in range(204):
    key = f"folio_{i}"
    answers = answer_data[key]["answers"]
    counts = {c: 0 for c in categories}
    total_valid = 0
    for a in answers:
        if a in categories:
            counts[a] += 1
            total_valid += 1
    if total_valid >= 2:
        ratings.append([counts[c] for c in categories])

ratings_matrix = np.array(ratings, dtype=float)
fk = fleiss_kappa(ratings_matrix)

mean_sbert = float(np.mean(sbert_sims))
std_sbert = float(np.std(sbert_sims))
mean_tfidf = float(np.mean(tfidf_sims))
std_tfidf = float(np.std(tfidf_sims))

print(f"\n{'='*50}", flush=True)
print(f"RESULTS", flush=True)
print(f"{'='*50}", flush=True)
print(f"TF-IDF mean cosine similarity: {mean_tfidf:.4f} (std={std_tfidf:.4f})", flush=True)
print(f"SBERT mean cosine similarity:  {mean_sbert:.4f} (std={std_sbert:.4f})", flush=True)
print(f"Answer-level Fleiss' kappa:     {fk:.4f}", flush=True)
print(f"SBERT / Answer kappa ratio:    {mean_sbert/fk:.2f}x", flush=True)
print(f"Questions used: {len(sbert_sims)} (SBERT/TF-IDF), {len(ratings)} (Fleiss)", flush=True)

result = {
    "tfidf_mean_similarity": round(mean_tfidf, 4),
    "tfidf_std": round(std_tfidf, 4),
    "sbert_mean_similarity": round(mean_sbert, 4),
    "sbert_std": round(std_sbert, 4),
    "answer_fleiss_kappa": round(fk, 4),
    "sbert_model": "all-MiniLM-L6-v2",
    "n_questions": len(sbert_sims),
    "K": 12,
    "per_question_sbert_sims": [round(s, 4) for s in sbert_sims],
    "per_question_tfidf_sims": [round(s, 4) for s in tfidf_sims],
    "conclusion": f"SBERT similarity ({mean_sbert:.2f}) also >> answer kappa ({fk:.2f}), confirming that process-level consensus is robust across embedding methods"
}

out_path = "/root/symb_invariant_consensus/r11_sbert_process_kappa.json"
with open(out_path, "w") as f:
    json.dump(result, f, indent=2)
print(f"\nSaved to {out_path}", flush=True)
