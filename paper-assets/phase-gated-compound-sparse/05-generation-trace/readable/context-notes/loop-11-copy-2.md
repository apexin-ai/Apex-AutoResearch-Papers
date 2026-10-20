# reviewer / loop_11.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`343ea30a0e6a71214496.json`](../../sessions/34/343ea30a0e6a71214496.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-16T02:29:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0~3（westd-22162 4× RTX 6000 Pro Blackwell）。当前 4 卡全空闲。
- DS accuracy 数据仅作定性观察（D086），QW 是 accuracy dose-response 定量主力。
- DS s030 截断计数已修正为 38（非 39），truncation_rate=76%（非 78%），non_truncated_accuracy=16.7%（非 18.2%）。论文已同步修正，但 registry conclusion 字段被错改为 "success"（应为 "negative"，4% accuracy）。
- 论文数据集名为 MATH-500，不是 GSM8K。刚修正过一次 critical 错误，防止回退。

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162(root)，代码根 /root/autodl-tmp/pacs
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct
- 评估脚本：/root/autodl-tmp/pacs/run_accuracy_eval.py（argparse default max_new_tokens=8192）
- 论文本地路径：artifacts/_project/paper/*.tex
- Figure data：artifacts/dose_curve_figure_data.json（已验证与修正后 registry 一致）
- 活跃进程：无。4 GPU 全空闲。无 cron/tmux 活跃。
- Registry：121 experiments，baseline=null

### 3. 📊 当前状态
刚完成 Round 10 写作审查。发现 2 critical（MATH-500 命名错误 + DS s030 过时数字）+ 2 warning，Paper Agent 已全部修正，我已验证 PASS。

RUNNING/PREPARING 实验：无。全部 38 plan experiments 完成（coverage 92.1%）。

等待中：Director 正在处理 Round 10 审稿报告 Action Matrix。涉及 LLaMA n=250 补实验、MATH-500 phase validation、bib 审计、track 决策（Main→Findings）等。我已收到 Action Matrix 全文但尚未回复审视意见。

### 4. 📋 待办
- Director 等待我对 Action Matrix 5 个问题的独立意见 → 逐条审视可行性（特别是：W-C3 LLaMA n=250 GPU 优先级、W-C4 circularity 论证、W-C2 track 选择、W-W3 H2O scoring 可行性）
- LLaMA n=250 实验启动 → 审查 GPU 合规（必须在 cuda:0~3 内）+ 验证用的是 DeepSeek-R1-Distill-Llama-8B
- Paper Agent 提交 bib 审计结果 → 用 reference-audit skill 独立核实
- Paper Agent 提交修订稿 → 做第 2 轮写作评审（评分模板）
- 任何新实验 DONE → 标准审计（数据一致性 + GPU 合规 + 结论可靠性）

### 5. 🎯 战略上下文
- 截稿 2026-05-25（~9 天），GPU 预算充裕（36h/250h used）
- 核心结论稳固：importance compound severity 随 sparsity 单调递增，n=500 confirmed（DS ρ=1.0 p=0.042, QW ρ=1.0 p=0.042）
- C4 entropy mechanism 是最薄弱环节：QW 在 s025 反转。Coverage 50%。论文必须限定为 model-dependent。
- C5b mitigation FAIL（oracle recovery 18% < 30% gate）→ 已降为 future work
- QW s015/s025 的 combined n100 数据存在于 acc_qw_s015_n100 / acc_qw_s025_n100 条目中（非 b1_8k 条目），之前误报为缺失。实际值：s015=0.42, s025=0.33。
- 易错点：(1) 原始 batch2 全部用了 8k default（已验证 JSON），b2_fix 实验是多余的；(2) DS extraction failure ≠ truncation，Agent 历史上反复混淆这两者；(3) LLaMA random 也有 non-trivial phase gradient（d_z 0.35-0.44），与 DS/QW pattern 不同，论文不能 over-claim cross-architecture consistency


---
