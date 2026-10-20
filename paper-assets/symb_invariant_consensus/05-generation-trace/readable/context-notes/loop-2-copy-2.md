# agent / loop_2.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`699c9ebc54548736f962.json`](../../sessions/69/699c9ebc54548736f962.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-15T18:55:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 只能用 westd-32608:cuda:0（gpu_ids 白名单只有这一张）
- QwQ-32B 是唯一允许的模型，不可替换
- vLLM max_model_len=16384（32768 会启动失败）
- May 19 UTC 前 MVP 未 pass → 放弃 EMNLP，切 AAAI 2027
- 环境用 conda base（不要创建 venv），激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608，账号 root，项目路径 /root/symb_invariant_consensus
- Python：/root/miniconda3/bin/python (3.12.3, conda base)
- 关键包：torch 2.11.0+cu130, vllm 0.20.2, z3-solver 4.15.4
- GPU：NVIDIA RTX PRO 6000 Blackwell 98GB, cuda:0，CUDA 12.8
- 模型路径：/root/autodl-tmp/models/QwQ-32B/Qwen/QwQ-32B/（ModelScope 嵌套结构）
- 数据：/root/symb_invariant_consensus/data/aime2024_subset.json (30题), math500_subset.json (50题)
- vLLM：port 8000, bfloat16, gpu_memory_utilization=0.90
- 活跃进程：**无**（sica_aime30_v2 已退出，vLLM 状态未知——诊断 Worker 正在查）
- 待回调 Worker：`worker_diagnose_sica_aime30_v2_20260515T155354`（正在 SSH 诊断日志）

### 3. 📊 当前状态
**刚收到 sica_aime30_v2 失败回调**（EXIT_CODE=129/SIGHUP，4/30 题完成后 vLLM 卡死在第 5 题）。已完成 session-start 初始化（registry 同步、cron reconcile、读 ROADMAP/memory/report），已派诊断 Worker 但**尚未收到回调结果**。

Registry 状态：
- `sica_aime30_v2` DONE/failed — AIME 30 题 v2，4/30 完成，3/4 正确（interim），vLLM 第 5 题卡死
- `sica_aime30_t07` DONE/killed — AIME v1，bug 版本被 kill
- `mvp_math50_t07` DONE/killed — MATH 50 题，bug 版本被 kill
- `sica_temp_diversity` DONE/negative — QwQ-32B 零答案分歧（MATH 太简单）
- `sica_smoke_5q` DONE/success — 5 题 smoke test 通过
- `crd_folio_main` DONE/success — CRD 实验（非 SICA，历史遗留）
- `smoke-test-5q` PREPARING/failed — 废弃条目

**尚未向 Director 汇报本次失败**——等诊断 Worker 回调后一并汇报。

### 4. 📋 待办
- 诊断 Worker 回调到达 → 根据 root_cause 更新 registry notes → 向 Director 汇报（带 [资源] 行）→ 提出修复方案或 v3 重跑建议
- vLLM 已死 → 需要重启 vLLM 后才能跑任何实验；vLLM 还活着 → 可立即重提交
- 诊断结论为 infrastructure 类（vLLM OOM/crash）→ spawn Worker 修复并重跑 v3
- 诊断结论为 resource 类（GPU 内存不够）→ 向 Director 汇报需要调整参数（降 max_tokens 或降并发）
- AIME v2/v3 稳定后 → 还需跑 MATH 50 题 + ProofWriter 10 题完成完整 MVP
- May 19 checkpoint 逼近（剩 ~3.5 天）——所有实验必须加速并行

### 5. 🎯 战略上下文
- **核心方向**：SICA（Symbolic Invariant Consensus Aggregation）— 从多条 LLM 推理路径提取符号约束，通过 MAX-SAT 找全局一致子集，替代统计共识 (SC)
- **MVP 三档判定**：PASS=提取率≥50% + 矛盾≥5题 + SICA≥SC+2pp；INCONCLUSIVE=扩展到100题；FAIL=提取率<30%或矛盾<3题
- **D006 是关键决策**：kill 旧 bug 版本 → 修 bug → AIME 30 题优先。v2 已修 regex/timeout/semaphore 但仍挂
- **已知关键 pattern**：QwQ-32B 在 MATH 上零分歧（太简单），AIME 上有真实约束矛盾（4 excluded by MaxSAT），SICA 价值确实随难度递增
- **最容易判断错的事**：不要以为 vLLM 一直活着——它可能因长推理 OOM 崩溃；每次提交实验前必须做健康检查。也不要假设 .venv 存在，这台机器用 conda base
- **易踩坑**：EXIT_CODE=129 是 SIGHUP 不是 OOM，可能是 tmux session 问题而非代码 bug；两次 v1 被 kill 是人为操作不是自动失败


---
