# reviewer / loop_1.md

**svs formal verification** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`8fc5781937fd213a41a1.json`](../../sessions/8f/8fc5781937fd213a41a1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T08:39:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- vLLM TP=2 只能跑在 cuda:0,1。cuda:2,3 当前分配为空闲/预留，任何训练或推理进程不得占用 cuda:0,1 以外未经 Director 批准的卡
- MVP 进程 PID 24681 正在运行，**禁止 kill**——这是唯一的正式实验数据源
- Formalization 使用外部 API (47.94.22.126)，**不是** DeepSeek 官方 API。不要改 endpoint 除非 Director 指示
- 代码部署路径是 `/root/svs_pipeline/`（不是 `/root/autodl-tmp/svs_formal_verification`）。本地 artifacts 和服务器代码可能不同步——**审查时两边都读**

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090（RTX 5090 32G × 4），SSH account: root
- 工作目录：`/root/svs_pipeline/`（pipeline 代码）；`/root/autodl-tmp/` 数据盘 220GB 可用
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型：`/root/autodl-tmp/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`（chain gen, vLLM port 8001）
- 模型下载中：`/root/autodl-tmp/models/Qwen/Qwen2___5-14B-Instruct/`（ModelScope，~3% 进度，PID 25228）
- 数据：ProofWriter HF cache `/root/.cache/huggingface/datasets/`；FOLIO `/root/autodl-tmp/data/folio/`
- MVP 日志：`/root/mvp_run.log`（11K+ 行，stdout+stderr 重定向）
- 活跃进程：PID 24681（MVP 50×8 运行），PID 12250（vLLM APIServer），PID 12517（vLLM EngineCore），PID 25228（Qwen 下载）

### 3. 📊 当前状态
**已完成审查**：8 个 worker（dual endpoint config / vLLM prep / SC baseline / stopword fix / vocab v2 / kill orphan vllm / FOLIO loader+cost fix / binary filter baseline）+ 1 次方法论深度审查（IC 全 SAT 退化）+ 1 次 ROADMAP 审查

**Registry**：mvp_001 RUNNING（唯一实验）

**MVP 进度**：Problem 1/50 完成（34 分钟），Problem 2/50 进行中。**实际运行时间 ~24-28 小时**（非 ROADMAP 声称的 4 小时）。已报告 Director。Problem 1 结果：SVS=Unknown（正确），SC=False（错误）——n=1 无法下结论但方向正面。

**等待中**：
- MVP 完成回调（预计 ~12-16 小时后）
- PCV 模块实现 worker 完成回调（Agent 正在编写）
- Director 对运行时间预警的响应（是否并行化 formalization API 调用）

### 4. 📋 待办
- MVP 完成 → 全面审查：P1 formalization rate / P2 IC discrimination / UNSAT 比例 / CCLC 诊断 / per-label breakdown / GPU 合规终检
- PCV 模块 worker 完成 → 审查代码：premise formalization 逻辑 / z3_checker 修改 / scoring 集成
- PCV 重评结果出来 → 对比原始 IC vs PCV-IC 的区分力，这是项目 make-or-break 判定
- Qwen 下载完成 → 确认模型完整性，提醒 Director 可启动 cross-model 实验
- 任何新 worker 部署代码 → 检查是否影响正在运行的 MVP（PID 24681 用的是部署时的代码快照，新代码需重启才生效）

### 5. 🎯 战略上下文
**决策链**：D001（MVP 设计）→ D002（50×8 参数）→ D003（本地 GPU）→ D004（外部 V3.2 formalization）→ D005（Qwen cross-model）→ D006（PCV pivot，基于 Reviewer 审查）

**核心风险**：IC 全 SAT 退化是已确认的方法论缺陷——Z3 只检查 internal coherence，现代推理模型的错误推理是"内部自洽的错误"。D006 PCV pivot 是应对方案。如果 PCV 也不能区分正确/错误链，项目需要 entailment checking ablation 或 analysis pivot。

**易错点**：
1. **不要被 Problem 1 的正面结果误导**——SVS 在 IC 退化下选对可能只是因为正确答案组恰好 FC 更高，n=1 无统计意义
2. **Vocab 仍有残余问题**：`tiger_then`, `cow_then`, `tiger_and` 等伪常量未被 stopword 过滤。不阻塞但影响 formalization prompt 质量
3. **cost_tracker 定价修复不影响当前 MVP 运行**——PID 24681 启动时加载的是旧代码，V3.2 费用仍显示 $0
4. **Binary filter baseline 在 IC 全 SAT 下退化为 SC**——threshold=0.5 时所有链都通过过滤，只有 PCV pivot 后才有意义
5. **report.md 严重过时**（显示所有 GPU 空闲），不要依赖它判断项目状态——以 registry + ssh_read_only 为准


---
