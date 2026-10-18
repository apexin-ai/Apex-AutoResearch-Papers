# research maven data prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_maven_data_prep_20260515T050740_result.json`
- **Structured JSON:** [`69f963f5e16b581ec4fb.json`](../../sessions/69/69f963f5e16b581ec4fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

## exp-004 MAVEN 数据准备 + BCS 计算 — 完成

### 产出文件��cqa1-38874）
| 文件 | 说明 |
|------|------|
| `data/maven_scs_matrix.json` | 168×168 SCS 完整矩阵 + 统计 + top-20 pairs |
| `data/maven_sim_matrix.pt` | PyTorch 格式，兼容 `compute_bcs.py` |
| `configs/maven_event_types.json` | 168 个事件类型名列表 |
| `src/compute_maven_scs.py` | 可复现的计算脚本 |

### 核心结果

**MAVEN SCS 分布** (all-MiniLM-L6-v2, type-name-only):
- mean=0.216, std=0.103, max=0.837
- 119 pairs (0.8%) 超过 SCS 0.5

**Top-5 confusable pairs**:
1. Commerce_buy ↔ Commerce_sell (0.84)
2. Choosing ↔ Deciding (0.82)
3. Motion ↔ Self_motion (0.79)
4. Death ↔ Killing (0.74)
5. Motion ↔ Motion_directional (0.73)

**与 Few-NERD 对比**（同模型公平对比）:
- MAVEN confusability 更稀疏（0.8% vs 5.3% pairs > 0.5）
- 但绝对数量相当（119 vs 114 pairs），因为 type space 大 6.5 倍
- 两者 max SCS 接近（0.84 vs 0.86），说明 confusability 机制可跨任务泛化

**实验设计适配性**：MAVEN 的稀疏 SCS + 明确 confusable 簇（Commerce/Motion/Crime）为 extreme batch 构造提供了理想条件。

---
