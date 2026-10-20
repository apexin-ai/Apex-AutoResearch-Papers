# research subtask predicate feasibility

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_subtask-predicate-feasibility_20260515T135307_result.json`
- **Structured JSON:** [`23e4ea16b3cfb9cb1f4d.json`](../../sessions/23/23e4ea16b3cfb9cb1f4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有调查完成。以下是结论。

---

## 调研结果

### Q1: HDF5 demo 文件中是否有 subtask predicate labels？

**没有。** HDF5 只包含：`actions(T,7)`, `dones`, `obs/{agentview_rgb, ee_ori, ee_pos, ee_states, eye_in_hand_rgb, gripper_states, joint_states}`, `rewards`, `robot_states(T,9)`, `states(T,47)`。无任何 predicate/subtask/goal 字段。

**但 `states(T,47)` 包含完整 MuJoCo 模拟器状态**（含物体位姿），且 `extract_subtask_labels.py` 已实现从中自动提取 subtask 完成标签。`subtask_labels.json` 已生成，覆盖全部 10 个 task、50 trajs/task、2 predicates（subtask_0, subtask_1）。

### Q2: BDDL predicate API / 重新标注工作量

服务器上 **libero 和 bddl 均未安装**，只有 robosuite。要获取真正的 BDDL predicates 需要：
1. 安装 libero + bddl
2. 编写 replay 脚本：加载 MuJoCo states → `mj_forward()` → 评估 BDDL predicates
3. 估算工作量：~1-2 天（含 debug）

**但这不是瓶颈。** 瓶颈在下面 Q3 后的分析。

### Q3: 已提取 hidden states 能否直接复用？

**能。** 三组特征齐全：
- `features/trained/` — 10 tasks × 50 trajs, `(T, 33, 4096)` per traj
- `features/untrained/` — 同上
- `features/dinov2/` — 10 tasks × 50 trajs, `(T, 1024)` per traj

`train_probes.py` 已支持 `--probe_type subtask_predicate --label_file`，含完整的 `train_classification_probe` + `run_subtask_predicate` + per-layer AUC 计算。

**发现一个 key 映射 bug**：VLA 特征用 `demo_X` 键名，标签用 `traj_X` 键名。`run_subtask_predicate` 在 VLA 特征上会因为 key 不匹配跳过所有数据。修复只需一行 key 转换。

---

### 关键分析：auto-extracted labels vs BDDL predicates

| 维度 | Auto-extracted（现有） | BDDL predicates |
|------|----------------------|-----------------|
| 方法 | 检测 MuJoCo state 维度的阶跃变化 | 语义谓词评估 |
| 示例 | "旋钮转角变化 > 80%" | `stove_is_on(stove)` |
| 粒度 | 2 subtasks (early/late cluster) | 多个谓词（is_grasped, is_on, is_in 等） |
| 本质 | **物理状态是否发生了视觉可见的变化** | **语义目标是否满足** |

**DINO-V2 在 auto-extracted labels 上 AUC=0.9717 的原因**：auto-extracted labels 检测的是物理状态突变点——物体位置/姿态的大幅变化。这些变化在相机视角下清晰可见。DINO 作为强视觉编码器天然擅长检测这类视觉变化。

**核心问题：即使换成 BDDL predicates，DINO 仍可能得高分。** 因为：
- `is_grasped(obj)` → 夹爪闭合+物体位移，视觉可辨
- `is_on_table(obj)` → 物体是否在桌面上，视觉可辨
- `is_in_drawer(obj)` → 物体是否在抽屉内，视觉可辨

在 LIBERO 的第三人称+手腕相机 128×128 设置下，**几乎所有 task-relevant predicates 都可以从视觉直接判断**。不需要理解动作语义——你看得到它在发生。

### 与已有 baseline (0.9717) 的关系

已有 DINO-V2 subtask AUC=0.9717 **就是用 auto-extracted labels 算的**（`subtask_auc_dinov2.py` + `subtask_labels.json`）。Auto-extracted labels 和 BDDL predicates 不等价，但在检测 subtask completion 这个粒度上近似等价——两者都标记"subtask 什么时候完成了"。

---

### 实施方案

**Option A：最小代价验证（~2小时）**
1. 修复 `train_probes.py` 的 key mismatch bug（`demo_X` → `traj_X` 映射）
2. 对 trained 和 untrained 分别运行 `--probe_type subtask_predicate`
3. 比较 trained vs untrained vs DINO-V2 的 macro_AUC

**预期结果**：trained 和 untrained VLA 的 AUC 都会很高（因为 SigLIP vision encoder 比 DINO 更强），且 Δ(trained - untrained) 很小——与 temporal distance 结论一致。

**Option B：真 BDDL predicates（~1-2天）**
额外安装 libero+bddl，写 replay 标注脚本，生成更细粒度的 predicate labels。

### 可行性评估

**Pivot 到 subtask predicate 不能解决根本问题。** 

根本问题是：在 LIBERO 的 tabletop manipulation 场景中，所有 task-relevant 状态都可以从视觉直接判断。无论用 temporal distance 还是 subtask completion，vision encoder 都足以解决，LLM 训练贡献不出差异。

要找到 VLA LLM 训练真正有贡献的 probing task，需要的是 **视觉不可达的信息**，例如：
- 未来 action 预测（给定当前状态，下一步做什么——需要策略知识）
- 跨 task 泛化（在从未见过的 task 上 zero-shot 表现——需要 language grounding）
- 因果推理（改变一个 subtask 的执行顺序会不会影响结果——需要 task 结构理解）

**建议**：先跑 Option A 确认（2小时），如果 Δ 确实很小，则这条 pivot 路径应放弃，转向 action prediction probe 或 cross-task transfer probe。

---
