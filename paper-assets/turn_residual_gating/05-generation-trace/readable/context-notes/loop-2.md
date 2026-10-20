# director / loop_2.md

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`ad494b854e0ae5e707e4.json`](../../sessions/ad/ad494b854e0ae5e707e4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-21T01:26:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**：仅 `westd-20861:cuda:0`（1×RTX PRO 6000 Blackwell, 102GB）。westd-22162/home-1x5090/westd-16980 **不在项目 gpu_ids 和 SSH config 中**，Reviewer 已正式确认（D043），System 反复追问此问题——直接引用 D043 终结，不再讨论。
- **seetacloud-bjb2-structtts 不属于本项目**，连接问题不管。
- **v8b 训练期间 GPU 不可共享**（M019 OOM 教训：eval + training 共享 98GB GPU 导致 OOM crash）。Llama TG 同理。
- **paper_framing.md SP1**：30× gap 在 **GAR-ours** 上测得（非 GAR-Dongre）。已修复，但下一个"你"如果改 framing 文档务必保持正确。

### 2. 🖥️ 基础设施快照
- **服务器**：westd-20861 (connect.westd.seetacloud.com)，工作目录 `/root/turn_residual_gating`
- **Python**：conda base 环境（`/root/miniconda3/bin/python`），aml-train 镜像
- **模型**：Qwen-2.5-7B 和 Llama-3.1-8B-Instruct 均在服务器本地（具体路径需 Agent 确认）
- **活跃进程**：Llama TG 训练 PID 199643，tmux=llama_tg，cuda:0，65% 完成，ETA ~12:00 UTC（约 2-3h）
- **v8b SS s123 脚本**：`launch_v8b_ss_s123.sh` 已就绪，Reviewer 确认无需修改（连续 3 epoch，与 s42 SS ratio 轨迹完全等价）

### 3. 📊 当前状态
**刚做完**：
- Reviewer 整体 story 审视（PASS，叙事 tight，5 negative 全已诊断）
- N=50 gen steering 聚合修复 + Paper 整合（3 commits: 474a9f3, 8bb82f8, 4cc5b24）
- §6.5 Llama cross-model preliminary 写入论文（commit 760d758）
- paper_framing.md SP1 GAR 指标名称 critical 修复
- ROADMAP 评分预估修正 ARR 3.0-3.5 + ablation 精简（D043）

**正在运行**：
- `llama_tg_training`：Llama-3.1-8B TG 训练，epoch 1 step ~1950/3000 (65%)，gate V-shape 与 Qwen 一致，ETA ~2-3h
- Agent 已收到指令：训练完成 → Llama eval (3-way: Base/TG/LoRA-only) → 汇报 → 启动 v8b SS s123

**等待中**：Agent 的 Llama TG 完成回调（cron 可能有监控间隔问题，上一次 4.8h 无回调）

### 4. 📋 待办（条件触发式）
- **Llama TG 完成** → Agent 启动 Llama 3-way eval（GAR-ours + GAR-Dongre + PPL）→ 汇报跨模型对比 → 如果 IID GAR ≈ 0.50 且 model-gen GAR 复现 30× gap → C5 claim 从 preliminary 升级，派 Paper Agent 更新 §6.5 + Abstract/Intro scope wording 从 "(Qwen-2.5-7B)" 扩展为 "(Qwen-2.5-7B, Llama-3.1-8B)"
- **Llama eval 完成** → 立即启动 multi-seed v8b SS s123（`launch_v8b_ss_s123.sh`，~8h）→ 与 s42 对比确认 C7 claim 统计可信度
- **v8b s123 完成** → 启动 multi-seed v7 TG s123（~6h）
- **Llama Phase 2 失败**（model-gen 不复现 30× gap）→ C5 降级为 footnote "Phase 1 confirms cross-model presence; method transfer remains open"，不影响其他 claim

### 5. 🎯 战略上下文
- **论文定位**："First empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization, with dual mitigation paths"。不是 solution paper，是 diagnostic + constructive directions。
- **评分上限**：Overall 8-8.5/10 ≈ **ARR 3.0-3.5 (Findings-Borderline Conference)**。天花板是 Originality（exposure bias 概念已知）。达到 4.0 需 downstream task eval 或更多模型——当前不在 plan 中。
- **关键决策链**：D037(steering 里程碑) → D038(Base TRC 无信息量) → D039(eval_200 P0) → D040(实验排序) → D041(v8b SUCCESS) → D042(C5 跨模型确认) → D043(ablation 精简)
- **易踩的坑**：(1) System 会反复追问空闲 GPU（westd-22162 等），直接引用 D043 Reviewer 确认终结；(2) Agent cron 回调可能丢失（本轮已发生两次），训练 ETA 到了要主动派 Agent 检查而非等回调；(3) N=5 和 N=50 gen steering 的 β=0 baseline 不可直接对比（数据源/对话长度不同），论文已处理但改写时注意保持；(4) "phase transition" 改为 "sharp nonlinearity"，全文已清理但新增文本不要用旧术语


---
