# infra install tmux and run

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_install-tmux-and-run_20260522T013502_result.json`
- **Structured JSON:** [`80ac0d167220c0da033b.json`](../../sessions/80/80ac0d167220c0da033b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本启动后立即报错：`ConnectionError: Couldn't reach 'cais/mmlu' on the Hub (OfflineModeIsEnabled)`

设置了 `HF_DATASETS_OFFLINE=1` 但本地没有缓存 `cais/mmlu` 数据集，导致无法加载。

**需要解决**：要么去掉 offline 模式先下载数据集，要么确认数据集已缓存在本地的路径。需要你决定下一步：
1. 去掉 `HF_DATASETS_OFFLINE=1` 和 `HF_HUB_OFFLINE=1`，让脚本联网下载
2. 检查本地是否有已缓存的数据集，修改代码加载路径

---
