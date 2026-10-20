---
loop: 21
reason: max_wall_time
updated: '2026-05-25T05:47:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-18266 只有 cuda:0（单卡 A100-80G），无 GPU 白名单冲突风险但注意不要在已有 vLLM 进程占用时再启推理
- 论文 main text 严格 8 页（EMNLP 2026）——上一轮刚修过 Conclusion 溢出，任何修改后必须验证页数
- Llama-70B DAF=101.0% 是真实值（Δ_nd=-0.30 为负），不是 bug——不要把它标为异常
- gen_death_action_comparison.py 中 Deterministic 侧数据是近似值（代码已标注）——不要把它当精确数据去交叉验证

### 2. 🖥️ 基础设施快照
- 服务器：westd-18266 (root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`
- 论文源码：`docs/paper/` (main.tex, experiments.tex, introduction.tex, etc.)
- 图表脚本：`docs/paper/figures/gen_*.py` + `paper_style.py`（统一样式模块）
- 关键数据：`results/plan_c/`（245 episodes 原始数据）、`results/retry_dose_response/`、`results/reflexion_dose_response/`、`results/llama70b/`
- 分析脚本：`scripts/death_taxonomy_245eps.py`（action distribution 数据源）
- 无活跃训练进程（全部实验 DONE）

### 3. 📊 当前状态
刚完成全图数据溯源审查（6 正文图 + 2 附录图），确认所有核心定量图数据与 registry 精确一致，无编造。报告已发 Director。

Registry 状态：全部 DONE，无 RUNNING/PREPARING 实验。最近完成的是 llama-70b-episodes。

3 个 paper-banana-calibration worker 连续失败（v1/v2 缺 key，v3 命令路径问题），但 matplotlib 图已升级完毕（Nature/Science 风格 + 校准常量），不阻塞。

无等待中的 Worker 回调或 Cron。

### 4. 📋 待办
- Director 触发 "pre-submission checklist" → 做最终 PDF 视觉审查（编译后全 8 页 + 图表渲染 + cross-ref）
- Director 转发章节写作审查 → 按 §5 审查模式 B 执行（维度评分 + Claim 溯源）
- 如有新 worker 完成通知 → 验证数据完整性（重点检查 paper_style 常量是否引入了未定义属性）
- Ethics Statement 可能需补充 Llama-70B GPU hours（当前只提 Qwen-72B）— Director 提出时审查

### 5. 🎯 战略上下文
- 核心结论：Death Avoidance 是 ScienceWorld 中 LLM agent routing signal 的主导机制（DAF 88-101%，跨 5 模型 3 规模）
- 论文 story 已固化：诊断框架 → DAF 指标 → cross-model/scale 验证 → negative contrast (MATH/ALFWorld) → intervention resistance (retry/reflexion plateau)
- 最容易判断错的事：(1) 不要把 Llama-70B DAF>100% 当 bug（Δ_nd 轻微负值是真实现象）；(2) 不要用人类时间直觉判断 deadline 风险（只看 GPU-hours）；(3) signal_reversal 图中 ALFWorld 25.9% 来自 Qwen（alfworld-counterfactual-full），不是 Llama（alfworld-llama-v3 只有 11.9%）
- 已修复的坑：Director 曾传入错误 Δ_full=28.57（实际 29.53）；Limitations 曾错写"两模型都降低 death rate"（只有 Qwen-72B 降低）
