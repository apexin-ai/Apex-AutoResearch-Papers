# director / loop_1.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`25942bf14e440e20dac1.json`](../../sessions/25/25942bf14e440e20dac1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-12T14:56:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 @ cqa1-38874（项目配置白名单唯一一张卡）
- cqa1-38874 是 AutoDL 实例，所有 tmux/submit 命令必须 `source /root/collapse-aware-mixing/env_init.sh` 开头（含 network_turbo + conda + SSL + HF_HOME + TRANSFORMERS_OFFLINE=1 + HF_DATASETS_OFFLINE=1）
- 不要用 `source` 执行含 `exit` 的脚本（用 `bash` 代替）——v4 第 5 次崩溃的根因
- 数据集是 wikitext-103-raw-v1（D003 决策），pack 后只有 57,052 sequences，tokens_per_generation 不能超过 90M（holdout=5000）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (connect.cqa1.seetacloud.com)，1×RTX PRO 6000 Blackwell 96GB
- 工作目录：`/root/collapse-aware-mixing/`（代码），`/root/autodl-tmp/output/`（输出）
- Python：`/root/miniconda3/bin/python3`，conda base 环境
- HF cache：`/root/autodl-tmp/.hf_cache/`（wikitext-103 + Pythia-1B 已缓存）
- 关键脚本：`env_init.sh`（环境 preamble）、`preflight.sh`（8 项 pre-flight）、`launch_pilot_v4.sh`
- 活跃进程：mvp_pilot_v4（PID 28147，tmux=mvp_pilot_v4，cuda:0），cron 已注册
- 日志：`/tmp/pilot_v4.log`
- W&B：未配置（--no_wandb）

### 3. 📊 当前状态
mvp_pilot_v4 在 GPU 上训练中（确认 GPU 100% 利用率）。参数：Pythia-1B，3 代 × 90M tokens，每 10M tokens 一个 checkpoint（152 steps），seed=42。G0 训练中，预计全流程 3-4 小时完成。

Registry: mvp_pilot_v4 RUNNING（当前运行可能未正式注册到 registry——Reviewer 上次提了 warning，让 Agent 补注册）。mvp_pilot / v2 / v3 均 DONE(failed)。

等待中：pilot 完成后 cron 回调 → Agent 读取 pilot_summary.json → 汇报给 Director 做 GO/NO-GO 判定。

### 4. 📋 待办
- pilot 完成 cron 回调 → Agent 读 pilot_summary.json 的 mvp_check 字段 → 汇报完整指标给你
- mvp_check verdict=GO（谱有效秩 lead PPL ≥1σ + KL>0.1）→ 调 complete_mvp()，进入 research 阶段，写 paper_framing.md + experiment_plan.yaml + dream_simulate
- verdict=CONDITIONAL_GO（谱与 PPL 同步但 CV 更小）→ pivot 到 secondary framing（higher-resolution indicator）
- verdict=KILL / EXTEND → 按 ROADMAP NO-GO 决策树行动
- MVP 通过后 → 向 Manager 申请扩容 GPU（全量实验需 ~200 H100-hours，当前 1 张卡不够）
- 全量实验代码已就绪：controller.py（PI 控制器，14 测试通过）、main_experiment.py（3 条件对比）、golden_ratio_baseline.py——Reviewer 审查的 3 个 bug 已修复（optimizer state 连续 / KL 传参 / golden ratio 默认 0.618）

### 5. 🎯 战略上下文
- 项目核心：用谱塌缩指标（embedding Gram 矩阵有效秩）驱动 PI 控制器动态调混合比，目标 EMNLP 2026 ARR（DDL 2026-05-25，剩 13 天）
- 决策链：D001（MVP 方案：Phase 0 pilot）→ D002（量化 GO/NO-GO 标准）→ D003（OpenWebText→wikitext-103，500M→90M tokens/gen）
- 6 次启动失败的教训全部沉淀在 env_init.sh + preflight.sh 中，后续实验不应再踩。但要注意 Agent 有"不读完整指令就执行"的倾向——参数不匹配问题（v4 第 6 次失败）就是 launch 脚本没传 CLI 参数导致 argparse 默认值覆盖 config.py
- 易错判断：如果 pilot 结果是 CONDITIONAL_GO（谱不 lead 但粒度更细），secondary framing（higher-resolution indicator）仍然有独立价值，不要轻易 KILL。IDEA_BRIEF 的 Human Review Note 建议的叙事方向是 NLP-research-problem-driven（"迭代合成预训练如何结构化损害语言能力"），不是 controller-design-centric
- 全量实验的主对比对象是 golden ratio 1/φ ≈ 0.618（不是 0.5），这是 IDEA_BRIEF 的核心 claim


---
