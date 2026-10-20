# code exp18 e2e finetune

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp18-e2e-finetune_20260520T122621_result.json`
- **Structured JSON:** [`4cae5cf31292c341facd.json`](../../sessions/4c/4cae5cf31292c341facd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

```
exp18 End-to-end Fine-tuning Results (F1 macro):

9-class E2E:
  seed42:  IID=1.000  DD_OOD=1.000  AA_OOD=1.000
  seed123: IID=1.000  DD_OOD=1.000  AA_OOD=0.990
  seed456: IID=1.000  DD_OOD=1.000  AA_OOD=1.000
  mean:    IID=1.000±0.000  DD_OOD=1.000±0.000  AA_OOD=0.997±0.005

对比 frozen probing (exp1):
  frozen:  IID=1.000±0.000  DD_OOD=0.994±0.005  AA_OOD=0.939±0.047
  e2e:     IID=1.000±0.000  DD_OOD=1.000±0.000  AA_OOD=0.997±0.005
  Δ:       IID=+0.000       DD_OOD=+0.006        AA_OOD=+0.058
```

**关键发现**：E2E fine-tuning 在 AA_OOD 上提升最大（+5.8%），将 ActorAttack OOD F1 从 0.939 提升到 0.997，同时方差大幅缩小（0.047→0.005）。DD_OOD 也从 0.994 提升到完美 1.000。

所有 seed 在 epoch 1 就达到 val_f1=1.0，随后 early stop。训练非常稳定。

**产出**：
- Checkpoints: `checkpoints/exp18_e2e_seed{42,123,456}/best.pt`（包含 encoder + GRU state dict）
- 结果 JSON: `results/exp18_e2e_results.json`
- 脚本: `scripts/exp18_e2e_finetune.py`

---
