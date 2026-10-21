# train exp2 actorattack ood v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_exp2-actorattack-ood-v2_20260518T113927_result.json`
- **Structured JSON:** [`3905289e22b30c4dcd83.json`](../../sessions/39/3905289e22b30c4dcd83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Results registered as `art_20260518_61267d`.

## EXP-2 ActorAttack OOD Results (F1 macro, mean±std, population std)

**Data: 80 jailbreak + 38 benign = 118 conversations**

| Variant | K=1 | K=2 | K=3 | K=5 | Full |
|---|---|---|---|---|---|
| **DeBERTa 9class** | 0.773±0.041 | 0.855±0.048 | 0.921±0.046 | 0.966±0.028 | 0.972±0.026 |
| **DeBERTa binary** | 0.788±0.020 | 0.935±0.018 | 0.976±0.005 | 0.995±0.005 | 0.995±0.005 |
| **DeBERTa scrambled** | 0.652±0.034 | 0.804±0.053 | 0.854±0.046 | 0.910±0.052 | 0.931±0.040 |
| **DeBERTa mlm** | 0.736±0.150 | 0.909±0.058 | 0.945±0.039 | 0.929±0.033 | 0.893±0.080 |
| **DeBERTa wiki_mlm** | 0.656±0.224 | 0.672±0.252 | 0.693±0.280 | 0.689±0.285 | 0.686±0.297 |
| **DeBERTa topic** | 0.513±0.077 | 0.580±0.109 | 0.565±0.100 | 0.615±0.111 | 0.625±0.141 |
| **DeBERTa vanilla** | 0.337±0.049 | 0.306±0.026 | 0.284±0.011 | 0.262±0.006 | 0.258±0.000 |
| **RoBERTa 9class** | 0.738±0.033 | 0.805±0.033 | 0.884±0.066 | 0.925±0.066 | 0.939±0.046 |
| **RoBERTa mlm** | 0.633±0.133 | 0.665±0.150 | 0.713±0.174 | 0.719±0.184 | 0.730±0.201 |
| **RoBERTa vanilla** | 0.410±0.126 | 0.425±0.143 | 0.432±0.144 | 0.466±0.144 | 0.466±0.163 |

**Key observations:**
- **binary** 在 OOD 上表现最强，K=3 即达 0.976，Full 达 0.995
- **9class** 紧随其后，Full 0.972，且方差更小更稳定
- **scrambled** 大幅落后于 9class（Full 0.931 vs 0.972），说明 persuasion label 顺序信息对 OOD 泛化有贡献
- **mlm** Full F1 反而低于 K=3/K=5（0.893 vs 0.945），存在 seed 456 异常表现
- **wiki_mlm** 方差极大（std ~0.22-0.30），三个 seed 差异悬殊
- **vanilla** 和 **rob_vanilla** 接近随机，确认 encoder 预训练是必要的
- DeBERTa 整体优于 RoBERTa 同类变体（9class: 0.972 vs 0.939, mlm: 0.893 vs 0.730）

---
