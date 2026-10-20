# director / loop_1.md

**trace distill repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`10479a614024d2e9ab95.json`](../../sessions/10/10479a614024d2e9ab95.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-14T18:49:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-18314 的 cuda:0 和 cuda:1。cuda:0 当前被 diagprobe 项目 GRPO 训练占用（PID 30171），不要在上面启动实验
- fastapi_1 和 fastapi_2 必须从所有分析中排除——trace 是 PydanticUserError import 崩溃，非 bug-triggering 执行路径（Reviewer CRITICAL 确认）
- API endpoint: `http://47.94.22.126/v1`，key_id: `openrouter_api_key`，Manager 指定的内部代理，不要改成其他 URL
- Claim 4（通用性/即插即用）已降级为 Future Direction（D003），不作为 core claim，不安排对应实验

### 2. 🖥️ 基础设施快照
- 服务器：westd-18314（SSH alias: rtx6000-diagprobe），RTX 6000 Pro 96GB × 2
- 工作目录：`/root/trace_distill_repair/`
- Python：`/root/miniconda3/bin/python3`（Python 3.12.3，需 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 数据：`/root/trace_distill_repair/pipeline_output/`（38 个实例的 trace + segments）
- API：OpenRouter 兼容，base_url `http://47.94.22.126/v1`，支持 DeepSeek V4-Flash/Pro
- 活跃进程：Phase 2 line scoring 可能仍在后台运行（`/tmp/phase2_line_scoring.log`），structural scoring 已完成但需重跑

### 3. 📊 当前状态
**刚发生的关键事件**：Phase 2 structural scoring 完成但结果有严重问题：
- 失败率 24.4%（110/451 segments NoneType 错误）
- Keep 率极低：仅 10/341 (2.9%) segments 标为 keep
- teacher_scorer.py 的 NoneType fix 已部署但 structural scoring 用的旧代码，需重跑
- Line scoring 仍在运行中（错误率暂低）

Registry: `mvp_trace_collect` DONE, `mvp_teacher_scoring` RUNNING

**等待中**：
- Line scoring 完成 → 对比 keep 率判断是否 prompt 问题
- Agent reset handoff → 新 Agent 需要继续处理 Phase 2 重跑

### 4. 📋 待办
- Line scoring 完成 → 检查 keep 率。如果同样极低(< 5%)，问题是 scoring prompt 太严，需调整 prompt 重新定义 "keep" 的标准（当前可能过于保守）
- Line scoring keep 率正常(10-30%) 但 structural 极低 → 说明 structural segments 粒度太大，teacher 倾向整体 drop，需考虑是否降低 structural segment 粒度
- 修复 teacher_scorer.py fallback（persistent None 应标 "error" 不是 "drop"）→ 重跑 structural scoring
- Structural scoring 重跑完成 + line scoring 完成 → 启动 Phase 3 repair comparison
- MVP 判定出来 → pass 则 `complete_mvp()` 进入 research 阶段

### 5. 🎯 战略上下文
- 决策链：D001(MVP 设计) → D002(扩大样本+操作化 kill) → D003(Claim 4 降级) → D004(启用 line events + sub-function 分段)
- **最大风险**：structural scoring keep 率 2.9% 暗示 teacher 可能认为绝大多数 structural segments 无诊断价值。如果这不是 prompt 问题而是真实信号，核心假设（structural > line）可能不成立。在下 kill 结论前必须：(1) 对比 line keep 率；(2) 检查 10 个 keep segments 的分布是否合理；(3) 评估 prompt 是否过严
- **易踩的坑**：不要把 24.4% NoneType 错误率和 2.9% keep 率混为一谈——前者是代码 bug（已修），后者可能是 prompt 设计问题或真实负面信号
- DDL: EMNLP 2026 ARR May 25（距今 11 天），MVP 必须 1-2 天内判定
- literature_map 补充 5 篇 + paper_framing Claim 4 降级 + experiment_plan 同步已完成


---
