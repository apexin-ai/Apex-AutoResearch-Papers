# paper update framing negative blocks

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_update_framing_negative_blocks_20260525T091315.jsonl`
- **Structured JSON:** [`e7599825fa6de47ee6c6.json`](../../sessions/e7/e7599825fa6de47ee6c6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-25T09:14:46.362160+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update_framing_negative_blocks_20260525T091315",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T09:14:46.362507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update_framing_negative_blocks_20260525T091315",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T09:14:46.362742+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "diff_collision_sdf",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update_framing_negative_blocks_20260525T091315",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "diff_collision_sdf",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T09:14:46.363146+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级\\n\\n## Core Insight\\n\\n当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。\\n\\n## Working Title\\n\\n\\\"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models\\\"\\n\\n> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 \\\"all SDF methods\\\"，聚焦 metric contamination 这一更可防御的贡献\\n\\n## Core Claims\\n\\n### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)\\nCAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。\\\"Collision-free\\\" ≠ \\\"collision-avoiding\\\"。\\n\\n**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0\\n\\n**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标\\n\\n### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)\\n更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。\\n\\n**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)\\n\\n**限制**: 仅 2 个 model families, Pi0 的 \\\"高 CAR\\\" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。\\n\\n### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\n\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\n\\n**限制**: \\\"EE-only 不够\\\" 是 expected result; 缺乏 full-body SDF 对照\\n\\n### Cl
…[truncated 6792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update_framing_negative_blocks_20260525T091315",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T09:14:46.363486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update_framing_negative_blocks_20260525T091315",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T09:14:46.363817+00:00_

1	# ColliForce-VLA Paper Framing
2	
3	> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级
4	
5	## Core Insight
6	
7	当前 VLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 严重污染，导致 "安全" 指标虚高。我们通过大规模实证分析（39 个实验, 5000+ episodes）揭示三个相互关联的问题，并提出 displacement-filtered CAR 作为修正指标。
8	
9	## Working Title
10	
11	"The Safety Illusion: How Action Collapse Contaminates Collision Avoidance Metrics in Vision-Language-Action Models"
12	
13	> 注：Title scope 已按 Reviewer Report #26 建议收窄——不再 claim 覆盖 "all SDF methods"，聚焦 metric contamination 这一更可防御的贡献
14	
15	## Core Claims
16	
17	### Claim 1: Fake Safety (Primary — 证据强度 ★★★★★)
18	CAR 指标被 action collapse 严重污染。在 SafeLIBERO benchmark 上，A1 (SDF auxiliary loss) 的 91.5% CAR 中 99.6% 是 fake safe（robot displacement < 1μm）。"Collision-free" ≠ "collision-avoiding"。
19	
20	**证据**: 800 episodes A1 per-episode displacement 分析; 200 episodes baseline 对比; Pi0.5 56/56 safe episodes displacement ≈ 0
21	
22	**贡献**: 提出 displacement-filtered CAR (real_CAR) 作为修正指标
23	
24	### Claim 2: Task Capability vs Safety Anti-correlation (Secondary — 证据强度 ★★★)
25	更强的 base model 完成更多任务但碰撞更多。Pi0.5 (TSR=74.7%) vs Pi0 (TSR≈0%): 能力越强 → 运动越多 → 碰撞越多。
26	
27	**证据**: Pi0.5 3-seed eval (TSR=74.7±1.5%, CAR=26.8±1.6%) vs Pi0 baseline (TSR≈0%, CAR=82%)
28	
29	**限制**: 仅 2 个 model families, Pi0 的 "高 CAR" 来自 action collapse 而非安全。Reviewer 建议降级为 observation, 不 claim 因果关系。
30	
31	### Claim 3: EE-only SDF Structural Limitation (Supporting — 证据强度 ★★★★)
32	End-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。
33	
34	**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系
35	
36	**限制**: "EE-only 不够" 是 expected result; 缺乏 full-body SDF 对照
37	
38	### Claim 4: SDF Auxiliary Loss Effectiveness on Strong VLA (Pending — 取决于实验)
39	在能力充分的 VLA (Pi0.5) 上，SDF auxiliary training loss 能否产生真实的碰撞避免行为？
40	
41	**状态**: 3-seed × 2-lambda 训练中, 
…[truncated 6630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update_framing_negative_blocks_20260525T091315",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T09:14:46.364111+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md",
  "old_string": "## Negative Results Narrative Strategy (D018 + 16 negatives)\n\n16 个阴性结果按叙事功能分为 3 层：\n\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\n这些 negative 本身就是 paper 的 finding：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\n\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\n提供边界信息，但非核心贡献：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\n\n### Tier C: 省略（技术失败 / 与结论无关）\n不进入论文正文或 appendix：\n\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\n- 被 kill 的实验（资源调度，无结论）\n\n### 叙事原则\n1. Tier A 的 negative 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" 而非 \"we failed to\"\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\n4. Tier C 完全不提",
  "new_string": "## Negative Results Narrative (4 Blocks)\n\n> Director 批准的 4-block 叙事结构（替代原 7 段独立叙事），每个 block 对应一个独立论点，论文 §4-5 按此顺序展开。\n\n### Block 1: Fake Safety Revelation\n- **Evidence**: eval_a1_lora_object_v11_rerun (800 episodes)\n- **Key finding**: CAR=91.5% with 99.6% fake safe (displacement < 0.1mm)\n- **Narrative**: Standard CAR metric is systematically contaminated by action collapse — \"collision-free\" episodes are actually frozen robots, not collision-avoiding ones. Proposes displacement-filtered CAR (real_CAR) as corrective metric.\n- **Supports**: Claim 1 (Primary)\n\n### Block 2: Stronger Models ≠ Safer (merged)\n- **Evidence**: eval_pi05_safelibero_object_v11 + eval_pi05_safelibero_spatial_v11\n- **Key finding**: Pi0.5 CAR=28% (object), 13% (spatial), real_safe=0.5%\n- **Narrative**: Counter-intuitive — better task capability (TSR=74.7%) leads to more collisions, not fewer. Pi0's high CAR (82%) is fake safety from action collapse; Pi0.5 actually moves and collides. Capability↑ ≠ Safety↑.\n- **Supports**: Claim 2 (Secondary)\n\n### Block 3: Oracle Upper Bound (merged triplet)\n- **Evidence**: oracle_true_gt_adaptive_alpha_v11 + oracle_true_gt_fixed_alpha_v11 + oracle_true_gt_feature_v11\n- **Key finding**: All oracles CAR 73-77% < baseline 82-83%\n- **Narrative**: Unified answer to \"does a better alpha schedule or representation fix runtime refinement?\" — No. Three oracle variants (adaptive alpha, fixed alpha, feature-space SDF) all perform worse than baseline, because gradient correction structurally fails on collapsed policies regardless of alpha/representation choice. Eliminates hyperparameter tuning as escape route.\n- **Supports**: Claim 3 (Supporting)\n- **Presentation**: Single unified table with 3 oracle rows + baseline row\n\n### Block 4: EE-only Boundary Condition\n- **Evidence**: eval_a1_lora_spatial_v11\n- **Key finding**: CAR≈0% in spatial tasks, all 6 safe episodes are frozen (displacement ≈ 0)\n- **Narrative**: EE-only SDF cannot address arm-body collisions — in spatial tasks where collisions come from the arm body sweeping through obstacles, EE-based correction has zero effect. Defines the structural scope boundary of the method.\n- **Supports**: Claim 3 (Supporting, boundary condition)\n\n### 叙事原则\n1. 每个 block 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" / \"we find\" 而非 \"we failed to\"\n2. Block 3 的三个 oracle 合并为一段 + 一个表格，统一回答一个问题，避免重复叙事\n3. Block 间按逻辑递进排列：metric 有问题 (B1) → 强模型也不安全 (B2) → runtime 修正无法解决 (B3) → method scope 边界 (B4)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update_framing_negative_blocks_20260525T091315",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md",
    "old_string": "## Negative Results Narrative Strategy (D018 + 16 negatives)\n\n16 个阴性结果按叙事功能分为 3 层：\n\n### Tier A: 显式讨论（核心贡献，论文 §4-5 正文）\n这些 negative 本身就是 paper 的 finding：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| Fake safety 量化 | A1-openpi 800ep (99.6% fake) | Claim 1 主证据 |\n| EE-only oracle 失败 | 3× GT oracle (adaptive/fixed/feature) | Claim 3 主证据 |\n| Gradient correction 失败 | collapsed policy 不接受修正 (D018) | Claim 3 补充机制分析 |\n| Task 3 碰撞转移 | SDF gradient 导致碰撞重分布 (D017) | Claim 3 补充（structural limitation） |\n\n### Tier B: 简要讨论（Ablation / boundary condition，论文 §5 或 Appendix）\n提供边界信息，但非核心贡献：\n\n| 类别 | 实验 | 论文功能 |\n|------|------|----------|\n| TSR-CAR tradeoff | Pi0.5+A1 10K/30K TSR 下降 | Claim 4 tradeoff 定量（Table 1 已含） |\n| Lambda sensitivity | λ=0.005 vs 0.01 差异 | Figure 5 lambda 曲线的数据点 |\n\n### Tier C: 省略（技术失败 / 与结论无关）\n不进入论文正文或 appendix：\n\n- spatial_bowl 训练失败（磁盘满 / 代码 bug → 非科学结论）\n- A3 runtime refine 早期版本（被 oracle 实验 supersede）\n- 被 kill 的实验（资源调度，无结论）\n\n### 叙事原则\n1. Tier A 的 negative 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" 而非 \"we failed to\"\n2. 多个 Tier A negative 收敛到同一 root cause (EE-only limitation) 时，叙事集中在 insight 上，各实验作为不同角度的验证\n3. Tier B 以 1-2 句话出现在 results discussion 或 appendix，不展开\n4. Tier C 完全不提",
    "new_string": "## Negative Results Narrative (4 Blocks)\n\n> Director 批准的 4-block 叙事结构（替代原 7 段独立叙事），每个 block 对应一个独立论点，论文 §4-5 按此顺序展开。\n\n### Block 1: Fake Safety Revelation\n- **Evidence**: eval_a1_lora_object_v11_rerun (800 episodes)\n- **Key finding**: CAR=91.5% with 99.6% fake safe (displacement < 0.1mm)\n- **Narrative**: Standard CAR metric is systematically contaminated by action collapse — \"collision-free\" episodes are actually frozen robots, not collision-avoiding ones. Proposes displacement-filtered CAR (real_CAR) as corrective metric.\n- **Supports**: Claim 1 (Primary)\n\n### Block 2: Stronger Models ≠ Safer (merged)\n- **Evidence**: eval_pi05_safelibero_object_v11 + eval_pi05_safelibero_spatial_v11\n- **Key finding**: Pi0.5 CAR=28% (object), 13% (spatial), real_safe=0.5%\n- **Narrative**: Counter-intuitive — better task capability (TSR=74.7%) leads to more collisions, not fewer. Pi0's high CAR (82%) is fake safety from action collapse; Pi0.5 actually moves and collides. Capability↑ ≠ Safety↑.\n- **Supports**: Claim 2 (Secondary)\n\n### Block 3: Oracle Upper Bound (merged triplet)\n- **Evidence**: oracle_true_gt_adaptive_alpha_v11 + oracle_true_gt_fixed_alpha_v11 + oracle_true_gt_feature_v11\n- **Key finding**: All oracles CAR 73-77% < baseline 82-83%\n- **Narrative**: Unified answer to \"does a better alpha schedule or representation fix runtime refinement?\" — No. Three oracle variants (adaptive alpha, fixed alpha, feature-space SDF) all perform worse than baseline, because gradient correction structurally fails on collapsed policies regardless of alpha/representation choice. Eliminates hyperparameter tuning as escape route.\n- **Supports**: Claim 3 (Supporting)\n- **Presentation**: Single unified table with 3 oracle rows + baseline row\n\n### Block 4: EE-only Boundary Condition\n- **Evidence**: eval_a1_lora_spatial_v11\n- **Key finding**: CAR≈0% in spatial tasks, all 6 safe episodes are frozen (displacement ≈ 0)\n- **Narrative**: EE-only SDF cannot address arm-body collisions — in spatial tasks where collisions come from the arm body sweeping through obstacles, EE-based correction has zero effect. Defines the structural scope boundary of the method.\n- **Supports**: Claim 3 (Supporting, boundary condition)\n\n### 叙事原则\n1. 每个 block 不是\"失败\"，是 **evidence for structural claims** — 用 \"we demonstrate\" / \"we find\" 而非 \"we failed to\"\n2. Block 3 的三个 oracle 合并为一段 + 一个表格，统一回答一个问题，避免重复叙事\n3. Block 间按逻辑递进排列：metric 有问题 (B1) → 强模型也不安全 (B2) → runtime 修正无法解决 (B3) → method scope 边界 (B4)"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T09:14:46.364481+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update_framing_negative_blocks_20260525T091315",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T09:14:46.364720+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md",
  "old_string": "> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级",
  "new_string": "> 维护者: Director | 最后更新: 2026-05-25 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级 | Negative results 升级为 4-block 结构"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_update_framing_negative_blocks_20260525T091315",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md",
    "old_string": "> 维护者: Director | 最后更新: 2026-05-24 12:30 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级",
    "new_string": "> 维护者: Director | 最后更新: 2026-05-25 UTC | Reviewer 预审反馈：补 LoRA 中间场景叙事 + Claim 4 措辞升级 | Negative results 升级为 4-block 结构"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T09:14:46.364977+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_update_framing_negative_blocks_20260525T091315",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-25T09:14:46.365216+00:00_

已完成。paper_framing.md 的 negative results 部分从原来的 3-tier (A/B/C) 分层结构替换为 Director 批准的 4-block 叙事结构：

- **Block 1**: Fake Safety — 800ep action collapse 证据
- **Block 2**: Stronger ≠ Safer — Pi0.5 object+spatial 合并
- **Block 3**: Oracle Upper Bound — 三个 oracle 合并为一段+一表
- **Block 4**: EE-only Boundary — spatial CAR≈0% scope 边界

其他 section（Claims、Contingency Plans、Dependencies 等）未改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_update_framing_negative_blocks_20260525T091315"
}
```

</details>

---
