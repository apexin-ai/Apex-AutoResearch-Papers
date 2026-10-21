# ssh root disk cleanup only

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_root_disk_cleanup_only_20260520T094958_result.json`
- **Structured JSON:** [`358a9650ee2addbe6d5f.json`](../../sessions/35/358a9650ee2addbe6d5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**A1 PID 185994**: 存活，运行 1h27m，step ~7421/30000 (25%)，loss ~0.26

**磁盘清理对比**:
| | Used | Avail | Use% |
|---|---|---|---|
| 清理前 | 16G | 15G | 53% |
| 清理后 | 15G | 16G | 50% |

**释放约 1G**，清理内容：
- HuggingFace datasets cache (`/root/.cache/huggingface/datasets/`) — 2.5G
- conda pkgs (`/root/miniconda3/pkgs/`) — 553M
- `/tmp/tmp4tc_1nbo` (临时 zip) — 58M
- torch/triton/pip cache — 已被上个 Worker 清过，本次 0

**后台运行中**: git gc 正在压缩 vlsa-aegis (.git 348M) 和 LIBERO (.git 214M)，完成后预计再释放 200-400M。

---
