# agent / loop_2.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`5c6647139b3cd21c5886.json`](../../sessions/5c/5c6647139b3cd21c5886.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-14T14:27:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`autodl-5090:cuda:0`, `autodl-5090:cuda:1`, `gpu-5090-2x-2:cuda:0`, `gpu-5090-2x-2:cuda:1`——其他设备号禁止使用
- autodl-5090 是 conda 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），**不要假设 .venv 存在**
- conf≥2 子集 (15,401 windows) 是主实验数据，全量 (54,809) 用于 robustness 分析——不要混淆哪个是主结果
- LF Oracle 在 conf≥2 上有循环论证问题（command_repetition 单 LF 0.9451 > probe 0.9055），论文必须透明讨论
- OpenRouter API key: `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`——LLM judge baseline 正在用

### 2. 🖥️ 基础设施快照
- **autodl-5090**: `/root/autodl-tmp/agent_progress_probe`, Python `/root/miniconda3/bin/python`, torch 2.10+cu128, conda base。密码 `H6BKr9xWo+8Z` 端口 23165
- **gpu-5090-2x-2**: `/root/autodl-tmp/agent_progress_probe`, account root。OpenHands embedding 双卡任务可能已完成（Worker 正在核查）
- Embeddings: `/root/autodl-tmp/agent_progress_probe/embeddings/`，emb_001 产出 1.1GB（54,809 windows, dim=1024）
- W&B 未配置，实验用 `train_history.json` / `results/*.json` 记录
- **活跃进程**: LLM judge 全量评估在 autodl-5090 运行中（原 PID 27419），160/1824 windows 完成，macro_f1=0.5388，预估 ~10min 完成

### 3. 📊 当前状态
刚完成 session 初始化 + OpenRouter key 获取。5 个实验全 DONE(success)，1 个 PREPARING(baseline-llm-judge)。

**运行中 Workers:**
- `flyingsquid-baseline`（20 turns，调试 predict_proba 接口问题）
- `annotation-prep`（准备人工标注材料和样本）
- `gpu-status-check`（核查两台服务器 GPU 占用，13 turns 检查 embeddings）

**等待中:**
- LLM judge 全量评估完成 → 需 Worker 读取最终结果、更新 registry
- gpu-status-check 回调 → 确认 OpenHands embedding 状态、GPU 空闲情况
- flyingsquid-baseline 回调 → FlyingSquid label model 结果
- annotation-prep 回调 → 人工标注材料产出

### 4. 📋 待办
- LLM judge 评估完成 → spawn worker 读 `results/llm_judge_full_zeroshot.json`，update_registry baseline-llm-judge → DONE，与 probe(0.9055) 对比汇报 Director
- gpu-status-check 回调显示 GPU 空闲 → 立即铺 outcome-bp-sensitivity 实验（ROADMAP 近期任务）
- OpenHands embedding 确认完成 → 启动 cross-agent probe 训练 + 评估
- annotation-prep 完成 → 发标注材料给 Director，推动人工标注启动（GO/NO-GO gate 前置依赖，5/16-17 检查点）
- flyingsquid 完成 → 记录 FlyingSquid baseline 指标，与 majority vote / probe 对比
- Director 回复状态汇报 → 根据指令调整优先级

### 5. 🎯 战略上下文
- **投稿目标**: EMNLP 2026 ARR 5/25 cycle，剩 11 天。关键路径 = 人工标注 → GO/NO-GO gate → temporal-label-model
- **核心 framing**: D009 后从 "lightweight probe" 升级为 "temporal label model"（三层贡献）。Dream 审稿三档均 Weak Reject(3/6)，novelty 不足是结构性问题，新 framing 尚未验证
- **GO/NO-GO gate (5/16-17)**: 人工标注完成后验证 Fleiss κ ≥ 0.6 + LF temporal roles 在 gold set 上成立 → GO temporal-label-model；否则 Plan B（降级为 empirical study）
- **易错点**: probe-002 全量数据 macro-F1=0.8468 远低于 conf≥2 的 0.9055——汇报时必须区分哪个数据集。multi-seed 的 0.9185 是 conf≥2 上的结果
- **决策链**: D007(MVP pass) → D009(Dream WR, framing 升级) → D013(gate temporal-label-model on gold set) → D014(EMNLP 5/25) → D015(cross-agent LF 适配修复)
- **资源**: 用户承诺 GPU + 标注人力管够，禁止 fallback 思维


---
