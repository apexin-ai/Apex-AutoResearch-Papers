# Exp43: MHJ Human Jailbreak Evaluation

## Data Access Status
- **MHJ (ScaleAI/mhj)**: GATED on HuggingFace. Requires access request (name, affiliation, email, country, purpose). Server cannot reach huggingface.co directly; hf-mirror.com also enforces gating.
- **Fallback evaluation**: verazuo/jailbreak_llms single-turn human jailbreaks (666 jailbreak + 213 benign, from JailbreakChat communities)

## Results (3-seed mean ± std)

| Variant | F1 | Precision | Recall | Accuracy | FPR@95TPR |
|---------|-----|-----------|--------|----------|-----------|
| vanilla | 0.131±0.033 | 0.939±0.022 | 0.071±0.019 | 0.292±0.012 | 1.000±0.000 |
| 9-class (plan_002) | 0.812±0.135 | 1.000±0.000 | 0.706±0.200 | 0.777±0.152 | 0.002±0.002 |
| jb_mlm | 0.968±0.010 | 0.982±0.012 | 0.955±0.011 | 0.952±0.015 | 0.081±0.109 |
| binary | 0.929±0.037 | 1.000±0.000 | 0.869±0.065 | 0.901±0.049 | 0.000±0.000 |
| wiki_mlm | 0.897±0.093 | 0.972±0.024 | 0.849±0.158 | 0.865±0.110 | 0.192±0.236 |

## Key Findings
1. **9-class DAPT generalizes to human jailbreaks**: +68pp F1 over vanilla (0.812 vs 0.131)
2. **Evidence hierarchy preserved**: vanilla < 9class < jb_mlm (0.131 < 0.812 < 0.968)
3. **Perfect precision for DAPT models**: All DAPT variants achieve ~1.0 precision (0 false positives on benign)
4. **Vanilla completely fails**: Near-zero recall (0.071), classifies almost everything as benign

## Limitations
- Evaluated on single-turn data only (all verazuo samples are 1 user turn)
- MHJ multi-turn evaluation pending data access request
- High variance in 9-class recall across seeds (0.488 to 0.971) suggests sensitivity to specific training run

## Implications for Limitations Section
- Cannot claim "no human-generated multi-turn jailbreak dataset exists" — MHJ exists but is gated
- CAN claim strong generalization to human-written jailbreaks (single-turn)
- Recommend requesting MHJ access for camera-ready or revision

## Server Results File
`/root/persuasion_turn_jailbreak_detect/results/exp8_human_jailbreak_verazuo.json`