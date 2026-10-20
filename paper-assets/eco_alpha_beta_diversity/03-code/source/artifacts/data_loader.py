# Download and preprocess the Doshi & Hauser (2024) Dryad dataset.

import os
import re
import glob
import zipfile
from collections import Counter

import numpy as np
import pandas as pd

DRYAD_DOI = "10.5061/dryad.qfttdz0pm"
DRYAD_API = "https://datadryad.org/api/v2"
STANDARD_CONDITIONS = ["no-AI", "AI-editor", "AI-ideas+editor"]


# ---------------------------------------------------------------------------
# Download
# ---------------------------------------------------------------------------

def download_dataset(output_dir, force=False):
    """Download the Dryad dataset. Returns path to extracted data directory."""
    import requests

    data_dir = os.path.join(output_dir, "data")
    marker = os.path.join(data_dir, ".download_complete")
    if os.path.exists(marker) and not force:
        print(f"[data] Already downloaded → {data_dir}")
        return data_dir

    os.makedirs(data_dir, exist_ok=True)
    doi_enc = DRYAD_DOI.replace("/", "%2F").replace(":", "%3A")

    # --- attempt 1: dataset-level download (returns zip) ---
    url = f"{DRYAD_API}/datasets/doi%3A{doi_enc}/download"
    print(f"[data] Downloading from {url}")
    try:
        resp = requests.get(url, allow_redirects=True, timeout=180, stream=True)
        resp.raise_for_status()
        zip_path = os.path.join(data_dir, "dataset.zip")
        with open(zip_path, "wb") as f:
            for chunk in resp.iter_content(8192):
                f.write(chunk)
        if zipfile.is_zipfile(zip_path):
            with zipfile.ZipFile(zip_path, "r") as zf:
                zf.extractall(data_dir)
            print(f"[data] Extracted to {data_dir}")
        open(marker, "w").write("ok")
        return data_dir
    except Exception as e:
        print(f"[data] Direct download failed: {e}")

    # --- attempt 2: per-file via API ---
    try:
        meta = requests.get(f"{DRYAD_API}/datasets/doi%3A{doi_enc}", timeout=30).json()
        ver_href = (meta.get("_links", {}).get("stash:version", {}).get("href")
                    or meta.get("_links", {}).get("curies", [{}])[0].get("href", ""))
        if not ver_href:
            latest = meta.get("latestVersion", meta.get("id", ""))
            ver_href = f"/api/v2/versions/{latest}"
        version = requests.get(f"https://datadryad.org{ver_href}", timeout=30).json()
        vid = version.get("id", version.get("_links", {}).get("self", {}).get("href", "").split("/")[-1])
        files_url = f"{DRYAD_API}/versions/{vid}/files"
        files_resp = requests.get(files_url, timeout=30).json()
        for finfo in files_resp.get("_embedded", {}).get("stash:files", []):
            fname = finfo.get("path", "file")
            fhref = finfo.get("_links", {}).get("stash:file-download", {}).get("href", "")
            if fhref:
                print(f"[data]   downloading {fname}")
                r = requests.get(f"https://datadryad.org{fhref}", timeout=180)
                with open(os.path.join(data_dir, os.path.basename(fname)), "wb") as out:
                    out.write(r.content)
        open(marker, "w").write("ok")
        return data_dir
    except Exception as e2:
        print(f"[data] API fallback failed: {e2}")

    raise RuntimeError(
        f"Could not download dataset. Please download manually from "
        f"https://doi.org/{DRYAD_DOI} and place files in {data_dir}"
    )


# ---------------------------------------------------------------------------
# Tokenisation
# ---------------------------------------------------------------------------

def tokenize(text):
    text = str(text).lower()
    try:
        from nltk.tokenize import word_tokenize
        tokens = word_tokenize(text)
    except (ImportError, LookupError):
        tokens = re.findall(r"\b[a-z]+\b", text)
    return [t for t in tokens if t.isalpha() and len(t) > 1]


# ---------------------------------------------------------------------------
# Parse stories from downloaded files
# ---------------------------------------------------------------------------

def _find_data_files(data_dir):
    exts = ["csv", "tsv", "xlsx", "xls", "json"]
    files = []
    for ext in exts:
        files.extend(glob.glob(os.path.join(data_dir, "**", f"*.{ext}"), recursive=True))
    files = sorted(files)
    writer_files = [f for f in files if "writer" in os.path.basename(f).lower()]
    other_files = [f for f in files if f not in writer_files]
    return writer_files + other_files


def _guess_text_col(df):
    if "ai_story_gen.1.player.story" in df.columns:
        return "ai_story_gen.1.player.story"
    suffix_candidates = [c for c in df.columns if c.lower().endswith((".story", ".text"))]
    if suffix_candidates:
        best = max(suffix_candidates,
                   key=lambda c: df[c].dropna().astype(str).str.len().mean())
        if df[best].dropna().astype(str).str.len().mean() > 50:
            return best
    candidates = []
    for col in df.columns:
        cl = col.lower()
        if any(k in cl for k in ("story", "text", "content", "essay", "writing", "narrative", "response")):
            avg_len = df[col].dropna().astype(str).str.len().mean()
            if avg_len > 50:
                candidates.append((col, avg_len))
    if candidates:
        return max(candidates, key=lambda x: x[1])[0]
    str_cols = df.select_dtypes(include=["object"]).columns
    if len(str_cols):
        avg = {c: df[c].dropna().astype(str).str.len().mean() for c in str_cols}
        best = max(avg, key=avg.get)
        if avg[best] > 50:
            return best
    raise RuntimeError(f"Cannot find story text column in {list(df.columns[:10])}...")


def _guess_cond_col(df):
    for col in df.columns:
        cl = col.lower()
        if any(k in cl for k in ("condition", "treatment", "group", "arm", "experimental")):
            if 2 <= df[col].nunique() <= 10:
                return col
    for col in df.select_dtypes(include=["object", "category"]).columns:
        if 2 <= df[col].nunique() <= 5:
            return col
    return None


CONDITION_MAP = {
    "human": "no-AI",
    "human_1ai": "AI-editor",
    "human_5ai": "AI-ideas+editor",
}


def _map_condition(value):
    raw = str(value).strip().lower()
    if raw in CONDITION_MAP:
        return CONDITION_MAP[raw]
    return None


def load_stories(data_dir):
    """Load stories from a data directory. Returns list of story dicts."""
    files = _find_data_files(data_dir)
    if not files:
        raise FileNotFoundError(f"No data files in {data_dir}")
    print(f"[data] Found files: {[os.path.basename(f) for f in files]}")

    stories = []
    for fpath in files:
        ext = os.path.splitext(fpath)[1].lower()
        try:
            if ext == ".csv":
                df = pd.read_csv(fpath, encoding="utf-8")
            elif ext == ".tsv":
                df = pd.read_csv(fpath, sep="\t", encoding="utf-8")
            elif ext in (".xlsx", ".xls"):
                df = pd.read_excel(fpath)
            elif ext == ".json":
                df = pd.read_json(fpath)
            else:
                continue
        except Exception as e:
            print(f"[data]   skip {os.path.basename(fpath)}: {e}")
            continue

        if len(df) < 5:
            continue

        try:
            text_col = _guess_text_col(df)
        except RuntimeError:
            print(f"[data]   no text column in {os.path.basename(fpath)}")
            continue
        cond_col = _guess_cond_col(df)
        print(f"[data]   Using {os.path.basename(fpath)}  text='{text_col}'  cond='{cond_col}'")
        if cond_col:
            print(f"[data]   Raw conditions: {list(df[cond_col].unique())}")

        for _, row in df.iterrows():
            text = str(row[text_col])
            if len(text) < 30:
                continue
            if cond_col:
                cond = _map_condition(row[cond_col])
                if cond is None:
                    continue
            else:
                cond = "unknown"
            tokens = tokenize(text)
            if len(tokens) < 10:
                continue
            stories.append({
                "id": f"story_{len(stories)}",
                "text": text,
                "condition": cond,
                "tokens": tokens,
                "word_freq": dict(Counter(tokens)),
                "word_count": len(tokens),
            })
        if stories:
            break

    if not stories:
        raise RuntimeError(f"Failed to load real data from {data_dir}: no valid stories found")

    cond_counts = Counter(s["condition"] for s in stories)
    print(f"[data] Loaded {len(stories)} stories")
    for c, n in sorted(cond_counts.items()):
        print(f"[data]   {c}: {n}")
    return stories


# ---------------------------------------------------------------------------
# Text-length statistics (confound control)
# ---------------------------------------------------------------------------

def text_length_stats(stories):
    from collections import defaultdict
    lens = defaultdict(list)
    for s in stories:
        lens[s["condition"]].append(s["word_count"])
    stats = {}
    for c, arr in sorted(lens.items()):
        a = np.array(arr)
        stats[c] = {
            "mean": float(np.mean(a)), "median": float(np.median(a)),
            "std": float(np.std(a)), "min": int(np.min(a)),
            "max": int(np.max(a)), "n": len(a),
        }
    return stats


# ---------------------------------------------------------------------------
# Synthetic data for dry-run
# ---------------------------------------------------------------------------

def generate_synthetic_data(n_per_condition=40, rng=None):
    """Generate data with the expected alpha↑ beta↓ pattern for AI conditions."""
    if rng is None:
        rng = np.random.default_rng(42)

    vocab = [f"w{i}" for i in range(600)]
    common = vocab[:40]
    medium = vocab[40:200]
    rare = vocab[200:]

    stories = []
    for cond in STANDARD_CONDITIONS:
        for i in range(n_per_condition):
            if cond == "no-AI":
                # each story uses a PERSONAL vocabulary slice → high beta
                n_words = rng.integers(80, 180)
                personal_med = list(rng.choice(medium, 25, replace=False))
                personal_rare = list(rng.choice(rare, 25, replace=False))
                pool = common + personal_med + personal_rare
                alpha_param = 1.2  # steeper Zipf → lower evenness → lower alpha
            elif cond == "AI-editor":
                n_words = rng.integers(120, 250)
                shared_med = medium[:45]
                personal_rare = list(rng.choice(rare[:80], 10, replace=False))
                pool = common + list(shared_med) + personal_rare
                alpha_param = 0.9
            else:
                n_words = rng.integers(150, 300)
                shared_med = medium[:55]
                shared_rare = rare[:15]
                personal = list(rng.choice(rare[15:60], 5, replace=False))
                pool = common + list(shared_med) + list(shared_rare) + personal
                alpha_param = 0.7  # flatter → higher evenness → higher alpha

            weights = np.array([1.0 / (k + 1) ** alpha_param for k in range(len(pool))])
            weights /= weights.sum()
            tokens = list(rng.choice(pool, size=int(n_words), replace=True, p=weights))

            stories.append({
                "id": f"synth_{cond}_{i}",
                "text": " ".join(tokens),
                "condition": cond,
                "tokens": tokens,
                "word_freq": dict(Counter(tokens)),
                "word_count": len(tokens),
            })

    cc = Counter(s["condition"] for s in stories)
    print(f"[synth] Generated {len(stories)} stories")
    for c in STANDARD_CONDITIONS:
        print(f"[synth]   {c}: {cc[c]}")
    return stories
