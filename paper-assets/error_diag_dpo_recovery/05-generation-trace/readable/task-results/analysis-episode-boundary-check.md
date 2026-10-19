# analysis episode boundary check

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_episode-boundary-check_20260512T151333_result.json`
- **Structured JSON:** [`71ed54ac40b83ab4e567.json`](../../sessions/71/71ed54ac40b83ab4e567.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here are the definitive findings:

---

## 结论

### 1. Episode 边界有问题吗？ — **否**

`collect_trajectories.py` 的 episode 逻辑正确：
- `env.reset()` 每次返回独立任务
- 一条 trajectory = 一个 episode
- `done` 信号来自 `env.step()` 返回的 `env_done[0]`，终止条件是 `done or reward`
- 不存在"一个 episode 包含多个子任务"的情况

### 2. failure_step=5 集中的真正原因 — **classify_errors.py 的 `format_trajectory()` BUG**

**根因：ICL 示例被当作模型实际动作计入了 step 编号。**

每条 trajectory 的 conversation 结构：

| 消息索引 | 内容 | format_trajectory 中的角色 |
|---------|------|--------------------------|
| msg[0] | instruction | 跳过 |
| msg[1] | "OK" | 跳过 |
| msg[2-11] | **ICL 示例**（5轮对话） | **被计为 Step 1-5** |
| msg[12] | **实际任务 obs**（env.reset()） | task obs |
| msg[13+] | **模型真实交互** | Step 6-45 |

两个 bug：
1. **task_desc 取错**：`format_trajectory` 取第一个含 "Your task is to:" 的消息（msg[2] = ICL），所以 classifier 看到的任务永远是 "put a toiletpaper in toiletpaperhanger"，而非实际任务
2. **step 编号偏移 5**：ICL 的 5 个 assistant 回复被计为 Step 1-5，模型真实动作从 Step 6 开始

LLM classifier 看到的画面：
- 任务："put toiletpaper on hanger"
- Step 1-5：完美完成了 toiletpaper 任务（其实是 ICL 示例）
- Step 5 之后观察突变为完全不同的房间（实际任务环境）
- Step 6+：模型做不相关的事

→ Classifier 自然把 **Step 5 标记为 failure point**（"agent completed one task then started an unrelated one"）

### 3. 交叉验证证据

实际 env 交互完全正常。以 task_id=0 为例：
- game_file: `pick_clean_then_place-Spoon-DiningTable`
- 实际任务: "put a clean spoon in diningtable"
- 模型真实 Step 1（msg[13]）: `go to sinkbasin 1` → **合理** — 找 spoon 去洗
- 模型真实 Step 2: `go to countertop 1` → 继续搜索
- 然后花 40 步搜索但未完成任务

**ALL 88 failed trajectories 的 "前5步相同" 是因为它们共享同一个 ICL 示例**，不是模型行为问题。

### 4. 分类数据可用性

| 分组 | 数量 | 有效性 |
|------|------|--------|
| failure_step=5 | 76/88 | **全部无效** — 检测的是 ICL→实际的边界 |
| failure_step<5 (1,3) | 3/88 | **无效** — 指向 ICL 内部步骤 |
| failure_step>5 | 9/88 | **可能有效** — 但 task_desc 仍是 ICL 任务，质量存疑 |

### 5. 修复建议

**最小修复（不需要重新收集轨迹）：修改 `classify_errors.py` 的 `format_trajectory`**

```python
def format_trajectory(traj: dict) -> str:
    convs = traj["conversations"]
    # Skip ICL: first 12 messages (instruction + OK + 10 ICL turns)
    convs = convs[12:]  
    
    # Use the FIRST message (actual task obs) as task_desc
    task_desc = convs[0]["content"] if convs else "(no task)"
    ...
```

然后重新跑分类即可。轨迹本身没问题，只是分类器的输入预处理有 bug。

---
