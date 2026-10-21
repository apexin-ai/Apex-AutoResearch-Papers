# diag figure sync verify

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_figure_sync_verify_20260518T194637_result.json`
- **Structured JSON:** [`cc4d6044b047d8aca202.json`](../../sessions/cc/cc4d6044b047d8aca202.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

远程服务器上不存在 `docs/paper/figures/` 目录，也没有任何 `degradation` 相关文件。远程没有更新版本可同步。

## 结果汇总

| 文件 | 大小 | 存在 | 最新状态 |
|------|------|------|----------|
| fig_degradation_curve.pdf | 30,258 B | ✓ | 远程无更新版本，本地即为最新 |
| fig_compression_curve.pdf | 30,955 B | ✓ | 最新 |
| fig_architecture.pdf | 30,361 B | ✓ | 最新 |
| fig_pixel_shuffle.pdf | 30,648 B | ✓ | 最新 |
| fig_entropy_layers.pdf | 28,917 B | ✓ | 最新 |

额外存在 3 个文件：`fig_action_divergence.pdf` (38KB)、`fig_attention_heatmap.pdf` (34KB)、`fig_cliff_edge.pdf` (34KB)。

远程服务器 `westd-27271` 上 `/root/autodl-tmp/importance_margin_vla_compress/` 下没有 `docs/` 目录，也没有任何 degradation_curve 文件。任务提到的 `cqa1-33015` 服务器不在当前项目配置中。如果需要从 `cqa1-33015` 同步，需要确认该服务器是否已配置。

---
