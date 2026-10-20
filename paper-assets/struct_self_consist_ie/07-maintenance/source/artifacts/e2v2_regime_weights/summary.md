# E2v2: Per-Regime Ensemble Weights — Summary

Date: 2026-05-20 19:35

## Data Availability

- Loaded: 10 configs
- Skipped: 6 configs (samples.jsonl not found)
- Missing: Qwen2.5_72B_zs_scierc, Qwen2.5_72B_zs_conll, Qwen2.5_72B_zs_fewnerd, Qwen2.5_72B_fs_scierc, Qwen2.5_72B_fs_conll, Qwen2.5_72B_fs_fewnerd
- Regime distribution: {'ft': 10}

**Warning: ZS and FS samples.jsonl data has been cleaned from the server.**
Only FT regime is available. Per-regime FT/ZS/FS comparison is NOT possible.
To enable this analysis, re-run ZS/FS inference to generate samples.jsonl.

## Per-Regime Optimal Weights

| Regime | #Configs | SJ | FK | VC | EM | LP | Full F1 | CV F1 | Delta(ens-single) |
|--------|----------|-----|-----|-----|-----|-----|---------|-------|----------------|
| FT | 10 | 0.0 | 0.0 | 0.1 | 0.0 | 0.9 | 0.7807 | 0.7807 | +0.30pp |
| ZS | — | — | — | — | — | — | — | — | — |
| FS | — | — | — | — | — | — | — | — | — |
| ALL | 10 | 0.0 | 0.0 | 0.1 | 0.0 | 0.9 | 0.7807 | 0.7807 | +0.30pp |

## Per-Model-Family Weights (within FT)

| Model | #Configs | SJ | FK | VC | EM | LP | Full F1 | LP weight |
|-------|----------|-----|-----|-----|-----|-----|---------|-----------|
| LLaMA-8B | 3 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.7877 | 1.0 |
| Qwen3-8B | 7 | 0.0 | 0.0 | 0.2 | 0.0 | 0.8 | 0.7745 | 0.8 |

## Regime vs Cross-Config Comparison

- **FT**: regime=0.7807 vs cross=0.7807, Delta=+0.00pp, p=1.0000 (not significant)

## LP Weight Across Regimes

- FT: LP=0.9
- ZS: no data
- FS: no data

**Cannot test hypothesis 'LP weaker in ZS' — ZS data unavailable.**

## Per-Config: Regime Weights vs Cross-Config Weights

Win/Tie/Loss: 0/10/0
Mean Delta_pp: +0.00

## LOO Validation: FT

- Hold out Qwen3_8B_ft_conll_s123: LOO_F1=0.9070, Full_F1=0.9070, Delta=+0.00pp
  LOO weights: {SJ: 0.0, FK: 0.0, VC: 0.1, EM: 0.0, LP: 0.9}
- Hold out Qwen3_8B_ft_conll_s456: LOO_F1=0.9018, Full_F1=0.9018, Delta=+0.00pp
  LOO weights: {SJ: 0.0, FK: 0.0, VC: 0.1, EM: 0.0, LP: 0.9}
- Hold out Qwen3_8B_ft_scierc_s456: LOO_F1=0.6476, Full_F1=0.6476, Delta=+0.00pp
  LOO weights: {SJ: 0.0, FK: 0.0, VC: 0.1, EM: 0.0, LP: 0.9}
- Hold out Qwen3_8B_ft_scierc_s789: LOO_F1=0.6575, Full_F1=0.6575, Delta=+0.00pp
  LOO weights: {SJ: 0.0, FK: 0.0, VC: 0.1, EM: 0.0, LP: 0.9}
- Hold out Qwen3_8B_ft_fewnerd_s123: LOO_F1=0.7706, Full_F1=0.7706, Delta=+0.00pp
  LOO weights: {SJ: 0.0, FK: 0.0, VC: 0.1, EM: 0.0, LP: 0.9}
- Hold out Qwen3_8B_ft_fewnerd_s456: LOO_F1=0.7679, Full_F1=0.7679, Delta=+0.00pp
  LOO weights: {SJ: 0.0, FK: 0.0, VC: 0.1, EM: 0.0, LP: 0.9}
- Hold out Qwen3_8B_ft_fewnerd_s789: LOO_F1=0.7666, Full_F1=0.7666, Delta=+0.00pp
  LOO weights: {SJ: 0.0, FK: 0.0, VC: 0.1, EM: 0.0, LP: 0.9}
- Hold out LLaMA_8B_ft_fewnerd_s42: LOO_F1=0.7858, Full_F1=0.7858, Delta=+0.00pp
  LOO weights: {SJ: 0.0, FK: 0.0, VC: 0.1, EM: 0.0, LP: 0.9}
- Hold out LLaMA_8B_ft_fewnerd_s123: LOO_F1=0.7882, Full_F1=0.7882, Delta=+0.00pp
  LOO weights: {SJ: 0.0, FK: 0.0, VC: 0.1, EM: 0.0, LP: 0.9}
- Hold out LLaMA_8B_ft_fewnerd_s456: LOO_F1=0.7881, Full_F1=0.7881, Delta=+0.00pp
  LOO weights: {SJ: 0.0, FK: 0.0, VC: 0.1, EM: 0.0, LP: 0.9}
- Mean LOO Delta: +0.00pp
