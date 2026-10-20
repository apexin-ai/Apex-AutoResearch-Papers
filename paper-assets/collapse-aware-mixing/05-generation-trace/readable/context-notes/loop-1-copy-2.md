# agent / loop_1.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`e336ec939587c5a0a4e7.json`](../../sessions/e3/e336ec939587c5a0a4e7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T17:11:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cqa1-38874 的 cuda:0（gpu_ids 白名单只有这一张）
- 服务器用 conda base 环境（/root/miniconda3/），不要创建 venv，不要用 --break-system-packages
- 输出必须写 /root/autodl-tmp/output/，根分区只有 ~30GB
- HF_HOME 必须指向 /root/autodl-tmp/.hf_cache，否则根分区爆满
- attn_implementation 必须用 "sdpa"，flash_attention_2 在此服务器编译失败
- lr=1e-5 对 Pythia-1B 会发散（v4 已验证，CE=114.79），安全范围 2e-6~5e-6
- submit_training_job 命令需 `bash -c "source env_init.sh && ..."` 包裹，tmux 默认用 sh

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874，1× RTX PRO 6000 96GB
- 工作目录：/root/collapse-aware-mixing/
- Python：/root/miniconda3/bin/python3 (3.12)，PyTorch 2.10.0，transformers 4.57.6
- conda：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 环境初始化脚本：/root/collapse-aware-mixing/env_init.sh（network_turbo + SSL + HF_HOME + conda）
- 数据集：/root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-103-raw-v1（~57052 packed seqs）
- 模型：EleutherAI/pythia-1b（HF cache 已下载）
- 输出：/root/autodl-tmp/output/
- 活跃进程：PID 32154, tmux session `mvp_pilot_v5`, cron 已注册
- 日志：~/runs/collapse-aware-mixing/mvp_pilot_v5.log
- 本地代码 artifacts：/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/

### 3. 📊 当前状态
mvp_pilot_v5 G0 训练中（step ~285/1373，约 21%），loss 2.55 grad_norm 1.13，训练正常。已保存 checkpoint-152 和 checkpoint-304。预计 G0 剩余 ~36 分钟，之后自动进入 eval → synthetic gen → G1 → G2。

Registry：
- mvp_pilot_v5: **RUNNING** — lr=2e-6, bf16 统一, EarlyStop 安全阀, 3 代 pipeline
- mvp_pilot_v4: DONE(failed) — lr=1e-5 发散确认
- mvp_pilot_v3/v2/v1: DONE(failed) — 基础设施问题（conda/network/tmux）

无等待中的 Worker。Cron 监控 PID 32154 中。Director 已收到前 300 步 loss+grad_norm 汇报。

### 4. 📋 待办
- Cron 回调 mvp_pilot_v5 进程退出 → 检查 pilot_summary.json 的 mvp_check.verdict 字段，这是 GO/NO-GO 判定
- verdict=GO → 汇报 Director，推进主实验（deploy main_experiment.py + golden_ratio_baseline.py）
- verdict=CONDITIONAL GO → 汇报 Director，建议加细粒度 checkpoint（每 5M tokens）验证谱是否真 lead
- verdict=EXTEND → 汇报 Director，建议加第 4 代
- verdict=KILL → 按 red-section skill 产出 Framing 调整提案，禁止默默跑下一个实验
- 训练异常中断 → 检查日志，如果 EarlyStop 触发说明 loss>15，需要进一步降 LR；如果 OOM/SIGHUP 则修复后重启
- config.py 默认 LR 已改为 2e-6（本地），但服务器上可能还是 1e-5（launch script 显式传参所以不影响当前运行）

### 5. 🎯 战略上下文
- 项目目标：验证 spectral effective rank（RankMe）是 model collapse 的 leading indicator，用它驱动 PI controller 做 real/synthetic 动态混合
- DDL：EMNLP 2026 ARR 2026-05-25（剩 13 天）
- 决策链：D001(MVP方案) → D002(GO/NO-GO量化标准) → D003(wikitext-103替代OpenWebText) → D004(v4发散确认) → D005(ratio=1.00排除报告artifact，真因LR过高)
- GO/NO-GO 标准：spectral rank drop ≥1σ before PPL rise ≥2pts/5%；KL > 0.1 nats
- 易错点：v5 全 pipeline 包含 G0 训练 + eval + synthetic gen + G1 + eval + G2 + eval，总时长可能 3-4 小时，不是只有 G0 的 46 分钟
- 易错点：pilot_pipeline.py 中 evaluate_checkpoints 会加载模型到 GPU 做 eval，如果训练模型没释放会 OOM——代码中有 `del model; torch.cuda.empty_cache()` 但要注意
- 本地 artifacts/code/ 和服务器 /root/collapse-aware-mixing/ 可能有版本差异（dtype hotfix 直接 sed 改的服务器，本地也改了但未必完全同步），未来部署时以本地为准 + 显式同步


---
