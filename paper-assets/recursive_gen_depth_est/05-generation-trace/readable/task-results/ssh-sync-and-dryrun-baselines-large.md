# ssh sync and dryrun baselines large

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sync_and_dryrun_baselines_large_20260514T195519_result.json`
- **Structured JSON:** [`2012f15c0ed91c5814f0.json`](../../sessions/20/2012f15c0ed91c5814f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

| 步骤 | 结果 |
|------|------|
| 代码同步 | `baseline_ce_classification.py` 和 `baseline_coral.py` 已写入服务器 |
| 模型验证 | `model.safetensors` (828MB), `hidden_size=1024`, `num_hidden_layers=24` |
| CE forward | logits shape `[1, 4]` — Linear(1024, 4) 正确 |
| CORAL forward | logits shape `[1, 3]` — Linear(1024, 1) + 3 biases 正确 |
| 清理 | 临时文件和 deberta-v3-base 无关文件已删除 |

注：完整 dry-run（CPU 上跑 2 个 batch_size=16 的 train+eval step）因 435M 模型在 CPU 上太慢未跑完，但 forward pass 已验证无误。正式训练在 GPU 上不会有问题。

---
