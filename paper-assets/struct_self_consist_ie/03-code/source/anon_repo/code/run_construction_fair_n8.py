"""Run entity construction fair evaluation on N=8 data.
Skips adaptive_combination_cv (confirmed gold label leakage)."""
import sys
import numpy as np
sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
import entity_construction_fair as ecf

ecf.DATASETS = {
    "scierc": "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
    "conll": "/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl",
    "fewnerd": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl",
}
ecf.OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_n8"

def noop_adaptive(data, **kwargs):
    n = len(data)
    return {
        "mean_f1": -1.0, "std_f1": 0.0,
        "fold_f1s": [-1.0]*5,
        "fold_params": [{"gate_threshold": 0, "construction_theta": 0}]*5,
        "per_instance_f1s": np.full(n, -1.0),
    }
ecf.adaptive_combination_cv = noop_adaptive

if __name__ == "__main__":
    ecf.main()
