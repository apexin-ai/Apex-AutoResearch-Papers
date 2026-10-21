# infra mvp param fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mvp-param-fix_20260514T053749_result.json`
- **Structured JSON:** [`db0e60d6313a0ce5a8e4.json`](../../sessions/db/db0e60d6313a0ce5a8e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

| 项目 | 结果 |
|------|------|
| `prepare_data.py` | `n_prompts` default → 5000 ✓；prompt 来源改为 `train_raw`（test set 仅 ~1500 条满足 ≥64 words，不够 5000） |
| `iterative_train.py` | `steps_per_gen` default → 5000 ✓ |
| 新 Prompts 数量 | 5000 ✓ |
| 旧数据/结果清理 | `data/wikitext103/prompts` 已重建，`results/mvp/` 已删除不存在 ✓ |

额外修改说明：WikiText-103 test split 过滤后仅约 1500 条 ≥64 words 的段落，无法满足 5000 prompts 需求，因此将 prompt 来源从 `test_raw` 改为 `train_raw`（716K 条）。Prompts 仅用作生成前缀种子，不参与损失计算，不影响评估数据完整性。

---
