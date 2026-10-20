# ops scp checkpoints to 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp_checkpoints_to_10894_20260525T031026_result.json`
- **Structured JSON:** [`3ceb372bac6b4eaf02f7.json`](../../sessions/3c/3ceb372bac6b4eaf02f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

传输完成，验证通过。

**结果汇总：**

| Checkpoint | 大小 | 状态 |
|---|---|---|
| vanilla_retrain_s0 / 50000_chkpt | 15G | ✓ 传输成功 |
| full_occ_retrain_s0 / 50000_chkpt | 15G | ✓ 传输成功 |

- 传输速度：~307-315 MB/s（服务器间直连 rsync）
- 10894 剩余磁盘：50G / 250G（81% 已用）
- 文件完整性：两个 checkpoint 均包含完整文件（4 个 model safetensors + action_head + lora_adapter + tokenizer 等）
- full_occ_retrain_s0 额外包含 `occ_head--50000_checkpoint.pt`，符合预期

现在 10894 上已有全部 4 个 same-seed checkpoint，可以开始梯度分析。

---
