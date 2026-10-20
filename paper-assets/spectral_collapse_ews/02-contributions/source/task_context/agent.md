---
loop: 9
reason: max_wall_time
updated: '2026-05-25T19:17:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx6000-diagprobe 上 cuda:0 和 cuda:1，两卡目前均空闲，Director 说"暂时不派新实验"
- 禁止在 GPU 上启动未经 registry 注册的训练任务（2026-05-24 事故教训：ε-clipping worker 未经授权启动训练占 38GB VRAM）
- r=0.25 跨架构结论必须用保守措辞："consistent with the Pythia phase boundary; the 3-generation window does not resolve the Type II/III distinction"（Director 明确决策 D039 附近）
- exp_021 (r=1.0) 的 SLV 数据不在 registry metrics 里，原始值在 `artifacts/exp_021/full_metrics.json`（gen3 log_det=812.97）

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe，2× NVIDIA RTX PRO 6000 Blackwell (98GB each)
- 工作目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/`
- 代码仓库（远程训练）：`/root/spectral-collapse-ews/` on rtx6000-diagprobe
- 远程 Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- PaperBanana venv：`/tmp/pb_venv/`（EC2 本地，非持久化）
- 活跃进程：无（所有实验已完成，所有 cron 已 reconcile 为空）
- wandb project：spectral-collapse-ews（未在本 session 使用）

### 3. 📊 当前状态
**刚完成**：
1. PaperBanana pipeline overview 图（Gemini 2.5 Pro 一次通过，VLM Critic "publication-ready"），已覆盖 `paper/figures/pipeline_overview.pdf`
2. 跨架构数据集成验证——逐项比对 registry 与论文 Table 5 / §3.6 / Abstract / Intro / Conclusion，**所有数值已正确集成，无需修改**
3. LaTeX 编译通过，零错误（仅 Underfull hbox 排版微调）
4. v2 Visual Design Language 全部 8 张图已就绪（7 张 v2 + 1 张 ews_heatmap）

**Registry 状态**：全部 DONE（success 20 / negative 1 / failed 3 / killed 2 = 26 total），无 RUNNING/PREPARING
**等待中**：无 Worker 回调、无 Cron、无待处理 Director 决策

### 4. 📋 待办
- Director 指示"启动新实验" → 检查 ideas.md / experiment_plan.yaml 选下一格，走 submit-experiment skill
- Director 指示"Round 2 提交" → 最终 paper-visual-review + reference-audit + 编译检查
- ROADMAP.md 需更新（仍显示 exp_020/022c/023 为 running/planned，实际全部 DONE）——可在下次 Director 交互时顺手更新
- 如 Director 对 PaperBanana pipeline 图不满意 → 需要重新申请 GOOGLE_API_KEY（已清理 /tmp 密钥文件），或修改 intent 文件 `/tmp/fig_pipeline_intent.txt` 重新生成

### 5. 🎯 战略上下文
- **核心结论**：递归合成训练产生三阶段谱坍缩（decompression→onset→acceleration），SLV 是最有效检测器，r_crit ∈ (0.25, 0.3] 是架构无关的相变边界
- **跨架构验证矩阵 4/4 完成**：exp_020 (r=0, Type I ✓), exp_023 (r=0.25, conservative ✓), exp_022c (r=0.3, Type III ✓), exp_021 (r=1.0, control ✓)
- **GPT-2-medium 的 SLV collapse 幅度远大于 Pythia**（-55.1% vs -11.6%），因初始 r_eff=23 远低于 Pythia 的 418（更各向异性的初始谱）
- **ε-clipping W2 concern 已解决**：min(σ) ≥ 0.016，比 ε=10⁻¹⁰ 高 8 个数量级，验证数据在 `artifacts/epsilon_clipping_verification.json`
- **易错点**：exp_023 registry 的 trajectory_type="II" 但论文必须用保守措辞（3 gen 不够分辨 Type II/III），这是 Director 明确决策不是遗漏
- **审稿状态**：Round 1 得分 3.0，目标 3.5+，24/27 issues resolved，剩余 3 条（R1-N2 r=0.5 缺 seed / R1-W1 r_crit coarseness / R2-C2 跨架构——最后这条现在已有数据支撑）
- **v2 图表设计系统**：`artifacts/visual_design_language_v2.py` 是权威规范，所有 gen_fig*.py 都 import 它。风格="ink-wash restraint"，dusty rose / copper / gold / teal / steel blue 五色语义绑定 mixing ratio
