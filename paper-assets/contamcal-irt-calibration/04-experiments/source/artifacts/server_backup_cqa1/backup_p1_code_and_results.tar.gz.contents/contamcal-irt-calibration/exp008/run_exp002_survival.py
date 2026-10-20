"""
Run exp-008 signal survival analysis using exp-002 signal data.
Creates per-benchmark symlinked directories, converts labels, runs analysis.
"""
import json
import os
import sys
from pathlib import Path

BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge"]
REGIMES = [("d000", "Qwen2.5-0.5B_d000_s42"),
           ("d005", "Qwen2.5-0.5B_d005_s42"),
           ("d100", "Qwen2.5-0.5B_d100_s42")]

EXP002_SIGNALS = Path("/root/autodl-tmp/exp002/signals")
LABELS_SRC = Path("/root/autodl-tmp/exp001/sft_data")
WORK_DIR = Path("/root/autodl-tmp/exp008_from_exp002")
OUTPUT_DIR = Path("/root/contamcal-irt-calibration/exp008/exp008_exp002_output")

def convert_labels(bench):
    """Convert array-format labels to {index: 0/1} dict format."""
    src = LABELS_SRC / f"contamination_labels_{bench}_d005.json"
    dst = WORK_DIR / "labels" / f"labels_{bench}.json"
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(src) as f:
        raw = json.load(f)
    labels = {str(i): v for i, v in enumerate(raw["labels"])}
    with open(dst, "w") as f:
        json.dump(labels, f)
    print(f"Labels {bench}: {raw['contaminated_count']}/{raw['total_items']} contaminated -> {dst}")
    return dst

def setup_signal_dirs(bench):
    """Create per-regime directories with symlinks to the right benchmark signal files."""
    regime_args = []
    for regime_name, dir_name in REGIMES:
        src_dir = EXP002_SIGNALS / dir_name
        dst_dir = WORK_DIR / "signals" / regime_name / bench
        dst_dir.mkdir(parents=True, exist_ok=True)
        
        merged_src = src_dir / f"signals_merged_{bench}.json"
        merged_dst = dst_dir / f"signals_merged_{bench}.json"
        if merged_src.exists():
            if merged_dst.exists() or merged_dst.is_symlink():
                merged_dst.unlink()
            os.symlink(merged_src, merged_dst)
        
        for sig_prefix in ["signal_embedding_", "signal_minkpp_", "signal_selfcritique_"]:
            sig_src = src_dir / f"{sig_prefix}{bench}.json"
            sig_dst = dst_dir / f"{sig_prefix}{bench}.json"
            if sig_src.exists():
                if sig_dst.exists() or sig_dst.is_symlink():
                    sig_dst.unlink()
                os.symlink(sig_src, sig_dst)
        
        regime_args.append(f"{regime_name}={dst_dir}")
    return regime_args

def main():
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    script_dir = Path(__file__).parent
    survival_script = script_dir / "run_signal_survival.py"
    
    all_results = {}
    
    for bench in BENCHMARKS:
        print(f"\n{'='*60}")
        print(f"Benchmark: {bench}")
        print(f"{'='*60}")
        
        labels_file = convert_labels(bench)
        regime_args = setup_signal_dirs(bench)
        
        out_dir = OUTPUT_DIR / "per_benchmark" / bench
        out_dir.mkdir(parents=True, exist_ok=True)
        
        cmd = [
            sys.executable,
            str(survival_script),
            "--regime-dirs"] + regime_args + [
            "--labels-file", str(labels_file),
            "--output-dir", str(out_dir),
        ]
        
        print(f"CMD: {' '.join(cmd)}")
        ret = os.system(" ".join(cmd))
        
        report_file = out_dir / "survival_report.json"
        if report_file.exists():
            with open(report_file) as f:
                report = json.load(f)
            all_results[bench] = report
            print(f"[OK] {bench} -> {report_file}")
        else:
            print(f"[FAIL] {bench} - no report generated (exit code {ret})")
    
    # Cross-benchmark summary
    if all_results:
        summary_file = OUTPUT_DIR / "cross_benchmark_summary.json"
        with open(summary_file, "w") as f:
            json.dump(all_results, f, indent=2, default=str)
        print(f"\n{'='*60}")
        print(f"Cross-benchmark summary -> {summary_file}")
        
        # Print AUC heatmap
        print(f"\n{'='*60}")
        print("AUC HEATMAP (signal × regime, per benchmark)")
        print(f"{'='*60}")
        for bench, report in all_results.items():
            print(f"\n--- {bench} ---")
            auc_matrix = report.get("auc_matrix", {})
            if auc_matrix:
                regimes = report.get("regime_names", [])
                signals = list(auc_matrix.keys())
                header = f"{'Signal':<20}" + "".join(f"{r:>12}" for r in regimes)
                print(header)
                for sig in signals:
                    vals = auc_matrix[sig]
                    row = f"{sig:<20}"
                    for r in regimes:
                        v = vals.get(r)
                        row += f"{v:>12.4f}" if v is not None else f"{'N/A':>12}"
                    print(row)

if __name__ == "__main__":
    main()
