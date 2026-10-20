# director / loop_22.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_22.md`
- **Structured JSON:** [`d09672465942874d5a87.json`](../../sessions/d0/d09672465942874d5a87.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: max_messages
updated: '2026-05-22T18:14:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 seetacloud-westd-4x5090，GPU 分配以 `get_project_status` 返回的 `gpu_ids` 为准，不得越界使用其他项目的卡
- Qwen3-14B 模型下载路径在 `/dev/shm/Qwen3-14B/`（ModelScope 临时目录），下载完成前不要移动或删除临时文件
- 项目已进入审稿阶段（review_chat_id: `oc_0ae20ec1ce60f9c0589d629648584eff`），研究端继续推实验，不干预 Group C 的论文格式/投稿工作
- EMNLP 2026 投稿目标，long paper 8 页限制，不降级会议

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westd-4x5090 (`connect.westd.seetacloud.com`)
- 工作目录：`/home/sonny/exec-sim-repair-verifier`
- 模型缓存：`/dev/shm/Qwen3-14B/`（Qwen3-14B 下载中）；已有模型在 `/root/autodl-tmp/` 下
- 4×RTX 5090 GPU
- 实验总数 254 个，成功 139 个

### 3. 📊 当前状态
- **Qwen3-14B 模型下载进行中**：曾从 6.0G 回退到 16M 后重启，Reviewer 报告时恢复到 3.1G，预计还需 1-1.5h（从 Reviewer 报告时算起）
- **RUNNING 实验**：
  - `cls14b-func-s42`：Qwen3-14B QLoRA CLS 训练，阻塞在模型下载上
  - `14b-baseline-0shot-3shot`：0-shot/3-shot baseline eval，脚本已写好（代码审查通过），等模型下载完才能执行
- **已派指令给 Agent**（刚发出，Agent 正在处理）：
  1. 监控下载进度，下载停滞则切换源
  2. 下载完成后训练和 eval 并行跑（不同 GPU）
  3. 每 30 分钟汇报下载进度

### 4. 📋 待办
- Qwen3-14B 下载完成 → 确认 cls14b-func-s42 训练自动启动 + 立即在另一张卡跑 `eval_14b_baseline.py`（0-shot 和 3-shot）
- 下载再次中断/停滞 → 切换到 HuggingFace mirror 或其他 ModelScope CDN 重试
- 14B 训练完成 → 分析结果，与 8B baseline (90.48%) 对比，确认 CLS 是否有 scaling trend（4B→8B→14B）
- 14B 0-shot/3-shot eval 完成 → 结果写入论文 Table，与 8B baselines 对比
- Agent 汇报 14B 全部完成 → 评估是否所有论文 claims 的实验证据已齐备，推进审稿迭代

### 5. 🎯 战略上下文
- 项目核心：exec-sim-repair-verifier，研究代码修复验证中的执行模拟方法
- 254 个实验已跑完 233 个，当前 14B 实验是收尾阶段——验证 scaling trend（从 4B→8B→14B）
- 论文已进入审稿循环（Group C 独立运作），研究端的任务是补齐 14B 数据点
- **易错点**：14B 模型下载不稳定（已重启过一次），需要持续监控直到确认完成；不要假设 Agent 处理了 worker_done 就等于 eval 已经跑了——Reviewer 确认过当前无任何结果文件产出
- 决策日志 163 条，论文溯源覆盖率 34/43，experiment_plan 有 18 个待处理实验


---
