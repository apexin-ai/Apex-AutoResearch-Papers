---
loop: 17
reason: idle_timeout
updated: '2026-05-29T14:13:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `get_project_status` 的 `execution.gpu_ids`：4 台服务器各 cuda:0-3
- w27 代码未同步，仅支持 none/random/l2norm，不要在 w27 上跑 attention 实验
- π0.5 eval 必须用 strict metric（非 lenient），论文数据全部基于 strict 版本
- Attn k=0.75 seed43 统一用 cqa1=52.0%（w27 不支持 attention scoring，w27 数据不可用）
- Random k=0.9 seed43 统一用 v2=35.0%（D292），不引用旧版 32.4%
- **CoRL 2026 Paper 截止 May 29**——实验硬截止已过（May 28 20:00 BJT），现在只收割结果 + 论文提交
- 脚本内 GPU 编号始终从 0 开始（框架自动注入 CUDA_VISIBLE_DEVICES）
- OV 实验需 ~7h，π0.5 ~2.5h——新 OV 实验已来不及

### 2. 🖥️ 基础设施快照
- **westd-27271**: w27，~/runs/importance_margin_vla_compress/，2 GPU（0,1），仅 random/l2norm
- **westd-38929**: w38，~/runs/importance_margin_vla_compress/，4 GPU（0-3）
- **westd-41074**: w41，~/runs/importance_margin_vla_compress/，4 GPU（0-3）
- **cqa1-33015**: cqa1，~/runs/importance_margin_vla_compress/，4 GPU（0-3），支持 attention
- 所有服务器：aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 活跃进程：cqa1 上 3 个 seed47 bonus（L2norm k=0.75 pid=379039 cuda:1, Random k=0.7 pid=379280 cuda:2, Random k=0.75 pid=379521 cuda:3）——提交于 17:05 UTC，π0.5 仅需 ~2.5h，**极大概率已完成但 registry 未更新**
- Worker `worker_check_seed47_harvest_cqa1_20260528T221102` 正在 SSH 检查并收割这 3 个实验

### 3. 📊 当前状态
Session-start 初始化刚完成（read_registry + reconcile_crons + ROADMAP + report.md）。发现：
- **Registry RUNNING 仅 3 个**（cqa1 seed47 bonus），相比 handoff 的 8 个 stale 已全部清理
- **0 个 QUEUED**——所有之前排队的实验已部署或取消
- **0 个 running Worker**（handoff 提到的 2 个 Worker 已完成）
- **5-seed 90/90 cell 零缺失**，数据验证通过，ROADMAP 已标记 submission-ready
- **Figures 已在前序轮次生成完毕**
- 派出 1 个 Worker（`worker_check_seed47_harvest_cqa1`）去 cqa1 收割 seed47 结果
- **未向 Director 发送本轮汇报**——等 seed47 收割完一并汇报

### 4. 📋 待办（条件触发式）
- `worker_check_seed47_harvest_cqa1` 回调 → 读 seed47 metrics → update_registry DONE → 更新 ROADMAP 6-seed 表（如果有价值）→ 向 Director 汇报 submission-ready 状态
- seed47 全部收割完 → 所有 GPU 空闲，无新实验可跑（截止已过），向 Director 确认"实验端全部关闭，等待 Paper Agent 最终提交"
- Director 发来任何 paper 相关指令 → 派 Worker 执行（论文微调、编译、格式检查等）
- 如果 seed47 某个实验 failed → 记录但不重跑（截止已过，5-seed 数据已足够）

### 5. 🎯 战略上下文
- **核心发现**：Importance Margin Inverted-U（peak k=0.9, +46.9pp）+ Attn cliff+plateau + Random anti-monotonicity（V-shape），支持 2-Axis Framework（scoring method × connector × task 三维交互）
- **数据状态**：π0.5 Long 5-seed 全闭合，OV Long 5-seed 全闭合，Crossover 16/16 全闭合。seed47 是 6th seed bonus for revision，非必需
- **论文状态**：Abstract 已提交（May 26），Narrative 定稿（D276），Figures 已生成。前序 Worker 做了 method refs 修复 + page count surgery。Paper Agent 应已接近 submission-ready
- **易错点**：
  - 不要混淆 lenient/strict——论文全用 strict
  - metrics 格式不一致（0.8 vs 80%），最终数据统一转百分比
  - seed47 是 bonus，即使 fail 也不影响 5-seed 表的完整性
  - ROADMAP 表已是最终版（5-seed），seed47 结果单独存 registry 供 revision 用，不改 ROADMAP 主表
  - 距 CoRL 提交仅剩数小时，任何操作以不破坏现有数据为第一原则
