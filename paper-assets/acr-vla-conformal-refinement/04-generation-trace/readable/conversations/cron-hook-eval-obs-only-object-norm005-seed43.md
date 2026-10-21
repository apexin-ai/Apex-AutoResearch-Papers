# cron hook eval obs only object norm005 seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 2
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/cron_hook_eval-obs-only-object-norm005-seed43.jsonl`
- **Structured JSON:** [`9f7e182cc4286f154993.json`](../../sessions/9f/9f7e182cc4286f154993.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

2 recorded events

### User

_source line 1 · 2026-05-21T19:31:07.480784+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #24。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5（共 17 张）。白名单外的 GPU 即使 Director 说了也必须 push back
- CRM training 在 bjb1-18228 上跑，eval 命令占位符 `&lt;CRM_CHECKPOINT_OBJECT>` / `&lt;CRM_CHECKPOINT_SPATIAL>` 必须等训练完成后填入实际 checkpoint 路径，不能猜
- π0.5 eval 必须传 `--obs_dim 2048`（默认 960 是 SmolVLA 的），漏传会静默产出错误结果
- SmolVLA 全部结果已 LOCKED，不得重跑或修改。π0.5 baseline 已 LOCKED（Object 81.5%, Spatial 84.2%）
- CoRL 2026 DDL **2026-05-29**，≤8 天

### 2. 🖥️ 基础设施快照
- **bjb1-18228**（训练服务器）：工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`，conda base
  - Object CRM training: PID 800111, cuda:0, output `/root/autodl-tmp/checkpoints/crm_pi05_full/object/`
  - Spatial CRM training: cuda:1, 有两个 Worker 正在处理（诊断 + 重跑 merge+train），状态不确定
  - Spatial CRM checkpoint（可能旧 run）: `/root/autodl-tmp/checkpoints/crm_pi05/spatial/crm_best.pt`
  - Object CRM checkpoint（当前 run）: `/root/autodl-tmp/checkpoints/crm_pi05_full/object/crm_best.pt`（训练中）
  - Precompute cache: `/root/autodl-tmp/crm_cache_pi05/`
- **bjb1-32546**（eval 服务器）：PyTorch 2.10.0+cu128, 6 GPU 全空闲, evaluate.py 33058 bytes ✅, π0.5 model 7.5GB ✅, 无 git remote（代码通过 rsync 同步）
- **bjb2-28827**（eval 服务器）：同上配置，6 GPU 全空闲 ✅
- **bjb2-40593**：1 GPU (cuda:0)，无 GPU 信息记录
- π0.5 模型路径：`/root/autodl-tmp/models/pi05_libero_finetuned/`（各 eval 服务器均已部署）
- Cron 活跃：crm-train-pi05-object-full（监控 PID 800111）
- Eval 命令已准备：`artifacts/pi05_eval_commands.md`（6 runs, 3 seeds × 2 benchmarks）

### 3. 📊 当前状态
- **Object CRM training** (crm-train-pi05-object-full): RUNNING, PID 800111, bjb1-18228 cuda:0。memory.md 记录 epoch 7/50, val_loss 0.005511, 预计剩余 ~5.5h（从 memory.md 写入时算起，实际可能已更近完成）
- **Spatial CRM training** (crm-train-pi05-spatial-full): RUNNING 状态但 reconcile 未找到对应 cron。有两个 Worker 正在处理：
  - `worker_diagnose_crm-train-pi05-spatial-full`（诊断 spatial 训练）
  - `worker_ops_spatial-merge-train-now`（spatial merge + 重新训练）
  - **下一个"我"优先检查这两个 Worker 的结果**——spatial 训练可能出了问题需要重跑
- 82 个 PREPARING 实验（大部分是历史遗留的 precompute shard 和 norm sweep）
- 14 GPU 空闲等 CRM training 完成后部署 eval

### 4. 📋 待办（条件触发式）
- Worker `worker_diagnose_crm-train-pi05-spatial-full` 和 `worker_ops_spatial-merge-train-now` 完成 → 读结果，确认 Spatial CRM training 是否正常。若失败需立即在 bjb1-18228 cuda:1 重启训练
- Object CRM training cron 回调（PID 800111 退出）→ 检查 conclusion，若 success 则立即部署 Object eval（3 seeds on bjb1-32546 cuda:0-1 + bjb2-28827 cuda:0）
- Spatial CRM training 完成 → 部署 Spatial eval（3 seeds on bjb2-28827 cuda:1 + bjb1-18228 cuda:0-1，注意 bjb1-18228 要等 Object 训练也完成后才能用）
- 6 个 eval 全部完成 → 分析 π0.5 CRM 增益（预期 ceiling effect，baseline 81-85%），写入论文
- 若 CRM 增益 ≥ 2pp → "cross-VLA generalization" narrative 成立
- 若 CRM 增益 < 1pp 或 negative → "no-harm + selective improvement" framing，已预期 ceiling effect
- 所有 π0.5 结果落地 → Paper Agent 写入论文 → final review → submission prep

### 5. 🎯 战略上下文
- **核心方法**：Adaptive inference-time compute for frozen VLAs — K=2 L2 distance + selective CRM correction (Plan A = Pareto optimal)
- **SmolVLA 结论（LOCKED）**：Plan A Object +7.5pp (18.3% vs 10.8%), Spatial +5.6pp (35.0% vs 29.4%)。Correction is the active mechanism, not selection。K=1 negative, K≥5 works
- **π0.5 是 cross-VLA generalization 验证**：SmolVLA 是弱 VLA (10-35% baseline)，π0.5 是强 VLA (81-85% baseline)。预期 ceiling effect —— CRM 增益在高 baseline 上受限。Framing 已预备 "no-harm + selective improvement on hard subtasks"
- **决策链**：D065 (correction > selection) → D067 (batch inference) → D076 (adaptive K) → D087 (OpenVLA) → D097 (latency) → D102 (K=20≈K=2) → D105 (π0.5 baseline locked)
- **易错点**：
  - Spatial CRM checkpoint 路径可能有两个版本（`crm_pi05/spatial/` 旧 run vs `crm_pi05_full/spatial/` 新 run），务必用 Worker 确认最新的 best checkpoint
  - eval 命令里 `--cache_dir` 不是 eval 参数（只有 train_crm.py 用），不要加
  - bjb1-18228 cuda:3 有旧 precompute 进程待清理（ROADMAP 记录），部署 eval 前检查
  - Object checkpoint 目录是 `crm_pi05_full/object/`（不是 `crm_pi05/object/`）

## 项目硬约束 (memory.md 节选)

## 3. Eval 环境检查

| 服务器 | PyTorch | CUDA | GPU 数量 | evaluate.py --help | pi05 模型 |
|--------|---------|------|----------|-------------------|-----------|
| bjb1-32546 | 2.10.0+cu128 ✅ | True ✅ | 6 | OK ✅ | 7.5GB model.safetensors ✅ |
| bjb2-28827 | 2.10.0+cu128 ✅ | True ✅ | 6 | OK ✅ | 7.5GB model.safetensors ✅ |

两台 eval 服务器环境就绪。

## 可查的历史
前 227 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-obs-only-object-norm005-seed43",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T19:31:13.470904+00:00_

You've hit your limit · resets 5pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-obs-only-object-norm005-seed43"
}
```

</details>

---
