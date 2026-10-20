#!/usr/bin/env python3
"""Cross-Domain Formal Comparison + 5-Model Mitigation Analysis."""

import json, os, sys
import numpy as np
import pandas as pd
from scipy import stats
from collections import Counter, defaultdict
from itertools import combinations

BASE = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts"

# ============================================================
# PART A: Cross-Domain Formal Comparison
# ============================================================

def classify_domain(system_prompt, user_message):
    """Classify episode as airline or retail based on content."""
    text = (system_prompt + " " + user_message).lower()
    airline_kw = ['flight', 'airline', 'boarding', 'baggage', 'luggage', 'airport',
                  'seat', 'booking', 'reservation', 'passenger', 'travel', 'cabin',
                  'boarding pass', 'check-in', 'gate', 'itinerary', 'miles',
                  'mileage', 'lounge', 'upgrade', 'economy', 'business class',
                  'first class', 'layover', 'connecting', 'departure', 'arrival',
                  'res-', 'platinum member', 'loyalty']
    retail_kw = ['order', 'product', 'shipping', 'return', 'refund', 'cart',
                 'purchase', 'item', 'delivery', 'store', 'warehouse', 'coupon',
                 'discount', 'price', 'payment', 'credit card', 'invoice',
                 'merchandise', 'catalog', 'subscription', 'ord-', 'sku',
                 'tracking number', 'package', 'exchange']

    airline_score = sum(1 for kw in airline_kw if kw in text)
    retail_score = sum(1 for kw in retail_kw if kw in text)

    if airline_score > retail_score:
        return 'airline'
    elif retail_score > airline_score:
        return 'retail'
    else:
        return 'ambiguous_domain'

def load_all_episodes():
    """Load all 2,997 episodes with domain classification."""
    episodes = []
    ep_dir = os.path.join(BASE, "full_study/episodes")
    for model_dir in sorted(os.listdir(ep_dir)):
        fpath = os.path.join(ep_dir, model_dir, "episodes.jsonl")
        if not os.path.isfile(fpath):
            continue
        with open(fpath) as f:
            for line in f:
                d = json.loads(line)
                user_msg = d['trajectory'][0]['content'] if d['trajectory'] else ''
                domain = classify_domain(d['system_prompt'], user_msg)
                episodes.append({
                    'episode_id': d['episode_id'],
                    'clause_id': d['clause_id'],
                    'ambiguity_type': d['ambiguity_type'],
                    'condition': d['condition'],
                    'model': d['model'],
                    'domain': domain
                })
    return pd.DataFrame(episodes)

def load_judgments():
    """Load judgment data to get violation outcomes."""
    judgment_dir = os.path.join(BASE, "full_study/episodes")
    # Judgments may be in a separate directory
    # First check if episodes have judgment info embedded
    # Otherwise use the aggregated_rates.csv which has violation counts
    return None

def load_judgment_outcomes():
    """Load episode-level violation outcomes from judgment files."""
    judgment_base = os.path.join(BASE, "full_study/judgments")
    if not os.path.exists(judgment_base):
        return {}

    outcomes = {}
    for model_dir in sorted(os.listdir(judgment_base)):
        mpath = os.path.join(judgment_base, model_dir)
        if not os.path.isdir(mpath):
            continue
        for fname in os.listdir(mpath):
            if not fname.endswith('.jsonl'):
                continue
            with open(os.path.join(mpath, fname)) as f:
                for line in f:
                    d = json.loads(line)
                    eid = d.get('episode_id', '')
                    j = d.get('judgment', {})
                    if isinstance(j, dict):
                        vl = j.get('violation_level', 'none')
                        # Any non-none level counts as violation
                        outcomes[eid] = vl != 'none'
    return outcomes

def fisher_exact_2x2(a, b, c, d_val):
    """Fisher's exact test for 2x2 table [[a,b],[c,d]]."""
    table = np.array([[a, b], [c, d_val]])
    odds_ratio, p = stats.fisher_exact(table, alternative='two-sided')
    return odds_ratio, p

def run_cross_domain_analysis(df):
    """Run all cross-domain analyses."""
    results = {}

    # Filter to airline and retail only
    df_dom = df[df['domain'].isin(['airline', 'retail'])].copy()

    # 1. Domain split
    domain_counts = df_dom.groupby('domain').size().to_dict()
    domain_condition = df_dom.groupby(['domain', 'condition']).size().unstack(fill_value=0)

    results['domain_split'] = {
        'episode_counts': domain_counts,
        'excluded_ambiguous_domain': len(df[df['domain'] == 'ambiguous_domain']),
        'total_classified': len(df_dom)
    }

    episode_violations = load_judgment_outcomes()
    print(f"Loaded {len(episode_violations)} episode-level violation judgments")

    df_dom = df_dom.copy()
    df_dom['violation'] = df_dom['episode_id'].map(episode_violations)
    df_analysis = df_dom.dropna(subset=['violation'])
    df_analysis['violation'] = df_analysis['violation'].astype(int)
    print(f"Episodes with both domain and violation: {len(df_analysis)}")

    if len(df_analysis) > 0:
        # 2. Per-domain C1 (ambiguous vs unambiguous)
        c1_results = {}
        for domain in ['airline', 'retail']:
            dd = df_analysis[df_analysis['domain'] == domain]
            amb = dd[dd['condition'] == 'ambiguous']
            unamb = dd[dd['condition'] == 'unambiguous']

            a = amb['violation'].sum()
            b = len(amb) - a
            c = unamb['violation'].sum()
            d_val = len(unamb) - c

            amb_rate = a / len(amb) if len(amb) > 0 else 0
            unamb_rate = c / len(unamb) if len(unamb) > 0 else 0
            delta_pp = (amb_rate - unamb_rate) * 100

            or_val, p_val = fisher_exact_2x2(a, b, c, d_val)

            c1_results[domain] = {
                'n_ambiguous': int(len(amb)),
                'n_unambiguous': int(len(unamb)),
                'ambiguous_violation_rate': round(amb_rate, 4),
                'unambiguous_violation_rate': round(unamb_rate, 4),
                'delta_pp': round(delta_pp, 1),
                'odds_ratio': round(or_val, 3),
                'fisher_p': p_val,
                'significant': p_val < 0.05
            }

        results['per_domain_c1'] = c1_results

        # 3. C2 type ranking per domain
        type_rankings = {}
        for domain in ['airline', 'retail']:
            dd = df_analysis[(df_analysis['domain'] == domain) & (df_analysis['condition'] == 'ambiguous')]
            type_rates = dd.groupby('ambiguity_type')['violation'].mean().sort_values(ascending=False)
            type_rankings[domain] = {t: {'rate': round(r, 4), 'rank': i+1} for i, (t, r) in enumerate(type_rates.items())}

        # Spearman correlation between domain rankings
        all_types = sorted(set(type_rankings.get('airline', {}).keys()) & set(type_rankings.get('retail', {}).keys()))
        if len(all_types) >= 3:
            airline_ranks = [type_rankings['airline'][t]['rank'] for t in all_types]
            retail_ranks = [type_rankings['retail'][t]['rank'] for t in all_types]
            rho, rho_p = stats.spearmanr(airline_ranks, retail_ranks)
        else:
            rho, rho_p = float('nan'), float('nan')

        results['c2_type_ranking'] = {
            'airline': type_rankings.get('airline', {}),
            'retail': type_rankings.get('retail', {}),
            'spearman_rho': round(rho, 4) if not np.isnan(rho) else None,
            'spearman_p': round(rho_p, 4) if not np.isnan(rho_p) else None,
            'types_compared': all_types
        }

        # 4. Domain × Condition interaction (logistic regression)
        try:
            import statsmodels.api as sm
            from statsmodels.formula.api import logit

            df_reg = df_analysis.copy()
            df_reg['cond_binary'] = (df_reg['condition'] == 'ambiguous').astype(int)
            df_reg['domain_binary'] = (df_reg['domain'] == 'airline').astype(int)
            df_reg['interaction'] = df_reg['cond_binary'] * df_reg['domain_binary']

            X = df_reg[['cond_binary', 'domain_binary', 'interaction']]
            X = sm.add_constant(X)
            y = df_reg['violation']

            model = sm.Logit(y, X).fit(disp=0)

            results['logistic_interaction'] = {
                'coefficients': {
                    'intercept': round(model.params['const'], 4),
                    'condition_ambiguous': round(model.params['cond_binary'], 4),
                    'domain_airline': round(model.params['domain_binary'], 4),
                    'interaction': round(model.params['interaction'], 4)
                },
                'p_values': {
                    'intercept': round(model.pvalues['const'], 6),
                    'condition_ambiguous': model.pvalues['cond_binary'],
                    'domain_airline': round(model.pvalues['domain_binary'], 6),
                    'interaction': round(model.pvalues['interaction'], 6)
                },
                'interaction_significant': bool(model.pvalues['interaction'] < 0.05),
                'interpretation': 'Domain does NOT moderate the ambiguity effect' if model.pvalues['interaction'] >= 0.05 else 'Domain DOES moderate the ambiguity effect',
                'n': int(len(df_reg)),
                'aic': round(model.aic, 1),
                'pseudo_r2': round(model.prsquared, 4)
            }
        except Exception as e:
            results['logistic_interaction'] = {'error': str(e)}

        # 5. Per-type domain comparison
        per_type_domain = {}
        for atype in sorted(df_analysis['ambiguity_type'].unique()):
            dd = df_analysis[(df_analysis['ambiguity_type'] == atype) & (df_analysis['condition'] == 'ambiguous')]
            type_domain = {}
            for domain in ['airline', 'retail']:
                ddd = dd[dd['domain'] == domain]
                if len(ddd) > 0:
                    type_domain[domain] = {
                        'n': int(len(ddd)),
                        'violations': int(ddd['violation'].sum()),
                        'rate': round(ddd['violation'].mean(), 4)
                    }

            # Fisher's exact between domains
            if 'airline' in type_domain and 'retail' in type_domain:
                a = type_domain['airline']['violations']
                b = type_domain['airline']['n'] - a
                c = type_domain['retail']['violations']
                d_val = type_domain['retail']['n'] - c
                or_val, p_val = fisher_exact_2x2(a, b, c, d_val)
                type_domain['fisher_p'] = p_val
                type_domain['odds_ratio'] = round(or_val, 3)
                type_domain['significant'] = p_val < 0.05
                type_domain['delta_pp'] = round((type_domain['airline']['rate'] - type_domain['retail']['rate']) * 100, 1)

            per_type_domain[atype] = type_domain

        results['per_type_domain'] = per_type_domain

        # Additional: domain split statistics
        results['domain_split']['per_domain_condition_counts'] = {}
        for domain in ['airline', 'retail']:
            dd = df_analysis[df_analysis['domain'] == domain]
            results['domain_split']['per_domain_condition_counts'][domain] = {
                'ambiguous': int(len(dd[dd['condition'] == 'ambiguous'])),
                'unambiguous': int(len(dd[dd['condition'] == 'unambiguous'])),
                'total': int(len(dd))
            }

    return results


# ============================================================
# PART B: 5-Model Mitigation Complete Analysis
# ============================================================

def load_mitigation_data():
    """Load mitigation results for all 5 models."""
    fpath = os.path.join(BASE, "mitigation_study/analysis/mitigation_results.json")
    with open(fpath) as f:
        data = json.load(f)
    return data

def run_mitigation_analysis(mit_data):
    """Run all 5-model mitigation analyses."""
    results = {}
    models = list(mit_data['per_model'].keys())
    types_exclude_coref = ['authorization_scope', 'conditional_precedence', 'incompleteness', 'lexical', 'scopal']

    # 1. Model × Type interaction table
    delta_table = {}
    baseline_table = {}
    mitigated_table = {}

    for model in models:
        delta_table[model] = {}
        baseline_table[model] = {}
        mitigated_table[model] = {}
        for atype in types_exclude_coref:
            td = mit_data['per_model'][model]['per_type'].get(atype, {})
            bl = td.get('baseline_rate', None)
            mt = td.get('mitigated_rate', None)
            delta = td.get('delta_pp', None)
            baseline_table[model][atype] = bl
            mitigated_table[model][atype] = mt
            delta_table[model][atype] = delta

    # Find best/worst improvements
    best_improvements = []
    worst_degradations = []
    for model in models:
        for atype in types_exclude_coref:
            d = delta_table[model][atype]
            if d is not None:
                best_improvements.append((model, atype, d))
                worst_degradations.append((model, atype, d))

    best_improvements.sort(key=lambda x: x[2])  # Most negative = most improvement
    worst_degradations.sort(key=lambda x: x[2], reverse=True)  # Most positive = worst degradation

    results['model_type_interaction'] = {
        'delta_table': delta_table,
        'baseline_table': baseline_table,
        'mitigated_table': mitigated_table,
        'top5_improvements': [{'model': m, 'type': t, 'delta_pp': d} for m, t, d in best_improvements[:5]],
        'degradations': [{'model': m, 'type': t, 'delta_pp': d} for m, t, d in worst_degradations if d > 0]
    }

    # 2. Baseline vulnerability vs mitigation responsiveness
    baselines = []
    deltas = []
    labels = []
    for model in models:
        for atype in types_exclude_coref:
            bl = baseline_table[model][atype]
            d = delta_table[model][atype]
            if bl is not None and d is not None:
                baselines.append(bl)
                deltas.append(d)
                labels.append(f"{model}_{atype}")

    baselines = np.array(baselines)
    deltas = np.array(deltas)

    pearson_r, pearson_p = stats.pearsonr(baselines, deltas)
    spearman_r, spearman_p = stats.spearmanr(baselines, deltas)

    results['vulnerability_responsiveness'] = {
        'n_cells': len(baselines),
        'pearson_r': round(pearson_r, 4),
        'pearson_p': round(pearson_p, 6),
        'spearman_rho': round(spearman_r, 4),
        'spearman_p': round(spearman_p, 6),
        'hypothesis': 'Higher baseline vulnerability → larger mitigation effect (negative correlation expected)',
        'conclusion': 'Supported' if pearson_r < 0 and pearson_p < 0.05 else 'Not supported' if pearson_r >= 0 else f'Trend exists (r={pearson_r:.3f}) but not significant (p={pearson_p:.3f})'
    }

    # 3. Auth scope analysis
    auth_scope_data = {}
    for model in models:
        td = mit_data['per_model'][model]['per_type'].get('authorization_scope', {})
        auth_scope_data[model] = {
            'baseline_rate': td.get('baseline_rate'),
            'mitigated_rate': td.get('mitigated_rate'),
            'delta_pp': td.get('delta_pp'),
            'baseline_n': td.get('baseline_n'),
            'mitigated_n': td.get('mitigated_n')
        }

    all_improve_auth = all(auth_scope_data[m]['delta_pp'] is not None and auth_scope_data[m]['delta_pp'] <= 0 for m in models)

    # Check which types have all models improving
    type_all_improve = {}
    for atype in types_exclude_coref:
        improve_count = sum(1 for m in models if delta_table[m][atype] is not None and delta_table[m][atype] < 0)
        worsen_count = sum(1 for m in models if delta_table[m][atype] is not None and delta_table[m][atype] > 0)
        unchanged_count = sum(1 for m in models if delta_table[m][atype] is not None and delta_table[m][atype] == 0)
        type_all_improve[atype] = {
            'improve': improve_count,
            'worsen': worsen_count,
            'unchanged': unchanged_count,
            'all_improve': improve_count == len(models)
        }

    # Fisher's exact for auth_scope per model
    auth_fisher = {}
    for model in models:
        td = mit_data['per_model'][model]['per_type'].get('authorization_scope', {})
        bl_n = td.get('baseline_n', 50)
        mt_n = td.get('mitigated_n', 50)
        bl_v = int(round(td.get('baseline_rate', 0) * bl_n))
        mt_v = int(round(td.get('mitigated_rate', 0) * mt_n))
        if mt_n > 0:
            or_val, p_val = fisher_exact_2x2(bl_v, bl_n - bl_v, mt_v, mt_n - mt_v)
            auth_fisher[model] = {
                'baseline_violations': bl_v,
                'baseline_n': bl_n,
                'mitigated_violations': mt_v,
                'mitigated_n': mt_n,
                'odds_ratio': round(or_val, 3),
                'fisher_p': round(p_val, 6),
                'significant': p_val < 0.05
            }

    results['auth_scope_analysis'] = {
        'per_model': auth_scope_data,
        'all_models_improve': all_improve_auth,
        'is_only_universally_improving_type': all_improve_auth and sum(1 for t in type_all_improve if type_all_improve[t]['all_improve']) == 1,
        'fisher_tests': auth_fisher,
        'safety_training_comparison': {
            'claude_low_baseline': auth_scope_data.get('claude-sonnet-4-6', {}).get('baseline_rate'),
            'claude_delta': auth_scope_data.get('claude-sonnet-4-6', {}).get('delta_pp'),
            'gpt54_high_baseline': auth_scope_data.get('gpt-5.4', {}).get('baseline_rate'),
            'gpt54_delta': auth_scope_data.get('gpt-5.4', {}).get('delta_pp'),
            'interpretation': 'Claude has low baseline (safety training floor) so mitigation adds little; GPT-5.4 has high baseline so mitigation has more room'
        }
    }

    # 4. Incompleteness analysis
    incomp_data = {}
    for model in models:
        td = mit_data['per_model'][model]['per_type'].get('incompleteness', {})
        incomp_data[model] = {
            'baseline_rate': td.get('baseline_rate'),
            'mitigated_rate': td.get('mitigated_rate'),
            'delta_pp': td.get('delta_pp')
        }

    improve_models = [m for m in models if incomp_data[m]['delta_pp'] is not None and incomp_data[m]['delta_pp'] < 0]
    worsen_models = [m for m in models if incomp_data[m]['delta_pp'] is not None and incomp_data[m]['delta_pp'] > 0]
    unchanged_models = [m for m in models if incomp_data[m]['delta_pp'] is not None and incomp_data[m]['delta_pp'] == 0]

    results['incompleteness_analysis'] = {
        'per_model': incomp_data,
        'models_improving': improve_models,
        'models_worsening': worsen_models,
        'models_unchanged': unchanged_models,
        'n_improve': len(improve_models),
        'n_worsen': len(worsen_models),
        'gap_filling_interpretation': 'Incompleteness mitigation may trigger gap-filling behavior: model tries to address gaps but fills them incorrectly, leading to more violations in some cases'
    }

    # 5. Mitigation responsiveness score per type
    type_responsiveness = {}
    for atype in types_exclude_coref:
        deltas_type = []
        for model in models:
            d = delta_table[model][atype]
            if d is not None:
                deltas_type.append(d)

        deltas_arr = np.array(deltas_type)
        mean_delta = np.mean(deltas_arr)
        se = np.std(deltas_arr, ddof=1) / np.sqrt(len(deltas_arr)) if len(deltas_arr) > 1 else 0
        ci_95 = (mean_delta - 1.96 * se, mean_delta + 1.96 * se)

        n_improve = sum(1 for d in deltas_type if d < 0)
        n_total = len(deltas_type)

        # Binomial test: H0: p(improve) = 0.5
        if n_total > 0:
            binom_p = stats.binomtest(n_improve, n_total, 0.5, alternative='greater').pvalue
        else:
            binom_p = 1.0

        type_responsiveness[atype] = {
            'mean_delta_pp': round(mean_delta, 2),
            'se': round(se, 2),
            'ci_95_lower': round(ci_95[0], 2),
            'ci_95_upper': round(ci_95[1], 2),
            'n_models_improve': n_improve,
            'n_models_total': n_total,
            'binom_p': round(binom_p, 6),
            'significant_improvement': binom_p < 0.05,
            'per_model_deltas': {m: delta_table[m][atype] for m in models}
        }

    # Sort by mean_delta (most negative = most responsive)
    sorted_types = sorted(type_responsiveness.keys(), key=lambda t: type_responsiveness[t]['mean_delta_pp'])
    results['type_responsiveness'] = {
        'ranking': sorted_types,
        'per_type': type_responsiveness
    }

    # Additional: overall model responsiveness
    model_overall = {}
    for model in models:
        deltas_model = [delta_table[model][t] for t in types_exclude_coref if delta_table[model][t] is not None]
        model_overall[model] = {
            'mean_delta_pp': round(np.mean(deltas_model), 2),
            'overall_baseline': mit_data['per_model'][model]['overall']['baseline_rate'],
            'overall_mitigated': mit_data['per_model'][model]['overall']['mitigated_rate'],
            'overall_delta_pp': mit_data['per_model'][model]['overall']['delta_pp']
        }

    results['model_overall'] = model_overall

    return results


# ============================================================
# Main
# ============================================================

if __name__ == '__main__':
    print("=" * 60)
    print("PART A: Cross-Domain Formal Comparison")
    print("=" * 60)

    df = load_all_episodes()
    print(f"Loaded {len(df)} episodes")
    print(f"Domain distribution: {df['domain'].value_counts().to_dict()}")

    cross_domain_results = run_cross_domain_analysis(df)

    # Save Part A
    with open(os.path.join(BASE, "analysis_cross_domain.json"), 'w') as f:
        json.dump(cross_domain_results, f, indent=2, default=str)
    print(f"\nSaved: analysis_cross_domain.json")

    print("\n" + "=" * 60)
    print("PART B: 5-Model Mitigation Analysis")
    print("=" * 60)

    mit_data = load_mitigation_data()
    mitigation_results = run_mitigation_analysis(mit_data)

    # Save Part B
    with open(os.path.join(BASE, "analysis_mitigation_5model.json"), 'w') as f:
        json.dump(mitigation_results, f, indent=2, default=str)
    print(f"Saved: analysis_mitigation_5model.json")

    # Print key results
    print("\n" + "=" * 60)
    print("KEY RESULTS SUMMARY")
    print("=" * 60)

    print("\n--- Part A: Cross-Domain ---")
    if 'per_domain_c1' in cross_domain_results:
        for domain, data in cross_domain_results['per_domain_c1'].items():
            print(f"  {domain}: Δpp={data['delta_pp']}, OR={data['odds_ratio']}, p={data['fisher_p']:.2e}, sig={data['significant']}")

    if 'c2_type_ranking' in cross_domain_results:
        print(f"  Spearman ρ (type rankings): {cross_domain_results['c2_type_ranking']['spearman_rho']}, p={cross_domain_results['c2_type_ranking']['spearman_p']}")

    if 'logistic_interaction' in cross_domain_results:
        li = cross_domain_results['logistic_interaction']
        if 'error' not in li:
            print(f"  Interaction p={li['p_values']['interaction']}, {li['interpretation']}")

    print("\n--- Part B: 5-Model Mitigation ---")
    print(f"  Vulnerability-responsiveness correlation: r={mitigation_results['vulnerability_responsiveness']['pearson_r']}, p={mitigation_results['vulnerability_responsiveness']['pearson_p']}")
    print(f"  Auth scope all improve: {mitigation_results['auth_scope_analysis']['all_models_improve']}")
    print(f"  Incompleteness: {mitigation_results['incompleteness_analysis']['n_improve']} improve, {mitigation_results['incompleteness_analysis']['n_worsen']} worsen")
    print(f"  Type responsiveness ranking: {mitigation_results['type_responsiveness']['ranking']}")
