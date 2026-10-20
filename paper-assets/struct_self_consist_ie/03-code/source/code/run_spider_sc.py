#!/usr/bin/env python3
"""Spider SQL Self-Consistency Pilot: SC failure modes on text-to-SQL.

Cross-task universality extension -- SQL has deterministic verification
via execution against SQLite databases.  Uses execution-result equivalence
(not SQL text) for agreement and degeneracy detection.

Usage:
    export OPENROUTER_API_KEY=[REDACTED]
    python run_spider_sc.py [--n_samples 8] [--temperature 1.0] [--seed 42]
                            [--output_dir ./results] [--test_api]
"""

import argparse
import json
import os
import random
import shutil
import signal
import sqlite3
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
from datasets import load_dataset
from openai import OpenAI
from scipy.stats import spearmanr, kendalltau

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
API_BASE_URL = "http://47.94.22.126/v1"
MODEL_ID = "openai/gpt-5.5"
SPIDER_DATASET = "xlangai/spider"
N_FEWSHOT = 3
SQL_TIMEOUT = 5
MAX_RETRIES = 5
RETRY_BASE_DELAY = 2.0
DEFAULT_DB_DIR = "./spider_databases"


# ---------------------------------------------------------------------------
# SQL Execution
# ---------------------------------------------------------------------------
class SQLTimeoutError(Exception):
    pass


def _timeout_handler(signum, frame):
    raise SQLTimeoutError("SQL execution timed out")


def execute_sql(db_path: str, sql: str, timeout: int = SQL_TIMEOUT):
    if not os.path.exists(db_path):
        return None, f"db not found: {db_path}"
    old = signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(timeout)
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA query_only = ON")
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        signal.alarm(0)
        return rows, None
    except SQLTimeoutError:
        signal.alarm(0)
        return None, "timeout"
    except Exception as e:
        signal.alarm(0)
        return None, str(e)
    finally:
        signal.signal(signal.SIGALRM, old)


def normalize_result(rows):
    if rows is None:
        return None
    try:
        return tuple(sorted(tuple(str(v) for v in r) for r in rows))
    except TypeError:
        return tuple(tuple(str(v) for v in r) for r in rows)


def extract_sql(text: str) -> str:
    text = text.strip()
    for prefix in ("```sql", "```SQL", "```"):
        if text.startswith(prefix):
            text = text[len(prefix):]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()
    lines = [l.strip() for l in text.split("\n")
             if l.strip() and not l.strip().startswith("--")]
    sql = " ".join(lines)
    while sql.endswith(";"):
        sql = sql[:-1].strip()
    return sql


# ---------------------------------------------------------------------------
# Data & Schema
# ---------------------------------------------------------------------------
def load_spider_data(n_examples: int, seed: int):
    ds = load_dataset(SPIDER_DATASET, split="validation")
    train_ds = load_dataset(SPIDER_DATASET, split="train")
    rng = random.Random(seed)
    indices = list(range(len(ds)))
    rng.shuffle(indices)
    sampled = [ds[i] for i in indices[:n_examples]]
    return sampled, train_ds


_schema_cache: dict[str, str | None] = {}


def get_schema(db_path: str, db_id: str) -> str | None:
    if db_id in _schema_cache:
        return _schema_cache[db_id]
    if not os.path.exists(db_path):
        _schema_cache[db_id] = None
        return None

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "SELECT name FROM sqlite_master "
        "WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    )
    tables = [r[0] for r in cur.fetchall()]

    parts = []
    for tbl in tables:
        cur.execute(f'PRAGMA table_info("{tbl}")')
        columns = cur.fetchall()
        col_strs, pk_cols = [], []
        for _, name, ctype, notnull, _, pk in columns:
            s = f"  {name} {ctype or 'TEXT'}"
            if notnull:
                s += " NOT NULL"
            col_strs.append(s)
            if pk:
                pk_cols.append(name)
        if pk_cols:
            col_strs.append(f"  PRIMARY KEY ({', '.join(pk_cols)})")
        cur.execute(f'PRAGMA foreign_key_list("{tbl}")')
        for fk in cur.fetchall():
            _, _, ref_tbl, from_col, to_col, *_ = fk
            col_strs.append(
                f"  FOREIGN KEY ({from_col}) REFERENCES {ref_tbl}({to_col})"
            )
        parts.append(f"CREATE TABLE {tbl} (\n" + ",\n".join(col_strs) + "\n);")

    conn.close()
    schema = "\n\n".join(parts)
    _schema_cache[db_id] = schema
    return schema


_train_by_db: dict[str, list[int]] = {}


def _index_train_by_db(train_ds):
    global _train_by_db
    if _train_by_db:
        return
    for i in range(len(train_ds)):
        db = train_ds[i]["db_id"]
        _train_by_db.setdefault(db, []).append(i)


def get_fewshot(train_ds, db_id: str, n: int = N_FEWSHOT) -> list:
    _index_train_by_db(train_ds)
    same = _train_by_db.get(db_id, [])
    if len(same) >= n:
        chosen = random.sample(same, n)
    else:
        others = [
            i for db, idxs in _train_by_db.items() if db != db_id for i in idxs
        ]
        chosen = same + random.sample(others, min(n - len(same), len(others)))
    return [train_ds[i] for i in chosen[:n]]


SYSTEM_MSG = (
    "You are a SQL expert. Given a database schema and a question, "
    "write the SQL query that answers the question. "
    "Output only the SQL query, nothing else."
)


def build_messages(example: dict, train_ds, db_dir: str) -> list[dict] | None:
    db_path = os.path.join(db_dir, example["db_id"], f"{example['db_id']}.sqlite")
    schema = get_schema(db_path, example["db_id"])
    if schema is None:
        return None

    fs_examples = get_fewshot(train_ds, example["db_id"])
    blocks = []
    for fs in fs_examples:
        fs_path = os.path.join(db_dir, fs["db_id"], f"{fs['db_id']}.sqlite")
        fs_schema = get_schema(fs_path, fs["db_id"])
        if fs_schema is None:
            continue
        blocks.append(
            f"Database schema:\n{fs_schema}\n\n"
            f"Question: {fs['question']}\nSQL: {fs['query']}"
        )
    blocks.append(
        f"Database schema:\n{schema}\n\n"
        f"Question: {example['question']}\nSQL:"
    )
    return [
        {"role": "system", "content": SYSTEM_MSG},
        {"role": "user", "content": "\n\n---\n\n".join(blocks)},
    ]


# ---------------------------------------------------------------------------
# API sampling (following humaneval_sc pattern)
# ---------------------------------------------------------------------------
def create_client() -> OpenAI:
    api_key = [REDACTED]"OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")
    return OpenAI(base_url=API_BASE_URL, api_key=[REDACTED]


def api_sample(
    client: OpenAI, messages: list[dict],
    n: int = 8, temperature: float = 1.0, max_tokens: int = 512,
) -> list[str]:
    for attempt in range(MAX_RETRIES):
        try:
            resp = client.chat.completions.create(
                model=MODEL_ID, messages=messages,
                n=n, temperature=temperature, max_tokens=max_tokens,
            )
            return [c.message.content for c in resp.choices]
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                raise
            delay = RETRY_BASE_DELAY * (2 ** attempt) + random.uniform(0, 1)
            print(f"  API error (attempt {attempt+1}/{MAX_RETRIES}): {e}")
            time.sleep(delay)
    return []


def api_greedy(
    client: OpenAI, messages: list[dict], max_tokens: int = 512,
) -> str:
    for attempt in range(MAX_RETRIES):
        try:
            resp = client.chat.completions.create(
                model=MODEL_ID, messages=messages,
                n=1, temperature=0.0, max_tokens=max_tokens,
            )
            return resp.choices[0].message.content
        except Exception as e:
            err_str = str(e)
            if "temperature" in err_str and "0" in err_str:
                resp = client.chat.completions.create(
                    model=MODEL_ID, messages=messages,
                    n=1, temperature=1.0, max_tokens=max_tokens,
                )
                return resp.choices[0].message.content
            if attempt == MAX_RETRIES - 1:
                raise
            delay = RETRY_BASE_DELAY * (2 ** attempt) + random.uniform(0, 1)
            time.sleep(delay)
    return ""


def test_api_connectivity(client: OpenAI) -> bool:
    print("Testing API connectivity...")
    try:
        resp = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "user",
                       "content": "Write SQL to select all from table t."}],
            n=1, temperature=1.0, max_tokens=64,
        )
        print(f"  Response: {resp.choices[0].message.content!r}")
        print("  API OK")
        return True
    except Exception as e:
        print(f"  API FAILED: {e}")
        return False


# ---------------------------------------------------------------------------
# Failure mode classification (aligned with NER diagnostic cascade)
# ---------------------------------------------------------------------------
def classify_failure_mode(
    is_degenerate: bool, agreement: float,
    mv_correct: bool, greedy_correct: bool,
) -> str | None:
    """F1-F4 cascade aligned with NER framework.

    F1: Degeneracy -- all execution results identical, no SC diversity
    F2: Low agreement -- diverse results, MV unreliable
    F3: High agreement but wrong -- confident consensus on wrong answer
    F4: Selection gap -- greedy correct but MV fails
    """
    if is_degenerate:
        return "F1_degeneracy"
    if agreement < 0.5:
        return "F2_low_agreement"
    if not mv_correct:
        return "F3_high_agreement_wrong"
    if greedy_correct and not mv_correct:
        return "F4_selection_gap"
    return None


# ---------------------------------------------------------------------------
# Spider database setup
# ---------------------------------------------------------------------------
def setup_spider_dbs(db_dir: str) -> bool:
    if os.path.isdir(db_dir):
        n = sum(1 for d in os.listdir(db_dir)
                if os.path.isdir(os.path.join(db_dir, d)))
        if n > 0:
            print(f"Spider databases: {db_dir} ({n} dbs)")
            return True

    print(f"Spider databases not found at {db_dir}, downloading...")
    os.makedirs(db_dir, exist_ok=True)
    tmp = db_dir + "_tmp_clone"
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1",
             "https://github.com/taoyds/spider.git", tmp],
            check=True, timeout=600,
        )
        src = os.path.join(tmp, "database")
        if not os.path.isdir(src):
            print("ERROR: spider clone has no database/ dir")
            return False
        for item in os.listdir(src):
            s = os.path.join(src, item)
            if os.path.isdir(s):
                shutil.copytree(s, os.path.join(db_dir, item),
                                dirs_exist_ok=True)
        shutil.rmtree(tmp, ignore_errors=True)
        n = sum(1 for d in os.listdir(db_dir)
                if os.path.isdir(os.path.join(db_dir, d)))
        print(f"Downloaded {n} databases to {db_dir}")
        return True
    except Exception as e:
        print(f"ERROR downloading: {e}")
        print(f"Manual: git clone https://github.com/taoyds/spider.git "
              f"&& cp -r spider/database/* {db_dir}/")
        return False


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def run_pipeline(args: argparse.Namespace):
    random.seed(args.seed)
    np.random.seed(args.seed)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    db_dir = args.db_dir

    if not setup_spider_dbs(db_dir):
        sys.exit(1)

    # Load data
    print(f"Loading Spider ({SPIDER_DATASET})...")
    examples, train_ds = load_spider_data(args.n_examples, args.seed)
    print(f"  {len(examples)} examples, "
          f"{len(set(e['db_id'] for e in examples))} dbs")

    # Build prompts
    print("Building prompts...")
    valid_examples, messages_list = [], []
    for ex in examples:
        msgs = build_messages(ex, train_ds, db_dir)
        if msgs is not None:
            valid_examples.append(ex)
            messages_list.append(msgs)
    print(f"  Valid: {len(valid_examples)}/{len(examples)}")

    # Client
    client = create_client()
    if args.test_api:
        if not test_api_connectivity(client):
            sys.exit(1)
        print()

    # Resume from checkpoint
    results: list[dict] = []
    checkpoint_path = output_dir / "checkpoint.jsonl"
    completed_idxs: set[int] = set()
    if checkpoint_path.exists():
        with open(checkpoint_path) as f:
            for line in f:
                rec = json.loads(line)
                results.append(rec)
                completed_idxs.add(rec["idx"])
        print(f"Resumed {len(results)} from checkpoint")

    remaining = [
        (i, ex, msgs)
        for i, (ex, msgs) in enumerate(zip(valid_examples, messages_list))
        if i not in completed_idxs
    ]
    print(f"Processing {len(remaining)} remaining "
          f"(N={args.n_samples}, T={args.temperature})...\n")

    t_total = time.time()

    for seq, (idx, ex, msgs) in enumerate(remaining):
        db_id = ex["db_id"]
        db_path = os.path.join(db_dir, db_id, f"{db_id}.sqlite")

        done = len(completed_idxs) + seq + 1
        print(f"[{done}/{len(valid_examples)}] {db_id}: "
              f"{ex['question'][:60]}...")

        # Gold execution
        gold_rows, gold_err = execute_sql(db_path, ex["query"])
        if gold_err:
            rec = dict(idx=idx, db_id=db_id, question=ex["question"],
                       gold_query=ex["query"], gold_error=gold_err,
                       skipped=True)
            results.append(rec)
            with open(checkpoint_path, "a") as f:
                f.write(json.dumps(rec, default=str) + "\n")
            print(f"  SKIP gold error: {gold_err}")
            continue

        gold_norm = normalize_result(gold_rows)

        # API sampling
        t0 = time.time()
        raw_samples = api_sample(
            client, msgs, n=args.n_samples, temperature=args.temperature,
        )
        greedy_raw = api_greedy(client, msgs)
        api_sec = time.time() - t0

        # Execute all samples
        sqls, norms, corrects, errors = [], [], [], []
        for raw in raw_samples:
            sql = extract_sql(raw)
            sqls.append(sql)
            rows, err = execute_sql(db_path, sql)
            norm = normalize_result(rows)
            norms.append(norm)
            errors.append(err)
            corrects.append((norm == gold_norm) and (err is None))

        # Greedy
        g_sql = extract_sql(greedy_raw)
        g_rows, g_err = execute_sql(db_path, g_sql)
        g_norm = normalize_result(g_rows)
        g_ok = (g_norm == gold_norm) and (g_err is None)

        # ── Bug 2 fix: degeneracy on EXECUTION RESULTS, not SQL text ──
        valid_norms = [n for n in norms if n is not None]
        unique_results = set(valid_norms) if valid_norms else set()
        is_degenerate = len(unique_results) <= 1

        # MV on execution results
        result_counts = Counter(n for n in norms if n is not None)
        if result_counts:
            mv_result = result_counts.most_common(1)[0][0]
            mv_ok = (mv_result == gold_norm)
            agreement = result_counts.most_common(1)[0][1] / args.n_samples
        else:
            mv_ok = False
            agreement = 0.0

        oracle_ok = any(corrects)

        # ── Bug 1 fix: failure modes aligned with NER cascade ──
        failure_mode = classify_failure_mode(
            is_degenerate, agreement, mv_ok, g_ok,
        )

        n_correct = sum(corrects)
        n_exec_err = sum(1 for e in errors if e is not None)
        print(f"  API {api_sec:.1f}s | correct {n_correct}/{args.n_samples} | "
              f"greedy={'OK' if g_ok else 'FAIL'} | MV={'OK' if mv_ok else 'FAIL'} | "
              f"agree={agreement:.2f} | {failure_mode or 'OK'}")

        rec = dict(
            idx=idx, db_id=db_id, question=ex["question"],
            gold_query=ex["query"],
            greedy_sql=g_sql, greedy_correct=g_ok,
            sample_sqls=sqls, sample_correct=corrects,
            n_unique_sqls=len(set(sqls)),
            n_unique_results=len(unique_results),
            is_degenerate=is_degenerate,
            mv_correct=mv_ok, oracle_correct=oracle_ok,
            agreement=agreement,
            correct_frac=n_correct / args.n_samples,
            failure_mode=failure_mode,
            n_exec_errors=n_exec_err,
            api_sec=round(api_sec, 2),
            skipped=False,
        )
        results.append(rec)
        with open(checkpoint_path, "a") as f:
            f.write(json.dumps(rec, default=str) + "\n")

    # ── Summary ────────────────────────────────────────────────────────
    valid = [r for r in results if not r.get("skipped")]
    nv = len(valid)
    if nv == 0:
        print("ERROR: no valid results")
        return

    t_elapsed = time.time() - t_total

    g_acc = sum(r["greedy_correct"] for r in valid) / nv
    mv_acc = sum(r["mv_correct"] for r in valid) / nv
    o_acc = sum(r["oracle_correct"] for r in valid) / nv

    agreement_list = [r["agreement"] for r in valid]
    correctness_list = [r["correct_frac"] for r in valid]

    sp_rho, sp_p = (np.nan, np.nan)
    kt_tau, kt_p = (np.nan, np.nan)
    if len(agreement_list) > 2:
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            sp_rho, sp_p = spearmanr(agreement_list, correctness_list)
            kt_tau, kt_p = kendalltau(agreement_list, correctness_list)

    # Failure mode counts
    fm_counts = Counter(r.get("failure_mode") for r in valid)
    f1 = fm_counts.get("F1_degeneracy", 0)
    f2 = fm_counts.get("F2_low_agreement", 0)
    f3 = fm_counts.get("F3_high_agreement_wrong", 0)
    f4 = fm_counts.get("F4_selection_gap", 0)

    degen_rate = sum(r["is_degenerate"] for r in valid) / nv
    total_exec_err = sum(r.get("n_exec_errors", 0) for r in valid)

    summary = dict(
        config=dict(
            model=MODEL_ID, api_base=API_BASE_URL,
            n_samples=args.n_samples, temperature=args.temperature,
            n_examples=args.n_examples, n_fewshot=N_FEWSHOT,
            seed=args.seed, task="text-to-sql", dataset="spider-dev",
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
        ),
        counts=dict(
            total=len(examples), valid=nv,
            skipped_gold_error=len(results) - nv,
        ),
        accuracy=dict(
            greedy=round(g_acc, 4),
            majority_voting=round(mv_acc, 4),
            oracle=round(o_acc, 4),
        ),
        sc_gain=dict(
            mv_minus_greedy=round(mv_acc - g_acc, 4),
            oracle_minus_greedy=round(o_acc - g_acc, 4),
        ),
        diagnostics=dict(
            degeneracy_rate=round(degen_rate, 4),
            spearman_rho=round(float(sp_rho), 4) if not np.isnan(sp_rho) else None,
            spearman_p=float(f"{sp_p:.6f}") if not np.isnan(sp_p) else None,
            kendall_tau=round(float(kt_tau), 4) if not np.isnan(kt_tau) else None,
            kendall_p=float(f"{kt_p:.6f}") if not np.isnan(kt_p) else None,
        ),
        failure_modes=dict(
            F1_degeneracy=f1, F1_rate=round(f1 / nv, 4),
            F2_low_agreement=f2, F2_rate=round(f2 / nv, 4),
            F3_high_agreement_wrong=f3, F3_rate=round(f3 / nv, 4),
            F4_selection_gap=f4, F4_rate=round(f4 / nv, 4),
        ),
        exec_errors_total=total_exec_err,
        timing=dict(elapsed_sec=round(t_elapsed, 1)),
    )

    with open(output_dir / "per_instance.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    with open(output_dir / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'='*60}")
    print("SPIDER SQL SC PILOT RESULTS")
    print(f"{'='*60}")
    print(f"Valid: {nv}/{len(examples)}")
    print(f"\nExecution Accuracy:")
    print(f"  Greedy:    {g_acc:.4f}")
    print(f"  MV:        {mv_acc:.4f}  ({mv_acc - g_acc:+.4f} vs greedy)")
    print(f"  Oracle:    {o_acc:.4f}  ({o_acc - g_acc:+.4f} vs greedy)")
    print(f"\nDiagnostics:")
    print(f"  Degeneracy:     {degen_rate:.4f} ({f1} F1 instances)")
    print(f"  Spearman rho:   {sp_rho:.4f} (p={sp_p:.2e})")
    print(f"  Kendall tau:    {kt_tau:.4f} (p={kt_p:.2e})")
    print(f"\nFailure Modes (NER-aligned cascade):")
    print(f"  F1 degeneracy:          {f1:3d} ({f1/nv:.1%})")
    print(f"  F2 low agreement:       {f2:3d} ({f2/nv:.1%})")
    print(f"  F3 high agree + wrong:  {f3:3d} ({f3/nv:.1%})")
    print(f"  F4 selection gap:       {f4:3d} ({f4/nv:.1%})")
    print(f"\nExec errors in samples: {total_exec_err}")
    print(f"Time: {t_elapsed:.0f}s")
    print(f"Saved to {output_dir}")

    return summary


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Spider SQL Self-Consistency Pilot"
    )
    parser.add_argument("--n_samples", type=int, default=8)
    parser.add_argument("--n_examples", type=int, default=200)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output_dir", type=str, default="./results")
    parser.add_argument("--db_dir", type=str, default=DEFAULT_DB_DIR)
    parser.add_argument("--test_api", action="store_true",
                        help="Test API connectivity before running")
    args = parser.parse_args()
    run_pipeline(args)


if __name__ == "__main__":
    main()
