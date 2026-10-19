# research plan019 eval 134 tasks

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan019-eval-134-tasks_20260517T175406_result.json`
- **Structured JSON:** [`896ea928cb7836bdd0f5.json`](../../sessions/89/896ea928cb7836bdd0f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息齐了。以下是结论：

---

## 调查结果

### 1. 当前 val task 加载机制

- `AlfworldSG` 的 `eval_dataset: "eval_in_distribution"` → AlfWorld 的 `valid_seen` split
- task 选择逻辑：`game_idx = seed % len(game_files)`
- es_manager 为 val 生成 seeds `[base_seed, base_seed+1, ..., base_seed + env_groups-1]`
- 当前 exp029 配置：`env_groups=32, group_size=1` → 只评估 32 个 tasks（从 140 个 valid_seen tasks 中取连续 32 个）

### 2. 数据 split 实际 task 数

| Split | 目录 | game files 数 |
|-------|------|--------------|
| valid_seen (eval_in_distribution) | `json_2.1.1/valid_seen` | **140** |
| valid_unseen (eval_out_of_distribution) | `json_2.1.1/valid_unseen` | **134** |

标准 ALFWorld 134-task eval 对应的是 **valid_unseen**（OOD split）。

### 3. 扩展所需改动

**纯 config 改动，不需要修改代码。** exp028c 已有先例（val env_groups=140）。

对于 134 tasks（valid_unseen）：
```yaml
# 方式 A: 改 envs.yaml 中 AlfworldSG 的 eval_dataset
env_config:
  eval_dataset: "eval_out_of_distribution"

# 方式 B: 或新建一个 tag（如 AlfworldSG_OOD）

# 然后在实验 config 中:
val:
  env_groups: 134
  group_size: 1
  env_configs:
    tags: ["AlfworldSG"]  # 或 AlfworldSG_OOD
    n_groups: [134]
```

对于 140 tasks（valid_seen，当前 split）：直接改 `env_groups: 140, n_groups: [140]`（同 exp028c）。

### 4. 风险评估

- **OOM 风险：低。** AlfWorld 是纯文本环境，134 个 env 实例内存开销极小。瓶颈在 vLLM 推理，与 env 数量无关（rollout 是串行/分批的）。
- **耗时影响：线性增长。** 32 → 134 tasks 约 4.2x 时间，32 → 140 约 4.4x。如果当前 32-task eval 耗时 T，full eval 约 4T~4.5T。
- **已验证可行：** exp028c 已配置 `env_groups: 140`，说明框架支持这个规模。
- **注意：** 如果要用标准 134-task（valid_unseen），需要改 `eval_dataset` 从 `"eval_in_distribution"` → `"eval_out_of_distribution"`，这改变了评估语义（从 seen 变 unseen），要确认这是否符合实验意图。

---
