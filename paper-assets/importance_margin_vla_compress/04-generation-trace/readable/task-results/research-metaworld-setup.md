# research metaworld setup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_metaworld_setup_20260524T154215_result.json`
- **Structured JSON:** [`a18aa3c728bb39bae4a9.json`](../../sessions/a1/a18aa3c728bb39bae4a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**调研结论**：
- MetaWorld 3.0.0 已安装在 westd-27271，验证通过
- OpenVLA 和 π0.5 都**没有** MetaWorld 实验，SmolVLA 有（0.45B 平均 57.3%）
- 无人做过 MetaWorld token pruning → 新颖贡献点
- HuggingFace 上有社区 checkpoint `jadechoghari/smolvla_metaworld`

**已产出**：
1. **`eval_smolvla_pruning_metaworld.py`** — 490 行，已验证环境部分，支持 4 种 pruning mode
2. **`metaworld_feasibility.md`** — 完整可行性报告

**下一步**：下载 `jadechoghari/smolvla_metaworld` checkpoint → 跑 baseline 验证端到端 pipeline → 启动 pruning sweep。

---
