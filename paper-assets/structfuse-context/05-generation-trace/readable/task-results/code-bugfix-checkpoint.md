# code bugfix checkpoint

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bugfix_checkpoint_20260512T102506_result.json`
- **Structured JSON:** [`bb24c356017384c33fa1.json`](../../sessions/bb/bb24c356017384c33fa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All fixes applied. Summary of changes:

**1. `train.py`** (both `code/training/` and `_project/intermediate/`): `_save_checkpoint` now saves `model.state_dict()` (complete StructFuseEncoder: backbone + projection + fusion_head + log_temperature), instead of only saving `model.backbone`.

**2. `eval_retrieval.py`**:
- Imports `StructFuseEncoder` from `contrastive_model` (via sys.path to sibling training dir)
- `StructFuseRetriever.__init__` reads `training_config.json` to reconstruct the full `StructFuseEncoder` with matching architecture, then loads `model.pt` state_dict
- `StructFuseRetriever.encode` calls `self.model.encode()` which goes through backbone → mean pool → projection head → L2 normalize, producing 256-dim embeddings (not raw backbone embeddings)
- Test file filter: changed from `"test" in rel.lower()` (too broad) to only skipping `test_*.py` and `*_test.py` filename patterns

**3. `contrastive_model.py`**: No changes needed — `encode()` already correctly chains backbone → mean pool → projection → normalize.

**4. `eval_swebench.py`**: `--depth 50` → `--depth 200`.

**Consistency check**: train saves `model.state_dict()` → eval loads with `model.load_state_dict()` on identically-constructed `StructFuseEncoder` — keys match. Encode output is 256-dim (proj_dim) in both training and evaluation.

---
