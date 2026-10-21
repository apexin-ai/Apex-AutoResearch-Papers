# check attention viz status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_attention_viz_status_20260517T111707_result.json`
- **Structured JSON:** [`cf1d9ddf0ed4e2977deb.json`](../../sessions/cf/cf1d9ddf0ed4e2977deb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## attention_viz 状态：已完成

**tmux session**: `attention_viz` 已退出，GPU 0 空闲 (1 MiB)。

### 产出文件（全部生成于 18:34）

| 文件 | 大小 |
|------|------|
| `attention_data.npz` | 32.6 MB |
| `attention_heatmap.pdf` / `.png` | 137 KB / 406 KB |
| `attention_distribution.pdf` / `.png` | 27 KB / 192 KB |
| `attention_per_task.pdf` / `.png` | 24 KB / 51 KB |
| `attention_metadata.json` | 500 B |
| `attention_viz.log` | 3.2 KB |

### Metadata 摘要

- **Checkpoint**: `checkpoints/libero_full_ft_100k/checkpoint.pt`
- **Suite**: `libero_object`, tasks [0, 3, 7]
- **Attention captures**: 2400 samples, shape `[2400, 15, 128]` (15 heads, 128 tokens)
- **Overall entropy**: 6.86 / 7.0 (uniformity ratio **0.98**) — attention 分布接近均匀
- **Cam1 fraction**: 0.538 — 两个相机的 attention 近乎均分

---
