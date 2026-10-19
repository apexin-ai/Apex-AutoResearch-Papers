# cron hook eval obs only object norm01 seed74

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 2
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/cron_hook_eval-obs-only-object-norm01-seed74.jsonl`
- **Structured JSON:** [`43987f0394e7cd4f11fc.json`](../../sessions/43/43987f0394e7cd4f11fc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

2 recorded events

### User

_source line 1 · 2026-05-21T19:30:12.967926+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #24。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单 17 张：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5。白名单外严禁启动
- CoRL 2026 DDL **2026-05-29**，剩余 ≤8 天。π0.5 CRM 是最后一个关键实验，完不成论文缺 cross-VLA generalization 证据
- SmolVLA 全部结果 **LOCKED**（D065-D092），禁止重跑或修改已锁定数据
- π0.5 baseline **LOCKED**（D105）：Object 81.5%±0.5%, Spatial 84.2%±1.0%。不要重新 eval
- Ceiling effect 预期：81-85% baseline 上 CRM 增益有限，framing 已准备 "no-harm + selective improvement" 叙事

### 2. 🖥️ 基础设施快照
- **bjb1-18228**（训练服务器）：工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`（aml-train 镜像，conda base）
  - CRM cache: `/root/autodl-tmp/crm_cache_pi05/{object,spatial}/`
  - Checkpoint 输出: `/root/autodl-tmp/checkpoints/crm_pi05_full/{object,spatial}/`
  - 活跃进程: Object CRM training PID 800111 (cuda:0, tmux, cron 监控中)
- **bjb1-32546**（eval 服务器）：PyTorch 2.10.0+cu128, 6×GPU, π0.5 模型 7.5GB, evaluate.py 33058B ✅
- **bjb2-28827**（eval 服务器）：同上配置，环境已验证 ✅
- Eval 命令已准备好：`read_project_file("pi05_eval_commands.md")`
- Cron: `crm-train-pi05-object-full` 活跃，监控 PID 800111

### 3. 📊 当前状态
- **crm-train-pi05-object-full** (RUNNING): bjb1-18228 cuda:0, epoch ~7/50, ~5.5h 剩余，val_loss 0.005511。Cron 监控中
- **crm-train-pi05-spatial-full** (RUNNING 但实际 failed): FileNotFoundError — spatial precomputed cache 路径不存在 `/root/autodl-tmp/crm_cache_pi05/spatial`。2 个 Worker 正在诊断和修复：
  - `worker_diagnose_crm-train-pi05-spatial-full` — 诊断失败原因
  - `worker_ops_spatial-merge-train-now` — 尝试 merge spatial 数据并重启训练
- 84 个实验处于 PREPARING（主要是旧 precompute shards 和 SmolVLA 补种 eval，大部分不需要执行）
- 等待：2 个 Worker 回调（spatial 修复）+ Object CRM cron 完成回调

### 4. 📋 待办（条件触发式）
- Worker spatial 修复回调 → 确认 spatial cache 存在 → 重新提交 `crm-train-pi05-spatial-full` (bjb1-18228 cuda:1)
- `crm-train-pi05-object-full` cron 回调 (DONE) → 立即用 `pi05_eval_commands.md` 部署 Object Plan A eval（3 seeds × bjb1-32546/bjb2-28827，6 GPU）
- Spatial CRM training 完成 → 部署 Spatial Plan A eval（同上 6 GPU）
- Object + Spatial eval 全部完成 → 汇报 Director，与 SmolVLA 对比，写入论文 cross-VLA section
- eval 结果 CRM ≥ baseline → "cross-VLA generalization confirmed" narrative；CRM < baseline → "no-harm + selective improvement" narrative（已准备）

### 5. 🎯 战略上下文
- **核心 story**: "Correction Over Selection" — CRM 学习到的 correction（而非 selection）是提升 frozen VLA 的主要机制。SmolVLA 已充分证明。π0.5 cross-VLA 是补充证据
- **决策链**: D077→D092→D097→D103→D104→D105。D105 锁定 π0.5 baseline。当前处于 CRM training → eval → 写入论文的最后冲刺
- **易错点 1**: Spatial CRM 当前是 FAILED 状态但 registry 标记为 RUNNING（Worker 正在修复）。不要以为 spatial 已在训练
- **易错点 2**: π0.5 obs_dim=2048（不是 SmolVLA 的 384）。所有 π0.5 CRM 训练和 eval 命令必须用 `--obs_dim 2048`
- **易错点 3**: eval 需要先把 CRM checkpoint 从 bjb1-18228 scp 到 bjb1-32546/bjb2-28827，不要假设 checkpoint 已在 eval 服务器上
- **时间预算**: Object CRM ~5.5h → eval ~8h → 分析+写入 ~2h = ~16h。Spatial 并行但要先修好。DDL 前有足够时间，但不能拖

## 项目硬约束 (memory.md 节选)

## 3. Eval 环境检查

| 服务器 | PyTorch | CUDA | GPU 数量 | evaluate.py --help | pi05 模型 |
|--------|---------|------|----------|-------------------|-----------|
| bjb1-32546 | 2.10.0+cu128 ✅ | True ✅ | 6 | OK ✅ | 7.5GB model.safetensors ✅ |
| bjb2-28827 | 2.10.0+cu128 ✅ | True ✅ | 6 | OK ✅ | 7.5GB model.safetensors ✅ |

两台 eval 服务器环境就绪。

## 可查的历史
前 226 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-obs-only-object-norm01-seed74",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T19:30:16.946104+00:00_

You've hit your limit · resets 5pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-obs-only-object-norm01-seed74"
}
```

</details>

---
