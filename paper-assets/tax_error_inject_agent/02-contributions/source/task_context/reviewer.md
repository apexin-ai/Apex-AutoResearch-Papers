---
loop: 8
reason: max_wall_time
updated: '2026-05-16T14:31:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0-3（autodl-5090 4×RTX 5090）。越界进程 → severity=critical + kill
- llama31-taxei-s0 训练需 `TMPDIR=/root/autodl-tmp/tmp`，否则 /tmp 溢出
- Detection rate 是 FAKE 指标（keyword "back" 匹配导航语言）——不可用于论文 claim
- Worker eval 完成通知 **不可信**——已连续 2 次虚假完成（llama31-taxei-s0-eval）。必须独立核实服务器文件和 registry

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (root)，工作目录 `/root/autodl-tmp/tax_error_inject_agent`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型路径：`/root/autodl-tmp/tax_error_inject_agent/output/llama31-{vanilla,taxei,random}-{s0,s42,s123}/`
- Qwen checkpoints：`/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_{vanilla,taxei,random}_sft_v4_seed{0,1,7,42,123}/`
- Eval 输出：`/root/autodl-tmp/tax_error_inject_agent/eval_results/`
- 活跃进程（截至 handoff）：
  - PID 277781 GPU 2: taxei-s123 或 random-s123 训练（~3387 steps, 估计 ~60min 剩余）
  - PID 277973 GPU 3: 同上
  - GPU 0-1: vanilla-s123 eval 运行中（clean + injected）

### 3. 📊 ���前状态
**刚完成**：
- Qwen Random recovery 5-seed 完整统计（s1=51.1%, s7=53.2% 新增）→ 修正 Random≈TaxEI
- llama31-taxei-s0-eval 确认完成（recovery=74.5%）→ LLaMA 2-seed 表完整
- llama31-vanilla-s123 训练完成（loss=0.4, acc=0.894），eval 在 GPU 0-1 运行中

**Registry RUNNING/PREPARING**：无 RUNNING 条目（registry 滞后，实际 taxei-s123 和 random-s123 训练中）

**等待中**：
- taxei-s123 + random-s123 训练完成（估计 ~60min）
- vanilla-s123 injected eval + clean eval 完成
- Director 对 "Random≈TaxEI" 修正报告和 "LLaMA 中性" 发现的响应

### 4. 📋 待办
- taxei-s123 训练完成 → 核实 checkpoint + 等 eval 启动 → 核实 eval 结果
- random-s123 训练完成 → 同上
- vanilla-s123 eval JSON 出现 → 核实 recovery rate，编入 3-seed LLaMA 表
- 3-seed LLaMA 完整后 → 编制最终 cross-model 对比表，确认 "LLaMA 中性" 是否在 s123 仍成立
- Director 若要求审查论文章节 → 按 CLAUDE.md §5 执行对抗审查（先查 red-section 合规）
- Scale-up 数据收集（PID 266815，目标 1000 successes from 405）→ 不定期检查进度

### 5. 🎯 战略上下文
**核心结论链**：
- D041: Recovery ≈ passive resilience, not active recovery skill
- Vanilla(67.3%) >> {Random(57.9%) ≈ TaxEI(57.4%)} >> RP(50.2%) — 分界线是"有无注入"
- TaxEI degradation 是 **Qwen-specific**：LLaMA 上三种条件完全一致（74.5%）
- 论文 framing: EMNLP 2026 Findings 8-page negative result

**易错点**：
- 不要用之前的 3-seed Random=61.7% 估计——已被 5-seed=57.9% 修正
- Worker "done" 通知 ≠ 实际完成（尤其 eval worker），必须核实文件+registry
- "LLaMA 中性"结论目前仅 2 seeds，s123 是关键第三数据点——若 s123 偏离则需重新评估
- Clean eval success_rate（无注入）和 recovery_rate（有注入）是不同指标，不要混用
