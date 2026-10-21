# code prepare h10 and adv analysis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_h10_and_adv_analysis_20260518T001231_result.json`
- **Structured JSON:** [`34652a9e7a85b17d9235.json`](../../sessions/34/34652a9e7a85b17d9235.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个子任务验证结果：

---

**子任务 1: ADV 数据路径** ✅

| 项目 | 值 |
|------|------|
| 路径 | `/root/runs/cost-verify-agent-rl/hsweep_h2_seed2/advantage_log.jsonl` |
| 大小 | 255,872 bytes, 2200 行 |
| 最后修改 | 2026-05-18 07:18 (仍在写入中) |
| 样本 | `{"episode_id": 89, "window_position": 0, "step_return": -0.106, "advantage": 0.00141, "uid": "11"}` |

数据格式与 `analyze_advantage_log_v2.py` 期望的字段完全吻合（episode_id, window_position, step_return, advantage）。

---

**子任务 2: analyze_advantage_log_v2.py** ✅

- 远程已存在：`/root/cost-verify-agent-rl/scripts/analyze_advantage_log_v2.py`
- 脚本默认输入路径 `DEFAULT_LOG` = `/root/runs/cost-verify-agent-rl/hsweep_h2_seed2/advantage_log.jsonl` — 与实际数据路径完全一致
- 无需同步，直接可用：`python /root/cost-verify-agent-rl/scripts/analyze_advantage_log_v2.py`

---

**子任务 3: hsweep_h10 配置** ✅

文件已存在：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_hsweep_h10.yaml`

关键参数：
- `step_independent_history_length: 10`（h=10）
- `context_window_mode: "step_independent"`
- `total_training_steps: 15`
- `CUDA_VISIBLE_DEVICES: "0,1"`（bjb1-17606 白名单内）
- `experiment_name: hsweep-h10`
- `checkpoint_dir: /root/autodl-tmp/checkpoints/hsweep-h10/`
- `val: 32 env_groups`（满足 C003 ≥16 episodes）

---

**结论：所有依赖就绪。** hsweep_h2_seed2 完成后可直接：
1. 运行分析：`python /root/cost-verify-agent-rl/scripts/analyze_advantage_log_v2.py`
2. 启动 h10：使用 `_alfworld_hsweep_h10.yaml` 配置（pre-flight checklist 需在启动前执行）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "episode_id": 89,
    "window_position": 0,
    "step_return": -0.106,
    "advantage": 0.00141,
    "uid": "11"
  }
}
```

</details>

---
