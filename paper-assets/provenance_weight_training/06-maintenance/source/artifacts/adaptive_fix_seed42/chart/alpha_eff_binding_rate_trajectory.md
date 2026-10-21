Server path: /root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/alpha_eff_binding_rate.pdf

Key findings - Binding rate per 1000-step window:
  Step 500:  alpha_eff binding rate = 0.121
  Step 1500: alpha_eff binding rate = 0.100
  Step 2500: alpha_eff binding rate = 0.379
  Step 3500: alpha_eff binding rate = 0.368
  Step 4500: alpha_eff binding rate = 0.371
  Step 5500: alpha_eff binding rate = 0.375
  Step 6500: alpha_eff binding rate = 0.371

Overall statistics (51913 samples):
- alpha_eff binding: 9926 (19.1%)
- ESS binding: 15304 (29.5%)
- Neither (b*=0 or intermediate): 51.4%

Analysis:
- Early training (step 0-2000): ESS constraint dominates, alpha_eff binding rate only ~10-12%
- Mid-to-late training (step 2000+): alpha_eff binding rate jumps to ~37% and stabilizes
- ESS binding remains more frequent overall
- The transition around step 2000 suggests the model learns contamination patterns, causing more batches to hit the alpha_eff upper bound (0.8)
- Neither constraint binding in ~51% of samples indicates moderate contamination levels where b* settles naturally without hitting constraints