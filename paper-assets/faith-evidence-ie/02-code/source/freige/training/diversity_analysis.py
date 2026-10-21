# Bug fix: 原版用 json.loads(output) 重新解析原始模型输出，truncated/repaired 的输出
# 会解析失败被跳过，导致 diversity 计算不准。改为直接使用 parsed_triples 字段，
# 它已由 parse_model_output 的 repair 逻辑正确处理。
import json
import sys
import statistics
from collections import defaultdict, Counter


def normalize_triple(t):
    return (
        str(t.get("head") or "").strip().lower(),
        str(t.get("relation") or "").strip().lower(),
        str(t.get("tail") or "").strip().lower(),
    )


def normalize_triple_ev(t):
    h, r, tl = normalize_triple(t)
    return (h, r, tl, tuple(sorted(t.get("evidence", []))))


def main():
    gen_dir = sys.argv[1] if len(sys.argv) > 1 else './outputs

    doc_gens = defaultdict(list)
    with open(gen_dir) as f:
        for line in f:
            rec = json.loads(line.strip())
            doc_id = rec['doc_id']
            parsed_triples = rec.get('parsed_triples') or []
            fmt_ok = rec.get('format_ok', True)
            doc_gens[doc_id].append({
                'triples': parsed_triples,
                'format_ok': fmt_ok,
                'gen_idx': rec.get('generation_idx', -1),
            })

    n_docs = len(doc_gens)
    print(f"Total docs: {n_docs}")
    print(f"Total lines: {sum(len(v) for v in doc_gens.values())}")

    unique_triple_only = []
    unique_with_ev = []
    format_ok_rates = []

    per_doc_details = []

    for doc_id, gens in doc_gens.items():
        n = len(gens)
        fmt_ok = sum(1 for g in gens if g['format_ok'])
        format_ok_rates.append(fmt_ok / n)

        triple_sets = []
        full_sets = []
        for g in gens:
            ts = frozenset(normalize_triple(t) for t in g['triples'])
            fs = frozenset(normalize_triple_ev(t) for t in g['triples'])
            triple_sets.append(ts)
            full_sets.append(fs)

        u_t = len(set(triple_sets))
        unique_triple_only.append(u_t)
        u_f = len(set(full_sets))
        unique_with_ev.append(u_f)

        per_doc_details.append((doc_id, len(gens), u_t, u_f))

    first_doc_gens = len(next(iter(doc_gens.values()))) if doc_gens else 8

    print(f"\n== DIVERSITY ANALYSIS ==")
    print(f"Docs analyzed: {len(unique_triple_only)}")

    if unique_triple_only:
        m = statistics.mean(unique_triple_only)
        med = statistics.median(unique_triple_only)
        print(f"\n--- Triple-set diversity (不含 evidence) ---")
        print(f"Mean unique: {m:.2f}/{first_doc_gens}")
        print(f"Median: {med:.1f}, Min: {min(unique_triple_only)}, Max: {max(unique_triple_only)}")
        dist = Counter(unique_triple_only)
        print("Distribution:")
        for k in sorted(dist.keys()):
            pct = dist[k]*100/len(unique_triple_only)
            bar = '#' * int(pct / 2)
            print(f"  {k} unique: {dist[k]:4d} ({pct:5.1f}%) {bar}")

    if unique_with_ev:
        m = statistics.mean(unique_with_ev)
        med = statistics.median(unique_with_ev)
        print(f"\n--- Full diversity (含 evidence) ---")
        print(f"Mean unique: {m:.2f}/{first_doc_gens}")
        print(f"Median: {med:.1f}, Min: {min(unique_with_ev)}, Max: {max(unique_with_ev)}")
        dist = Counter(unique_with_ev)
        print("Distribution:")
        for k in sorted(dist.keys()):
            pct = dist[k]*100/len(unique_with_ev)
            bar = '#' * int(pct / 2)
            print(f"  {k} unique: {dist[k]:4d} ({pct:5.1f}%) {bar}")

    if format_ok_rates:
        print(f"\nFormat OK rate: {statistics.mean(format_ok_rates):.4f}")

    per_doc_details.sort(key=lambda x: x[2])
    print(f"\n--- Bottom 10 docs (lowest triple-only diversity) ---")
    for doc_id, n, ut, uf in per_doc_details[:10]:
        print(f"  {doc_id[:50]:50s}  gens={n}  unique_triple={ut}  unique_full={uf}")

    if unique_triple_only:
        m = statistics.mean(unique_triple_only)
        if m >= 3:
            print(f"\nCONCLUSION: DIVERSITY OK (mean={m:.2f} >= 3/{first_doc_gens})")
        else:
            print(f"\nCONCLUSION: DIVERSITY LOW (mean={m:.2f} < 3/{first_doc_gens}) — consider higher temperature")

if __name__ == '__main__':
    main()
