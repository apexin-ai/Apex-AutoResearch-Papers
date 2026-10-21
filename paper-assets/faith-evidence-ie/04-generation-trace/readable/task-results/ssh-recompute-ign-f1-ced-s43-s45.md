# ssh recompute ign f1 ced s43 s45

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_recompute_ign_f1_ced_s43_s45_20260516T052547_result.json`
- **Structured JSON:** [`f8f3cd5645da7d6314a5.json`](../../sessions/f8/f8f3cd5645da7d6314a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。metrics_v2.json 已生成：

| 实验 | f1 | ign_f1 (v2) | delta |
|------|-----|-------------|-------|
| rsft_ced_s43 | 0.4601 | 0.4512 | -0.0089 |
| rsft_ced_s45 | 0.4514 | 0.4416 | -0.0098 |
| rsft_flat_nli_s44 | 0.4615 | 0.4521 | -0.0094 |
| rsft_flat_nli_s45 | 0.4551 | 0.4462 | -0.0089 |

CED s43/s45 值与 metrics.json 一致（本就正确）。flat-NLI s44/s45 已从 recompute 脚本获得正确的 ign_f1（低于 f1 约 0.9pp）。seed_comparison.py 现在可以正常读取这四个目录。

---
