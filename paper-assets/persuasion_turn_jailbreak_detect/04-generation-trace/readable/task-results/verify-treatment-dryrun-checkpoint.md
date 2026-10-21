# verify treatment dryrun checkpoint

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_treatment-dryrun-checkpoint_20260517T075606_result.json`
- **Structured JSON:** [`67900747368603beefd8.json`](../../sessions/67/67900747368603beefd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. dry_run 是否设计为不保存 checkpoint

**不是。** `train_deberta.py` 的逻辑中，checkpoint 保存代码在 `if args.dry_run: break` **之前**执行。dry_run 只限制训练为 2 batches，但仍会走完 validation 和 save 流程。之前 checkpoints/ 为空说明 dry-run 从未成功执行完成（可能是环境问题，如 PATH 中无 python）。

### 2. 非 dry-run 1 epoch 训练结果

成功。训练指标：
- Train Loss: 2.0448
- Val Loss: 1.2419
- Val Persuasion Acc: 1.0000
- Val Intent Acc: 0.5000

### 3. Checkpoint 文件

```
checkpoints/treatment_dryrun/
├── epoch_1/
│   ├── model.pt          (702M)
│   ├── tokenizer.json    (8.0M)
│   └── tokenizer_config.json (538B)
└── best/
    ├── model.pt          (702M)
    ├── tokenizer.json    (8.0M)
    └── tokenizer_config.json (538B)
```

文件大小正常（DeBERTa-v3-base ~702MB），checkpoint 保存功能验证通过。

---
