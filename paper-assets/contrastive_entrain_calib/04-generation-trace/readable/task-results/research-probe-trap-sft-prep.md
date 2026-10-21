# research probe trap sft prep

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_probe-trap-sft-prep_20260524T130927_result.json`
- **Structured JSON:** [`d5a028424f44e8047f9e.json`](../../sessions/d5/d5a028424f44e8047f9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。报告已保存到 `artifacts/exp008_sft_prep.md`。

**摘要**：

1. **SFT 脚本确认存在**：`/root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py`，使用标准 SFT loss + 可微 probe penalty，非 GRPO。

2. **Probe reward trap 条件满足**：probe 权重 frozen 但 hidden states 梯度不 detach → 模型可学习操纵 representations 来降低 S(t)。每 500 steps retrain probe。

3. **与 GRPO 关键差异**：SFT 版 probe 是可微 penalty（梯度直接回传），GRPO 版只是 binary reward signal。LoRA 配置也不同（SFT: alpha=128, 7模块 vs GRPO: alpha=64, 4模块）。

4. **需要的修改**：
   - LoRA alpha 128→64, modules 7→4（匹配 GRPO 公平对比）
   - `--max_steps 2000`（命令行已支持）
   - Seed 已参数化 ✓

5. **GPU 状态**：PID 553700 跑的是 exp003（非 exp008），无意外启动的 GRPO 训练。

---
