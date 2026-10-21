# agent / loop_3.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`fb1e6c70d640ec16d78e.json`](../../sessions/fb/fb1e6c70d640ec16d78e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T17:58:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（均在 rtx5090-4x 上）。rtx5090-4x 和 gpu-5090-4x-1 是同一台机器（D004），不要当两台用
- submit_training_job 的 command 如果包含 source/conda activate 必须 bash -c 包裹；但 r3/r5 系列用 `python -m freige.training.grpo_trainer ...` 直接提交成功，不需要 bash -c
- kl_coef + QLoRA 4-bit 不兼容（D008）：kl_coef>0 时 KL 会爆炸到 10^8-10^11。ced_kl001 (kl_coef=0.01) 正在验证这个边界——如果也爆了，结论是"kl_coef 必须严格为 0"
- SFT eval 用 `--quantize` 标志 + batch_size=16，所有 GRPO checkpoint eval 必须用同样配置保证 apple-to-apple

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x（别名 gpu-5090-4x-1），4× RTX 5090 32GB
- 工作目录：/root/autodl-tmp/（conda base 环境）
- Python：/root/miniconda3/bin/python（conda base，不用 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：/root/autodl-tmp/models/Qwen3-4B（base）、/root/autodl-tmp/sft_output（SFT checkpoint）
- 数据：/root/autodl-tmp/data/docred（train 3027, dev 985）
- NLI cache：/root/autodl-tmp/nli_cache/
- SFT eval 输出：/root/autodl-tmp/sft_eval_results/
- HF cache：/root/autodl-tmp/.hf_cache
- 活跃进程（提交时间 2026-05-14）：
  - mvp2_grpo_ced_r5: cuda:0, PID 53066, tmux=mvp2_grpo_ced_r5
  - mvp2_grpo_ced_kl001: cuda:1, PID unknown（刚提交）, tmux=mvp2_grpo_ced_kl001
  - mvp2_grpo_extract_r3: cuda:2, PID 53144, tmux=mvp2_grpo_extract_r3
  - mvp2_grpo_flatnli_r3: cuda:3, PID 53287, tmux=mvp2_grpo_flatnli_r3
- Cron 监控：ced_r5, extract_r3, flatnli_r3 各有 cron（ced_kl001 的 cron 应由 submit_training_job 自动注册）

### 3. 📊 当前状态
**刚做完**：收到 mvp2_sft_eval_r2 CRON 完成回调 → 派 Worker (worker_analysis_mvp2_sft_eval_r2_20260514T145314) 分析结果 → 提交 ced_kl001 到 cuda:1 → 向 Director 汇报

**等待中**：
- Worker 回调：analysis worker 正在 SSH 读取 sft_eval_r2 日志和输出文件，提取 SFT baseline 指标（Rel-F1, Evi-F1）。**这个回调到了必须立即处理**——更新 registry 为 DONE + 设 metrics/conclusion，然后向 Director 汇报完整 baseline 数据
- CRON 回调：4 个 GRPO 训练中，预计 8-16h 后陆续完成
- mvp2_sft_eval_r3 (PREPARING)：统一 eval 代码版本的 eval，等有空闲 GPU 或 Director 决定是否需要

**Registry 快照**：
- RUNNING: ced_r5 (cuda:0), ced_kl001 (cuda:1), extract_r3 (cuda:2), flatnli_r3 (cuda:3)
- ANALYZING: mvp2_sft_eval_r2（Worker 正在分析）
- PREPARING: mvp2_sft_eval_r3, mvp2_grpo_ced_kl001→已提交应已转 RUNNING

### 4. 📋 待办（条件触发式）
- **analysis worker 回调到达** → 读取 SFT baseline 指标 → update_registry(mvp2_sft_eval_r2, status=DONE, metrics=...) → 更新 report.md → 向 Director 汇报完整 baseline（这是 MVP-2 pass criteria 的锚点）
- **ced_r5 完成** → spawn worker eval best+last checkpoint（统一 eval 脚本，--quantize, batch_size=16）→ 与 SFT baseline 对比 Evi-F1，核心 pass criteria: (CED_Evi-F1 − SFT_Evi-F1) ≥ 2pp
- **extract_r3 完成** → eval → 与 SFT baseline 对比 F1（回答 "GRPO 本身是否改善 F1"）
- **flatnli_r3 完成** → eval → 与 SFT baseline 对比 Evi-F1（消融: 简化 NLI reward 效果），然后 CED vs flat-NLI 方向正确即可
- **ced_kl001 完成** → 若 KL 爆炸 → 结论 "kl_coef 必须严格为 0 in QLoRA"（对论文有价值的 negative finding）；若稳定训练 → 与 ced_r5 对比，回答 kl_coef 边界
- **所有 4 路 GRPO + SFT eval 完成** → 构建完整对比矩阵 → MVP-2 判定 → 向 Director 汇报 pass/fail + 建议下一步（post-MVP 或 pivot）
- **有 GPU 空闲且 Director 无其他指令** → 提交 mvp2_sft_eval_r3（统一 eval 代码对比）

### 5. 🎯 战略上下文
- **核心假设**：CED（对比证据判别）reward 能让 LLM 在 DocRE 中同时改善抽取 F1 和证据质量 Evi-F1
- **MVP-1 已通过**：CED 信号验证 margin=0.48, accuracy=81.5%, r=0.34
- **SFT warmup 已通过**：eval_loss=0.72, accuracy=83.5%
- **关键发现 D008**：kl_coef + QLoRA 4-bit 不兼容，KL 值爆炸到 10^8+。r1/r2/r3 全因此失败。当前 r5 系列全部用 kl_coef=0.0 跑
- **决策链**：D002(MVP-1 pass) → D003(smoke pass) → D005/D006(r1 mode collapse) → D007/D008(KL爆炸根因) → D009(保守配置) → D010(保留 kl=0 实验) → D011(Reviewer 评估框架)
- **MVP-2 pass criteria**（D011）：CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp，F1 不退化 ≤ 5pp，CED > flat-NLI 方向正确
- **易错点**：
  1. 不要把不同 eval 配置的结果直接对比（必须统一 --quantize + batch_size=16 + 同一 parsing）
  2. kl_coef=0 有稳定性风险，必须 eval best reward checkpoint + last checkpoint，不能只看最终
  3. flatnli_r3 的 `--ced_reward_weight 1.0` 实际含义是 evidence reward weight（stage 2 = flat-NLI，不是 CED），命名容易误解
  4. report.md 的 auto-facts 部分可能未反映最新提交（ced_kl001），下一轮应该 reconcile_crons 后自动更新


---
