# cron hook eval obs only object norm003 seed73

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 2
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/cron_hook_eval-obs-only-object-norm003-seed73.jsonl`
- **Structured JSON:** [`e7682a8a3c646740ad87.json`](../../sessions/e7/e7682a8a3c646740ad87.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

2 recorded events

### User

_source line 1 · 2026-05-21T19:19:44.184177+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #24。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单必须从 `get_project_status` 的 `execution.gpu_ids` 读取，当前 4 台服务器各有分配，不要假设全部可用
- Eval 实验不走 W&B，写 JSON 输出文件。Cron 报 "no W&B metrics" 是误报——必须 SSH 读 JSON output 确认真实结果，不要直接标 failed
- CRM checkpoint 路径固定：`/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`（所有服务器相同）
- 脚本内 GPU 编号始终从 0 开始（`--gpu 0`），框架自动映射物理 GPU
- CoRL 2026 DDL: 2026-05-29，剩 8 天，所有决策以此为锚

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: norm sweep eval（seed66 三条 ε=0.03/0.05/0.1 在跑）
- **bjb1-32546**: norm sweep eval（seed67 ε=0.05 在跑；seed51-r3 ε=0.1 状态待确认）
- **bjb2-28827**: norm sweep eval（seed67 ε=0.03 在跑）；刚完成 seed72-75 批次（已清理 failure_reason）
- **bjb2-40593**: π0.5 baseline eval（eval-pi05-baseline-object-seed42, PID 802634）
- 工作目录（所有服务器）：`/root/autodl-tmp/acr-vla-conformal-refinement/`
- Python：`/root/miniconda3/bin/python`（aml-train 镜像，conda base）
- 数据集：LIBERO-Object / LIBERO-Spatial（在各服务器本地）
- 活跃 cron 监控：12 条（reconcile 刚跑过）

### 3. 📊 当前状态
**刚做完**：处理 cron 误报——eval-obs-only-object-norm003-seed73 实际 conclusion=success (SR=16%)，cron 因无 W&B 误报 failed。同批 seed72/74/75 也有相同问题，已全部清理 stale failure_reason。

**RUNNING 实验（10 条）**：
- eval-pi05-baseline-object-seed42 — π0.5 VLA-only baseline（bjb2-40593），D095 新实验线
- eval-obs-only-object-norm003-seed66/67 — ε=0.03 norm sweep 补种
- eval-obs-only-object-norm005-seed66/67 — ε=0.05 norm sweep 补种
- eval-obs-only-object-norm01-seed66/67/71 — ε=0.1 norm sweep 补种
- eval-obs-only-object-norm01-seed51-r3 — ε=0.1 重跑（bjb1-32546，miss 3/5 待确认）
- eval-adaptive-k-spatial-p90-seed44-bjb2 — Adaptive K Spatial P90 第三 seed

**等待中**：
- 3 个 Worker 在跑：verify:process-gone-batch、diagnose:bjb2-28827-process-gone-batch、diagnose:bjb1-32546-seed51-r3
- seed71 cron miss 4/5，下次 poll 可能 auto-resolve → 需 Worker 先抢读 JSON
- 未向 Director 汇报本轮状态（非关键，都是 norm sweep 补种）

### 4. 📋 待办
- Worker `diagnose:bjb2-28827-process-gone-batch` 回调 → 确认批次结果，更新 report.md
- seed71 (ε=0.1) cron 到 miss 5/5 前 → Worker 必须抢先读 JSON 确认结果，避免被错误标 failed
- π0.5 baseline (seed42) 完成 → 检查 SR。若 >15% 且 action diversity 足够 → 进 Phase 3 CRM pipeline；若 near-deterministic（like OpenVLA）→ 报 Director applicability boundary
- 所有 norm sweep seed 完成 → 汇总 ε∈{0.03, 0.05, 0.1} 均值±std，更新 ROADMAP norm sweep 表，生成 Figure 2
- Director 未决：threshold calibration（flatten-L2 vs per-step-mean-L2）、paper writing 指令

### 5. 🎯 战略上下文
**核心结论链**：D088→D090(Learned Head NO-GO)→D092(Plan A K=2 GO: Object 18.3%±2.1%, Spatial 35.0%±1.0%)→D093(OpenVLA CRM 0%, applicability boundary)→D095(π0.5/π 新实验线)

**Plan A 已 LOCKED**：K=2 conformal + selective CRM，80% compute reduction vs K=10，性能持平或略优。这是论文核心 claim。

**Norm sweep 目的**：填充 ε∈{0.03, 0.05, 0.1} 的统计 seed 数量，当前各 ε 有 6-9 seeds，目标是每个 ε 至少 10 seeds 以支撑误差棒。

**易错点**：
- Eval 实验的 cron 几乎全会报 "no W&B"——这是系统性误报，不是真 failure。必须读 JSON output 确认
- OpenVLA CRM 线已 CLOSED (D093)，不要再尝试
- π0.5 是 flow-matching 模型，action distribution 特性与 SmolVLA 不同，不要假设 CRM 一定适用
- ROADMAP 里 ε=0.05 mean SR 是 13.8%（不是 14.3%），paper_framing.md 待修正

## 项目硬约束 (memory.md 节选)

## 3. Eval 环境检查

| 服务器 | PyTorch | CUDA | GPU 数量 | evaluate.py --help | pi05 模型 |
|--------|---------|------|----------|-------------------|-----------|
| bjb1-32546 | 2.10.0+cu128 ✅ | True ✅ | 6 | OK ✅ | 7.5GB model.safetensors ✅ |
| bjb2-28827 | 2.10.0+cu128 ✅ | True ✅ | 6 | OK ✅ | 7.5GB model.safetensors ✅ |

两台 eval 服务器环境就绪。

## 可查的历史
前 223 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-obs-only-object-norm003-seed73",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T19:19:47.924058+00:00_

You've hit your limit · resets 5pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-obs-only-object-norm003-seed73"
}
```

</details>

---
