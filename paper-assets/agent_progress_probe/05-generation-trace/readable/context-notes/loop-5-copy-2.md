# agent / loop_5.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`46628304b7c60f4f1d8a.json`](../../sessions/46/46628304b7c60f4f1d8a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-15T01:12:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1 @ bjb2-23165**，无其他可用 GPU
- OH 数据必须用 **embeddings_fixed.pt**（stag_rate=21.45%），旧 embeddings.pt（6.56%）已废弃——旧数据上的所有结论已反转（D046-D051）
- Structural data scaling **禁止表述为 "data scarcity robustness"**——必须标注 circular eval caveat（structural features ≈ LF inputs，10% 即可逆向工程 LF→label）
- **禁止 "去掉 X 后 F1 更高" 的 claim**（LF holdout 实验跨 test set 偏移假象）
- 旧 **+17.6pp cmd_rep ablation claim 已死**——修复后反转为 -6.5pp，cmd_rep 核心价值是 coverage（-29.4pp prevalence-matched），不是噪声源
- Gold set 人工标注是 **GO/NO-GO gate**——论文成立的唯一 non-circular 验证，不可跳过或降级

### 2. 🖥️ 基础设施快照
- 服务器：**bjb2-23165**，工作目录 `/root/autodl-tmp/agent_progress_probe`
- GPU：RTX 5090 32G × 2（cuda:0 + cuda:1），当前空闲
- Python 路径：需 SSH 确认（可能 conda base 或 venv，先 detect_image）
- 模型 checkpoint：`checkpoints_full/best_model.pt`（probe_001, seed 42）
- Gold set pipeline：`evaluate_gold_set.py`（本地项目目录）
- 活跃进程：无 RUNNING 实验，无活跃 cron（reconcile=0）
- 3 个 Worker 运行中：
  - `worker_analysis_oh-crossagent-error-analysis_20260515T010007`
  - `worker_paper_framing-reaudit-full-fix_20260515T010601`
  - `worker_eval_gold-dryrun-v4_20260515T010911`

### 3. 📊 当前状态
实验主体全部完成。32 plan 中 31 个 DONE（24 success / 6 negative / 1 killed），1 个 planned（gold-set，等用户确认标注人力）。Registry 无 RUNNING/PREPARING 实验（gold-dryrun-v4 刚创建 PREPARING 由 Worker 处理中）。

刚完成的关键工作：
- OH 标签修复（embeddings_fixed.pt）+ 全部 OH 实验重跑（oh-full-finetune 0.976, oh-cmdrep-ablation 反转, cross-agent GB 0.998）
- f1-stag-analysis 完成：瓶颈 = recall_stag 0.77，85% 错误来自 OB-conflict 窗口
- paper_framing.md 已更新到 D051（Claim 2 reframing: temporal dynamics + label quality as transfer bottleneck）
- 论文核心技术章节（method/experiments/analysis）已有草稿，Intro/Related/Conclusion/Abstract 待写

等待中：
- 3 个 Worker 回调（error-analysis / framing-reaudit / gold-dryrun-v4）
- 用户确认标注人力（650 窗口 gold set，ROADMAP 标注最晚 5/16 必须启动）

### 4. 📋 待办（条件触发式）
- gold-dryrun-v4 Worker 完成 → 确认 pipeline end-to-end 通过 → 向 Director 汇报 "pipeline ready, 等用户确认标注人力"
- framing-reaudit-full-fix Worker 完成 → 检查全文一致性修复（旧 claim 是否全部清除，新 framing 是否贯穿）→ 送 Reviewer 审查
- oh-crossagent-error-analysis Worker 完成 → 整合到 analysis.tex §6
- 用户确认标注人力 → 启动 650 窗口标注 → 标注完成后 `evaluate_gold_set.py` 一键出结果
- Gold set 结果出来 → structural vs probe vs LLM-judge 三方对比 → 决定 Claim 1 最终措辞
- Paper 写作窗口：spawn Writer Workers 并行写 Intro / Related Work / Conclusion / Abstract（不依赖 gold set）

### 5. 🎯 战略上下文
**D039 Pivot 是项目转折点**：从 method paper（TLM 是主 claim）转为 empirical analysis paper（structural signal discovery 是主 claim）。TLM 三种实现全败，降为 Claim 3 negative finding。

**核心决策链**：D039（TLM 失败→pivot）→ D042-D044（baseline 引用规则）→ D047-D049（OH 标签修复）→ D050-D051（Claim 1/2 reframing）

**易错点**：
1. **不要混淆旧/新 OH 数字**——memory.md 和 registry 中同时存在旧值和新值，以 `data_note: "FIXED OH labels"` 为准
2. **Circular eval 贯穿全文**——structural 0.9951 in-domain 是 circularity 上界，不是检测能力证明；只有 gold set 能验证真实能力
3. **DDL 5/25 只剩 10 天**——gold set 标注是关键路径，论文写作可以并行推进但 gold set 不可替代
4. **Probe 50% FT 追平 structural（0.968≈0.967）**——Claim 1 不是 "structural 永远更好"，而是 "零数据部署的默认选择 + 有数据时收敛"
5. **cmd_rep prevalence-matched ablation -29.4pp**——这是 coverage 贡献证据，不是 "cmd_rep 很重要所以不能去"


---
