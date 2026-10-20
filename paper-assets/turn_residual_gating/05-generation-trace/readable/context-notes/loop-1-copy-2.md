# agent / loop_1.md

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`d6ce0e544c1d1e65abbb.json`](../../sessions/d6/d6ce0e544c1d1e65abbb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-21T17:24:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- 只能用 westd-20861:cuda:0（唯一白名单 GPU，其他设备号必须 push back Director）
- 训练完成 → 必须先跑 eval → 确认结果 → 再启动下一个训练（本次 v8b s123 因跳过 eval 延迟 10h，Director P0 批评）
- 所有训练必须走 submit_training_job，不用 nohup/bash 直接启动（否则无 cron 监控，回调丢失）
- 禁止将 AR nGAR 与 TF raw GAR 对比（M020 教训：TF nGAR=11.88 不是 0.484）
- 论文绝不能使用 "normalization artifact" 叙事（Director 明令）

### 2. 🖥️ 基础设施快照
- 服务器：westd-20861，GPU: 1×RTX PRO 6000 Blackwell 102GB
- 工作目录：/root/turn_residual_gating
- Python：source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
- Qwen 模型：/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct
- Llama 模型：/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/
- 数据：/root/turn_residual_gating/data/ultrachat_8k (8000 samples)
- 活跃进程：v7_tg_s123 PID 245628（cron 已注册，interval=120s）
- 无 W&B 集成（训练脚本不用 W&B）

### 3. 📊 当前状态
刚完成：v8b SS s123 训练确认（success, final_loss=0.9316）+ v7 TG s123 启动 + v8b s123 eval 脚本创建。

Registry RUNNING：
- **v7_tg_s123** (PID 245628, ~4.5h elapsed, ETA ~05-22 02:00 UTC) — seed=123 multi-seed 验证，与 v7 s42 相同配置

等待：v7_tg_s123 cron 完成回调。⚠️ 历史上 cron 回调连续 3 次丢失（v8b 因未走 submit_training_job），这次已手动 register_cron，但仍需警惕。

### 4. 📋 待办
- v7_tg_s123 cron 回调到达（或 Director 手动催） → spawn worker 验证完成 + 提取 metrics → update_registry DONE
- v7 确认完成后 → **先跑 v8b SS s123 eval**（`bash scripts/eval_v8b_ss_s123.sh`，8 runs，~1h）→ 提取 GAR TF/AR gap ratio，与 s42 对比（s42: gap 32×→1.57×）
- v8b eval 完成后 → 跑 v7 TG s123 eval（`bash scripts/eval_v7_tg_s123.sh`，最多 16 runs，~2h）
- 两个 eval 都完成 → 汇报 Director multi-seed 对比表（C7 完成）
- 如有 GPU 余力 → Llama LoRA-only (plan_011, nice-to-have)

### 5. 🎯 战略上下文
项目核心结论：ThreadGate 的 auxiliary GAR loss 在 exposure bias 下失败（20-33× TF/AR gap），PCGrad 因果排除梯度冲突，TRC 确认 attention-specific。双路 mitigation 已验证：inference-time steering (β=5, GAR 0.03→0.70) + training-time SS (gap 32×→1.57×)。跨模型 Llama 确认（12.5× gap）。

D040 序列进度：N=50 ✅ → Llama ✅ → instruction retention ✅ → v8b SS s123 训练 ✅ → **v8b eval ⏳** → **v7 TG s123 🔄** → v7 eval ⏳

易错点：
- v8b s123 checkpoint 在 `checkpoints/tg_v8b_ss_s123/epoch_2/`（不是 `runs/` 目录）
- s42 目录名是 `tg_v8b_ss_fixed_s42`（不是 `tg_v8b_ss`）
- 日志 step 是 microsteps（per-epoch 0-7999），optimizer_steps = microsteps/8，总 24000 microsteps = 3000 optimizer steps
- Cron 回调不可靠——如果超过预期完成时间 1h 没收到回调，主动 spawn worker 检查


---
