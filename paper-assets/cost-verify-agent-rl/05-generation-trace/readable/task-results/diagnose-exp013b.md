# diagnose exp013b

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp013b_20260514T082633_result.json`
- **Structured JSON:** [`9889303c5f066a5356ac.json`](../../sessions/98/9889303c5f066a5356ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总：

**时间线**：
- 16:18:28 — Ray session 启动
- 16:19:21 — 模型加载完成
- ~16:20-16:22 — Validation 完成（108s，140 games，group_size=1）
- ~16:22-16:24 — Training step 6 rollout 开始（8 env_groups × 16 group_size = 128 并发 ALFWorld 游戏）
- 16:24:14 — Plasma object store 崩溃（store.cc EOF），级联杀死 TaskRunner

**关键发现**：
- **容器 cgroup 内存限制 220GB**（`free -h` 显示的 1TB 是宿主机内存）
- `memory.events` 中 `oom_kill=0`：不是 cgroup OOM killer，而是 plasma store **分配失败**（mmap 返回 ENOMEM）后自行崩溃
- Worker .out 日志在打印 validation metrics 后戛然而止——无 Python 异常，确认是外部杀死
- exp012（AlfworldSG）vs exp013b（AlfworldSG_Dense）唯一差异是 env tag，密集奖励需要额外 per-step 状态追踪（`valid_action_bonus: 0.15`），128 并发实例下内存放大
- 今天有 8 个 Ray session，当前已无残留进程

```json
{"root_cause":"Plasma object store crashed (store.cc:365 connection error code 2: End of file) during training step 6 rollout generation with 128 concurrent ALFWorld Dense environments. Container cgroup memory limit is 220GB (not 1TB), and the rollout phase exceeded available memory causing mmap ENOMEM, not kernel OOM kill (oom_kill=0).","error_type":"resource","fix_steps":["减少 env_groups 从 8 到 4（64 并发游戏），或 group_size 从 16 到 8","启动前执行 ray stop --force 清理残留 session","在 config 中设置 RAY_object_store_memory 限制（如 30GB）避免 plasma 抢占过多内存","考虑设置 param_offload: True 或 optimizer_offload: True 将部分 FSDP 状态卸载到 CPU/NVMe"],"can_auto_fix":true,"memory_details":"cgroup limit=220GB, current_usage=130GB(post-crash), Ray detected memory=164GB + object_store=70GB(~234GB>220GB limit), GPU=2×RTX PRO 6000 96GB(0MB used now), disk: /=25% /autodl-tmp=54%"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "Plasma object store crashed (store.cc:365 connection error code 2: End of file) during training step 6 rollout generation with 128 concurrent ALFWorld Dense environments. Container cgroup memory limit is 220GB (not 1TB), and the rollout phase exceeded available memory causing mmap ENOMEM, not kernel OOM kill (oom_kill=0).",
    "error_type": "resource",
    "fix_steps": [
      "减少 env_groups 从 8 到 4（64 并发游戏），或 group_size 从 16 到 8",
      "启动前执行 ray stop --force 清理残留 session",
      "在 config 中设置 RAY_object_store_memory 限制（如 30GB）避免 plasma 抢占过多内存",
      "考虑设置 param_offload: True 或 optimizer_offload: True 将部分 FSDP 状态卸载到 CPU/NVMe"
    ],
    "can_auto_fix": true,
    "memory_details": "cgroup limit=220GB, current_usage=130GB(post-crash), Ray detected memory=164GB + object_store=70GB(~234GB>220GB limit), GPU=2×RTX PRO 6000 96GB(0MB used now), disk: /=25% /autodl-tmp=54%"
  }
}
```

</details>

---
