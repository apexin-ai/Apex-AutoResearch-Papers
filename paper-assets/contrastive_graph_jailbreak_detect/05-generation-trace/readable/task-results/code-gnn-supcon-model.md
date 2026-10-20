# code gnn supcon model

**contrastive graph jailbreak detect** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gnn-supcon-model_20260517T055215_result.json`
- **Structured JSON:** [`c0d7dede4b527657c468.json`](../../sessions/c0/c0d7dede4b527657c468.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

- `Models OK` — GINEncoder + SupConLoss import 正常
- `Augmentations OK` — dual_augment import 正常
- `train_mvp.py --help` — CLI 参数解析正常

已创建 5 个文件：
- `src/models/__init__.py`
- `src/models/gin_encoder.py` — 3-layer GIN + projection head, L2 normalized output
- `src/models/supcon_loss.py` — SupConLoss with log-sum-exp trick
- `src/augmentations.py` — dropout_edge / drop_feature / subgraph + dual_augment
- `src/train_mvp.py` — 完整训练入口，支持 5-fold CV 和 cross-failure-mode holdout

---
