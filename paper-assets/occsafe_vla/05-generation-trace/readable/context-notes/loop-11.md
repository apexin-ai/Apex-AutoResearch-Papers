# director / loop_11.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`368ba919026986e6f1b6.json`](../../sessions/36/368ba919026986e6f1b6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-26T19:43:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- 两台服务器：westd-10894 和 westd-34685，GPU 分配以 `get_project_status` 返回为准
- ANOVA 脚本数据必须与 registry 完全一致——本轮刚因 Cell 1/Cell 3 数据遗漏被 Reviewer CRITICAL
- 论文中 factorial interaction 相关措辞已统一改为描述性语言（"pattern consistent with"），禁止用 "reveals"/"demonstrates"/"confirms" 描述交互效应，除非 n=5 ANOVA 达到 p<0.05
- report.md AUTO-FACTS 区不能手写，只能调 `auto_build_report_facts`

### 2. 🖥️ 基础设施快照
- 服务器 1：westd-10894 (connect.westd.seetacloud.com)，root，/root/occsafe_vla
- 服务器 2：westd-34685 (connect.westd.seetacloud.com)，root，/root/occsafe_vla
- westd-10894：运行 3 个 v2 rebuild 实验（detach_ln_v2_s0, full_occ_ln_v2_s0, full_occ_ln_v2_s1）
- westd-34685：4 GPU (cuda:0-3)，本轮指令 Agent 启动 detach_ln_v2_s1 + 3 个 n=5 expansion（Agent idle 16h 被 reset 前是否执行未确认）
- W&B / Git 未配置；飞书 A+B+C 群已配置
- 审稿 C 群：oc_faa96524df7d6444f5c8cbc48d5a616b

### 3. 📊 当前状态
**刚做完**：
- Paper Agent 完成 Reviewer 预审 8 项修改（编译 PASS，18 页）
- Paper Agent 完成 factorial interaction 措辞全面调整（7 个 .tex，15 处修改）
- 向 Agent 派了两个任务：(1) 启动 westd-34685 上 5 个待处理实验 (2) 修复 ANOVA 脚本数据不完整问题——**Agent 在执行前因 idle 16h 被 reset，这两个任务需要重新下达**

**RUNNING**（3 个，均在 westd-10894）：
- detach_ln_v2_s0 — Cell 4 v2 rebuild, seed 42
- full_occ_ln_v2_s0 — Cell 2 v2 rebuild, seed 42
- full_occ_ln_v2_s1 — Cell 2 v2 rebuild, seed 43

**PENDING**（5 个，未启动）：
- detach_ln_v2_s1 — Cell 4 v2 rebuild, seed 43（**优先级 1，论文阻塞**）
- detach_ln_s4, ablation_occ_detach_s4, full_occ_ln_s4, mvp_occ_s4 — n=5 expansion seed 46

### 4. 📋 待办
- Agent reset 完成 → **立即重新下达**：(1) westd-34685 启动 5 个 pending 实验 (2) 修复 ANOVA 脚本 Cell 1 补 0.776、Cell 3 补 0.794 并重跑
- v2 rebuild 全部完成 → 跑 all-v2 factorial ANOVA，看交互效应 p 值变化
- n=5 expansion 全部完成 → 跑正式 n=5 ANOVA，若 p<0.05 则让 Paper Agent 升级措辞回 "reveals"
- ANOVA 修复结果回来 → 核对更新后的 F/p/η² 是否与论文一致，不一致则再派 Paper Agent patch
- 任何实验 DONE 回调 → 检查 westd-34685 是否有空闲 GPU，有则启动下一个 pending

### 5. 🎯 战略上下文
- 项目核心：2×2 factorial design (Gradient Flow × Normalization) 分析 OCC auxiliary loss 对 VLA safety 的影响
- 当前 story：effect sizes 大（d=1.41, η²=0.37）但 n 太小无法达统计显著——n=5 expansion 是关键补充
- v1→v2 codebase 迁移：v1 有 bug，所有 Table 1 数据需替换为 v2 结果。Cell 1 和 Cell 3 已有足够 v2 数据，Cell 2 和 Cell 4 的 v2 实验正在跑
- 易错点：(1) Agent reset 后两个任务丢失，必须重新下达 (2) ANOVA 脚本数据与 registry 不同步已被 Reviewer 抓过一次，任何数据更新后都要核对一致性 (3) 论文措辞已锁定为描述性语言，n=5 结果出来前不得擅自升级
- 决策日志 62 条，论文溯源覆盖 18/23


---
