# MAVEN Event Detection — Data Preparation & BCS Report (exp-004)

## Dataset Statistics
| Split | Docs | Events | Mentions | Types | Neg Triggers |
|-------|------|--------|----------|-------|--------------|
| train | 2913 | 73496  | 77993    | 168   | 323992       |
| valid | 710  | 17726  | 18904    | 168   | 79699        |
| test  | 857  | -      | -        | -     | -            |

## SCS Distribution (all-MiniLM-L6-v2, type-name-only)
| Metric   | Few-NERD | MAVEN |
|----------|----------|-------|
| n_types  | 66       | 168   |
| n_pairs  | 2145     | 14028 |
| mean     | 0.1917   | 0.2161|
| std      | 0.1447   | 0.1030|
| max      | 0.8560   | 0.8368|
| median   | 0.1528   | 0.2121|
| q90      | 0.4238   | 0.3457|
| q95      | 0.5145   | 0.3892|
| pairs>0.5| 114 (5.3%)| 119 (0.8%)|

## Top-10 Most Confusable MAVEN Pairs
| SCS    | Type A            | Type B             |
|--------|-------------------|--------------------|
| 0.8368 | Commerce_buy      | Commerce_sell      |
| 0.8179 | Choosing          | Deciding           |
| 0.7900 | Motion            | Self_motion        |
| 0.7363 | Death             | Killing            |
| 0.7308 | Motion            | Motion_directional |
| 0.7092 | Robbery           | Theft              |
| 0.7078 | Process_end       | Process_start      |
| 0.6891 | Coming_to_be      | Coming_to_believe  |
| 0.6822 | Legal_rulings     | Legality           |
| 0.6704 | Being_in_operation| Military_operation |

## Key Observations
1. **MAVEN has sparser confusability**: only 0.8% pairs exceed SCS 0.5 (vs 5.3% for Few-NERD)
2. **Clear confusable clusters exist**: Commerce_*, Motion_*, Crime-related types form natural high-SCS groups
3. **Good experimental properties**: large type space (14028 pairs) provides ample low-SCS controls; confusable clusters enable extreme batch construction
4. **Cross-task validation feasibility**: both datasets show max SCS ~0.84, suggesting the SCS-confusion mechanism generalizes across NER and ED

## Outputs
- `/root/schema-dag-extraction/data/maven_scs_matrix.json` — full matrix + stats
- `/root/schema-dag-extraction/data/maven_sim_matrix.pt` — PyTorch format for compute_bcs.py
- `/root/schema-dag-extraction/configs/maven_event_types.json` — 168 type names
- `/root/schema-dag-extraction/src/compute_maven_scs.py` — reproducible script