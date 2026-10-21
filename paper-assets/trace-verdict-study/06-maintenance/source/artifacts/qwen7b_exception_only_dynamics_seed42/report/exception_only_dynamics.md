# Exception_only Training Dynamics (Qwen-7B, seed42)

## Learning Curve (eval every 50 steps)

| Step | Accuracy | Loss | Pass F1 | Fail F1 |
|------|----------|------|---------|---------|
| 50 | 99.33% | 0.1897 | 0.9953 | 0.9883 |
| 100 | 99.33% | 0.1272 | - | - |
| 150 | 99.33% | 0.0793 | - | - |
| 200 | **99.83%** | 0.0475 | - | - |
| 250 | 99.83% | 0.0437 | - | - |
| 300 | 99.83% | 0.0378 | - | - |
| 350 | 99.83% | 0.0333 | - | - |
| 400 | 99.83% | 0.0347 | - | - |
| 444 | 99.83% | 0.0329 | 0.9988 | 0.9971 |

## Key Findings

- **Saturation at step 200**: accuracy jumps from 99.33% to 99.83% and stays flat
- **Step 50 already at 99.33%**: the task is nearly trivial from the first eval point
- **Loss continues declining** (0.19→0.03) even after accuracy saturates
- **Perfect precision** for pass class (1.0), **perfect recall** for fail class (1.0)
- Total GPU time: 2.56 hours
