# code shuffle encoder verify

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_shuffle-encoder-verify_20260520T092537_result.json`
- **Structured JSON:** [`a0795dfac37012b5c640.json`](../../sessions/a0/a0795dfac37012b5c640.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论明确：

## Shuffle 实验使用的是 RoBERTa-large（exp15），不是 DeBERTa-v3-base

**证据：**

1. **脚本文档字符串**（`turn_shuffle_ablation.py` 第1行）：`"Uses exp15 (RoBERTa-large) checkpoints"`

2. **Checkpoint 路径**：
   - 9-class: `checkpoints/exp15_roberta_large_9class_seed{42,123,456}/`
   - vanilla: `checkpoints/exp15_roberta_large_vanilla_seed{42,123,456}/`

3. **Encoder 来源**：`ROBERTA_LARGE = "/root/autodl-tmp/roberta-large-local"`，tokenizer 和 encoder 均从此路径加载（hidden_size=1024）

4. **数值匹配**：结果中 9-class DD OOD original 均值 ≈ 0.987、vanilla DD OOD original 均值 ≈ 0.927，精确匹配 exp15 RoBERTa-large baseline，与 exp1 DeBERTa-v3 的 0.997 / 0.312 不符

**Reviewer 的怀疑是对的**——论文如果声称 shuffle ablation 用的是 DeBERTa-v3（exp1），那就是报错了。实际用的是 exp15 RoBERTa-large 的 checkpoint。需要在论文中修正这一点。

---
