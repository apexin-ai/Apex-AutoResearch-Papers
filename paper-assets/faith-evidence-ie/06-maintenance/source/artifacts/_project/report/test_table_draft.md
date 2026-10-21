# Test Set Scaling Table (Re-DocRED)

| Model | SFT test ign_f1 | RSFT test ign_f1 | Δ (RSFT−SFT) | evi_f1_joint | edcr | Trunc.% |
|:------|:---------------:|:----------------:|:------------:|:------------:|:----:|:-------:|
| Qwen3-1.7B | *(pending)* | 0.2933 | — | 0.2320 | 0.8169 | 73.8 |
| Qwen3-4B | *(running)* | —† | — | — | — | — |
| Qwen3-8B | *(running)* | 0.3353 | — | 0.2526 | 0.7993 | 1.8 |
| Qwen3-14B | *(running)* | 0.3849 | — | 0.2688 | 0.7865 | 13.4 |
| LLaMA-3.1-8B | *(running)* | 0.3599 | — | 0.2509 | 0.8391 | 56.6 |

† 4B RSFT s42 checkpoint irrecoverable; dev ign_f1=0.4482 (Method A, N=3)
