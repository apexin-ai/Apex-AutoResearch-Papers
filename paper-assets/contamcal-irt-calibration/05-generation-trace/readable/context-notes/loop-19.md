# director / loop_19.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_19.md`
- **Structured JSON:** [`ff23faba1e01e948341c.json`](../../sessions/ff/ff23faba1e01e948341c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_messages
updated: '2026-05-21T07:28:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd cuda:0/1/2/3 + cqa1 cuda:0，严禁用白名单外的卡
- lora_alpha=32 是 C006 硬约束，每次 adapter 验证必须确认
- C009 evaluate.py 有两个版本（37591 vs 37775 bytes），当前所有 eval 统一用 37775 版本，不要混用同一 seed 的 eval 结果
- 论文 8 页主体限制（EMNLP 2026），refs/limitations/appendix 不计入
- 禁止 kill GPU 进程来做 CPU 操作（M041 教训）
- Bootstrap CI 汇报必须列出实际 seed 列表和数据源路径（M039 教训）
- Abstract 中 "+2.4pp mean" 是 Gemma-2 MMLU n=3 均值（非单 seed）

### 2. 🖥️ 基础设施快照
- **westd-29999**: connect.westd.seetacloud.com, root, 代码 `/root/contamcal-irt-calibration`
- **cqa1-21977**: connect.cqa1.seetacloud.com, root, 代码 `/root/contamcal-irt-calibration`
- 两台均 aml-train 镜像：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`/root/autodl-tmp/models/` (Qwen2.5-7B, Qwen2.5-14B, google/gemma-2-9b, microsoft/phi-4, allenai/OLMo-2-7B)
- Checkpoints: `/root/autodl-tmp/exp001/checkpoints/{model}_{dosage}_{seed}/lora_adapter/`
- Eval 结果: `results/` (mmlu_eval/, arc_eval/, gsm8k_eval/) + legacy `eval_results_v2/`
- 论文本地路径: `projects/contamcal-irt-calibration/docs/paper/`
- 活跃进程（westd）：
  - cuda:0: Gemma-2 s0 GSM8K batch (PID 492703)
  - cuda:1: Qwen-14B d100 s0 GSM8K (PID 481803, ~70%)
  - cuda:2: Qwen-14B d050 s0 GSM8K (PID 492186)
  - cuda:3: Phi-4 s0 GSM8K batch (PID 493644)
- cqa1 cuda:0: 空闲
- 数据归一化 Worker: s0 数据从 results/ 复制到 eval_results_v2/（进行中）

### 3. 📊 当前状态
**刚做完**：
- 5/5 家族 n=3 BCa bootstrap CI 全部通过数据完整性审计（D200）
- Gemma-2 ARC s42 "幽灵数据" 问题解决——来自 sweep，经独立 eval 证实 CI 不变 [-1.97, +1.42]
- Paper Agent 完成 Qwen-14B n=3 全文 patch + 数值一致性检查（编译通过，正文 8 页）
- 论文已提交审稿：`submit_paper_to_review` → approval_id `apr_20260521T071147_h94l`（pending 用户批准）

**等待中**：
- 用户批准审稿提交（continue mode，验证 16/18 resolved issues）
- Reviewer 核实 Qwen-7B n=3 状态（Agent 说 n=3 ✅，Reviewer 最新报告说 n=2 — 有矛盾，已 post_to_reviewer 请求澄清）
- 4 张卡跑 GSM8K eval（info-level，appendix 补充数据，不阻塞提交）
- 数据路径归一化（CPU 任务，进行中）

### 4. 📋 待办（条件触发式）
- 用户批准审稿 → Review Director 接手，等审稿报告回来 → 按 review-report-action skill 处理
- Reviewer 回复 Qwen-7B n=3 核实结果 → 如果确认 n=2，需要 SCP s0 数据到 westd 重跑 bootstrap；如果确认 n=3，关闭此项
- GSM8K eval 完成 → 收集结果，写入 appendix（Qwen-14B Collapse 跨 benchmark、Qwen-7B Benefit 跨 benchmark）。GSM8K 不进主表
- 审稿报告回来 → 读 review-report-action skill → Holistic Pass → Per-Comment Action Matrix → 派 Agent/Paper Agent 修改
- **5/5 n=3 + 审稿修改完成 → 终稿提交（目标 May 24-25，ARR DDL）**

### 5. 🎯 战略上下文
- **核心论文**: "Not All Models Are Inflated" — SFT contamination 产生 4 种 dose-response pattern（Immune/Collapse/V-recovery/Benefit），非统一 inflation
- **5/5 n=3 CI 汇总**：Phi-4 Immune, OLMo-2 Benefit, Qwen-7B V-recovery, Gemma-2 Benefit(MMLU)/Inconclusive(ARC), Qwen-14B Collapse。Dir-Con 4/5（Gemma-2 例外）
- **关键决策链**: D198(Gemma-2 benchmark-conditional) → D199(cross-benchmark 4/5→3/5) → D200(5/5 n=3 完成)
- **review_issues**: 16/18 resolved。R1-C2 (cross-family MAE CI) + R6-W2/W3/W4 (info) 未关闭，均不阻塞
- **最容易判断错的事**：
  - Qwen-7B n=3 状态有矛盾（Agent 说 ✅，Reviewer 说 n=2）—— 先核实再做决策
  - bootstrap_triple_seed.py 只读 eval_results_v2/，但 s0 数据在 results/ — 数据归一化完成前不要用这个脚本验证 n=3
  - Gemma-2 ARC s42 中间 dosage 极端波动（d005=77.82%, d050=71.08%）是真实数据不是 bug，但 d100-d000 delta 正常
  - `paper_compile_and_check` 的 max_pages=8 会报 over_limit（它算总页数 18），实际正文 8 页符合 EMNLP 限制
  - `check_paper_consistency` 报 3 个 orphan bib 是误报（`\citealp{}` 不被解析）


---
