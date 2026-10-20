# director / loop_2.md

**trace distill repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`6d5b519e98f4c08550e3.json`](../../sessions/6d/6d5b519e98f4c08550e3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-15T01:43:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- Line scoring 必须单 Worker 串行执行，禁止多 Worker 同时操作 scoring 进程（D008，5 次失败的血泪教训）
- 服务器名是 `rtx6000-diagprobe`（不是 `gpu-6000pro-1`，不是 `westd-18314`，已在本轮修正）
- GPU 分配为 cuda:0 + cuda:1，但 MVP 阶段全程 API-only 不用 GPU
- API 端点 `http://47.94.22.126/v1`，模型 `deepseek/deepseek-v4-flash`，max_concurrent 已降到 3

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (connect.westd.seetacloud.com:18314)，root 用户
- 工作目录：/root/trace_distill_repair
- Python：系统有 torch 2.10.0+cu128，transformers 4.57.6, accelerate 1.13.0 等已装好
- GPU：2× RTX PRO 6000 Blackwell (96GB each)
- 已有模型：Qwen3-8B + Qwen3-30B-A3B (73GB)，student model 未定
- 活跃进程：PID 74506 line scoring（segment 470+ of youtube-dl_20，最后一个大实例）
- 磁盘：数据盘 175GB/250GB 可用

### 3. 📊 当前状态
Line scoring (mvp_line_scoring_clean) 接近完成——35/38 实例已完成，最后一个 youtube-dl_20 (12764 segments) 在跑 segment 470+。Registry 仍显示 RUNNING。有 finalize Worker 在监控，进程结束后自动：收集结果 → 更新 registry → 启动 structural scoring 重跑。

- `mvp_line_scoring_clean`: RUNNING（接近完成）
- 其余 6 个实验全 DONE（1 success: trace_collect, 5 failed/killed: 全是之前互踩的 line scoring）
- 等待：finalize Worker 回调确认 line scoring 完成 + structural scoring 重跑结果

### 4. 📋 待办
- Line scoring 完成回调 → 确认 phase2_line_scores.json 完整性（38 实例 + 错误率 <10%）→ 更新 registry DONE(success)
- Structural scoring 重跑完成 → 确认脏数据已清除（旧 16 error + confidence=0.5 条目消失）→ 注册 mvp_structural_scoring_clean
- 两项 scoring 都完成 → 启动 Phase 3 repair comparison（4-condition: structural_filtered / line_filtered / full_trace / no_trace）
- Phase 3 结果出来 → 判断 MVP pass/fail（>2K token 子集 structural win rate > 50%, p<0.15）
- MVP pass → complete_mvp() + 进入 research 阶段（post-mvp-kickoff skill）

### 5. 🎯 战略上下文
- 核心假设：结构化分段过滤优于行级过滤，修正 EMNLP 2025 "Do Code Semantics Help?" 的负面结论
- Kill 标准：structural win rate ≤ 50% in >2K subset → 终止项目
- 目标：EMNLP 2026 ARR May，DDL 2026-05-25（距今 11 天），时间极紧
- 易错点：(1) 不要再派多 Worker 碰 scoring；(2) structural scores 旧文件含脏数据必须重跑才能用于 Phase 3；(3) API 不稳定时降并发而不是重启进程
- Student model 选型未定（ROADMAP 说 0.6B，服务器有 Qwen3-8B/30B-A3B），research 阶段再决策
- D001-D008 决策链在 decisions.yaml，关键决策：D005 采样策略、D008 单Worker串行


---
