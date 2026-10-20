## Diagnosis Results (2026-05-18)

### Root Cause Confirmed
- GAR values on vanilla Qwen2.5-7B are ~0.01 per turn
- Adjacent turn GAR differences are << 0.02
- epsilon=0.02 completely suppresses ReLU(drop - epsilon), making L_GAR always 0

### Gradient Chain
- Attention weights have requires_grad=True (verified layers 0-2)
- Gradient path is intact

### Dry-Run Verification (cumulative mode, epsilon=0.001)
```
Epoch 0 Step 0 | L_NTP=1.9171 L_GAR=0.1317 Loss=1.9829 | Gate=0.9923 | Mem=42.3GB
Epoch 0 Step 1 | L_NTP=1.2565 L_GAR=0.1253 Loss=1.3192 | Gate=0.9922 | Mem=42.3GB
Epoch 0 Step 2 | L_NTP=1.4601 L_GAR=0.0864 Loss=1.5033 | Gate=0.9922 | Mem=46.7GB
Epoch 0 Step 3 | L_NTP=1.6076 L_GAR=0.0936 Loss=1.6544 | Gate=0.9927 | Mem=46.7GB
Epoch 0 Step 4 | L_NTP=1.8240 L_GAR=0.0579 Loss=1.8529 | Gate=0.9925 | Mem=46.7GB
Gate parameters received gradients during training: True
```

### Changes Made
1. config.py: GAR_EPSILON 0.02 -> 0.001
2. gar.py: compute_gar_loss now supports mode=pairwise|cumulative|maximize
3. train_phase2.py: added --gar-loss-mode (default cumulative) and --gar-epsilon (default 0.001) args
