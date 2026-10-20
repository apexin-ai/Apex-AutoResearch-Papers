# reviewer / loop_1.md

**trace distill repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`d9902fad6e272be29520.json`](../../sessions/d9/d9902fad6e272be29520.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T16:39:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 SSH 工具名是 `gpu-6000pro-1`（不是 `westd-18314`，后者是配置文件里的别名，SSH 工具不识别）
- fastapi_1/2 的 trace 是 import 阶段 PydanticUserError 崩溃产物（不是 bug-triggering 执行路径），如果它们的 repair 结果异常应排除，不要当正常数据用
- fastapi_3 和 fastapi_5 trace 收集持续失败（0 events），不要再尝试修复这两个
- MVP 阶段 API-only，GPU 不涉及。但 Research 阶段 cuda:0 被 diagprobe 项目占用（GRPO 训练），注意回避

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-1 (RTX 6000 Pro × 2)，工作目录 `/root/trace_distill_repair/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 数据：`/root/trace_distill_repair/pipeline_output/` — 38 个实例的 trace + structural/line segments + summary.json（23:46 UTC 全量干净重建）
- BugsInPy 实例：`/root/trace_distill_repair/bugsinpy_workspace/instances/`
- 本地 artifacts：`/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/trace_distill_repair/artifacts/`（15 个文件已同步）
- 无活跃进程，无 tmux session，无 cron

### 3. 📊 当前状态
Phase 1（trace 收集 + 结构化分段）全部完成，数据质量已审查通过。

Registry：`mvp_trace_collect` = DONE（38/40 成功，95%，491 structural segments，完整字段已验证）。无 RUNNING/PREPARING 实验。

**唯一阻塞项：DeepSeek API key**。Phase 2（teacher scoring）和 Phase 3（4-condition repair comparison）全部等 API key。experiment_plan.yaml 中 `mvp_teacher_scoring` 仍标为 BLOCKED（应改为 READY，我已通知 Director）。

无等待中的 Worker/Cron。

### 4. 📋 待办
- **API key 到位 → 审查 Phase 2 teacher scoring 结果**：重点验证 teacher model 是否为 DeepSeek-V4-Flash（`deepseek-chat` 的映射待确认）、precision 抽查方法是否用了 ground truth 还是 confidence proxy、50 segments 抽样是否分层
- **Phase 3 repair comparison 完成 → 审查 mvp_analysis.py 输出**：核对 exact binomial test 计算、>2K token subset 的实例选取、win rate 是否排除了 fastapi_1/2 import-only trace
- **任何 RUNNING 训练实验出现 → 必须 `nvidia-smi` 检查 GPU 设备号**，cuda:0 被 diagprobe 占用是硬约束
- **论文写作审查请求 → 先检查 Agent 是否读过 red-section skill**（L1 合规检查），再做内容审查

### 5. 🎯 战略上下文
**决策链**：D001（MVP teacher-only 设计）→ D002（参数扩展 40 实例/50 segments/p<0.15）→ D003（Claim 4 降级为 future direction）→ D004（启用 line events + basic_block 分段）

**核心假设**：结构化 trace 分段在 >2K token 子集中 win rate > 50%。kill criterion 是 win rate ≤ 50%。灰区（50-55% + p>0.15）用 5 case 定性分析做 tiebreaker。

**最容易判断错的事**：
1. 不要因为 38/40 = 95% 就认为所有实例数据质量相同。8 个实例 structural segments < 5（小 trace），~15 个实例区分度低。真正有意义的 structural vs line 对比来自约 24 个 ≥5 segments 的实例
2. literature_map 中 tracerepair2026 和 tracecoder2026 的 authors 仍是 placeholder，论文定稿前必须补全
3. paper_framing.md 中 "第一个 structure-aware learned compression for execution traces" 的 novelty claim 已初步验证成立（Squeez 最接近但只做 flat text），但要精确表述避免被 Squeez 的 tool output 覆盖范围挑战
4. DDL 2026-05-25，距今 11 天。API key 每拖一天压缩后续所有 phase 的时间窗口


---
