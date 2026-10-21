# reviewer / loop_6.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`0fdc58aedb4276d6b492.json`](../../sessions/0f/0fdc58aedb4276d6b492.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-14T20:43:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-39279 上 cuda:0 和 cuda:1（execution.gpu_ids）。进程跑在其他卡上 → CRITICAL
- Prolog STA s44 的 strict classifier 报 "100% Genuine" 是错的——Reviewer 已独立核实为 query-as-fact gaming（95/97 n_necessary=1，功能性 H7）。任何引用此实验的文本必须用功能分析结论，不能信 strict classifier
- 全文 ISR 统一报 proved-only ISR*（排除 unproved=0）。registry 中 "isr_mean" / "mean_isr" 多为 all-sample mean，需除以 PR 才得 proved-only。已因此导致 experiments Table 3 Prolog s44 报错（0.885 应为 0.912）
- ISR β=0.1 的 "genuine ISR 优势" 已被 premise-count-matched 分析否定（1.06×），论文中禁止报 raw 2.4× 或 3.2× 差异作为结构优势证据

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，代码根目录 /root/solver-trace-ablation
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- 模型：/root/autodl-tmp/models/Qwen3-4B
- 数据：/root/solver-trace-ablation/data/train_500_seed42.jsonl（500 训练）+ proofwriter_fol_100.jsonl（100 eval）
- Checkpoints：/root/autodl-tmp/outputs/plan*（磁盘 ~240G/250G，注意空间）
- 无 wandb 配置（所有实验 --no_wandb）
- 活跃进程：无（所有 50 实验已完成）
- 论文本地路径：projects/solver-trace-ablation/paper/（main.tex 为主入口，编译产物 main.pdf 18 页）

### 3. 📊 当前状态
全部 50 个实验 DONE（12 success / 18 negative / 18 failed+killed）。无 RUNNING/PREPARING。

我刚完成的审查：
- **appendix.tex**: WARNING — H1 prevalence "52-93%" 与 ISR s43/s44 H1=0% 矛盾（已报 Director）
- **introduction.tex**: PASS — 数据一致，minor 99.5% vs 99.6% 不一致
- **experiments.tex**: WARNING — H1 range 同上 + genuine_count 25 vs 26 + ~68-81% 不精确
- **compile-and-audit**: CRITICAL — **主体 ~12.5 页 vs ACL 8 页限制**；Table 2 与文字重叠不可读
- **reference-audit**: PASS — author={Various} 已修复，logic-rl 作者仍不完整

等待中：Director 对页面超限的决策（是否启动压缩 worker）

### 4. 📋 待办
- Director 指派压缩任务 → 审查压缩后是否丢失关键数据/claim，验证页数 ≤8
- 新版 experiments.tex 到达 → 验证 Table 2 重叠修复 + Prolog s44 ISR* 改为 0.912 + H1 范围统一为 "68-97% (H1 or H7)"
- appendix 修订到达 → 验证 H1 prevalence 表述与 experiments taxonomy 一致
- 如有新 paper PDF → 重新检查 overfull hbox（当前 14 处，appendix 宽表最严重 89pt）

### 5. 🎯 战略上下文
论文 3 Claims 全部闭环（Claim 1 STA 诊断 ✅, Claim 2 Goodhart/ISR 无结构优势 ✅, Claim 3 跨逻辑泛化 ✅）。核心结论链：exec-only hacking (D001) → ISR-as-reward Goodhart (D033→D043→D051→D057) → premise-count confound 否定结构优势 (D051) → Prolog universal Goodhart 3/3 (D056)。SFT baseline 确认 hacking 是 RL-specific。

**下一个"我"最容易判错的事**：
1. registry 中 isr_mean 不是 proved-only——必须查是否有 proved_only_mean_isr 字段，没有就手算（isr_mean / prove_rate）
2. 不要被 strict H7/H1 classifier 的数字骗了——Prolog s43/s44 需要看 n_necessary 分布做功能分析
3. 页面压缩时不要删 premise-count confound 分析（§4.3 第 3-4 段）——这是 Claim 2 的关键方法学支撑，删了审稿人必问
4. paper.tex 和 main.tex 是两个不同入口文件（不同标题、不同包），main.tex 是正确的规范版本


---
