"""
Direction Q: Premise Mutation Robustness Test
Tests SC and SICA answer stability under semantics-preserving premise perturbations.
Input:  FOLIO dataset (folio_full.json)
Output: Per-mutation flip rates and accuracy changes for SC vs SICA

Mutation strategies:
  1. synonym    - Replace content words with WordNet synonyms
  2. reorder    - Shuffle premise order
  3. inject     - Add one irrelevant premise from another problem
  4. combined   - Apply all three simultaneously
"""
import argparse
import asyncio
import json
import logging
import os
import random
import re
import sys
import time
from collections import Counter

import httpx

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT
from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
from sica.scorer import InvariantScorer

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

SOLVE_PROMPT = (
    "Solve the following math problem step by step. Show all your reasoning.\n"
    "At the end, put your final answer in \\boxed{{}}.\n\n"
    "Problem: {problem}"
)

PROTECTED_WORDS = {
    'all', 'every', 'each', 'some', 'no', 'none', 'any', 'not', 'if', 'then',
    'either', 'or', 'and', 'neither', 'nor', 'both', 'only', 'but', 'when',
    'whenever', 'unless', 'because', 'since', 'therefore', 'thus', 'hence',
    'true', 'false', 'unknown', 'uncertain',
    'given', 'determine', 'whether', 'following', 'premises', 'conclusion',
    'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
    'shall', 'should', 'may', 'might', 'must', 'can', 'could',
    'that', 'this', 'these', 'those', 'who', 'whom', 'which', 'what',
    'where', 'when', 'how', 'than', 'to', 'of', 'in', 'for', 'on',
    'with', 'at', 'by', 'from', 'about', 'into', 'through',
    'it', 'its', 'he', 'she', 'they', 'them', 'his', 'her', 'their',
    'not', 'does', 'did', 'don', 'doesn', 'didn', 'won', 'wouldn',
}

BUILTIN_SYNONYMS = {
    'all': ['every', 'each'],
    'every': ['all', 'each'],
    'people': ['individuals', 'persons'],
    'person': ['individual'],
    'happy': ['joyful', 'pleased'],
    'smart': ['intelligent', 'clever'],
    'intelligent': ['smart', 'clever'],
    'clever': ['smart', 'bright'],
    'rich': ['wealthy', 'affluent'],
    'wealthy': ['rich', 'affluent'],
    'poor': ['impoverished', 'destitute'],
    'fast': ['quick', 'rapid', 'swift'],
    'quick': ['fast', 'rapid'],
    'slow': ['sluggish', 'unhurried'],
    'big': ['large', 'huge'],
    'large': ['big', 'huge'],
    'small': ['tiny', 'little'],
    'good': ['fine', 'decent'],
    'nice': ['pleasant', 'agreeable'],
    'kind': ['generous', 'benevolent'],
    'generous': ['kind', 'liberal'],
    'strong': ['powerful', 'mighty'],
    'powerful': ['strong', 'mighty'],
    'weak': ['feeble', 'frail'],
    'beautiful': ['attractive', 'gorgeous'],
    'ugly': ['unattractive', 'hideous'],
    'old': ['elderly', 'aged'],
    'young': ['youthful', 'juvenile'],
    'new': ['novel', 'fresh'],
    'easy': ['simple', 'effortless'],
    'hard': ['difficult', 'tough'],
    'difficult': ['hard', 'challenging'],
    'important': ['significant', 'crucial'],
    'famous': ['renowned', 'celebrated'],
    'quiet': ['silent', 'hushed'],
    'loud': ['noisy', 'boisterous'],
    'brave': ['courageous', 'valiant'],
    'afraid': ['scared', 'frightened'],
    'angry': ['furious', 'irate'],
    'like': ['enjoy', 'prefer'],
    'enjoy': ['like', 'relish'],
    'hate': ['despise', 'detest'],
    'love': ['adore', 'cherish'],
    'help': ['assist', 'aid'],
    'assist': ['help', 'aid'],
    'begin': ['start', 'commence'],
    'start': ['begin', 'initiate'],
    'finish': ['complete', 'conclude'],
    'complete': ['finish', 'conclude'],
    'make': ['create', 'produce'],
    'create': ['make', 'produce'],
    'show': ['display', 'exhibit'],
    'tell': ['inform', 'notify'],
    'give': ['provide', 'supply'],
    'take': ['grab', 'seize'],
    'want': ['desire', 'wish'],
    'need': ['require', 'demand'],
    'think': ['believe', 'consider'],
    'believe': ['think', 'assume'],
    'know': ['understand', 'comprehend'],
    'understand': ['comprehend', 'grasp'],
    'work': ['labor', 'toil'],
    'play': ['engage', 'participate'],
    'study': ['examine', 'investigate'],
    'teach': ['instruct', 'educate'],
    'learn': ['acquire', 'absorb'],
    'write': ['compose', 'author'],
    'read': ['peruse', 'examine'],
    'speak': ['talk', 'converse'],
    'talk': ['speak', 'converse'],
    'walk': ['stroll', 'amble'],
    'run': ['sprint', 'dash'],
    'live': ['reside', 'dwell'],
    'student': ['pupil', 'learner'],
    'teacher': ['instructor', 'educator'],
    'friend': ['companion', 'ally'],
    'enemy': ['foe', 'adversary'],
    'house': ['home', 'dwelling'],
    'city': ['town', 'municipality'],
    'country': ['nation', 'state'],
    'school': ['academy', 'institution'],
    'place': ['location', 'site'],
    'part': ['portion', 'segment'],
    'group': ['team', 'collective'],
    'world': ['globe', 'earth'],
    'program': ['scheme', 'initiative'],
    'system': ['framework', 'structure'],
    'problem': ['issue', 'challenge'],
    'result': ['outcome', 'consequence'],
    'reason': ['cause', 'motive'],
    'often': ['frequently', 'regularly'],
    'always': ['constantly', 'perpetually'],
    'never': ['rarely'],
    'sometimes': ['occasionally', 'periodically'],
    'usually': ['typically', 'generally'],
    'also': ['additionally', 'moreover'],
    'very': ['extremely', 'highly'],
    'really': ['truly', 'genuinely'],
    'quite': ['rather', 'fairly'],
}

try:
    from nltk.corpus import wordnet as _wn
    _wn.synsets('test')
    _HAS_WORDNET = True
except Exception:
    _HAS_WORDNET = False


# ---------------------------------------------------------------------------
# Parsing & reconstruction
# ---------------------------------------------------------------------------

def parse_folio_problem(problem_text):
    """Extract list of premise strings and conclusion from FOLIO problem text."""
    parts = re.split(r'\n\n\s*Determine whether', problem_text)
    if len(parts) < 2:
        return None, None

    premise_section = parts[0]
    conclusion_section = 'Determine whether' + parts[1]

    premise_text = re.sub(
        r'^Given the following premises:\s*\n?', '', premise_section
    ).strip()

    # Split on ". " followed by uppercase (robust to double-space)
    raw = re.split(r'(?<=\.)\s+(?=[A-Z])', premise_text)
    premises = [s.strip() for s in raw if s.strip()]

    m = re.search(
        r'(?:true|false|uncertain|unknown)[.:]\s*\n?(.*)',
        conclusion_section, re.IGNORECASE | re.DOTALL,
    )
    conclusion = m.group(1).strip() if m else conclusion_section.strip()

    return premises, conclusion


def reconstruct_problem(premises, conclusion):
    """Rebuild FOLIO problem text from premises + conclusion."""
    premises_text = " ".join(p.strip() for p in premises)
    return (
        f"Given the following premises:\n{premises_text}\n\n"
        f"Determine whether the following conclusion is true, false, "
        f"or uncertain:\n{conclusion}"
    )


# ---------------------------------------------------------------------------
# Mutation strategies
# ---------------------------------------------------------------------------

def _get_synonym(word):
    """Return a single-token synonym or None. Tries WordNet first, falls back to built-in dict."""
    low = word.lower()
    if low in PROTECTED_WORDS or len(low) <= 3:
        return None
    if _HAS_WORDNET:
        for pos in [_wn.NOUN, _wn.ADJ, _wn.VERB, _wn.ADV]:
            for syn in _wn.synsets(low, pos=pos)[:2]:
                for lemma in syn.lemmas():
                    name = lemma.name().replace('_', ' ')
                    if name.lower() != low and ' ' not in name and len(name) > 2:
                        return name
    if low in BUILTIN_SYNONYMS:
        return BUILTIN_SYNONYMS[low][0]
    return None


def mutate_synonym(premises, rng, replace_prob=0.3):
    """Replace ~30 % of eligible content words with synonyms."""
    mutated, total_replaced = [], 0
    for premise in premises:
        words = premise.split()
        new_words = []
        for w in words:
            clean = re.sub(r'[^\w]', '', w).lower()

            if clean in BUILTIN_SYNONYMS and rng.random() < 0.5:
                cands = [c for c in BUILTIN_SYNONYMS[clean] if ' ' not in c]
                if cands:
                    rep = rng.choice(cands)
                    if w[0].isupper():
                        rep = rep.capitalize()
                    trail = re.search(r'(\W+)$', w)
                    if trail:
                        rep += trail.group(1)
                    new_words.append(rep)
                    total_replaced += 1
                    continue

            if (clean not in PROTECTED_WORDS
                    and len(clean) > 3
                    and rng.random() < replace_prob):
                syn = _get_synonym(clean)
                if syn:
                    if w[0].isupper():
                        syn = syn.capitalize()
                    trail = re.search(r'(\W+)$', w)
                    if trail:
                        syn += trail.group(1)
                    new_words.append(syn)
                    total_replaced += 1
                    continue

            new_words.append(w)
        mutated.append(' '.join(new_words))
    return mutated, total_replaced


def mutate_reorder(premises, rng):
    """Shuffle premise order (logically irrelevant)."""
    shuffled = list(premises)
    rng.shuffle(shuffled)
    return shuffled


def mutate_inject(premises, pool, rng):
    """Insert one premise drawn from a different problem."""
    if not pool:
        return list(premises)
    irr = rng.choice(pool)
    result = list(premises)
    pos = rng.randint(0, len(result))
    result.insert(pos, irr)
    return result


def mutate_combined(premises, pool, rng):
    """Synonym + reorder + inject."""
    result, _ = mutate_synonym(premises, rng)
    result = mutate_reorder(result, rng)
    result = mutate_inject(result, pool, rng)
    return result


# ---------------------------------------------------------------------------
# Answer helpers
# ---------------------------------------------------------------------------

def _extract_boxed(text):
    matches = re.findall(r'\\boxed\{([^}]*(?:\{[^}]*\}[^}]*)*)\}', text)
    return matches[-1].strip() if matches else ""


def normalize_answer(ans):
    ans = str(ans).strip().lower()
    if ans in ('true', 'yes', 't'):
        return 'True'
    if ans in ('false', 'no', 'f'):
        return 'False'
    if ans in ('unknown', 'uncertain', 'u', 'undetermined'):
        return 'Unknown'
    return ans.capitalize()


def extract_logic_answer(text):
    """Extract True/False/Unknown from a reasoning trace."""
    boxed = _extract_boxed(text)
    if boxed:
        return normalize_answer(boxed)
    for line in reversed(text.strip().split('\n')[-5:]):
        ll = line.lower()
        if 'the answer is' in ll or 'conclusion is' in ll:
            for label in ['true', 'false', 'unknown', 'uncertain']:
                if label in ll:
                    return normalize_answer(label)
    for line in reversed(text.strip().split('\n')[-5:]):
        for label in ['true', 'false', 'unknown']:
            if re.search(r'\b' + label + r'\b', line, re.IGNORECASE):
                return normalize_answer(label)
    return ''


# ---------------------------------------------------------------------------
# Async vLLM helpers
# ---------------------------------------------------------------------------

async def generate_traces(client, model_id, problem_text, k, temperature):
    """Generate K reasoning traces concurrently via vLLM."""
    prompt = SOLVE_PROMPT.format(problem=problem_text)

    async def _one(idx):
        payload = {
            'model': model_id,
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 4096,
            'temperature': temperature,
            'top_p': 0.95,
        }
        for attempt in range(3):
            try:
                resp = await client.post(
                    '/v1/chat/completions', json=payload, timeout=120,
                )
                resp.raise_for_status()
                text = resp.json()['choices'][0]['message']['content']
                return {'trace': text, 'answer': extract_logic_answer(text),
                        'trace_idx': idx}
            except Exception as e:
                if attempt < 2:
                    await asyncio.sleep(2)
                else:
                    logger.warning("trace gen failed idx=%d: %s", idx, str(e)[:120])
                    return {'trace': '', 'answer': '', 'trace_idx': idx}

    return list(await asyncio.gather(*[_one(i) for i in range(k)]))


async def extract_constraints_batch(client, model_id, traces):
    """Extract FOL constraints from all traces concurrently."""

    async def _one(trace_text):
        if not trace_text.strip():
            return []
        prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text)
        payload = {
            'model': model_id,
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 2048,
            'temperature': 0.1,
        }
        for attempt in range(2):
            try:
                resp = await client.post(
                    '/v1/chat/completions', json=payload, timeout=120,
                )
                resp.raise_for_status()
                raw = resp.json()['choices'][0]['message']['content']
                text = re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL).strip()
                m = re.search(r'\{[\s\S]*\}', text)
                if not m:
                    return []
                data = json.loads(m.group())
                return data.get('constraints', [])
            except Exception:
                if attempt < 1:
                    await asyncio.sleep(1)
        return []

    return list(await asyncio.gather(*[_one(t['trace']) for t in traces]))


# ---------------------------------------------------------------------------
# SC / SICA
# ---------------------------------------------------------------------------

def run_sc(traces):
    answers = [t['answer'] for t in traces if t['answer']]
    if not answers:
        return {'answer': '', 'vote_count': 0, 'distribution': {}}
    counts = Counter(answers)
    best = max(sorted(counts.keys()), key=lambda k: counts[k])
    return {'answer': best, 'vote_count': counts[best],
            'distribution': dict(counts)}


def run_sica_from_constraints(all_constraints, traces):
    dedup = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    unique = dedup.deduplicate(list(all_constraints))
    maxsat = solver.solve(unique, timeout_ms=10000)

    candidates = sorted(set(t['answer'] for t in traces if t['answer']))
    if not candidates:
        candidates = ['True', 'False', 'Unknown']
    counts = Counter(t['answer'] for t in traces if t['answer'])
    scores = scorer.score(maxsat, traces, candidates)
    selected = scorer.select_answer(scores, counts)

    return {
        'answer': selected,
        'scores': scores,
        'constraints_stats': {
            'total_extracted': sum(len(c) for c in all_constraints),
            'unique_after_dedup': len(unique),
        },
    }


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

def compute_summary(results):
    mutations = ['original', 'synonym', 'reorder', 'inject', 'combined']
    n = len(results)
    if n == 0:
        return {}

    per_mutation = {}
    for mut in mutations:
        sc_ok = sum(
            1 for r in results
            if r['mutations'].get(mut, {}).get('sc_correct', False)
        )
        sica_ok = sum(
            1 for r in results
            if r['mutations'].get(mut, {}).get('sica_correct', False)
        )
        stats = {
            'sc_accuracy': round(sc_ok / n, 4),
            'sica_accuracy': round(sica_ok / n, 4),
            'sc_correct': sc_ok,
            'sica_correct': sica_ok,
        }
        if mut != 'original':
            sc_flips = sum(
                1 for r in results
                if (r['mutations'].get(mut, {}).get('sc_answer')
                    != r['mutations'].get('original', {}).get('sc_answer'))
            )
            sica_flips = sum(
                1 for r in results
                if (r['mutations'].get(mut, {}).get('sica_answer')
                    != r['mutations'].get('original', {}).get('sica_answer'))
            )
            stats.update({
                'sc_flip_rate': round(sc_flips / n, 4),
                'sica_flip_rate': round(sica_flips / n, 4),
                'sc_flips': sc_flips,
                'sica_flips': sica_flips,
            })
        per_mutation[mut] = stats

    return {'n_problems': n, 'per_mutation': per_mutation}


# ---------------------------------------------------------------------------
# Main experiment loop (async)
# ---------------------------------------------------------------------------

async def run_experiment(parsed_problems, args, rng, all_premises_pool):
    base_url = f'http://localhost:{args.vllm_port}'
    async with httpx.AsyncClient(base_url=base_url, timeout=180) as client:
        resp = await client.get('/v1/models')
        model_id = resp.json()['data'][0]['id']
        logger.info("Model: %s", model_id)

        mutation_names = ['original', 'synonym', 'reorder', 'inject', 'combined']
        results = []
        total_start = time.time()

        for pidx, prob in enumerate(parsed_problems):
            t0 = time.time()
            premises = prob['_premises']
            conclusion = prob['_conclusion']
            gold = normalize_answer(prob['answer'])
            other_pool = [p for p in all_premises_pool if p not in set(premises)]

            prob_result = {
                'problem_id': prob['id'],
                'gold': gold,
                'n_premises': len(premises),
                'mutations': {},
            }

            for mut_name in mutation_names:
                if mut_name == 'original':
                    mut_premises = list(premises)
                    mut_info = {}
                elif mut_name == 'synonym':
                    mut_premises, n_rep = mutate_synonym(premises, rng)
                    mut_info = {'n_replaced': n_rep}
                elif mut_name == 'reorder':
                    mut_premises = mutate_reorder(premises, rng)
                    mut_info = {}
                elif mut_name == 'inject':
                    mut_premises = mutate_inject(premises, other_pool, rng)
                    mut_info = {'n_premises_after': len(mut_premises)}
                elif mut_name == 'combined':
                    mut_premises = mutate_combined(premises, other_pool, rng)
                    mut_info = {'n_premises_after': len(mut_premises)}
                else:
                    continue

                problem_text = reconstruct_problem(mut_premises, conclusion)

                traces = await generate_traces(
                    client, model_id, problem_text, args.k, args.temperature,
                )
                sc = run_sc(traces)

                all_constraints = await extract_constraints_batch(
                    client, model_id, traces,
                )
                sica = run_sica_from_constraints(all_constraints, traces)

                prob_result['mutations'][mut_name] = {
                    'sc_answer': sc['answer'],
                    'sc_correct': sc['answer'] == gold,
                    'sc_distribution': sc['distribution'],
                    'sica_answer': sica['answer'],
                    'sica_correct': sica['answer'] == gold,
                    'sica_scores': sica['scores'],
                    'constraints_stats': sica['constraints_stats'],
                    'mutation_info': mut_info,
                }

            results.append(prob_result)

            elapsed = time.time() - t0
            orig = prob_result['mutations']['original']
            logger.info(
                "[%d/%d] %s gold=%s orig_sc=%s orig_sica=%s (%.1fs)",
                pidx + 1, len(parsed_problems), prob['id'], gold,
                orig['sc_answer'], orig['sica_answer'], elapsed,
            )
            for mn in ['synonym', 'reorder', 'inject', 'combined']:
                m = prob_result['mutations'][mn]
                sc_f = '!' if m['sc_answer'] != orig['sc_answer'] else '='
                sica_f = '!' if m['sica_answer'] != orig['sica_answer'] else '='
                logger.info(
                    "  %s: sc=%s%s sica=%s%s",
                    mn, m['sc_answer'], sc_f, m['sica_answer'], sica_f,
                )

            summary = compute_summary(results)
            os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
            with open(args.output, 'w') as f:
                json.dump(
                    {'summary': summary, 'results': results},
                    f, indent=2, ensure_ascii=False, default=str,
                )

            avg_t = (time.time() - total_start) / (pidx + 1)
            remaining = len(parsed_problems) - pidx - 1
            if remaining > 0:
                logger.info(
                    "ETA: %.1f min (%d remaining)",
                    avg_t * remaining / 60, remaining,
                )

        summary = compute_summary(results)
        with open(args.output, 'w') as f:
            json.dump(
                {'summary': summary, 'results': results},
                f, indent=2, ensure_ascii=False, default=str,
            )

        logger.info("=== FINAL SUMMARY ===")
        for mn in mutation_names:
            s = summary['per_mutation'][mn]
            flip = ""
            if mn != 'original':
                flip = (f" sc_flip={s['sc_flip_rate']*100:.1f}%"
                        f" sica_flip={s['sica_flip_rate']*100:.1f}%")
            logger.info(
                "  %s: sc_acc=%.1f%% sica_acc=%.1f%%%s",
                mn, s['sc_accuracy'] * 100, s['sica_accuracy'] * 100, flip,
            )
        logger.info("Total: %.1f min", (time.time() - total_start) / 60)
        logger.info("DIRECTION_Q_DONE")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Direction Q: Premise Mutation Robustness",
    )
    parser.add_argument('--data', required=True)
    parser.add_argument('--n-questions', type=int, default=None)
    parser.add_argument('--k', type=int, default=12)
    parser.add_argument('--vllm-port', type=int, default=8020)
    parser.add_argument('--output', required=True)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--temperature', type=float, default=0.7)
    args = parser.parse_args()

    rng = random.Random(args.seed)

    with open(args.data) as f:
        data = json.load(f)
    if args.n_questions:
        data = data[:args.n_questions]

    all_premises_pool = []
    parsed = []
    for p in data:
        premises, conclusion = parse_folio_problem(p['problem'])
        if premises is None:
            logger.warning("Skip unparseable: %s", p['id'])
            continue
        parsed.append({**p, '_premises': premises, '_conclusion': conclusion})
        all_premises_pool.extend(premises)

    logger.info("Parsed %d problems, %d premises in pool", len(parsed),
                len(all_premises_pool))

    asyncio.run(run_experiment(parsed, args, rng, all_premises_pool))


if __name__ == '__main__':
    main()
