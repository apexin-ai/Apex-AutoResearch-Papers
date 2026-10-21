# code 008e dryrun prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_008e_dryrun_prep_20260514T040710_result.json`
- **Structured JSON:** [`cdb7566a8163703df438.json`](../../sessions/cd/cdb7566a8163703df438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码检查完成。

**结论：Ready for dryrun = True**

关键发现：
- `--gate_dt_embed_dim 0` 通过 argparse 正确解析为 `int(0)`
- `networks.py` 中 `nn.Embedding(8, 0)` 会被创建（因为 `max_dt > 1`），但输出为 `(batch, 0)` 的空张量
- `torch.cat` 拼接 0-dim 张量等价于 no-op，linear 层 input_dim 不受影响
- imagination 路径中 dt 仍被计算和传递，但 embedding 贡献为零

无需代码修改。唯一风险点是依赖 PyTorch 对 0-sized tensor 的支持（PyTorch 2.x 已完全支持）。非阻塞建议：未来可加 `and dt_embed_dim > 0` 守卫让意图更显式。

---
