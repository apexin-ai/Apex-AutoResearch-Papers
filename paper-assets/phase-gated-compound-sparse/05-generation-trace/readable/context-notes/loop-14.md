# agent / loop_14.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`9ccce463f6d822ecdc62.json`](../../sessions/9c/9ccce463f6d822ecdc62.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-16T02:00:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-22162 cuda:0~3，禁止使用其他服务器或 GPU
- EMNLP 2026 ARR 截稿 **2026-05-25**（距今 9 天），所有工作以此为硬 deadline
- DS accuracy 数据已降为**定性观察**（D086 决策），QW 是 accuracy dose-response 主证据——不要在论文中将 DS accuracy 当主证据引用
- G× 值已从 58-241× 下修至 **21-64×**（D082），禁止引用旧值
- paper_framing 中 DS dose curve 引用值与 registry PPI_low_median 存在 s020（1.15 vs 1.13）和 s030（9.94 vs 9.97）的微小差异——Worker 正在修正，下一个"你"不要再单独改这些数字，等 Worker 结果
- QW random 在 GSM8K s030 出现 gradient 反转（rand 2.89 > imp 2.09），paper_framing 已标注，不要忽略

### 2. 🖥️ 基础设施快照
- 服务器：**westd-22162**，工作目录 `/root/autodl-tmp/pacs`，账号 root
- Python/conda：需 SSH 探测确认（aml-train 镜像可能性高，用 `detect_image` 确认）
- 模型/数据：均在 `/root/autodl-tmp/pacs` 下，具体子目录需 SSH 确认
- W&B：项目配置中未显式列出 wandb project name，需查 config 或服务器 `.env`
- GPU：RTX 6000 Pro ×4（cuda:0~3），**全部空闲**（所有 121 实验已完成）
- 活跃进程：无（0 active experiments, 0 crons）
- 活跃 Worker：`worker_knowledge_fix_paper_framing_numbers_20260516T015219`（running，修正 paper_framing 中的数值引用）

### 3. 📊 当前状态
**刚完成**：Round 10 dual dose curve 全部跑完（DS 5-point 0.74→0.04 + QW 5-point n=100 0.46→0.19），全 38 个 plan experiments 完成（coverage 92.1%）。数据编译 + consistency check 已完成并写入 memory.md。

**Registry 总览**：121 实验全部 DONE（58 success / 18 negative / 16 failed），0 RUNNING / 0 PREPARING。

**正在进行**：
- 1 个 Worker running：修正 paper_framing 数值引用（预期分钟级完成）
- 待 Reviewer 核实：DS s030 截断判定差异
- 待执行：论文 dose curve 数据更新 + Figure 生成 → Round 10 审稿提交

**等待中**：
- Worker `fix_paper_framing_numbers` 完成回调
- Round 10 审稿结果 → Director 做最终提交决策

### 4. 📋 待办（条件触发式）
- `fix_paper_framing_numbers` Worker 完成 → 检查修正结果，更新 report.md，确认 consistency issues 已解决
- paper_framing 数值修正完成 → 派 Worker 更新论文 dose curve sections + 生成 Figure（DS+QW dual dose curve plot）
- DS s030 截断判定差异 Reviewer 核实完成 → 根据裁定更新 registry 和 paper
- 论文更新完成 → 提交 Round 10 审稿（派 Reviewer Worker）
- Round 10 审稿 PASS → 向 Director 汇报，请求最终提交决策
- Round 10 审稿有 critical → 按反馈补实验/改论文，GPU 全部空闲可立即响应
- Director 决定提交 → 执行 LaTeX 编译 + 最终检查流程

### 5. 🎯 战略上下文
**核心发现**：importance-based pruning 的 compound interaction severity 随 sparsity 单调递增，跨模型（DS/QW/LLaMA）跨 benchmark（MATH-500/GSM8K）一致。这是论文核心 claim。

**关键决策链**：
- D086: DS accuracy 降为定性观察（截断效应主导），QW 为主证据
- D089: DS 双 regime 结构确认（s≤0.20 截断驱动，s025+ 双重崩溃）
- D057: C5b mitigation 降为 future work（oracle recovery 18% < 30% gate）
- D082: G× 下修至 21-64×

**易错点**：
1. memory.md §3 consistency checklist 有 3 个 ⚠️ 未解决（DS 引用值微差、G× 不可追溯、Cohen's d 定义），不要在这些问题解决前声称数据一致
2. C8（LLaMA 跨架构）仅 partially confirmed（imp_vs_rand 仅 s030 显著，n=50 功效不足），论文中措辞必须 hedged
3. QW random GSM8K s030 gradient 反转是已知 anomaly，不要试图解释掉——paper_framing 已处理为 "raw II_low reversal, gradient still valid"
4. 全部 GPU 空闲但这不是失职——所有 plan experiments 已完成，当前阶段是写作+审稿，GPU 保留给审稿后补充实验
5. 距截稿 9 天，重心是论文完善而非新实验，除非 Round 10 审稿提出 critical gap


---
