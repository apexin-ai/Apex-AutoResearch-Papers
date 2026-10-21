# director / loop_1.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`fed1c92d839c3704baf5.json`](../../sessions/fe/fed1c92d839c3704baf5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T21:55:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-47453 的 cuda:0~3（项目配置 `execution.gpu_ids`），不可用其他服务器的卡
- MVP 混合数据比例必须是 **40% synthetic / 60% human**（D004），刚发现 Agent 组装成了 67% synthetic，已派指令修正但尚未确认修复
- Grid-b baseline 必须是 **fixed-b per training run**（每个 b 值跑完整训练），不是 per-batch 自适应选 b — 这个 bug 已修但要警惕回退
- Detector gate check 硬约束: AUC ≥ 0.95 且 ECE ≤ 0.05，不通过不能开始预训练
- 远程服务器用 conda 环境，python 在 `/root/miniconda3/bin/`，`python3` 不在 PATH，脚本必须先 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`

### 2. 🖥️ 基础设施快照
- 服务器: westd-47453, SSH `ssh -p 47453 root@connect.westd.seetacloud.com`, 密码存 secret `ssh_password_westd47453`
- GPU: 4× NVIDIA RTX PRO 6000 Blackwell Server Edition 96GB
- 工作目录: `/root/provenance_weight_training/`
- Python: `/root/miniconda3/bin/python` (conda base env)
- PyTorch 2.10.0+cu128, transformers 4.57.6, accelerate 1.13.0
- ModernBERT 需要 `TORCHDYNAMO_DISABLE=1`
- 模型缓存: Qwen3-0.6B 和 ModernBERT-base 已下载到默认 HF cache
- 人类数据: `/root/provenance_weight_training/data/human/{train,detector,eval_holdout}.jsonl` (120M/50M/50M tokens)
- 合成数据: `/root/provenance_weight_training/data/synthetic/` (4 shards, 132M tokens total)
- 本地代码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/`
- 活跃进程: 检测器训练在 cuda:0 运行中（ModernBERT-base fine-tuning）
- W&B/wandb: 未配置
- Cron: 无

### 3. 📊 当前状态
- **合成数据生成**: 完成（132M tokens, 退化率 0.87% 合格）
- **混合数据组装**: 已完成但比例错误（67% synthetic vs 目标 40%），已发指令修正，等 Agent 确认
- **检测器训练**: 正在 cuda:0 上跑（ModernBERT-base, 预计 15-45 分钟）
- **代码修复**: 全部 6 项 critical/warning 已修复并同步到远程（Reviewer 确认）
- Registry: 空（MVP 阶段尚未注册正式实验）
- 等待: Agent 回复混合数据修正确认 + 检测器训练完成回调

### 4. 📋 待办
- Agent 确认混合数据已修正为 40% → 继续等检测器完成
- 检测器训练完成 → gate check (AUC ≥ 0.95, ECE ≤ 0.05)：通过 → 对修正后的 mixed dataset 打 q(x) scores；不通过 → 让 Agent 排查（加数据/调超参）
- q(x) scores 就绪 → 启动 24 runs MVP 预训练（3 seeds × 8 configs: 1 uniform + 6 grid-b + 1 adaptive），4 卡并行 ~6 batch × ~2h
- 24 runs 全部完成 → eval (ppl + HellaSwag + MMLU) → compare_results.py 跑 multi-seed 聚合 → 判定 Pass/Fail
- MVP PASS → complete_mvp() 进入 research 阶段 → 写 paper_framing.md + experiment_plan.yaml + dream_simulate
- MVP FAIL → 按 kill criteria 分级处理（D004: Level 1 查校准 / Level 2 查 pipeline / Level 3 pivot）

### 5. 🎯 战略上下文
- 投稿目标: **EMNLP 2026 ARR May 25**（主攻，D003），AAAI 2027 后备。用户明确要求不要保守
- 核心假设: adaptive b*（从 α_eff 推导）无需 grid search 即可匹配/超越 grid-searched b
- 决策链: D001(AAAI 主攻) → D003(修正为 EMNLP 主攻，用户要求) → D002(MVP 设计) → D004(采纳 Reviewer 补全: 3 seeds/gate/grid定义/kill criteria)
- 12 天排期: Day 1-2 代码+数据（接近完成）→ Day 2-3 检测器+MVP → Day 3-7 全矩阵 → Day 7-10 论文 → Day 10-12 迭代提交
- 易错点: (1) RTX 6000 Pro 性能约 H100 的 50-60%，wall-clock 估算要乘 1.5-2x；(2) 200M tokens 对 0.6B 模型欠训练（0.33 tok/param），如果 3 seeds 方差大到条件间 CI 重叠，需增到 300-400M tokens；(3) 合成数据比例必须是 40% 不是 67%，这个错误刚被发现，确认 Agent 真的改了再放行预训练


---
