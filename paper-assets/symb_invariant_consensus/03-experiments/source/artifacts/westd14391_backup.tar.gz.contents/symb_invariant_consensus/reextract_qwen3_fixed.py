#!/usr/bin/env python3
"""Re-extract constraints using Qwen3 with thinking mode properly disabled.

Fixes bug: extra_body wrapper prevented chat_template_kwargs from reaching vLLM.
Re-runs: extraction_qwen3_same and extraction_qwen3_cross_mistral.
"""
import json, os, re, sys, glob, time, logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import httpx

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    handlers=[logging.StreamHandler(sys.stdout)])
log = logging.getLogger(__name__)

QWEN3_PORT = 8001
T_EXT = 0.3
BASE = '/root/symb_invariant_consensus/results/exp_d126_crossmodel_sica'
QWEN3_INTER_DIR = '/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/intermediates'

VALID_ANSWERS = {'True', 'False', 'Unknown'}

def normalize_answer(ans):
    s = str(ans).strip()
    low = s.lower()
    mapping = {'true': 'True', 'false': 'False', 'unknown': 'Unknown',
               'yes': 'True', 'no': 'False', 'uncertain': 'Unknown',
               'undetermined': 'Unknown', 't': 'True', 'f': 'False', 'u': 'Unknown'}
    return mapping.get(low, s.capitalize())

def strip_thinking(text):
    idx = text.find('</think>')
    if idx >= 0:
        return text[idx + len('</think>'):].strip()
    idx = text.find('<think>')
    if idx >= 0:
        return ''
    return text

def get_model_id(port):
    r = httpx.get(f'http://localhost:{port}/v1/models', timeout=10)
    return r.json()['data'][0]['id']

def extract_one(trace_text, model_id):
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text)
    payload = {
        'model': model_id,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 2048,
        'temperature': T_EXT,
        'chat_template_kwargs': {'enable_thinking': False}
    }
    try:
        resp = httpx.post(f'http://localhost:{QWEN3_PORT}/v1/chat/completions',
                          json=payload, timeout=120)
        resp.raise_for_status()
        raw = resp.json()['choices'][0]['message']['content'] or ''
        text = strip_thinking(raw.strip())
        json_match = re.search(r'\{[\s\S]*\}', text)
        if not json_match:
            return {'error': 'no JSON', 'constraints': []}
        data = json.loads(json_match.group())
        return {'constraints': data.get('constraints', []),
                'extracted_answer': data.get('answer', '')}
    except json.JSONDecodeError:
        return {'error': 'JSON parse', 'constraints': []}
    except Exception as e:
        return {'error': str(e)[:200], 'constraints': []}

def reextract_direction(trace_files, out_dir, direction_name, model_id, max_workers=4):
    os.makedirs(out_dir, exist_ok=True)
    total_success = 0
    total_traces = 0
    total_constraints = 0

    for fi, tf in enumerate(trace_files):
        pid = os.path.splitext(os.path.basename(tf))[0]
        out_file = os.path.join(out_dir, f'{pid}.json')

        with open(tf) as f:
            raw_data = json.load(f)

        if isinstance(raw_data, dict):
            traces = raw_data.get('traces', raw_data.get('per_trace', []))
            gt = raw_data.get('gt', '')
        else:
            traces = raw_data
            gt = ''

        if not traces:
            continue

        per_trace = []
        def _do(t):
            trace_text = t.get('trace', t.get('content', ''))
            if not trace_text:
                return None
            result = extract_one(trace_text, model_id)
            return {
                'trace_idx': t.get('trace_idx', 0),
                'answer': normalize_answer(t.get('answer', '')) if t.get('answer') else '',
                'constraints': result.get('constraints', []),
                'extracted_answer': result.get('extracted_answer', ''),
                'error': result.get('error'),
            }

        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futs = {ex.submit(_do, t): i for i, t in enumerate(traces)}
            for fut in as_completed(futs):
                r = fut.result()
                if r is not None:
                    per_trace.append(r)

        per_trace.sort(key=lambda x: x['trace_idx'])

        for t in per_trace:
            total_traces += 1
            nc = len(t.get('constraints', []))
            total_constraints += nc
            if nc > 0:
                total_success += 1

        output = {'pid': pid, 'gt': gt, 'per_trace': per_trace}
        with open(out_file, 'w') as f:
            json.dump(output, f, indent=2)

        if (fi + 1) % 10 == 0 or fi == len(trace_files) - 1:
            log.info(f"  [{direction_name}] {fi+1}/{len(trace_files)} files, "
                     f"success={total_success}/{total_traces} "
                     f"({100*total_success/max(total_traces,1):.1f}%), "
                     f"avg_constr={total_constraints/max(total_traces,1):.1f}")

    log.info(f"[{direction_name}] DONE: {total_success}/{total_traces} "
             f"({100*total_success/max(total_traces,1):.1f}%), total_constr={total_constraints}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--direction', choices=['same', 'cross', 'both'], default='both')
    parser.add_argument('--max-workers', type=int, default=4)
    args = parser.parse_args()

    model_id = get_model_id(QWEN3_PORT)
    log.info(f"Qwen3 model: {model_id}")

    # Get the 152 PIDs used in the experiment
    mistral_pids = set(
        os.path.splitext(os.path.basename(f))[0]
        for f in glob.glob(os.path.join(BASE, 'mistral_traces', '*.json'))
    )
    log.info(f"Experiment PIDs: {len(mistral_pids)}")

    if args.direction in ('cross', 'both'):
        old_dir = os.path.join(BASE, 'extraction_qwen3_cross_mistral')
        bak_dir = os.path.join(BASE, 'extraction_qwen3_cross_mistral_buggy')
        if os.path.exists(old_dir) and not os.path.exists(bak_dir):
            os.rename(old_dir, bak_dir)
            log.info(f"Backed up -> {bak_dir}")

        trace_files = sorted(glob.glob(os.path.join(BASE, 'mistral_traces', '*.json')))
        reextract_direction(trace_files,
                            os.path.join(BASE, 'extraction_qwen3_cross_mistral'),
                            'qwen3_cross_mistral', model_id, args.max_workers)

    if args.direction in ('same', 'both'):
        old_dir = os.path.join(BASE, 'extraction_qwen3_same')
        bak_dir = os.path.join(BASE, 'extraction_qwen3_same_buggy')
        if os.path.exists(old_dir) and not os.path.exists(bak_dir):
            os.rename(old_dir, bak_dir)
            log.info(f"Backed up -> {bak_dir}")

        # Only process PIDs in the experiment set
        all_qwen3 = glob.glob(os.path.join(QWEN3_INTER_DIR, '*.json'))
        trace_files = sorted([f for f in all_qwen3
                              if os.path.splitext(os.path.basename(f))[0] in mistral_pids])
        log.info(f"Filtered Qwen3 traces: {len(trace_files)}/{len(all_qwen3)}")
        reextract_direction(trace_files,
                            os.path.join(BASE, 'extraction_qwen3_same'),
                            'qwen3_same', model_id, args.max_workers)

    log.info("Re-extraction complete.")
