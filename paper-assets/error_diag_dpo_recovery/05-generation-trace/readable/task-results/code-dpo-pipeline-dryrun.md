# code dpo pipeline dryrun

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo-pipeline-dryrun_20260513T063757_result.json`
- **Structured JSON:** [`fae518a993f1c5715f05.json`](../../sessions/fa/fae518a993f1c5715f05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

测试结果总结：

**49 项检查：46 PASS / 3 FAIL**

### 通过的关键验证
1. 合成数据 `tests/synthetic_dpo.jsonl` — 10 条，格式正确，gamma_e 覆盖 0.85-0.97，d 分布 0.1-0.9，三种 error_type 全覆盖
2. `DPODataset` 两种模式均正常加载 — etadn 模式从 JSONL 读 gamma_e，single_gamma 模式用 CLI 参数
3. `collate_dpo` 正确 pad 和 batch
4. `dmpo_loss` / `dmpo_loss_batch` 计算正常，梯度有限
5. `etadn_discount` 三种 loss variant 均产出有限值

### 发现并修复的问题
- **`train_dpo.py:78-83`** — `apply_chat_template` 在 transformers 5.x 默认返回 `BatchEncoding` 而非 `list[int]`，导致 `collate_dpo` crash。已加 `return_dict=False` 修复。

### 发现的设计问题（未修复，需决策）
- **φ weights 不归一化** — `dmpo_loss.py` docstring 声称 "already normalized (sum=1)" 是错的。实际 sum 分别为 4.22 (γ=0.85)、4.82 (γ=0.92)、5.25 (γ=0.97)。当 chosen/rejected 长度不同时，φ weight sum 不同可能引入长度偏置。需要决定是改为归一化还是文档化当前行为。

---
