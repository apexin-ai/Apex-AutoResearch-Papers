## Multi-seed Selection F1 Analysis (3 seeds × bootstrap 10000)

| Config | N | Best Signal | Δ greedy | p (Fisher) |
|--------|---|------------|----------|------------|
| Qwen SciERC NER N=16 | 529 | LP | +0.0047 | 0.066 |
| Qwen SciERC RE N=16 | 397 | LP | +0.0101 | 0.053 |
| Qwen SciERC NER N=8 | 529 | LP | +0.0004 | 0.541 |
| LLaMA SciERC NER N=8 | 529 | FK | -0.0014 | 0.698 |
| LLaMA CoNLL NER N=16 | 2756 | VC | +0.0028 | 0.0001 |

- CoNLL N=16: all 5 signals beat greedy (p<0.001)
- SciERC: no signal reaches p<0.05 (LP closest at 0.05-0.07)
- VC hurts on SciERC (Δ≈-0.03)
- Oracle gap: NER +17.6pp, RE +23.8pp

Server files: code/compute_selection_f1.py, output/multiseed_selection_f1.json