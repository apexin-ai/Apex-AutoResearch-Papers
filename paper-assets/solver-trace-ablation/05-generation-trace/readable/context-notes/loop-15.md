# agent / loop_15.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`1ba9e30ef5341c7f56fb.json`](../../sessions/1b/1ba9e30ef5341c7f56fb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: idle_timeout
updated: '2026-05-16T00:43:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `westd-39279:cuda:0` 和 `westd-39279:cuda:1`，不可用其他设备
- D095 Narrative A 已生效——所有 paper 内容必须与 D095 一致，不可回退旧 framing
- H7a 是 GRPO 通用 seed-dependent（非 ISR 独有），H7b 才是 ISR-specific——写论文/改论文时极易滑回 "H7 is ISR-specific" 旧表述，已来回修正 8 次（D087-D094）
- genuine rate ISR 6.06% vs Random 9.54%，p=0.182 不显著——**禁止 claim genuine rate 有显著差异**
- 2.4x ISR 结构优势已作废（D051），premise-count-matched 仅 1.06x
- genuine = proved − |H7 ∪ H1 ∪ H8|（集合排除公式 C013），不是简单减法
- EMNLP 主体 ≤8 页硬限制（当前恰好 8 页，不能膨胀）

### 2. 🖥️ 基础设施快照
- **服务器**: `westd-39279`（Seeta Cloud），host=`connect.westd.seetacloud.com:39279`，user=`root`
- **GPU**: 2 × RTX PRO 6000 96GB，当前 2/2 空闲
- **工作目录**: `/root/solver-trace-ablation`
- **Python**: 未检测到预置镜像，服务器环境需按 Phase 1-5 流程探测（上次使用时已就绪，但重启后可能变）
- **W&B**: 无（本项目未用 wandb）
- **HF cache**: N/A（本地模型训练）
- **活跃进程**: 无——所有 86 实验已完成，0 个 cron，0 个 Worker，0 个 tmux session
- **论文 TeX**: `projects/solver-trace-ablation/paper/` 目录，`main.tex` 入口，19 页 PDF（body 8 页 + refs + appendix）

### 3. 📊 当前状态
**上一个 session 完成了全部实验和论文审查流程的步骤 1-10（共 11 步）。** 具体：
- 86 实验全部 DONE（success 26 / negative 28 / failed 26）
- D095 Narrative A 批准 + paper_framing.md 全文改写完成
- TeX 全量数据已同步到 D095 最终数字
- Provenance 36/36 完成
- 引用审计 30/30 真实
- 一致性检查 0 critical
- 页数压缩 ≤8 页达标
- Checklist 验证通过
- PDF 视觉审查完成（修复了 Table 4/5 重叠 + Table 8 超宽）

**Registry 里没有 RUNNING/PREPARING 实验。** 没有等待中的 Worker/Cron/Director 决策。

**唯一剩余**: 步骤 11——最终润色 + 提交准备。ROADMAP 还标了"TeX 全量数据同步（Paper Agent）"和"Paper Agent 启动全文写作"为未完成，但 report.md 显示 TeX 数据已同步、final-sync-compile Worker 已完成，可能是 ROADMAP 未更新。

### 4. 📋 待办（条件触发式）
- Director 下达"最终润色"指令 → 派 Worker 做最后一轮 proofreading + camera-ready 格式检查
- Director 下达"提交"指令 → 走 submission approval 流程（always_require: true），准备 supplementary materials，打包提交
- 如果 Director 要求新实验（补充审稿人可能的 concern）→ GPU 空闲可即时启动
- 如果 ROADMAP 的"TeX 全量数据同步"和"全文写作"确实未完成 → 需派 Paper Agent Worker 启动

### 5. 🎯 战略上下文
**项目核心结论**: ISR 是优秀的 reward hacking 诊断工具（Claim 1），但作为训练信号会触发 meta-level Goodhart's Law（Claim 2），且该现象跨逻辑语言泛化（Claim 3: Prolog 3/3 gaming, 0% genuine）。

**决策链关键节点**:
- D051: 2.4x 作废 → 1.06x premise-count-matched
- D087-D094: H7 归因从 "ISR-specific" → "additive-specific" → "GRPO-general seed-dependent"（8 次修正）
- D095: Narrative A 定稿——H7a GRPO-general（ISR amplified 5x, p<10⁻³⁹）+ H7b ISR-specific

**最容易判断错的事**:
1. 看到 Random H7=13.7% 就以为 H7 很少——实际是 s43-r3 贡献 38.3%，其余 seed 为 0%，必须同报 per-seed 和 pooled
2. 以为 genuine rate 差异显著——p=0.182 明确不显著
3. ROADMAP 标了两个未完成项但 report.md 说已完成——需验证 TeX 文件实际状态再判断

**DDL**: 2026-05-25 EMNLP ARR 提交，剩 9 天。GPU 全部空闲，论文进入最终润色阶段。


---
