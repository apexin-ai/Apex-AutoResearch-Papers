# agent / loop_4.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`548987c4898ed644c340.json`](../../sessions/54/548987c4898ed644c340.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T21:21:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0,1,2,3（全在 rtx5090-4x 一台机器上）。rtx5090-4x 和 gpu-5090-4x-1 和 bjb2-12179 是同一台机器的不同 SSH endpoint
- **训练提交禁止 bash -c 内联引号**（D035，第 4+ 次踩坑）：必须先写 .sh 脚本到 `/root/autodl-tmp/scripts/`，再 `bash /path/to/script.sh` 提交
- kill_job 后必须验证子进程终止（`ps -p &lt;PID>` + `nvidia-smi -i &lt;GPU>`），tmux wrapper 死了但 python 子进程可能仍占显存
- TRL 1.1.0 API：`tokenizer=` → `processing_class=`，`max_seq_length` → `max_length`
- flash_attn 未装，必须用 `attn_implementation="sdpa"`
- QLoRA 4-bit + kl_coef 要小心：kl_coef=0.05 爆炸，0.0 collapse，0.01 是唯一验证过的值
- 不能从 kl_coef=0 的 checkpoint 恢复加 KL penalty，必须从 SFT 重新训练

### 2. 🖥️ 基础设施快照
- **服务器**：rtx5090-4x（4× RTX 5090 32GB），SSH endpoint 还有 bjb2-12179
- **Python**：`/root/miniconda3/bin/python`（conda base，不是 venv）。激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **项目代码**：`/root/autodl-tmp/freige`
- **模型**：`/root/autodl-tmp/models/Qwen3-4B`（7.6GB，ModelScope 下载）
- **SFT adapter**：`/root/autodl-tmp/sft_output`
- **数据**：`/root/autodl-tmp/data/docred`（train 3053, dev 985）
- **GRPO 输出**：P0 → `/root/autodl-tmp/grpo_ced_lr5e6`，P0+P1 → `/root/autodl-tmp/grpo_ced_lr5e6_rp`
- **Eval 结果**：`/root/autodl-tmp/eval_results/`
- **训练脚本**：`/root/autodl-tmp/scripts/`
- **wandb**：entity=`xiaoyucorynne-`，project=`freige-grpo`
- **活跃进程**：
  - mvp2_grpo_ced_lr5e6_r1: PID 90080, tmux session, cuda:0, cron 监控中
  - mvp2_grpo_ced_lr5e6_rp_r2: PID 94753 (wrapper) / 实际训练可能不同, tmux, cuda:3, cron 监控中
  - mvp2_eval_lr5e6_r1_ckpt20: PID 96500, tmux, cuda:1, cron 监控中
- **AutoDL 环境前置**：脚本头部需 `source /etc/network_turbo` + `HF_HOME=/root/autodl-tmp/.hf_cache` + `HF_HUB_DISABLE_XET=1` + SSL cert 环境变量

### 3. 📊 当前状态
**刚完成**：mvp2_eval_ced_kl001_r4_multi 被 cron auto-resolved 为 failed（进程死 5 次无 sentinel）。这个实验已不重要——整个 kl001_r4 系列（lr=5e-5）已判 FAIL (D027)，方向已转向 lr=5e-6。

**正在运行（3 实验，3/4 GPU）**：
| exp_id | GPU | 内容 | 预计完成 |
|--------|-----|------|---------|
| mvp2_grpo_ced_lr5e6_r1 | cuda:0 | **P0**: lr=5e-6 CED GRPO 200 步训练 | ~数小时 |
| mvp2_grpo_ced_lr5e6_rp_r2 | cuda:3 | **P0+P1**: lr=5e-6 + recall_penalty | ~8h |
| mvp2_eval_lr5e6_r1_ckpt20 | cuda:1 | P0 ckpt-20 early eval（MVP gate） | ~2.5h |

**cuda:2 空闲**——mvp2_eval_ced_kl001_r4_multi 刚释放。按 ROADMAP 应安排 P0 ckpt-40 eval（等 lr5e6_r1 训练到 step 40 产出 checkpoint 后）。

**PREPARING 中 3 条都是历史遗留**（r2/r3 是早期 infra 失败，r4_last 被拆分后作废），可忽略。

**Worker 池 = 0**（违反 L1 红线 #4，但当前 3 个实验都在跑且无需 Worker 干预——等 cron 回调）。

### 4. 📋 待办（条件触发式）
- **mvp2_eval_lr5e6_r1_ckpt20 完成（cron 回调）** → 这是 MVP-2 P0 的关键 gate：
  - rel_f1 > 0.30 → **P0 PASS**，更新 registry conclusion=success，汇报 Director，立即在 cuda:1 启动 P0+P1 ckpt-20 eval
  - rel_f1 ≤ 0.30 → P0 FAIL，走 red-section framing 提案流程，汇报 Director
- **mvp2_grpo_ced_lr5e6_r1 到 step 40** → 在 cuda:2 启动 P0 ckpt-40 eval（需 Worker 写 eval 脚本 + submit）
- **mvp2_grpo_ced_lr5e6_r1 完成（全 200 步）** → eval best reward ckpt + last ckpt
- **mvp2_grpo_ced_lr5e6_rp_r2 到 step 20** → 在空闲 GPU 启动 P0+P1 ckpt-20 eval
- **P0 和 P0+P1 都有 ckpt-20 eval 结果** → 对比隔离 recall_penalty 的贡献，这是论文的核心 ablation
- **cuda:2 持续空闲** → 派 Worker 检查 lr5e6_r1 当前 step，如已过 step 40 则立即跑 ckpt-40 eval

### 5. 🎯 战略上下文
**项目核心**：FREIGE = 用 CED (Contrastive Evidence Discrimination) reward 训练 LLM 做文档级关系抽取 + 可验证证据生成。

**关键发现链**：
- D008: QLoRA 4-bit + kl_coef 不兼容（KL 爆炸），kl_coef=0.01 是折中
- D024: **CED reward 有 anti-mode-collapse 作用**（论文核心 finding）——同配置下 CED 成功、extraction-only/flat-NLI 都 collapse
- D027/D029: lr=5e-5 全灭（灾难性遗忘），转 lr=5e-6
- D032: CED 有 recall shortcut（少预测→高 CED），已部署 --ced_recall_penalty fix

**SFT baseline**：F1=0.4057, Evi-F1=0.7979, EDCR=0.7118

**MVP-2 判定标准**：
- 核心：(CED_Evi-F1 − SFT_Evi-F1) ≥ 2pp
- F1 不退化：CED_F1 ≥ max(extraction-only_F1, SFT_F1) − 5pp
- 当前 gate：P0 ckpt-20 rel_f1 > 0.30（不灾难性遗忘）

**最容易判断错的事**：
1. ced_kl001_r4 训练 reward 很漂亮（0.22→1.37）但 eval F1 崩了——**不要被训练 reward 骗，必须看 eval F1**
2. batch_size=1 GRPO 方差极大，单 checkpoint eval 不可信，必须 eval 多个 checkpoint
3. 三条 PREPARING 实验是历史遗留，不要尝试恢复它们
4. wandb MCP 工具有 bug（`wandb_project` 参数传递错误），用 `fetch_wandb_run_history` + 已知 run_id 替代


---
