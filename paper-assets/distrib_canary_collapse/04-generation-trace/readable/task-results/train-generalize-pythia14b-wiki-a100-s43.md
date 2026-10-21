# train generalize pythia14b wiki a100 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_generalize_pythia14b_wiki_a100_s43_20260518T024437_result.json`
- **Structured JSON:** [`b674c5ad96e5ef040c65.json`](../../sessions/b6/b674c5ad96e5ef040c65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动：

- **exp_id**: `generalize_pythia14b_wiki_a100_s43`
- **PID**: 314396
- **GPU**: cuda:1（已占用 24.8 GiB，利用率 79%）
- **模型**: `/root/autodl-tmp/.hf_cache/pythia-1.4b-local`（因 HF 缓存不完整，改用本地路径）
- **参数**: seed=43, α=1.0, 10 gen, 5000 steps/gen, batch_size=8
- **日志**: `~/runs/distrib_canary_collapse/generalize_pythia14b_wiki_a100_s43.log`

注意：命令中 `--model_name` 从 `EleutherAI/pythia-1.4b` 改为本地路径 `/root/autodl-tmp/.hf_cache/pythia-1.4b-local`，因为 HF cache 只有 ref 没有 snapshots，`TRANSFORMERS_OFFLINE=1` 模式下无法加载。参考 s42 和 pythia-1b 实验也使用了本地路径。

---
