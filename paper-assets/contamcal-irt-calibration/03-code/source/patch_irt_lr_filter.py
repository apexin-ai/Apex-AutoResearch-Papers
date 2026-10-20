#!/usr/bin/env python3
"""D076: Add lr filter to IRT scripts. Reads lr from train_config.json."""
import sys

# ── Patch run_irt_calibration.py ──
fpath = "/root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
with open(fpath) as f:
    code = f.read()

# 1. Add get_train_lr before load_matrix
old = 'def load_matrix(path):'
new = '''def get_train_lr(dirname, checkpoint_dir):
    """Read lr from checkpoint's train_config.json (D076)."""
    ckpt_name = re.sub(r'(_para)?(_aligned)?$', '', dirname)
    config_path = os.path.join(checkpoint_dir, ckpt_name, "train_config.json")
    try:
        with open(config_path) as f:
            return json.load(f).get("lr")
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def load_matrix(path):'''
assert old in code, "FAIL: cannot find load_matrix"
code = code.replace(old, new, 1)

# 2. Modify load_eval_results signature
old = ('def load_eval_results(eval_dir, benchmarks=None, skip_para=True,\n'
       '                      model_scale=None, seed_filter=None, aligned_only=False):')
new = ('def load_eval_results(eval_dir, benchmarks=None, skip_para=True,\n'
       '                      model_scale=None, seed_filter=None, aligned_only=False,\n'
       '                      lr_filter=None, checkpoint_dir=None):')
assert old in code, "FAIL: cannot find load_eval_results signature"
code = code.replace(old, new, 1)

# 3. Add lr filter after seed_filter check
old = ('        if seed_filter is not None and info["seed"] != seed_filter:\n'
       '            log.info("Skipping dir (seed mismatch): %s", d.name)\n'
       '            continue\n'
       '        info["path"] = str(d)')
new = ('        if seed_filter is not None and info["seed"] != seed_filter:\n'
       '            log.info("Skipping dir (seed mismatch): %s", d.name)\n'
       '            continue\n'
       '        # D076: lr filter — exclude checkpoints trained with non-standard lr\n'
       '        if lr_filter is not None and checkpoint_dir:\n'
       '            lr = get_train_lr(d.name, checkpoint_dir)\n'
       '            if lr is None or abs(lr - lr_filter) > 1e-6:\n'
       '                log.info("Skipping dir (lr=%s, want %.1e): %s",\n'
       '                         f"{lr:.1e}" if lr is not None else "unknown",\n'
       '                         lr_filter, d.name)\n'
       '                continue\n'
       '        info["path"] = str(d)')
assert ('        if seed_filter is not None and info["seed"] != seed_filter:\n'
        '            log.info("Skipping dir (seed mismatch): %s", d.name)\n'
        '            continue\n'
        '        info["path"] = str(d)') in code, "FAIL: cannot find seed check block"
code = code.replace(
    '        if seed_filter is not None and info["seed"] != seed_filter:\n'
    '            log.info("Skipping dir (seed mismatch): %s", d.name)\n'
    '            continue\n'
    '        info["path"] = str(d)',
    new, 1)

# 4. Modify load_pooled_eval_results signature
old = 'def load_pooled_eval_results(eval_dir, scales, benchmarks=None, **kwargs):'
new = ('def load_pooled_eval_results(eval_dir, scales, benchmarks=None,\n'
       '                              lr_filter=None, lr_filter_scales=None,\n'
       '                              checkpoint_dir=None, **kwargs):')
assert old in code, "FAIL: cannot find load_pooled_eval_results signature"
code = code.replace(old, new, 1)

# 5. Modify data loading in pooled loop
old = '        data = load_eval_results(eval_dir, benchmarks, model_scale=scale, **kwargs)'
new = ('        kw = dict(kwargs)\n'
       '        if lr_filter is not None and checkpoint_dir:\n'
       '            if lr_filter_scales is None or scale in lr_filter_scales:\n'
       '                kw["lr_filter"] = lr_filter\n'
       '                kw["checkpoint_dir"] = checkpoint_dir\n'
       '        data = load_eval_results(eval_dir, benchmarks, model_scale=scale, **kw)')
assert old in code, "FAIL: cannot find pooled load line"
code = code.replace(old, new, 1)

# 6. Add CLI args after --aligned-only
old = ('    parser.add_argument("--aligned-only", action="store_true",\n'
       '                        help="Only load aligned-format eval directories.")\n'
       '    parser.add_argument("--output-dir", type=str, required=True)')
new = ('    parser.add_argument("--aligned-only", action="store_true",\n'
       '                        help="Only load aligned-format eval directories.")\n'
       '    parser.add_argument("--checkpoint-dir", type=str, default=None,\n'
       '                        help="Checkpoint dir for lr verification (D076)")\n'
       '    parser.add_argument("--lr-filter", type=float, default=None,\n'
       '                        help="Only accept checkpoints with this lr (D076)")\n'
       '    parser.add_argument("--output-dir", type=str, required=True)')
assert ('    parser.add_argument("--aligned-only", action="store_true",\n'
        '                        help="Only load aligned-format eval directories.")\n'
        '    parser.add_argument("--output-dir", type=str, required=True)') in code, \
    "FAIL: cannot find aligned-only arg"
code = code.replace(
    '    parser.add_argument("--aligned-only", action="store_true",\n'
    '                        help="Only load aligned-format eval directories.")\n'
    '    parser.add_argument("--output-dir", type=str, required=True)',
    new, 1)

# 7. Pass lr_filter/checkpoint_dir in main() Mode 2
old = ('    data = load_eval_results(args.eval_dir, args.benchmarks,\n'
       '                              model_scale=args.model_scale,\n'
       '                              seed_filter=args.data_seed,\n'
       '                              aligned_only=args.aligned_only)')
new = ('    data = load_eval_results(args.eval_dir, args.benchmarks,\n'
       '                              model_scale=args.model_scale,\n'
       '                              seed_filter=args.data_seed,\n'
       '                              aligned_only=args.aligned_only,\n'
       '                              lr_filter=args.lr_filter,\n'
       '                              checkpoint_dir=args.checkpoint_dir)')
assert old in code, "FAIL: cannot find main load_eval_results call"
code = code.replace(old, new, 1)

with open(fpath, 'w') as f:
    f.write(code)
print("OK: run_irt_calibration.py patched")


# ── Patch run_pooled_4bench_irt.py ──
fpath2 = "/root/contamcal-irt-calibration/exp006/run_pooled_4bench_irt.py"
with open(fpath2) as f:
    code2 = f.read()

# 1. Update docstring
old = ('Exclusion rules:\n'
       '  D044: GSM8K exclude d000 configs (format confound)\n'
       '  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept\n'
       '  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)\n'
       '  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)')
new = ('Exclusion rules:\n'
       '  D044: GSM8K exclude d000 configs (format confound)\n'
       '  D045: 0.5B MMLU/ARC excluded (position bias); 0.5B GSM8K/HumanEval kept\n'
       '  D046/D047: base_pretrained excluded (via aligned_only + dirname filter)\n'
       '  D018: 3B d000 s42 v3 excluded (already deprecated, double-check)\n'
       '  D076: 3B lr=2e-4 excluded (lr confound); only lr=5e-5 checkpoints accepted')
assert old in code2, "FAIL: cannot find docstring exclusion rules"
code2 = code2.replace(old, new, 1)

# 2. Add constants after MAX_ITEMS
old = 'MAX_ITEMS = 2000'
new = ('MAX_ITEMS = 2000\n'
       '\n'
       'CHECKPOINT_DIR = "/root/autodl-tmp/exp001/checkpoints"\n'
       '# D076: exclude lr=2e-4 confound — only 3B has mixed lr across dosage runs\n'
       'STANDARD_LR = 5e-5\n'
       'LR_FILTER_SCALES = {"3B"}')
assert old in code2, "FAIL: cannot find MAX_ITEMS"
code2 = code2.replace(old, new, 1)

# 3. Update load_pooled_eval_results call
old = ('    data = load_pooled_eval_results(\n'
       '        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n'
       '    )')
new = ('    data = load_pooled_eval_results(\n'
       '        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True,\n'
       '        lr_filter=STANDARD_LR, lr_filter_scales=LR_FILTER_SCALES,\n'
       '        checkpoint_dir=CHECKPOINT_DIR,\n'
       '    )')
assert ('    data = load_pooled_eval_results(\n'
        '        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n'
        '    )') in code2, "FAIL: cannot find load_pooled_eval_results call"
code2 = code2.replace(
    '    data = load_pooled_eval_results(\n'
    '        EVAL_DIR, SCALES, benchmarks=BENCHMARKS, aligned_only=True\n'
    '    )',
    new, 1)

# 4. Update exclusions list
old = ('            "exclusions": ["D044_gsm8k_d000", "D045_05B_mmlu_arc",\n'
       '                           "D046_D047_base_pretrained", "D018_deprecated"],')
new = ('            "exclusions": ["D044_gsm8k_d000", "D045_05B_mmlu_arc",\n'
       '                           "D046_D047_base_pretrained", "D018_deprecated",\n'
       '                           "D076_3B_lr_confound"],')
assert old in code2, "FAIL: cannot find exclusions list"
code2 = code2.replace(old, new, 1)

with open(fpath2, 'w') as f:
    f.write(code2)
print("OK: run_pooled_4bench_irt.py patched")
