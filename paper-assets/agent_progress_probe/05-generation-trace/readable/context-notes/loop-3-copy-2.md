# agent / loop_3.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`7483eff969a0b6e53cbc.json`](../../sessions/74/7483eff969a0b6e53cbc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T18:27:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `cuda:0`, `cuda:1`（bjb2-23165），其他 GPU 编号禁止使用
- 服务器别名 autodl-5090 / gpu-5090-2x-2 / bjb2-23165 指向**同一台机器**（D018 确认），仅 2×RTX 5090 32G，不是 4 张
- TWV ablation 梯度反转已确认（D037/D038），**不要再跑 TWV 相关优化实验**——σ=2.0 是孤立峰值，noise-level improvement
- Registry 中 temporal-label-model 的 σ 值错报（实际 2.0 记为 3.0），引用指标时以 twv-ablation 结果为准
- F1_stag=0.000 声明已证伪（D025/D026），论文中 OB 移除效应用 0.641（3-seed）不用 0.000
- LF holdout ablation 的自集 F1 **不可跨变体比较**（test set 大小/难度不同），禁止 claim "去掉 X 后 F1 更高"

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165，工作目录 `/root/autodl-tmp/agent_progress_probe`
- Python：需确认（可能 conda base 或 venv，前面 session 用的是 aml-train 镜像的 conda）
- GPU：2×RTX 5090 32G，cuda:0 + cuda:1，当前空闲
- 数据：embeddings + labels 在 `/root/autodl-tmp/agent_progress_probe/` 下
- HF cache：`/root/autodl-tmp/.hf_cache`（AutoDL 磁盘限制，根分区 30GB 禁存大文件）
- 活跃进程：无 RUNNING 实验。1 个 running worker `worker_code_twv-no-temporal-sigma2_20260514T182530`（代码编写任务，可能已完成待回调）
- Cron：reconcile 返回 0 条，无活跃 cron 监控

### 3. 📊 当前状态
**刚完成**：密集的一天——从 session 开始到现在完成了 ~20 个 Worker、38 个决策（D001-D038）。关键转折：
- D034/D035/D036：structural features 跨域碾压 probe（GB 0.967 vs probe FT 0.751），probe 作为核心贡献已死，论文 pivot 到 TLM + structural signal discovery
- D037/D038：TWV ablation negative（梯度反转：MV > no_temporal > full），TLM 从 core claim 降级为 "promising direction"，需 gold set 验证

**Registry 汇总**：41 实验，27 success / 7 negative / 2 failed / 3 killed / 2 stale(PREPARING/QUEUED)。**无 RUNNING 实验。**

**等待中**：
- Worker `twv-no-temporal-sigma2` running（代码任务，编写 TWV 无 temporal 版本 σ=2 的实验代码）
- 🔴 **Gold set 人工标注未启动**——材料就绪（650 样本+标注指南），等待用户确认标注人力。这是**唯一关键路径**

### 4. 📋 待办（条件触发式）
- `twv-no-temporal-sigma2` Worker 完成回调 → 读产出，评估是否值得跑（鉴于 D038 TLM 已降级，可能优先级很低）
- 用户确认标注人力 → 立即启动 650 窗口标注（SWE 450 + OH 200），这是打破 circular eval 的唯一出路
- 标注完成 → Fleiss κ ≥ 0.6 检查 → GO: 在 gold set 上验证 TWV vs MV（如果 TWV 在 gold set 上胜出，TLM 回升为 core claim）；NO-GO → Plan B（降级 Claim 1）
- data-scaling FAILED（FileNotFoundError 路径 bug）→ 修复重跑（低优先级，circular eval 内的实验）
- Director 发新指令 → 按指令执行，汇报时带 `[资源]` 行

### 5. 🎯 战略上下文
**论文当前三层贡献（D034 pivot 后）**：
1. ~~TLM 方法论~~ → **降级为 promising direction**（D038，TWV ablation negative，需 gold set 救活）
2. Structural signal discovery（stagnation 信号本质是结构性的，非语义性的）——需 gold set 验证才有 ground-truth 支撑
3. LF temporal dynamics + cross-agent analysis（robust 发现：2/3 LF 角色跨域一致，cmd_rep 反转）

**最易判断错的事**：
- 不要被 in-domain 高 F1（probe 0.906, structural 0.995）迷惑——这些全是 circular eval，MV 标签是 LF 的确定性函数。所有在 MV 标签上的新实验边际价值极低
- TWV σ=2.0 的 +0.57pp 看起来是 improvement 但在 multi-seed noise range（±1.1pp）内，且 σ=1.0/-8.4pp, σ=3.0/-2.4pp 说明不稳定
- Gold set 是**三个 claim 的共同根基**——没有它，论文只有 circular eval 数据，EMNLP reviewer 会直接打回
- 投稿 deadline 5/25（11 天），关键路径：标注(2-3天) → TLM gold set 验证(1天) → paper(3-4天) = 最少 7 天。今天不推标注就几乎来不及

**决策链关键节点**：D007(MVP pass) → D009(Dream WR, pivot to TLM) → D014(回退 EMNLP 5/25) → D020(OB 信号确认) → D034(structural crush probe, pivot) → D038(TWV negative, TLM conditional)


---
