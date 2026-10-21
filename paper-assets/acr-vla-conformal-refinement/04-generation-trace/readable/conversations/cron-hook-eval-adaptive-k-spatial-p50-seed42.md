# cron hook eval adaptive k spatial p50 seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 2
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/cron_hook_eval-adaptive-k-spatial-p50-seed42.jsonl`
- **Structured JSON:** [`b43e401f210fb14d75a1.json`](../../sessions/b4/b43e401f210fb14d75a1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

2 recorded events

### User

_source line 1 · 2026-05-21T19:29:40.783459+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #24。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- `allocated_gpus` 为空——项目无正式 GPU 配额，实验靠事实占用。提交新实验前确认 Director 知情
- Adaptive K 阈值 τ=0.074855 来自 Object P50 校准，**不可 per-benchmark tuning**（跨 benchmark 泛化是核心 claim）
- CRM checkpoint 固定用 `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`，norm02 版本
- bjb2-40593 磁盘 90% 已用（仅 44GB 可用），**不要在这台机器跑新实验**（π0.5 baseline 已在跑是例外）
- evaluate.py 路径在所有服务器上是 `src/evaluate.py`（不是根目录），命令必须包含 `src/` 前缀
- 提交命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&`（bjb1-32546 上 `python` 不在 PATH）

### 2. 🖥️ 基础设施快照
- **bjb2-40593**: `/root/acr-vla-conformal-refinement`, conda base (`/root/miniconda3`), 磁盘紧张 90%
- **bjb1-32546**: `/root/acr-vla-conformal-refinement`, conda base, 磁盘 4% (400GB 可用)
- **bjb2-28827**: `/root/acr-vla-conformal-refinement`, conda base, 磁盘 5% (399GB 可用)
- **bjb1-18228**: `/root/acr-vla-conformal-refinement`, conda base, 磁盘 4% (400GB 可用)
- HF cache: `/root/autodl-tmp/.hf_cache`（所有服务器）
- 活跃进程（8 GPU）：
  - eval-adaptive-k-spatial-p90-seed44-bjb2: PID 975409, bjb2-28827:cuda:0（Spatial sweep 最后一格）
  - eval-pi05-baseline-object-seed42: PID 802634, bjb2-40593:cuda:0（D095 π0.5）
  - eval-obs-only-object-norm003-seed66: PID 642428, bjb1-18228:cuda:0
  - eval-obs-only-object-norm005-seed66: PID 642506, bjb1-18228:cuda:2
  - eval-obs-only-object-norm01-seed66: PID 642775, bjb1-18228:cuda:3
  - eval-obs-only-object-norm003-seed67: PID 969788, bjb2-28827:cuda:5
  - eval-obs-only-object-norm005-seed67: PID 805840, bjb1-32546:cuda:2
  - eval-obs-only-object-norm01-seed67: PID 666593, bjb1-18228:cuda:1

### 3. 📊 当前状态
Session #23 完成了 session-start 初始化：read_registry + reconcile_crons + 向 Director 汇报。关键发现：handoff 中列为 RUNNING 的实验全部已完成（Spatial P50 3 seeds、latency profile、random-selection 等），均已在 registry 中记录为 DONE/success。

**已完成的关键结果（本 session 确认）：**
- Spatial Adaptive K P50: 32.0%±1.7% (seeds 30/33/33%), avg_K=6.35, fast_path=46%
- Spatial P75: 32.7%±1.5%, Spatial P25: 31.7%±1.5%（所有阈值 SR 几乎相同）
- Latency N=1000: VLA K=1 256.5ms, adaptive speedup 1.82×, CRM overhead -1.66%
- eval-adaptive-k-spatial-p50-seed42 诊断结果：进程正常完成 SR=30%，cron 误判

**RUNNING 8 个**（上面列出）。**PREPARING ~35 个**（历史遗留）。

**等待中：**
- Worker `worker_monitor_running-experiments-progress_20260521T032142` — SSH 检查 8 个 RUNNING 实验进度
- Worker `worker_analysis_norm-sweep-aggregation_20260521T032154` — 聚合所有 norm sweep 统计
- Director 回复：是否 LOCK Spatial sweep、闲置 GPU 用途、是否启动 Paper Agent
- P90 seed44 cron 回调（Spatial sweep 最后一格）
- π0.5 baseline cron 回调
- norm sweep seed66/67 cron 回调

### 4. 📋 待办
- P90 seed44 cron 回调（success）→ Spatial sweep 4×3 全部完成，更新 memory.md Spatial sweep 表格，汇报 Director 标记 LOCKED
- π0.5 baseline 完成 → 检查 SR 和 action diversity，决定是否进入 CRM pipeline（D095/D096）
- norm sweep seed66/67 完成 → 更新各 ε 的 n/mean/std，检查是否需要更多 seeds
- Director 回复"启动 Paper Agent" → 派 Worker 写 Method / Results 章节（Plan A 为核心）
- Director 回复"继续 norm sweep" → 在闲置 GPU（bjb1-32546 5张、bjb2-28827 4张）铺更多 seeds
- 两个 Worker 回调到达 → 读结果，更新 report.md，如有异常立即处理

### 5. 🎯 战略上下文
- **核心 narrative (D077→D092)**: Plan A (K=2 conformal + selective CRM) 是论文核心。Object 18.3%±2.1%, Spatial 35.0%±1.0%——均优于 K=10 CRM 且省 80% compute。Plan A 在两个 benchmark 上均 beats 所有 Adaptive K P-threshold 变体
- **Spatial sweep 关键洞察**: 所有阈值 SR 几乎相同 (31.7-32.7%)，Object 上 P50 Pareto-optimal 的结论不适用于 Spatial。但 Plan A (K=2) 35.0% 仍优于所有 Adaptive K 变体
- **信号已关闭**: FMVD NO-GO (ρ=0.0825), CRM magnitude NO-GO (ρ=0.1523)。K=2 L2 distance 是唯一可用信号 (ρ=0.9979)
- **OOD 结论已定**: Goal neutral (-0.7pp n.s.), Long marginal (+2.3pp, p=0.061 n.s.), LTO catastrophic (-12pp)
- **OpenVLA CLOSED (D093)**: CRM eval 0%, near-deterministic, applicability boundary
- **CoRL DDL 2026-05-29（8 天）**: 核心实验数据基本齐备，等 Director 决定启动论文写作
- **易错点**: (1) Cron false positive 频繁——eval 脚本不写 sentinel，进程正常退出会被误判 failed，确认前先 tail 日志和检查 output JSON (2) metrics 字段格式不统一：`overall_success_rate` vs `success_rate`，值可能是 0.16 或 16 (3) 闲置 GPU 多但 allocated_gpus 为空，新实验提交需 Director 知情

## 项目硬约束 (memory.md 节选)

## 3. Eval 环境检查

| 服务器 | PyTorch | CUDA | GPU 数量 | evaluate.py --help | pi05 模型 |
|--------|---------|------|----------|-------------------|-----------|
| bjb1-32546 | 2.10.0+cu128 ✅ | True ✅ | 6 | OK ✅ | 7.5GB model.safetensors ✅ |
| bjb2-28827 | 2.10.0+cu128 ✅ | True ✅ | 6 | OK ✅ | 7.5GB model.safetensors ✅ |

两台 eval 服务器环境就绪。

## 可查的历史
前 225 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T19:29:43.782998+00:00_

You've hit your limit · resets 5pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-adaptive-k-spatial-p50-seed42"
}
```

</details>

---
