# director / loop_4.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`bdf97e25b590b0be2838.json`](../../sessions/bd/bdf97e25b590b0be2838.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-15T21:36:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 1 张 GPU（cuda:0），服务器 cqa1-38874，不可用其他设备
- Qwen3-32B-FP8 占 ~80GB VRAM，与 LLaMA-8B 无法并行，必须串行
- exp_fewrel_40rel_r4 正在跑（PID 325591），不要 kill——增量保存已启用，4h 推理中
- Paper Agent 独立运行写作流水线，不要重复派写作任务给 Main Agent
- 审稿阶段已启动（Group C 独立审稿），研究侧继续推实验不停

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (connect.cqa1.seetacloud.com)，root
- 工作目录：/root/schema-dag-extraction
- GPU：单卡，Qwen3-32B-FP8 加载时占 84.5/97.9 GB VRAM
- 活跃进程：exp_fewrel_40rel_r4 PID 325591（cuda:0，6960 inferences，~4h 总时长）
- LLaMA 模型：LLaMA-3.1-8B-Instruct（具体路径需 Agent 确认，脚本尚未创建）

### 3. 📊 当前状态
- **exp_fewrel_40rel_r4** RUNNING：Qwen3-32B-FP8 + FewRel 40-rel count curve + BCS-controlled，exp1 有 105 batches / 6960 inferences，约 4h 完成。启动于约 3h 前，应接近完成
- **exp012_llama_fewrel_ch2** PREPARING：LLaMA-3.1-8B FewRel 80-rel BCS-controlled exp2，排队等 40-rel 完成后启动。Reviewer 已确认远程无脚本文件，Agent 需在 40-rel 完成后创建并启动
- Paper Agent 刚完成 Limitations Channel 2 诚信修正（"pending" → 诚实报告 8B negative 结果），编译成功 12 页
- ARR DDL：2026-05-25（距今 10 天）

### 4. 📋 待办
- exp_fewrel_40rel_r4 完成回调 → 快速检查 exp1 结果（count curve 趋势 + BCS effect），决定是否需要 exp2 → 立即启动 exp012_llama_fewrel_ch2
- exp012_llama_fewrel_ch2 完成 → 审查结果，判断 LLaMA 8B 在 FewRel 上的 BCS effect 是否 robust → 结果通知 Paper Agent 更新论文
- 两个实验全部完成 → 评估是否所有 claims 证据链完整，考虑是否需要 dream_simulate 或提交审稿

### 5. 🎯 战略上下文
- 核心 story：type confusability 独立于 type count 预测 LLM IE 退化，跨 NER/RE/ED 三任务验证
- Claim 1+2 证据链已强（Few-NERD ✓, FewRel 80-rel ✓, MAVEN ✓），Claim 3 (SDGD) 已放弃转 negative result
- 多模型验证（exp-012 系列）是最后的证据补强：LLaMA-8B exp1 count curve 成功，但 exp2 random batches 不 robust（8B floor effects + BCS range compression）——论文 Limitations 已诚实报告
- 40-rel 实验填补 16-rel 和 80-rel 之间的 scaling gap，展示 confusability effect 随 schema 规模放大
- 易错点：LLaMA-8B 能力天花板低，不要期待与 Qwen3-32B 同等 effect size；extreme batches 方向一致但 random batches 可能不显著，这是已知现象不是 bug


---
