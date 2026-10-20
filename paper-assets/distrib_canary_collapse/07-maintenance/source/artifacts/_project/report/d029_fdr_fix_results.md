## D029 FDR Fix Results

### Consensus Classification: 6 robust 不变
token_entropy→d1/d2/d3 + ece→d1/d2/d3 均保持 robust。内部移动：
- ece→d1: TY seeds 3→2，仍 4/5 methods
- token_entropy→d3: permG seeds 4→3，仍 5/5 methods

### FPR/FNR (diff ground truth, FDR-corrected)
| Method | FPR | FNR |
|--------|:---:|:---:|
| naive | 100% | 0% |
| differenced | 0% | 0% |
| threshold | 9.1% | 0% |
| TY | 0% | 25.0% |
| permG | 0% | 4.2% |
| consensus | 0% | 0% |

### LOO FPR/FNR
permG 综合最优 (FPR_loo=12.5%, FNR_loo=28.1%)

### Sensitivity
- token_entropy→d1/d2: 9/9 stable
- token_entropy→d3: 8/9 (permG 在 5/5+4/4 配置下掉)
- ece→d2/d3: 7/9 (TY dissenter)

注意：FPR ground truth 将由 D028 改为 α=0.0 null control。