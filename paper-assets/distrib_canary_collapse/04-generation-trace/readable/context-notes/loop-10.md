# director / loop_10.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`468ef5ce1b98eb616a44.json`](../../sessions/46/468ef5ce1b98eb616a44.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-17T16:31:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-19828 的 cuda:0 和 cuda:1，仅此两张，不可用其他卡
- OPT-1.3B Threshold Onset bug 已修复，后续分析必须用 `analyze_generalize.py`（导入 `method_ablation.py` 的 `_onset_gen`），禁止用 `analyze_opt1b_full.py` 的旧 `_onset` 函数
- Table 5 GPT-2m 行只有 6 pairs（无 MAUVE），其他行 8 pairs，表格 caption 已注明
- VERSION A 已确认 (D054)，不可降级回 VERSION B 除非新数据明确否定

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828 (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/autodl-tmp/distrib_canary_collapse
- 磁盘：879G 可用（3% 已用）
- 活跃进程（RUNNING）：
  - `generalize_pythia1b_c4_a100_s42_v2` — cuda:0，Pythia-1B/C4 跨域实验，ETA ~20:00-22:00 UTC
  - `generalize_pythia14b_wiki_a100_s42` — cuda:1，Pythia-1.4B/WikiText scale check，PID 274091，ETA ~22:00-00:00 UTC

### 3. 📊 当前状态
本轮完成的关键工作：
- OPT-1.3B 训练完成 + Threshold Onset bug 修复 → K≥4/5 从 2/8 恢复到 6/8
- VERSION A 确认 (D054)：三架构 (Pythia-410M, GPT-2m, OPT-1.3B) 全部 K≥4/5 ≥ 6/8，PermG 方向性完美
- Paper Agent 完成：文献对比表 (tab:method-comparison)、Table 5 三行填充、Contribution 4 升级为 "three families"、五行预写框架（含 [TBD] placeholder）、Limitations scale 约束声明
- C4 实验之前 v1 失败（模型下载问题），v2 用 aria2c 修复后重启成功
- 两卡满载等实验完成

等待中：两个 RUNNING 实验完成后的 cron 回调 + 5-method 分析

### 4. 📋 待办
- Pythia-1.4B 训练完成 → 触发 8-pair 6-method 分析（用 analyze_generalize.py）→ 如果 K≥4/5 ≥ 6/8 → 填 Table 5 Scale 行 + 激活 Discussion/Conclusion 条件式草稿
- Pythia-1B/C4 训练完成 → 同上分析 → 如果 K≥4 ≥ 4/8 → 填 Table 5 Domain 行 + 激活条件式草稿；如果 K≥3 但不到 K≥4 → 用 Reviewer 建议的 "domain sensitivity qualifier" 叙事（方向性保持即可）
- 两个实验都完成 + Table 5 填满 → Contribution 4 升级为 "three architectures with scale and domain robustness"（一条 contribution 不拆两条，Reviewer 建议）→ 提交 Round 2 审稿 (`submit_paper_to_review`)
- 用户要求"执行文献对比表" → 已完成 ✅

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 Main Track（ARR June cycle，DDL ~June 15）
- 核心 narrative (D027 Option B)：方法论陷阱 + 多方法共识框架，canary prediction 为 case study
- D054 VERSION A confirmed：三架构全部达到 Tier 3 consensus，论文从 borderline 提升到 accept 水准
- Reviewer 评估：claim 升级不要拆成独立 contribution，保持 "three architectures with scale and domain robustness"；Limitations 需要写 "≤1.4B, 7B+ 是 open question"（已加）
- 易错点：(1) C4 可能部分正向（K≥3 不到 K≥4），这不是 VERSION B 回退，用 "domain sensitivity qualifier" 处理即可（只要 PermG 方向性保持）；(2) Pythia-1.4B 和 Pythia-1B/C4 是不同模型规模，Table 5 每行独立，不交叉 scale×domain；(3) Paper Agent 预写了大量注释块标 [CONDITIONAL]，数据到了取消注释 + 填数字即可
- 23 个成功实验，累计 GPU ~8.4h，Paper Agent session 活跃


---
