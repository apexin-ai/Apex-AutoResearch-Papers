# collect gpu2 spatial physical

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_gpu2-spatial-physical_20260515T131742_result.json`
- **Structured JSON:** [`5ad543a237cabf955ca8.json`](../../sessions/5a/5ad543a237cabf955ca8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 0 数据收集（GPU 2）完成。

**产出汇总：**

| 扰动类型 | 文件 | Episodes | 大小 | label_6class | label_3class |
|----------|------|----------|------|-------------|-------------|
| objects_layout | `activations/objects_layout.pt` | 81 | 17M | 4 | 1 |
| robot_initial_states | `activations/robot_initial_states.pt` | 80 | 17M | 5 | 2 |

**注意事项：**
- objects_layout 有较高失败率（~50%，因部分 LIBERO-Plus 新物体 XML 资产文件缺失），通过增加总尝试次数补偿，最终收集到 81 个成功 episodes
- robot_initial_states 0 失败率，80/80 全部成功
- 两种类型均超过目标的 80 episodes

---
