# research failure diagnosis v5

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_failure_diagnosis_v5_20260512T190111_result.json`
- **Structured JSON:** [`970d4e7410a124d5c730.json`](../../sessions/97/970d4e7410a124d5c730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。下面是完整诊断结果。

---

## V5 失败轨迹诊断报告

**数据规模**: 177 条失败 / 280 条总轨迹 (63.2% 失败率)

### 关键发现

**所有失败都耗尽 40 步上限**，没有提前退出的情况。每条轨迹包含 4 个 episode（前 3 个是固定热身任务，第 4 个是实际测试任务）。

### 一、四类失败模式分布

| 模式 | 数量 | 占比 | 说明 |
|------|------|------|------|
| **Exhaustive search** (20+ go to) | 117 | 66.1% | 逐个遍历 receptacle 找物品，步数耗尽 |
| **Loop behavior** (3+ 连续重复) | 86 | 48.6% | 多数是重复 "finish"/"exit" |
| **Parse failure** (3+ Nothing happens) | 82 | 46.3% | 输出无效 action |
| **Completion signal failure** | 59 | 33.3% | 完成任务后无法终止 |
| 任一类别命中 | 175 | **98.9%** | |
| 未分类 | 2 | 1.1% | |

**重叠严重**：parse+loop=69, finish+parse=54, finish+loop=52。根因链条：模型尝试 `finish` → 环境返回 "Nothing happens"（parse failure）→ 重复尝试（loop）。

### 二、"Nothing happens" 的真正原因

导致 "Nothing happens" 的 top actions：

| 次数 | Action | 性质 |
|------|--------|------|
| **762** | `finish` | 完成信号（非法 action） |
| 86 | `exit` | 完成信号 |
| 66 | `Nothing to do.` | 无效格式 |
| 61 | `done` | 完成信号 |
| 33 | `None` | 无效格式 |
| 29 | `None needed. Task completed.` | 完成信号 |
| 28 | `end` | 完成信号 |
| 25 | `put towel 1 in/on toilet 1` | 合法格式但对象错误 |

**762 次 `finish`** 是最大的失败源。模型完成了任务但不知道如何终止，反复输出无效的终止命令。

### 三、按 task_type 的分布

| Task Type | N | Parse | Loop | Exhaust | Finish |
|-----------|---|-------|------|---------|--------|
| pick_cool_then_place | 45 | 62% | **69%** | 47% | **69%** |
| pick_two_obj | 32 | 56% | 47% | 66% | 34% |
| pick_clean_then_place | 38 | 50% | 45% | 74% | 26% |
| pick_heat_then_place | 42 | 26% | 33% | 71% | 12% |
| pick_and_place | 18 | 22% | 39% | **94%** | 6% |

- **pick_cool_then_place** 最难：69% loop + 69% finish signal，模型完成 cool 后困在终止循环
- **pick_and_place** 几乎纯搜索问题：94% 穷举搜索，模型知道怎么做但找不到物品

### 四、样本定性分析

1. **EXHAUST ONLY** (uid=cuda0_0, pick_clean_then_place): 任务 "put a clean spoon in diningtable"，50 个 action 中 44 个 unique，模型逐一检查 cabinet 1→10、countertop 1→2、sinkbasin，始终没找到 spoon。**探索策略低效但 action 格式正确**。

2. **FINISH SIGNAL** (uid=cuda0_3, pick_heat_then_place): 任务 "heat some tomato and put it in sidetable"，最后 3 个 action 全是 `finish`。模型完成了任务但 **action space 中没有终止命令**。

3. **PARSE HEAVY** (uid=cuda0_13, pick_clean_then_place): 任务 "clean some egg and put it in microwave"，20 次 Nothing happens，最后 3 个 action 是 `Nothing to do.`。模型 **放弃并输出自然语言而非合法 action**。

### 五、Taxonomy 建议

原始三类划分（parse / loop / logic）不足以覆盖实际失败模式。建议修订为：

| 类别 | 性质 | 是否根因 |
|------|------|----------|
| **Completion signal failure** | Action space 设计缺陷，模型无法终止 | **根因** |
| **Exploration inefficiency** | 逐一遍历 receptacle，策略低效 | **根因** |
| **Invalid action format** | 输出 "Nothing to do" 等非法 action（排除 finish 类） | **根因** |
| **Action loop** | 重复 action，多数是 finish loop 的症状 | 症状 |

核心结论：**`finish` 信号缺失是 v5 最大的单一失败源（762 次触发）**。如果在 action space 中加入合法终止动作，或在 episode 切换时自动 reset，可能消除约 1/3 的失败轨迹。

---
