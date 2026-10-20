# ops persist ood and check aeff

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_persist_ood_and_check_aeff_20260523T231028_result.json`
- **Structured JSON:** [`c7a61711f15945e1c53a.json`](../../sessions/c7/c7a61711f15945e1c53a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 持久化

已复制全部 `/tmp/eval_bs8_*` 文件（log + json）到 `/root/provenance_weight_training/logs/`。确认 seed456 文件已持久化：

| 文件 | 大小 |
|------|------|
| `eval_bs8_adaptive_seed456.json` | 284B |
| `eval_bs8_adaptive_seed456.log` | 1406B |
| `eval_bs8_uniform_seed456.json` | 282B |
| `eval_bs8_uniform_seed456.log` | 1402B |

同时复制了 OOD 文件（owt/wiki 的 adaptive/uniform 各 log+json 共 8 个文件）。

## aeff_only 进度

- **step 3475/6103 (56.9%)**, ~2.98s/it
- ETA: 约 **2h10m** → 预计 **~09:00 UTC** 完成
- GPU 1 占用 100%，45643 MiB 显存，其余 GPU 空闲

---
