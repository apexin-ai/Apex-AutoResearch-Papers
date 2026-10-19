---
loop: 2
reason: max_messages
updated: '2026-05-12T22:36:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 cqa1-21977 的 cuda:0 和 cuda:1。D019 事故：曾在 cuda:3 启动进程被 Director CRITICAL + kill
- submit_training_job 命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...`
- v6 ICL 启动命令中 `--gpu 0/1` 是逻辑编号，框架注入 CUDA_VISIBLE_DEVICES 映射物理卡。不要手动设 CUDA_VISIBLE_DEVICES 再用 --gpu 非 0
- 分类 prompt 存在循环引导问题（taxonomy 嵌入 span 范围 → LLM 看到长 span 自动归 planning）。D024 要求修复但 Worker 尚未完成——不要用旧 prompt 对 v6 做全量分类
- P1 gate 判定必须两版 KW 都显著（with/without PCB override），单版显著不算 pass

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，工作目录 /root/autodl-tmp/error_diag_dpo_recovery
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：14B-AWQ 在 /root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ（classify 和 ICL 均用此路径）；8B 在 HF cache（v5 用）
- Expert 数据：data/alfworld_sft.json (3119 条, 18.5MB)
- v5 数据：data/trajectories_v5_cuda0/train.jsonl (250条) + data/trajectories_v5_cuda1/train.jsonl (250条)
- v5 分类输出：data/classified/v5_full_classified.jsonl (251 matched)
- 直方图：artifacts/correction_span_histogram.png/.pdf
- 活跃进程（v6 ICL）：
  - cuda:0: tmux `v6_icl_cuda0`, ~10GB VRAM, 300 tasks, part_idx=0, seed=42
  - cuda:1: PID 633155, 300 tasks, part_idx=1, seed=42
  - 日志：logs/v6_icl_cuda0.log, logs/v6_icl_cuda1.log
- HF cache：HF_HOME=/root/autodl-tmp/.hf_cache
- AutoDL 特殊：pip/git 前需 `source /etc/network_turbo`；HF 下载设 HF_HUB_DISABLE_XET=1 + SSL 证书环境变量

### 3. 📊 当前状态
**刚做完**：v5 全量分类 → P1 FAIL（LLM 98.4% planning, KW p=0.135）→ v6 ICL 两卡已启动

**Registry RUNNING**：
- `datagen_v6_icl_cuda0` — 14B-AWQ ICL 收集, cuda:0, 300 tasks, ~6h
- `datagen_v6_icl_cuda1` — 14B-AWQ ICL 收集, cuda:1, 300 tasks, ~6h

**等待中**：
- Worker `worker_check_v6_cuda_verify` — 验证 v6 CUDA_VISIBLE_DEVICES 正确性（已派，未回调）
- D024 要求的分类 prompt 修复 Worker（`--no-span-hint` 模式）— **尚未派发**，被 WRITE HANDOFF 打断
- v6 完成 cron 回调
- Director 决策：分类 prompt 改进方向确认

### 4. 📋 待办（条件触发式）
- BOOT 后立即 → 派 Worker 修改 classify_errors.py 增加 `--no-span-hint` 模式（D024 未完成项，CPU 任务，不占 GPU）
- v6_cuda_verify Worker 回调 → 检查 CUDA_VISIBLE_DEVICES，如有越界立即 kill + 修正重启
- v6 cron 回调（~6h 后）→ 立即全量分类（两版 prompt 并行：有/无 span hint），两卡各跑一版
- 分类完成 → 跑双版 KW × 两版 prompt = 4 组结果，汇报 P1 gate
- action 组仍 n < 10 → escalate Director，可能需要更激进的 ICL 策略或换模型
- v6 ICL 进程异常退出 → 检查 OOM/环境问题，用相同配置重启

### 5. 🎯 战略上下文
**项目**：ETADN — error-type-specific γ_e 时间折扣因子用于 DPO 训练。核心假设：不同错误类型有结构性不同的 correction span（action < verification < planning）。

**决策链**：D009(放弃自生成→用 expert) → D012(correction span 重定义) → D014-D015(温度采样) → D019(GPU 越界) → D020(v5 双卡重叠保留) → D021(ICL v6 准备) → D022(CSF 后处理) → D023(PCB→verification) → D024(P1 FAIL recovery)

**P1 现状**：ordinal ordering 成立 (action 7.5 < verification 10.4 < planning 11.3) 但统计不显著。两个瓶颈：(1) action 样本太少 (n=2)；(2) LLM 分类 prompt 循环引导导致 98.4% planning。v6 ICL 解决 (1)，`--no-span-hint` 解决 (2)。

**易错点**：
- v5 用 8B 模型，v6 用 14B-AWQ——不要混淆模型能力导致的差异和方法论差异
- PCB override（82 条 planning→verification）是 rule-based 强制的，不是 LLM 判断的。without_override 版本是真实 LLM 分布
- 分类 prompt 修复是 v6 分类的 **blocker**——不要用旧 prompt 分类 v6 数据
- v6 配置实际是 300 tasks/GPU（非 Director 说的 250），已启动不要中断
- May 15 是 MVP gate deadline，当前 Day 1 尾声，Day 2 必须完成 v6 + 分类 + P1 重测
