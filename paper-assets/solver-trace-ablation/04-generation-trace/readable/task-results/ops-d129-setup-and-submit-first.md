# ops d129 setup and submit first

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d129-setup-and-submit-first_20260517T210847_result.json`
- **Structured JSON:** [`cfe52051029c51c93f18.json`](../../sessions/cf/cfe52051029c51c93f18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。

## 报告

1. **环境正常**
   - 模型: `/root/autodl-tmp/models/Qwen3-1.7B/` (3.8GB, 2 shards) ✓
   - 训练脚本: `train_grpo.py` ✓
   - 数据: `train_500_seed42.jsonl` (500 examples) ✓
   - Eval 脚本: `eval_sta.py`, `classify_h7.py` ✓
   - GPU: NVIDIA RTX PRO 6000 (98GB), cuda:0 空闲 → 现已占用 ✓
   - Python: conda base, Python 3.12, torch 2.10.0+cu128, trl 1.1.0 ✓
   - 磁盘: 61G 可用 ✓

2. **第一个实验成功提交** ✓
   - exp_id: `d129-1.7b-isr-b01-s43`
   - reward_mode: additive_bonus, β=0.1, seed=43, 500 steps

3. **PID: 14701**, tmux session: `d129-1.7b-isr-b01-s43`
   - 仅占用 cuda:0 (10970 MiB)，符合 C002/C005

4. **预估完成时间**: step 1-2 约 10-13s/it，500 steps ≈ 1.5-1.8 小时，预计 **~06:45 UTC** 完成。

---
