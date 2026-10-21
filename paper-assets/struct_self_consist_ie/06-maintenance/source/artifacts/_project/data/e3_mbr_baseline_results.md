## E3 MBR Baseline Results (Micro-F1)

| Dataset | Greedy | LP | MBR | MV | Oracle | MBR−Grd | MV−Grd |
|---------|--------|------|------|------|--------|---------|--------|
| SciERC (529) | .6663 | .6639 | .6657 | .6579 | .7795 | −0.06pp | −0.84pp |
| CoNLL (2756) | .9116 | .8968 | .9115 | .9132 | .9547 | −0.01pp | +0.15pp |
| FewNERD (32565) | .7916 | .7919 | .7840 | .7690 | .8856 | −0.76pp | −2.27pp |

### Key Findings
1. MBR fails to beat greedy on all 3 datasets (micro-F1)
2. MV only positive on CoNLL (+0.15pp), negative on SciERC/FewNERD
3. LP (log-probability) has weak positive signal on FewNERD instance-avg (+1.37pp) but near-zero micro-F1 gain
4. Oracle gap remains 4-11pp → information exists in samples but no unsupervised method extracts it

### Data Sources
- SciERC: scierc_mf4v2_seed456 (N=8)
- CoNLL: exp_002_conll_n16_r1024 (N=16, subsampled)
- FewNERD: fewnerd_mf4v2_seed456 (N=8)

### Paper Implication
MBR as theoretically optimal unsupervised selection still cannot beat greedy. Confirms paper_framing core claim: unsupervised selection faces structural bottleneck in NER, not a utility function design problem.