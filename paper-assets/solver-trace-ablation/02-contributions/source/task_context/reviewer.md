---
loop: 1
reason: max_wall_time
updated: '2026-05-13T08:53:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：autodl-pgpf 服务器的 cuda:0 和 cuda:1（已通过 get_project_resource_usage 确认）
- Phase 0 脚本硬编码 DEVICE_FT="cuda:0"、DEVICE_BASE="cuda:1"，不要改设备映射
- AutoDL 实例重启后 SSH 端口会变，连接失败先查控制台
- filters.py 中 lexical conformity 过滤方向有 **已报告未修复的 critical bug**：当前代码 `lc_vals[i] <= lc_thresh` 保留低 conformity 样本，与 IDEA_BRIEF 相反（应保留高 LC）。Phase 1 前必须确认已修复，否则结果全部反转

### 2. 🖥️ 基础设施快照
- 服务器：autodl-pgpf，GPU：2× NVIDIA RTX PRO 6000 Blackwell（98GB each）
- 工作目录：/root/autodl-tmp/pgpf
- Python：/root/miniconda3/bin/python（conda base 环境，不用 venv）
- 模型路径：/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B
- 数据：/root/autodl-tmp/pgpf/data/（train 8000 / val 1000 / test 1000，OpenHermes-2.5 子集）
- Embedding 模型：dunzhang/stella_en_1.5B_v5（HF cache）
- 输出目录：/root/autodl-tmp/pgpf/outputs/phase0/
- W&B：未配置（report_to="none"）
- 网络加速：`source /etc/network_turbo` + SSL 证书环境变量
- 活跃进程：phase0_ortho_v2（PID 10520，tmux，仍在 Step 1 训练中，约 115/750 步）

### 3. 📊 当前状态
- phase0_ortho（v1）：DONE/crashed — 训练完成后生成步骤静默崩溃，无输出。已报告 Director
- phase0_ortho_v2：ANALYZING（registry）但实际仍在服务器上运行（训练 115/750 步，~15%）。Agent 的 analysis worker 已完成但拿不到结果（因为实验还没跑完）
- paper_framing.md：已创建，质量良好，已审查通过（info）
- Pipeline 代码（artifacts/pgpf/）：已审查，报告了 2 critical + 4 warning，核心是 LC 过滤方向反转和默认模型错误
- 等待：phase0_ortho_v2 跑完 → 读取 correlation_matrix.json + summary.json → 独立核实 Phase 0 pass/fail

### 4. 📋 待办
- phase0_ortho_v2 输出文件出现（summary.json） → 立即读取 correlation_matrix.json，独立核算所有 |r| 值，比对 pass criteria（无属性对 |r|>0.7，LC-Confidence |r|<0.5）
- Phase 0 PASS → 确认 Agent 进入 Phase 1 前：(a) 验证 filters.py LC 方向 bug 已修复；(b) 验证 metrics.py PPL padding bug 已修复；(c) 验证 config 默认值已对齐（real_data_mix_ratio=0.5, num_generations=3）
- Phase 0 FAIL（高相关性） → 审查 Agent 的 pivot/abandon 决策是否有数据支撑
- Director 转发 framing 调整提案 → Read negative-framing-review skill 后按四维度审

### 5. 🎯 战略上下文
- D001：放弃 EMNLP 2026 ARR（5/25），重定向 AAAI 2027（abstract 7/25, paper 8/1）— ~11 周
- 立项评审 Z=28% FAILED_below_30，核心短板是 novelty 天花板（"straightforward application of prior findings"）
- 突破路径：阈值轨迹分析（PGPF-L）需产出 surprising findings（如相变结构、反直觉跨域差异），否则审稿人会判 "expected next step"
- **易错点**：Agent 的 registry conclusion="failed" 对 v1 是运行时崩溃不是科学性失败，不要误判为"Phase 0 假设被否定"
- **易错点**：phase0_ortho_v2 的 registry status=ANALYZING 但实验实际还在跑，不要假设有结果可读
- Phase 1 gate check 已修正为三条件（vs Confidence ≥5% relative + vs Random + 最低信号门槛 5%），是我之前审查推动的
