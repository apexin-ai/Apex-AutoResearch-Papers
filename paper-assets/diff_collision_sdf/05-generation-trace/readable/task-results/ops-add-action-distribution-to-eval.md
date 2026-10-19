# ops add action distribution to eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_add_action_distribution_to_eval_20260523T021853_result.json`
- **Structured JSON:** [`e4faac4de834fb791c34.json`](../../sessions/e4/e4faac4de834fb791c34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`save_project_file` 对 artifacts 目录无写权限，但本地文件已通过 Edit 工具直接更新。

完成总结：

**eval 脚本修改（westd-45947 + westd-35807 均已部署）**：
- **L160-161**: episode 开始时初始化 `action_norms=[]`, `action_vectors=[]`
- **L192-194**: 每个 timestep 获取 action 后，记录 L2 norm 和原始 vector
- **L243-246**: per-episode result dict 新增 4 个字段：`mean_action_magnitude`, `std_action_magnitude`, `mean_action_variance`, `action_count`
- **L289-291**: per-task summary 新增 3 个聚合字段
- **L432-434**: overall output 新增 3 个聚合字段

**分析脚本修改（本地 artifacts/analyze_d012_results.py）**：
- 新增 `extract_action_stats()` 函数
- 新增 ACTION DISTRIBUTION ANALYSIS 段：per-model action 统计表、pairwise KS test（p>0.05 标记 "SDF not affecting actions"）、per-lambda 聚合
- 自动处理 baseline 无 action 数据的情况（提示需用新版 eval 重跑）

---
