import pandas as pd
import os

BASE = "/root/entrainment_gated_ft/analysis"
OUT = os.path.join(BASE, "paper_data")

# ============================================================
# A. Table 1: Task-Specificity Results
# ============================================================
rob = pd.read_csv(os.path.join(BASE, "robustness_results.csv"))

categories = {
    "LAMBADA": "Retrieval",
    "HellaSwag": "Reasoning",
    "WinoGrande": "Commonsense",
    "ARC-Easy": "Reasoning",
    "ARC-Challenge": "Reasoning",
    "MMLU": "Knowledge",
}

table1 = pd.DataFrame({
    "Benchmark": rob["benchmark"],
    "Category": rob["benchmark"].map(categories),
    "rho_spearman": rob["spearman_rho"].round(4),
    "p_exact": rob["p_value_exact"].round(4),
    "bonferroni_adj_p": rob["bonferroni_adj_p"].round(4),
    "bh_fdr_adj_p": rob["bh_fdr_adj_p"].round(4),
    "boot_ci_lower": rob["boot_ci_lower"].round(4),
    "boot_ci_upper": rob["boot_ci_upper"].round(4),
    "sigma_pure": rob["std_attn0"].round(6),
    "sigma_h24_1": rob["std_attn1"].round(6),
    "sigma_h12_1": rob["std_attn2"].round(6),
    "sigma_h6_1": rob["std_attn4"].round(6),
    "sigma_h3_1": rob["std_attn8"].round(6),
    "cohen_d": rob["cohen_d"].round(4),
    "cohen_d_ci_lo": rob["cohen_d_ci_lo"].round(4),
    "cohen_d_ci_hi": rob["cohen_d_ci_hi"].round(4),
    "eta_squared": rob["eta_squared"].round(6),
    "omega_squared": rob["omega_squared"].round(6),
    "monotone_decreasing": rob["monotone_decreasing"],
})

table1.to_csv(os.path.join(OUT, "table1_task_specificity.csv"), index=False)
print("=== Table 1 ===")
print(table1.to_string(index=False))
print()

# ============================================================
# B. Figure 1 data: Decoupling Visualization
# ============================================================
bridge = pd.read_csv(os.path.join(BASE, "exp010_bridge_results.csv"))

fig_data = pd.DataFrame({
    "variant": bridge["variant"],
    "attention_ratio": bridge["attention_ratio"],
    "cross_arch_std": bridge["cross_arch_std"].round(6),
    "mean_jaccard_helped": bridge["mean_jaccard_helped"].round(6),
    "mean_jaccard_hurt": bridge["mean_jaccard_hurt"].round(6),
    "mean_net_asymmetry": bridge["mean_net_asymmetry"].round(6),
})

fig_data.to_csv(os.path.join(OUT, "fig1_decoupling_data.csv"), index=False)
print("=== Figure 1 Data ===")
print(fig_data.to_string(index=False))
print()

# ============================================================
# C. GDN-excluded Sensitivity Table
# ============================================================
gdn = pd.read_csv(os.path.join(BASE, "robustness_supplement_gdn_excluded.csv"))

gdn_table = pd.DataFrame({
    "Benchmark": gdn["benchmark"],
    "rho_all_3_arch": gdn["rho_full"].round(4),
    "p_all_3_arch": gdn["p_full"].round(4),
    "rho_gdn_excluded": gdn["rho_gdn_excluded"].round(4),
    "p_gdn_excluded": gdn["p_gdn_excluded"].round(4),
    "direction": gdn["direction"],
})

gdn_table.to_csv(os.path.join(OUT, "table_gdn_sensitivity.csv"), index=False)
print("=== GDN Sensitivity ===")
print(gdn_table.to_string(index=False))

print("\n=== All paper data files written to", OUT, "===")
