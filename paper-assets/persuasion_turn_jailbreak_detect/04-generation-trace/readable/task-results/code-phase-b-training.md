# code phase b training

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase-b-training_20260517T063023_result.json`
- **Structured JSON:** [`e0783c60f60c2731ee50.json`](../../sessions/e0/e0783c60f60c2731ee50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。最终代码结构和验证结果：

```
/root/persuasion_turn_jailbreak_detect/
├── data/
│   ├── mock_train.jsonl    # 5条对话 mock 数据
│   └── mock_val.jsonl
└── src/
    ├── data/
    │   ├── dataset.py      # TurnDataset + ConversationDataset ✓
    │   └── collator.py     # TurnCollator + ConversationCollator ✓
    ├── models/
    │   ├── deberta_multitask.py  # DeBERTa 8-class persuasion + binary intent ✓
    │   ├── gru_classifier.py     # Bi-GRU + attention pooling + MLP ✓
    │   └── baseline.py           # Frozen vanilla DeBERTa + GRU ✓
    ├── train_deberta.py    # Stage 1 dry-run 通过 (loss=2.34) ✓
    ├── train_classifier.py # Stage 2 dry-run 通过 (loss=0.68) ✓
    └── evaluate.py         # F1/early detection/FPR/per-attack metrics ✓
```

关键修复：DeBERTa-v3 权重默认加载为 FP16，所有 `from_pretrained` 调用已加 `dtype=torch.float32`，mixed precision 设为 `"no"` 避免精度冲突。

---
