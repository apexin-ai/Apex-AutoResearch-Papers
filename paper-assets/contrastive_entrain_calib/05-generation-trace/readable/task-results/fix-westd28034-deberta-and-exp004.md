# fix westd28034 deberta and exp004

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd28034_deberta_and_exp004_20260518T153826_result.json`
- **Structured JSON:** [`4c468b7e65c186b1439c.json`](../../sessions/4c/4c468b7e65c186b1439c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练稳定运行中。

## 完成状态

### Task A: DeBERTa 预下载 ✅
- `microsoft/deberta-v3-base` tokenizer + model 已通过 hf-mirror 下载
- tiktoken 依赖已安装

### Task B: exp-004 ACT baseline ✅
- 脚本：`/root/contrastive_entrain_calib/training/run_exp004_act_baseline.py`
- 训练已启动，step 10/8000 正常输出：
  - `sft=2.59, l2=2.43, total=2.83`
  - GPU 0: 21.4GB / 32.6GB (充裕)
  - 10 steps 用时 85s → 预计 ~19h 完成
- Registry 已更新为 RUNNING

**关键设计**：
- L2 consistency 在 generation prompt 位置（第4轮 assistant 起始）提取 hidden states，此时模型已处理完不同的 user2（valid vs invalid），确保比较有意义
- SFT labels 仅覆盖 assistant1 content tokens（用 `<|im_end|>` 搜索定位，避免 Qwen3 `&lt;think>` 标签干扰 `apply_chat_template` prefix 不匹配问题）
- Hooks 不 detach，梯度可穿过 L2 loss 回传

---
