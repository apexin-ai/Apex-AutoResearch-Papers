# cron hook exp 001 sft 0pct 15B s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/cron_hook_exp_001_sft_0pct_15B_s123.jsonl`
- **Structured JSON:** [`55bf617744ad93c2c0cf.json`](../../sessions/55/55bf617744ad93c2c0cf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

1 recorded events

### User

_source line 1 · 2026-05-14T06:22:14.484770+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #4。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- 服务器 cqa1-21977 的 6 块 GPU (cuda:0-5) 全部分配给本项目，但 **只能用 `get_project_status` 白名单里的 GPU**，不能用其他服务器/项目的 GPU
- `server: local` 实验（exp_004_sim_sweep PID 340553、exp_005_noise_prop_v3 PID 339838）**禁止用 SSH 查进程**，必须用本地 `ps -p PID`，也**不注册 cron**。两次误标 DONE 的事故教训
- 1.5B/3B SFT 必须 `batch_size=1, grad_accum=16`，否则 24GB 4090D OOM
- `--gpu` 参数必须匹配物理 GPU 编号（不是逻辑编号），submit_training_job 会注入 CUDA_VISIBLE_DEVICES
- 论文结果必须用 CmdStanPy Bayesian MCMC（D011/D013），不能用 PyTorch MLE
- 所有 dosage SFT 使用 ALL paraphrases（含 QC fail）= "noisy contamination" condition（D010）

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-21977, 6× RTX 4090D (cuda:0-5)
- **工作目录**: `/root/contamcal-irt-calibration/`
- **Python**: `/root/miniconda3/bin/python`，激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型缓存**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{0.5B,1.5B,3B}`
- **SFT 数据**: `/root/autodl-tmp/exp001/sft_data/sft_dosage_{000,005,025,050,100}.jsonl`
- **Checkpoints**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{size}_d{dosage}_s{seed}/`
- **Eval 输出**: `/root/autodl-tmp/exp001/eval_results/{Model}_d{dosage}_s{seed}/`
- **Stan model**: `contam_irt_4pl_simple.stan`（Simple IRT，ME model 已弃用）
- **活跃 cron 监控** (8 个): exp_001_sft_d100_15B_v2 (PID 251924), exp_001_eval_3B_d000_s42 (PID 249294), exp_001_eval_05B_d005 (PID 255322), exp_001_eval_05B_d000_s42_v5 (PID 266511), exp_001_eval_05B_d100_v5 (PID 266780), exp_001_sft_d005_15B (PID 271916), exp_001_sft_d100_3B (PID 291373), exp_001_sft_d025_05B_v2 (PID 299016)
- **本地进程** (无 cron): exp_004_sim_sweep (PID 340553), exp_005_noise_prop_v3 (PID 339838)
- **活跃 Worker**: worker_analysis_3B_gsm8k_inversion_v2, worker_ops_restart_exp004_sweep

### 3. 📊 当前状态
**刚完成**: Phase 2 dosage 数据 v3 生成、Fisher 推导 appendix.tex、多轮 eval pipeline debug（v1-v5）、exp_004 断点续跑修复、exp_005_v3 误标修复

**10 个 RUNNING 实验**:
| 实验 | GPU | 类型 | 备注 |
|------|-----|------|------|
| exp_001_sft_d005_15B | GPU 4 | SFT | 1.5B 5% dosage |
| exp_001_sft_d100_15B_v2 | GPU 0 | SFT | 1.5B 100% dosage |
| exp_001_sft_d100_3B | GPU ? | SFT | 3B 100% dosage (~214min) |
| exp_001_sft_d025_05B_v2 | GPU 5 | SFT | 0.5B 25% dosage (~53min) |
| exp_001_eval_3B_d000_s42 | GPU 1 | Eval | 3B baseline eval |
| exp_001_eval_05B_d005 | GPU ? | Eval | 0.5B 5% dosage eval |
| exp_001_eval_05B_d000_s42_v5 | GPU ? | Eval | 0.5B baseline eval v5 |
| exp_001_eval_05B_d100_v5 | GPU ? | Eval | 0.5B 100% eval v5 |
| exp_004_sim_sweep | CPU local | Sim | 27/120 done, ETA May 16-17 |
| exp_005_noise_prop_v3 | CPU local | Sim | PID 339838, ETA ~14:30 UTC today |

**等待中**:
- 2 个 Worker 在跑：一个分析 3B GSM8K inversion 异常，一个重启 exp004 sweep
- exp-002 signal pipeline 代码编写（**关键路径最高优先级**，阻塞整条管线）
- exp-006 baselines 代码编写（7 baselines + 统一接口）
- 多个 PREPARING 态的 eval 实验等 GPU 空出

### 4. 📋 待办（条件触发式）
- **0.5B eval (v5) 完成** → GPU 空出 → 先跑 exp-002 signals on 0.5B {d000, d005, d100}（~1-2 GPU-h），再提交 d025 相关任务
- **exp-002 signal pipeline 代码完成** → 在 0.5B 上 dry-run → 跑 signals → exp-003 RRF → exp-006 IRT calibration（**整条管线首次验证**）
- **1.5B d005/d100 SFT 完成** → GPU 0/4 空出 → 提交 3B d005/d100 SFT
- **exp_005_noise_prop_v3 完成**（~今天 14:30 UTC）→ 本地 `ps -p 339838` 检查 → 分析 noise propagation 结果 → 更新 registry
- **exp_004_sim_sweep 每个 AUC 条件 10 seeds 完成** → 增量分析 γ recovery
- **3B d000 eval 完成** → 拿到 3B baseline scores → 与 0.5B/1.5B baseline 对比
- **所有 0.5B d000/d005/d025/d100 eval 完成** → 画 dose-response 曲线（4 点）
- **exp-002 + exp-006 代码 + 0.5B 全 eval 完成** → 跑通 0.5B 端到端管线 → 这是 paper Table 1 的第一行数据

### 5. 🎯 战略上下文
- **投稿目标**: EMNLP 2026 ARR May 25，距今 11 天
- **核心瓶颈是软件不是算力**: exp-002 signal pipeline 和 exp-006 baselines 的代码编写阻塞了从 SFT→eval→calibration 的整条管线。GPU 6/6 满载但最终 IRT calibration 结果还没出来
- **3 个 Core Claims**: C1 = 4PL+γ IRT calibration 有效, C2 = signal survival under RL (exp-008 未启动，**Table 2 风险**), C3 = identifiability bounds (exp-004/005 在跑)
- **D015 重要决策**: C2 "cliff-like" RL degradation 因无中间 checkpoint 需降级表述
- **D014**: C1 γ recovery 需 N≥50 且 σ_e≥0.3 条件限定
- **exp-004 早期发现**: γ 在 AUC=0.55 就可辨识（比预期好），但 AUC=0.80 处 CI 反常更宽（疑似 exposure-ability collinearity），需更多 seeds 确认
- **易错点**: (1) 不要混淆 server:local 和远程实验的检查方式 (2) eval pipeline 有 paraphrased benchmark loading bug 未修 (3) d050 已降优先级不要主动跑 (4) Stan model 只用 simple 不用 ME (5) Worker 写的 exp-002/006 代码质量直接决定论文能否按时提交，催促优先级最高

## 项目硬约束 (memory.md 节选)

## Phase 3 GPU 调度优先级 (Director 2026-05-14, 更新 03:23 UTC)
**原则：每个 model size 先跑两端极值 (d005, d100)，再填 d025。d050 降为 P2+ 可选。**

**新增：GPU 1/2 eval 完成后，先跑 0.5B exp-002 signals（1-2 GPU-hours），再提交 d025 SFT。**
原因：0.5B 已有 d000/d005/d100 三个 checkpoint，可在 0.5B 上先跑通 exp-002→003→006 整条管线验证，同时大模型 SFT 继续。

优先级从高到低：
1. 1.5B d005 + d100 — ✅ 均已在跑 (GPU 4 / GPU 0)
2. 3B d005 + d100 — 等有 GPU 空出
3. **0.5B exp-002 signals** — GPU 1 或 GPU 2 eval 完成后立即跑（~1-2 GPU-hours）
4. **0.5B d025 SFT+eval+signals** — P2 恢复，紧跟 exp-002 signals（~1h SFT + 1-2h eval）
5. 1.5B d025 — P4，填充 dose-response 曲线
6. 3B d025 — P4，最后填充
7. d050 全部 — P2+ 可选

**免审批：** GPU 空出时直接按优先级启动，事后汇报。

**条件触发队列**：GPU 1/2 eval 完成 → exp-002 signals on 0.5B → 0.5B d025 SFT → 0.5B d025 eval → 0.5B d025 signals

**Why:** 3 点 (d000/d005/d100) 天然单调，审稿人会打回 monotonicity claim。0.5B d025 恢复 P2：成本极低 (~1+2 GPU-h)，4 点曲线 (d000/d005/d025/d100) 显著增强 claim 可信度。

## 可查的历史
前 32 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:exp_001_sft_0pct_15B_s123",
  "source": "system:ralph_loop"
}
```

</details>

---
