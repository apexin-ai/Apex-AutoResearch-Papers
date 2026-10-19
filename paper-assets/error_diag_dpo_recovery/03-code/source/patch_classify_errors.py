#!/usr/bin/env python3
"""Patch classify_errors.py: add llm_original_type field + dual-version KW (with/without PCB override)."""
import sys

PATH = '/root/autodl-tmp/rl-active-probe-fl/src/classify_errors.py'

with open(PATH) as f:
    code = f.read()

n_orig = code.count('\n')

# ===== PATCH 1: Update docstring =====
code = code.replace(
    '  task_id, task_type, game_file, error_type, divergence_step,\n'
    '  correction_span, expert_total_steps, model_total_steps, reasoning',
    '  task_id, task_type, game_file, error_type, llm_original_type,\n'
    '  llm_original_type_source, divergence_step, correction_span,\n'
    '  expert_total_steps, model_total_steps, reasoning',
    1  # only first occurrence
)
print("PATCH 1 (docstring): OK")

# ===== PATCH 2: Replace run_dual_analysis =====
START = '\ndef run_dual_analysis('
END = '\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n'

si = code.index(START)
ei = code.index(END, si)

NEW_FUNC = r'''
def run_dual_analysis(records: list[dict], output_dir: str, is_dry_run: bool = False):
    """Dual-version KW: with vs without PCB override, for methodological fairness.

    Reviewer requirement: P1 (correction_span ordering) must hold in both the
    override version (PCB -> verification) and the no-override version (using
    llm_original_type) to rule out the possibility that the conclusion depends
    on the PCB reclassification bias.
    """
    from scipy.stats import kruskal as kruskal_test

    DEDUP_SEED = 42
    ERROR_TYPES = ["action", "verification", "planning"]

    def _stats(recs, type_key="error_type"):
        groups = {}
        for et in ERROR_TYPES:
            spans = [r["correction_span"] for r in recs if r.get(type_key) == et]
            if spans:
                groups[et] = {
                    "n": len(spans),
                    "mean": round(mean(spans), 2),
                    "median": round(median(spans), 2),
                    "std": round(stdev(spans), 2) if len(spans) > 1 else 0.0,
                    "_spans": spans,
                }
        valid = [g for g in groups.values() if g["n"] >= 3]
        kw_h, kw_p = None, None
        if len(valid) >= 2:
            h, p = kruskal_test(*[g["_spans"] for g in valid])
            kw_h, kw_p = round(float(h), 4), round(float(p), 6)
        elif len(valid) < 2:
            logger.warning("Kruskal-Wallis skipped: need >=2 groups with n>=3, got %d", len(valid))
        return groups, kw_h, kw_p

    def _check_ordinal(groups):
        medians = {et: groups[et]["median"] for et in ERROR_TYPES if et in groups}
        if len(medians) < 3:
            return None
        return medians["action"] < medians["verification"] < medians["planning"]

    def _dedup(recs, seed):
        rng = random.Random(seed)
        by_task: dict[str, list] = {}
        for r in recs:
            by_task.setdefault(normalize_game_file(r["game_file"]), []).append(r)
        return [rng.choice(v) for v in by_task.values()]

    def _to_json(groups):
        return {et: {k: v for k, v in g.items() if k != "_spans"}
                for et, g in groups.items()}

    # --- Prepare three record sets ---
    # with_override: PCB error_type = verification (current logic)
    # without_override: use llm_original_type (excluding unknown/DRY_RUN)
    # pcb_excluded: drop PCB records entirely
    valid_types = set(ERROR_TYPES)
    no_override_recs = []
    for r in records:
        lot = r.get("llm_original_type")
        if lot in valid_types:
            no_override_recs.append({**r, "error_type": lot})
    pcb_excluded_recs = [r for r in records if not r.get("is_pcb")]
    n_pcb = sum(1 for r in records if r.get("is_pcb"))

    # --- Compute stats for each version ---
    all_results = {}
    for label, recs in [
        ("with_override", records),
        ("without_override", no_override_recs),
        ("pcb_excluded", pcb_excluded_recs),
    ]:
        groups, h, p = _stats(recs)
        deduped = _dedup(recs, DEDUP_SEED)
        groups_d, h_d, p_d = _stats(deduped)
        all_results[label] = {
            "full": {"n": len(recs), "groups": groups, "h": h, "p": p,
                     "ordinal": _check_ordinal(groups)},
            "dedup": {"n": len(deduped), "groups": groups_d, "h": h_d, "p": p_d,
                      "ordinal": _check_ordinal(groups_d)},
        }

    # --- Task-type stratified (with_override only) ---
    by_task_type: dict[str, list] = {}
    for r in records:
        tt = r.get("task_type") or "unknown"
        by_task_type.setdefault(tt, []).append(r)

    version_c_groups = {}
    for tt, tt_recs in sorted(by_task_type.items()):
        et_groups = {}
        for et in ERROR_TYPES:
            spans = [r["correction_span"] for r in tt_recs if r["error_type"] == et]
            if spans:
                et_groups[et] = spans
        valid_et = [g for g in et_groups.values() if len(g) >= 3]
        if len(valid_et) < 2:
            version_c_groups[tt] = {
                "n": len(tt_recs), "error_types": len(et_groups),
                "kruskal_h": None, "kruskal_p": None, "verdict": "insufficient"
            }
        else:
            h, p = kruskal_test(*valid_et)
            verdict = "significant" if p < 0.05 else "not_significant"
            version_c_groups[tt] = {
                "n": len(tt_recs), "error_types": len(et_groups),
                "kruskal_h": round(float(h), 4), "kruskal_p": round(float(p), 6),
                "verdict": verdict
            }

    # --- P1 gate ---
    wo = all_results["with_override"]["full"]
    wno = all_results["without_override"]["full"]
    pe = all_results["pcb_excluded"]["full"]

    override_sig = wo["p"] is not None and wo["p"] < 0.05 and wo["ordinal"] is True
    no_override_sig = wno["p"] is not None and wno["p"] < 0.05 and wno["ordinal"] is True
    pcb_excl_sig = pe["p"] is not None and pe["p"] < 0.05 and pe["ordinal"] is True
    p1_pass = override_sig and (no_override_sig or pcb_excl_sig)

    # --- Print ---
    if is_dry_run:
        print("\n⚠️  WARNING: rule-based classification — stats are tautological, for pipeline testing only")

    print(f"\n=== P1 Correction Span Analysis (PCB trajectories: {n_pcb}) ===")

    for label in ["with_override", "without_override", "pcb_excluded"]:
        res = all_results[label]
        for sub_label, sub in [("Full", res["full"]), ("Deduplicated", res["dedup"])]:
            print(f"\n{label} / {sub_label} (N={sub['n']}):")
            for et in ERROR_TYPES:
                if et in sub["groups"]:
                    g = sub["groups"][et]
                    print(f"  {et+':':<17s} N={g['n']}, mean={g['mean']:.2f}, "
                          f"median={g['median']:.1f}, std={g['std']:.2f}")
                else:
                    print(f"  {et+':':<17s} N=0")
            if sub["h"] is not None:
                print(f"  Kruskal-Wallis: H={sub['h']:.4f}, p={sub['p']:.6f}")
                ord_str = "✓" if sub["ordinal"] else "✗"
                print(f"  Ordinal (action < verification < planning): {ord_str}")
            else:
                print(f"  Kruskal-Wallis: SKIPPED (need >=2 groups with n>=3)")

    print(f"\nTask-type stratified (with_override):")
    vc_sig = sum(1 for g in version_c_groups.values() if g["verdict"] == "significant")
    vc_insuf = sum(1 for g in version_c_groups.values() if g["verdict"] == "insufficient")
    vc_total = len(version_c_groups)
    for tt in sorted(version_c_groups):
        g = version_c_groups[tt]
        h_str = f"H={g['kruskal_h']:.4f}" if g["kruskal_h"] is not None else "H=N/A"
        p_str = f"p={g['kruskal_p']:.6f}" if g["kruskal_p"] is not None else "p=N/A"
        print(f"  {tt+':':<30s} N={g['n']}, {h_str}, {p_str} [{g['verdict'].upper()}]")
    print(f"  Summary: {vc_sig}/{vc_total} groups significant, {vc_insuf} insufficient")

    print(f"\n{'='*50}")
    print(f"P1 GATE: {'PASS ✓' if p1_pass else 'FAIL ✗'}")
    wo_p = '%.6f' % wo['p'] if wo['p'] is not None else 'N/A'
    wno_p = '%.6f' % wno['p'] if wno['p'] is not None else 'N/A'
    pe_p = '%.6f' % pe['p'] if pe['p'] is not None else 'N/A'
    print(f"  with_override:    p={wo_p}, ordinal={wo['ordinal']}")
    print(f"  without_override: p={wno_p}, ordinal={wno['ordinal']}")
    print(f"  pcb_excluded:     p={pe_p}, ordinal={pe['ordinal']}")
    print(f"{'='*50}")

    # --- Save JSON ---
    analysis = {
        "tautological_warning": is_dry_run,
        "n_pcb": n_pcb,
        "p1_gate": {
            "pass": p1_pass,
            "with_override_significant": override_sig,
            "without_override_significant": no_override_sig,
            "pcb_excluded_significant": pcb_excl_sig,
        },
    }
    for label in ["with_override", "without_override", "pcb_excluded"]:
        res = all_results[label]
        for sub_label in ["full", "dedup"]:
            sub = res[sub_label]
            key = f"{label}_{sub_label}"
            analysis[key] = {
                "n": sub["n"],
                "kruskal_h": sub["h"],
                "kruskal_p": sub["p"],
                "ordinal_holds": sub["ordinal"],
                "groups": _to_json(sub["groups"]),
            }
    analysis["task_type_stratified"] = {
        "groups": version_c_groups,
        "summary": {"significant": vc_sig, "insufficient": vc_insuf, "total": vc_total},
    }
    analysis["dedup_seed"] = DEDUP_SEED

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "p1_analysis.json"
    with open(json_path, "w") as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)
    logger.info("Dual analysis saved → %s", json_path)

'''

code = code[:si] + NEW_FUNC + code[ei:]
print("PATCH 2 (run_dual_analysis): OK")

# ===== PATCH 3: Dry-run output - add llm_original_type =====
OLD_DRYRUN = '''                rec = {
                    "task_id": m["traj"].get("task_id"),
                    "task_type": m["traj"].get("task_type"),
                    "game_file": m["traj"]["game_file"],
                    "error_type": "DRY_RUN",
                    "divergence_step": d["divergence_step"],
                    "correction_span": d["correction_span"],
                    "expert_total_steps": d["expert_total_steps"],
                    "model_total_steps": d["model_total_steps"],
                    "expert_action_at_div": d["expert_action_at_div"],
                    "model_action_at_div": d["model_action_at_div"],
                    "reasoning": "dry_run",
                }
                if "csf_details" in m["traj"]:
                    rec["error_type"] = "verification"
                    rec["sub_type"] = "premature_completion_belief"
                    rec["csf_details"] = m["traj"]["csf_details"]
                    rec["reasoning"] = "D023: CSF pattern with incomplete task — agent failed to verify critical sub-steps"'''

NEW_DRYRUN = '''                is_pcb = "csf_details" in m["traj"]
                rb_type = _rule_based_error_type(d["correction_span"])
                rec = {
                    "task_id": m["traj"].get("task_id"),
                    "task_type": m["traj"].get("task_type"),
                    "game_file": m["traj"]["game_file"],
                    "error_type": "DRY_RUN",
                    "llm_original_type": rb_type if is_pcb else "DRY_RUN",
                    "llm_original_type_source": "rule-based" if is_pcb else "dry_run",
                    "divergence_step": d["divergence_step"],
                    "correction_span": d["correction_span"],
                    "expert_total_steps": d["expert_total_steps"],
                    "model_total_steps": d["model_total_steps"],
                    "expert_action_at_div": d["expert_action_at_div"],
                    "model_action_at_div": d["model_action_at_div"],
                    "reasoning": "dry_run",
                }
                if is_pcb:
                    rec["error_type"] = "verification"
                    rec["sub_type"] = "premature_completion_belief"
                    rec["csf_details"] = m["traj"]["csf_details"]
                    rec["reasoning"] = "D023: CSF pattern with incomplete task — agent failed to verify critical sub-steps"'''

assert OLD_DRYRUN in code, "PATCH 3: old dry-run block not found"
code = code.replace(OLD_DRYRUN, NEW_DRYRUN, 1)
print("PATCH 3 (dry-run output): OK")

# ===== PATCH 4: Dry-run analysis_recs =====
OLD_DRYRUN_ANALYSIS = '''        analysis_recs = []
        for m in matched:
            d = m["divergence"]
            if "csf_details" in m["traj"]:
                et = "verification"
            else:
                et = _rule_based_error_type(d["correction_span"])
            analysis_recs.append({
                "game_file": m["traj"]["game_file"],
                "task_type": m["traj"].get("task_type", "unknown"),
                "error_type": et,
                "correction_span": d["correction_span"],
            })
        run_dual_analysis(analysis_recs, str(Path(args.output_file).parent), is_dry_run=True)'''

NEW_DRYRUN_ANALYSIS = '''        analysis_recs = []
        for m in matched:
            d = m["divergence"]
            is_pcb = "csf_details" in m["traj"]
            rb_type = _rule_based_error_type(d["correction_span"])
            et = "verification" if is_pcb else rb_type
            analysis_recs.append({
                "game_file": m["traj"]["game_file"],
                "task_type": m["traj"].get("task_type", "unknown"),
                "error_type": et,
                "llm_original_type": rb_type if is_pcb else et,
                "is_pcb": is_pcb,
                "correction_span": d["correction_span"],
            })
        run_dual_analysis(analysis_recs, str(Path(args.output_file).parent), is_dry_run=True)'''

assert OLD_DRYRUN_ANALYSIS in code, "PATCH 4: old dry-run analysis block not found"
code = code.replace(OLD_DRYRUN_ANALYSIS, NEW_DRYRUN_ANALYSIS, 1)
print("PATCH 4 (dry-run analysis_recs): OK")

# ===== PATCH 5: Full-run output - add llm_original_type =====
OLD_FULLRUN = '''            rec = {
                "task_id": m["traj"].get("task_id"),
                "task_type": m["traj"].get("task_type"),
                "game_file": m["traj"]["game_file"],
                "error_type": res["error_type"] if res else "unknown",
                "divergence_step": d["divergence_step"],
                "correction_span": d["correction_span"],
                "expert_total_steps": d["expert_total_steps"],
                "model_total_steps": d["model_total_steps"],
                "reasoning": res.get("reasoning", "") if res else "LLM parse failed",
            }
            if "csf_details" in m["traj"]:
                rec["error_type"] = "verification"
                rec["sub_type"] = "premature_completion_belief"
                rec["csf_details"] = m["traj"]["csf_details"]'''

NEW_FULLRUN = '''            llm_type = res["error_type"] if res else "unknown"
            rec = {
                "task_id": m["traj"].get("task_id"),
                "task_type": m["traj"].get("task_type"),
                "game_file": m["traj"]["game_file"],
                "error_type": llm_type,
                "llm_original_type": llm_type,
                "llm_original_type_source": "llm",
                "divergence_step": d["divergence_step"],
                "correction_span": d["correction_span"],
                "expert_total_steps": d["expert_total_steps"],
                "model_total_steps": d["model_total_steps"],
                "reasoning": res.get("reasoning", "") if res else "LLM parse failed",
            }
            if "csf_details" in m["traj"]:
                rec["error_type"] = "verification"
                rec["sub_type"] = "premature_completion_belief"
                rec["csf_details"] = m["traj"]["csf_details"]'''

assert OLD_FULLRUN in code, "PATCH 5: old full-run block not found"
code = code.replace(OLD_FULLRUN, NEW_FULLRUN, 1)
print("PATCH 5 (full-run output): OK")

# ===== PATCH 6: Full-run analysis_recs =====
OLD_FULLRUN_ANALYSIS = '''    analysis_recs = []
    for m, res in zip(matched, results):
        d = m["divergence"]
        if "csf_details" in m["traj"]:
            et = "verification"
        else:
            et = res["error_type"] if res else "unknown"
        analysis_recs.append({
            "game_file": m["traj"]["game_file"],
            "task_type": m["traj"].get("task_type", "unknown"),
            "error_type": et,
            "correction_span": d["correction_span"],
        })
    run_dual_analysis(analysis_recs, str(Path(args.output_file).parent), is_dry_run=False)'''

NEW_FULLRUN_ANALYSIS = '''    analysis_recs = []
    for m, res in zip(matched, results):
        d = m["divergence"]
        is_pcb = "csf_details" in m["traj"]
        llm_type = res["error_type"] if res else "unknown"
        et = "verification" if is_pcb else llm_type
        analysis_recs.append({
            "game_file": m["traj"]["game_file"],
            "task_type": m["traj"].get("task_type", "unknown"),
            "error_type": et,
            "llm_original_type": llm_type,
            "is_pcb": is_pcb,
            "correction_span": d["correction_span"],
        })
    run_dual_analysis(analysis_recs, str(Path(args.output_file).parent), is_dry_run=False)'''

assert OLD_FULLRUN_ANALYSIS in code, "PATCH 6: old full-run analysis block not found"
code = code.replace(OLD_FULLRUN_ANALYSIS, NEW_FULLRUN_ANALYSIS, 1)
print("PATCH 6 (full-run analysis_recs): OK")

# ===== Write =====
with open(PATH, 'w') as f:
    f.write(code)

n_new = code.count('\n')
print(f"\nAll patches applied. Lines: {n_orig} -> {n_new}")
print(f"File written to {PATH}")
