# deploy sync exp008 to westd28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_sync-exp008-to-westd28034_20260518T182251_result.json`
- **Structured JSON:** [`80211d8e571a25e6ee06.json`](../../sessions/80/80211d8e571a25e6ee06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**同步结果：**

| 文件 | md5sum (本地=远程) | 状态 |
|------|-------------------|------|
| `run_exp008_binary_probe_penalty.py` | `43fc178c3e8b95eba32c63a207ecc2f1` | 一致 |
| `probe_module.py` | `3f92ce6b6ba023d971553f477a41c123` | 一致 |

**验证结果：**
- Probe import: `feat_mean shape: torch.Size([4096])`, `feat_std shape: torch.Size([4096])` — OK
- 数据文件: `calibration_v2_1_expanded.jsonl` (367KB) — 存在
- Activations: `activations.pt` (407MB) — 存在

westd-28034 上代码和数据已就绪，可以启动 exp-008 训练。

---
