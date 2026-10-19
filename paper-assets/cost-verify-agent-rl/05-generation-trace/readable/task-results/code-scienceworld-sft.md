# code scienceworld sft

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld_sft_20260519T143540_result.json`
- **Structured JSON:** [`acef01f98f5f74b83205.json`](../../sessions/ac/acef01f98f5f74b83205.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ScienceWorld SFT 训练已成功启动。

**总结：**
- **模型**: Qwen3-1.7B（与 ALFWorld SFT 一致），从 ModelScope 下载到 westd
- **数据**: JSONL → Parquet 转换，3592 train / 1796 val，添加 `enable_thinking=False` 列
- **配置**: FSDP2 × 4 GPU, LR=5e-6, 2 epochs, batch=16, max_length=16384 + left truncation
- **代码修改**: `fsdp_sft_trainer.py` 将硬编码 `flash_attention_2` 改为可配置（默认 `sdpa`），兼容 Blackwell GPU
- **运行状态**: GPU 100% 利用率, 47GB/96GB 显存, ~19s/step, 初始 loss ~0.6
- **预计完成**: ~2.4 小时
- **W&B**: Run `dqoxg94e`, 项目 `cost-verify-agent-rl`
- **Checkpoint 输出**: `/root/autodl-tmp/checkpoints/scienceworld_sft/`

---
