#!/usr/bin/env python3
"""SDGD Stage 1: CPU-only decomposition. No vLLM, no CUDA."""
import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', required=True,
                        choices=['sdgd_zero', 'single_pass', 'per_type', 'random_batch'])
    parser.add_argument('--types_file', required=True)
    parser.add_argument('--sim_matrix_path', default=None)
    parser.add_argument('--k', type=float, default=1.0)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--min_batch_size', type=int, default=0,
                        help='Minimum batch size. Batches smaller than this are '
                             'merged into the least-confusable larger batch. '
                             'Set to 0 to disable (default). Recommended: 8.')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    with open(args.types_file) as f:
        type_defs = json.load(f)
    all_types = sorted(type_defs.keys())

    if args.mode == 'single_pass':
        batches = [all_types]
        meta = {'tau': None, 'k': None, 'graph_stats': None}

    elif args.mode == 'per_type':
        batches = [[t] for t in all_types]
        meta = {'tau': None, 'k': None, 'graph_stats': None}

    else:
        if not args.sim_matrix_path:
            parser.error(f'{args.mode} requires --sim_matrix_path')

        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from sdgd.similarity import load_sim_matrix, adaptive_threshold
        from sdgd.graph import (build_threshold_graph, color_graph,
                                group_by_color, get_graph_stats,
                                enforce_min_batch_size)

        sim_matrix, type_names = load_sim_matrix(args.sim_matrix_path)
        tau = adaptive_threshold(sim_matrix, k=args.k)
        G = build_threshold_graph(sim_matrix, tau, type_names)
        coloring = color_graph(G)
        sdgd_batches = group_by_color(coloring)
        stats_before = get_graph_stats(G, sdgd_batches)

        if args.mode == 'sdgd_zero':
            if args.min_batch_size > 0:
                sdgd_batches = enforce_min_batch_size(
                    sdgd_batches, args.min_batch_size,
                    sim_matrix=sim_matrix, type_names=type_names)
            batches = [sdgd_batches[cid] for cid in sorted(sdgd_batches.keys())]
            stats = get_graph_stats(G, sdgd_batches)
            meta = {
                'tau': float(tau), 'k': args.k,
                'graph_stats': stats,
                'min_batch_size': args.min_batch_size,
                'graph_stats_before_merge': stats_before if args.min_batch_size > 0 else None,
            }
        else:  # random_batch
            import random
            n_batches = len(sdgd_batches)
            rng = random.Random(args.seed)
            shuffled = sorted(all_types)
            rng.shuffle(shuffled)
            batch_dict = {}
            for i, t in enumerate(shuffled):
                batch_dict.setdefault(i % n_batches, []).append(t)
            batches = [batch_dict[bid] for bid in sorted(batch_dict.keys())]
            meta = {'tau': float(tau), 'k': args.k, 'graph_stats': stats_before,
                    'seed': args.seed, 'ref_n_batches': n_batches}

    result = {
        'mode': args.mode,
        'n_batches': len(batches),
        'batch_sizes': [len(b) for b in batches],
        'batches': batches,
        **meta,
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"[decompose] mode={args.mode} batches={len(batches)} sizes={[len(b) for b in batches]}")
    if meta.get('tau') is not None:
        print(f"  tau={meta['tau']:.4f} k={meta['k']}")
    if args.min_batch_size > 0:
        print(f"  min_batch_size={args.min_batch_size}")


if __name__ == '__main__':
    main()
