# CKA vs Transfer Degradation Analysis

## Qwen2.5-7B-Instruct (mvp_001)
- Overall Spearman(CKA, degradation): rho=-0.3086, p=0.0527 (marginal)
- Per-language: no individual language reaches significance

## Llama-3.1-8B-Instruct (mvp_003)
- Overall Spearman(CKA, degradation): rho=-0.5192, p=0.0012 **
- Per-language: hi significant (rho=-0.7333, p=0.025)

## Cross-model comparison
| Lang | Qwen_CKA | Llama_CKA | Qwen_Deg | Llama_Deg |
|------|----------|-----------|----------|-----------|
| zh   | 0.7388   | 0.7527    | 0.1148   | 0.1462    |
| ar   | 0.6934   | 0.6776    | 0.1542   | 0.1698    |
| ko   | 0.6559   | N/A       | 0.1516   | N/A       |
| hi   | 0.4359   | 0.3805    | 0.2164   | 0.1698    |
| sw   | 0.4158   | 0.4788    | 0.2246   | 0.2090    |

## Language ranking
- By CKA: zh > ar > {ko} > sw/hi (both models agree on top-2 and bottom-2)
- By degradation: zh < ar < {ko} < hi < sw (consistent)
