# agent / loop_1.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`9787b8b1f3c3858d0360.json`](../../sessions/97/9787b8b1f3c3858d0360.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-14T11:05:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单只有 `autodl-5090:cuda:0` 和 `autodl-5090:cuda:1`，但实际实验全在 `gpu-5090-2x-2` 上跑的（历史原因，config 未更新）。提交前必须确认 Director 是否已将 gpu-5090-2x-2 加入白名单，否则需要 push back
- baseline-llm-judge 需要 API key（`request_secret('openrouter_api_key')`），base_url=`http://47.94.22.126/v1`，预算 $50-200。**未获 key 前不得启动**
- 人工标注 gold set（400+ 窗口）是 temporal-label-model 的硬前置依赖，**不能跳过或用自动标签替代**——这是 Claim 1 的根基
- EMNLP 2026 ARR deadline 5/25，只剩 **11 天**。D014 用户承诺资源管够
- conf≥2 子集（15,401 windows）上 command_repetition 单 LF (0.9451) 超过 probe (0.9055)——论文必须透明讨论此循环性限制，不得回避

### 2. 🖥️ 基础设施快照
- **主服务器**: gpu-5090-2x-2（RTX 5090 32G × 2），account=root
- **备用服务器**: autodl-5090（RTX 5090 × 2），密码 H6BKr9xWo+8Z，端口 23165
- **工作目录**: `/root/autodl-tmp/agent_progress_probe`
- **Python**: `/root/miniconda3/bin/python`，激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **数据**: `data/embeddings.pt`（1.1GB, 54,809 windows, 1024-dim）, `data/windows_labeled.jsonl`（1,824 labeled windows for LLM judge pilot）
- **Checkpoints**: `checkpoints/best_model.pt`（conf≥2, seed42）, `checkpoints_seed123/`, `checkpoints_seed456/`, `checkpoints_full/`（全量数据）
- **活跃进程**: 无。所有 cron 已 reconcile，0 个活跃 Worker
- **OpenHands cross-agent embedding**: ROADMAP 标记"进行中"但 registry 无对应条目——需要 SSH 确认实际状态

### 3. 📊 当前状态
**刚完成**: probe-multiseed 三种子验证（mean macro-F1=0.9185±0.0113），所有 seed 均满足 >0.70 且 gap >5pp 条件。

**Registry 摘要**（6 条，全部 DONE 或 PREPARING）:
| ID | Status | 关键指标 |
|---|---|---|
| emb_001 | DONE(success) | 54,809 windows embedded, 1024-dim |
| probe_001 | DONE(success) | macro-F1=0.9055, gap=6.24pp vs Repeat-3 |
| probe-002 | DONE(success) | macro-F1=0.8468 (全量, conf≥0) |
| baseline-meanpool-lr | DONE(success) | macro-F1=0.8435, GRU gap=+6.2pp |
| probe-multiseed | DONE(success) | mean=0.9185±0.0113, 3 seeds |
| baseline-llm-judge | PREPARING | 等 API key |

**等待中**: 
- 无 Worker 运行、无 Cron 活跃
- baseline-llm-judge 等 API key 审批
- human-annotation 等 Director 确认标注人力安排
- OpenHands cross-agent embedding 状态不明（ROADMAP 说在跑但 registry 无条目）

### 4. 📋 待办（条件触发式）
- API key 到手 → 启动 baseline-llm-judge Worker（pilot 50 windows → 全量）
- Director 确认标注人力 → 准备标注材料（采样策略 + 标注指南 + 界面），派 Worker 执行
- OpenHands embedding 确认完成 → 跑 cross-agent 迁移评估（probe 在 OpenHands 上的 zero-shot 表现）
- GPU 空闲 → 并行铺 cosinesim-check（CPU）+ flyingsquid-baseline（CPU）+ outcome-bp-sensitivity（1 GPU）
- human-annotation gold set 完成 → GO/NO-GO 检查点：Fleiss κ ≥ 0.6 + LF temporal dynamics 在人工标签上验证 → GO 则启动 temporal-label-model 实现；NO-GO 则转 Plan B（empirical study 定位）
- Re-dream 报告返回 → 分析新 framing 的审稿模拟结果，必要时调整 paper_framing.md

### 5. 🎯 战略上下文
**核心结论链**:
- D007: MVP 通过，probe 有效（0.9055, +6.24pp）
- D009: Dream 三档 Weak Reject，novelty 不足 → framing 升级为 temporal label model（方法论贡献）
- D010: 全量数据 F1 降至 0.8468，但 GRU vs MeanPool gap 反而扩大（4.83→12.74pp），证明时序建模在噪声数据上价值更大
- D013: temporal-label-model 必须 gate on gold set，否则循环论证
- D014: 回退到 EMNLP 5/25（原定 ACL 8月），用户承诺资源管够
- D015: Cross-agent LF 适配失败，需修 LF + OpenHands 人工标注 200 窗口

**最容易判断错的事**:
1. **不要把 conf≥2 和 conf≥0 的指标混用**——conf≥2 是"clean"子集（0.9055），conf≥0 是全量（0.8468），论文不同 claim 用不同子集
2. **temporal-label-model 目前零实现零证据**——这是 Claim 1 的核心，但完全依赖 gold set 验证。Plan B 已就绪但需要 Director 触发
3. **OpenHands cross-agent 的 LF 不能直接复用**——D015 已确认 SWE-agent 的 LF 在 OpenHands 上不工作，需要适配
4. **experiment_plan.yaml 中很多条目 registry_id 未关联**（如 probe-multiseed plan 里 status=planned 但 registry 里已 DONE）——plan 和 registry 有脱节，以 registry 为准
5. **Worker 池当前 = 0，违反 L1 红线**（Worker 池 <2 = 失职）——但当前确实全部阻塞在 API key + 标注人力 + OpenHands 状态确认上，应立即向 Director 汇报阻塞项并请求解除


---
