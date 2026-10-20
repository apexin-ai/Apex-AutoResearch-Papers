# research trl qwen mismatch fix

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_trl-qwen-mismatch-fix_20260512T173600_result.json`
- **Structured JSON:** [`adbd4562cf5cc4f43d8b.json`](../../sessions/ad/adbd4562cf5cc4f43d8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dpo-002 仍在 cuda:3 上运行（12 分钟），未受影响。

---

## 报告

### 1. TRL 版本 + 问题根因

| 项 | 值 |
|---|---|
| TRL | 1.4.0（最新版） |
| transformers | 4.57.6 |
| tokenizers | 0.22.2 |

**根因**：TRL `DPOTrainer._prepare_dataset()` 的 `tokenize_fn`（`dpo_trainer.py:930`）对 conversational 数据硬编码 `add_generation_prompt=True`。这会在 prompt_ids 末尾追加 3 个 token `<|im_start|>assistant\n`（151644, 77091, 198），假定 completion 是 assistant 角色。但本项目的 chosen/rejected 是 **user 角色** 消息，实际 continuation 开头是 `<|im_start|>user\n`（151644, 872, 198）。token 位置 129 处 `assistant`(77091) ≠ `user`(872)，导致 100% mismatch。

这是已知 issue（TRL GitHub #5213），TRL 1.4.0 未修复，且无更新版本可升级。

### 2. 修复方向测试结果

| 方向 | 可行性 | 结果 | 说明 |
|------|--------|------|------|
| **A: add_generation_prompt=False** | ✅ 可行 | 0/1563 mismatch | 需 monkey-patch TRL 内部代码，不稳定 |
| **B: 转纯文本格式** | ✅ **推荐** | 0/3126 checks 全部通过 | 不修改 TRL，数据预处理中转换 |
| C: 升级 TRL | ❌ 不可行 | 1.4.0 已是最新 | 无修复版本 |
| D: padding/label 配置 | ❌ 不可行 | — | mismatch 发生在 tokenization 阶段，padding 配置无法修复 |

### 3. 推荐修复方案（Fix B）

在 `load_dpo_dataset()` 中用 `tokenizer.apply_chat_template()` 将 conversational messages 转为 plain text strings，然后以 `{"prompt": str, "chosen": str, "rejected": str}` 格式传给 DPOTrainer。TRL 检测到非 conversational 数据后走文本 tokenization 路径，不会追加 generation prompt。

额外修复：`padding_side="right"`（原脚本用 `"left"`，causal LM DPO 训练应右 padding）。

### 4. dpo-003 训练脚本

- **脚本路径**：`/root/democalib/train_dpo_v3.py`
- **启动命令**：
```bash
CUDA_VISIBLE_DEVICES=0 python train_dpo_v3.py \
  --model-path /root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct \
  --data-path data/dpo_pairs_v2.jsonl \
  --output-dir /root/democalib/dpo_output_v3/ \
  --wandb-run-name dpo-003-mismatch-fix \
  --batch-size 4 \
  --gpu-id 0
```

### 5. 预期效果

- mismatch 警告：**完全消除**（0/1563）
- loss：应从 ~0.69（随机水平）显著下降，预期 epoch 3 后 < 0.5
- reward accuracy：应从 ~50%（随机）提升到 60-70%+
- 训练脚本超参与 dpo-001/002 一致（lr=5e-7, beta=0.1, epochs=3, LoRA r=16/α=32）

---
