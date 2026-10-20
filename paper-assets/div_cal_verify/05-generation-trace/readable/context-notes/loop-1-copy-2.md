# agent / loop_1.md

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`c1185900f6bc10220656.json`](../../sessions/c1/c1185900f6bc10220656.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T20:25:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-11235 的 cuda:0 和 cuda:1，双卡模式用 `--gpu_ids 0,1`（generator cuda:0, student cuda:1）
- 根分区只有 30GB，**所有实验输出必须写数据盘** `/root/autodl-tmp/div_cal_verify/results*/`，绝不用 `--output_dir ./results`
- GPT2 模型必须用 `torch.float32`（不支持 bfloat16），代码已 patch 但部署时需验证
- HuggingFace 直连被墙，Qwen 模型用 ModelScope 下载，Contriever 用 hf-mirror，GPT2 走代理（`source env.sh`）
- MVP 结论已判定 NEGATIVE（D004），**禁止未经 Director 批准启动新 Qwen 实验**——Phase 2 需 Phase 1 确认崩塌后才能跑

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (connect.westd.seetacloud.com:11235, root, 2× RTX PRO 6000 Blackwell 96GB)
- 镜像：aml-train，conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 环境脚本：`/root/div_cal_verify/env.sh`（设 HF_HOME/SSL/network_turbo）
- 模型路径：Qwen3-1.7B → `/root/models/Qwen/Qwen3-1.7B`，Qwen3-4B → `/root/models/Qwen/Qwen3-4B`，GPT2 系列自动 HF 下载
- 数据路径：Qwen 数据 → `/root/div_cal_verify/data/`，GPT2 数据 → `/root/div_cal_verify/data_gpt2/`
- 结果路径：MVP → `/root/autodl-tmp/div_cal_verify/results/`，Phase 1 → `/root/autodl-tmp/div_cal_verify/results_phase1/`
- **活跃进程**：Phase 1 GPT2 崩塌验证 PID 93696 (bash) / 93704 (python rgds)，GPU 1，tmux 无（nohup）
- **活跃 Cron**：`phase1_gpt2_collapse`，监控 PID 93696，600s 间隔
- GPU 0 有 ~49GB 僵尸显存（无对应进程，无法 reset，不影响实验）

### 3. 📊 当前状态
刚完成 MVP 结果分析并向 Director 提交 Framing 调整提案（NEGATIVE）。Director 批准 D004 高强度崩塌验证两阶段方案。

**Phase 1 正在跑**（`phase1_gpt2_collapse`, RUNNING）：GPT2-125M + GPT2-medium，1M tokens/gen，5 epochs，lr=1e-4，6 generations，串行跑 rgds → uncurated。预计 ~2h 完成。

Registry 活跃实验：
- `phase1_gpt2_collapse`: RUNNING — GPT2 快速崩塌验证（cuda:1）
- 其余全部 DONE（mvp_rgds_v1~v3, mvp_ext_v1~v2, mvp_serial_v3~v4 均已关闭）

等待：Phase 1 cron 回调（进程退出时触发）

### 4. 📋 待办
- Phase 1 cron 回调到达 → spawn worker 读日志和 metrics → 判断崩塌是否发生（RankMe 下降 >20%?）
- Phase 1 崩塌确认（RankMe >20% 下降 + PPL 恶化）→ 向 Director 汇报 → 准备 Phase 2 高强度 Qwen 实验（5M tokens/gen, 3 epochs, lr=5e-5, 6 gens, 3 方法串行双卡）
- Phase 1 崩塌未发生 → 向 Director 汇报 negative，说明即使极端训练也不崩塌 → 可能需要 pivot 研究方向
- Phase 1 崩溃/报错 → 诊断修复重跑（注意 uncurated 方法的 rank_correlation 已修复，但可能有其他 GPT2 兼容性问题）
- **uncurated 方法需验证**：这是第一次成功跑 uncurated（之前一直崩溃），注意观察是否通过

### 5. 🎯 战略上下文
- **核心科学问题**：student 模型的内部表征在迭代合成训练中是否会崩塌？如果崩塌，RGDS 的 failsafe 机制能否检测并缓解？
- **D001**: MVP 方案定义（3 方法 × 4 代 × WikiText-103）
- **D002**: MVP gate 改为二元 PASS/FAIL（RGDS vs external ≥5% PPL 改善）
- **D003**: 识别训练强度不足风险（250K tokens/gen 对 1.7B 模型几乎无影响）
- **D004**: MVP FAIL 确认，启动两阶段高强度验证
- **关键发现**：rank correlation 为负（-0.37~-0.39），internal 和 Contriever diversity scores 方向相反——可能是 interesting finding 也可能是 noise
- **易错点**：
  - 不要把 Phase 1 GPT2 结果直接和 MVP Qwen 结果对比（模型规模差 14x，训练强度差 20x）
  - GPU 0 的 49GB 僵尸显存是已知问题，不要反复尝试清理
  - `run_all_methods.sh` / `run_phase1.sh` 需要 `set -o pipefail`，否则 Python 崩溃会被 tee 吞掉
  - registry 状态机必须 PREPARING → QUEUED → ALLOCATED → RUNNING，不能跳步
  - 投稿目标 EMNLP 2026 ARR DDL 2026-05-25（剩 13 天），时间极紧


---
