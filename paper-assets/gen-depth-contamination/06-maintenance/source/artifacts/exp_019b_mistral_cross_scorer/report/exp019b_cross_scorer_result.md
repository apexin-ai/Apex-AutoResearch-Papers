# exp-019b Mistral Cross-Scorer Result (2026-05-16)

## Conclusion: Mistral K*=1 is GENUINE, not self-scorer artifact

| Pair | Self-scorer (exp-019) | Cross-scorer Qwen-base (exp-019b) | Cross CI |
|------|----------------------|-----------------------------------|----------|
| 0v1 | 0.9843 | 0.9209 | [0.9189, 0.9229] |
| 1v2 | 0.5935 | **0.5695** | [0.5645, 0.5746] |
| 2v3 | 0.5402 | 0.5335 | [0.5283, 0.5382] |

Cross-scorer AUC全线低于self-scorer。如果K*=1是self-scoring虚高，cross应更高——实际相反。

## Framing impact
- "all N conditions K*=2" claim needs revision
- Score so far: 6/7 model configs K*=2, Mistral-7B K*=1
- LLaMA-8B pending (exp-018)
