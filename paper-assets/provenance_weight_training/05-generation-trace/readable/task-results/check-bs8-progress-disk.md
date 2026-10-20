# check bs8 progress disk

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bs8_progress_disk_20260523T201817_result.json`
- **Structured JSON:** [`e2ac00f54a1e3ae93239.json`](../../sessions/e2/e2ac00f54a1e3ae93239.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
| GPU | Utilization | Memory |
|-----|------------|--------|
| 0 | 100% | 92098/97887 MiB |
| 1 | 0% | 0/97887 MiB |
| 2 | 100% | 92066/97887 MiB |
| 3 | 0% | 0/97887 MiB |

## B=8 训练进度
- **bs8_nmin4_adaptive_seed456_r2** (cuda:0): step 4801/6103 (78.7%), 剩余 ~1h53m
- **bs8_nmin4_uniform_seed456_r2** (cuda:2): step 4946/6103 (81.0%), 剩余 ~1h45m

Uniform 比 Adaptive 快约 145 步。两个任务均正常运行，GPU 满载。

## 磁盘
/root/autodl-tmp: 82% used, 46G available

结论: 空间充足。aeff_only_nmin1_seed456 训练约需 5-10GB，剩余 46GB 完全够用。

---
