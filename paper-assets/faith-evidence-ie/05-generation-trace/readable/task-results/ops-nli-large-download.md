# ops nli large download

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_nli_large_download_20260518T052631_result.json`
- **Structured JSON:** [`f105931d6028e78e7b36.json`](../../sessions/f1/f105931d6028e78e7b36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

| 项目 | 结果 |
|------|------|
| 下载状态 | 成功 |
| 模型类型 | deberta-v2 |
| 参数量 | **435.1M**（符合预期） |
| 磁盘占用 | **1.7GB** |
| 离线加载 | 通过（HF_HUB_OFFLINE=1 验证成功） |
| `rsft_score_filter.py` | **不存在**。但 `--nli_model` 参数在 `rewards/ced_reward.py`、`training/grpo_trainer.py`、`analysis/ced_signal_validation.py` 中均支持，默认值为 `cross-encoder/nli-deberta-v3-base`。使用 large 版本时传 `--nli_model cross-encoder/nli-deberta-v3-large` 即可。 |

---
