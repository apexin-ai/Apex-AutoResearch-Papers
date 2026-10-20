# agent / loop_1.md

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`23473831be8c117ed446.json`](../../sessions/23/23473831be8c117ed446.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T10:25:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器只有 `autodl-rtx6000pro` 一台，GPU 由 vLLM 独占，不能同时跑其他 GPU 任务
- **代码同步必须 cat/grep 验证** — 之前 3 次 Worker 声称"已同步"但服务器文件未变，被 Reviewer CRITICAL。不信 Worker 自报，回调后 spawn 验证 Worker
- config.py 服务器版本和本地版本不同（服务器 localhost:8000 + dummy key + price=0），同步时**绝对不要覆盖服务器 config.py**
- mvp_pipeline_002 当前状态是 RUNNING（10 条测试中），不要重复创建实验条目

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-rtx6000pro`（ssh -p 32608 root@connect.westd.seetacloud.com，密码 36uUcUDBKOtE）
- GPU：NVIDIA RTX PRO 6000 Blackwell 98GB
- 工作目录：`/root/autodl-tmp/crdd/src/`（pipeline 代码），`/root/autodl-tmp/crdd/results/`（结果）
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 模型：`/root/autodl-tmp/models/Qwen3-32B-AWQ`
- vLLM：awq_marlin 量化，port 8000，max-model-len 16384，~64 tokens/s
- 数据：`/root/autodl-tmp/crdd/data/folio-validation.jsonl`（204 条 FOLIO validation）
- 活跃进程：vLLM server + pipeline v3 测试（Worker 在监控中）
- 本地代码：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/cross_representation_disagreement_diagno/artifacts/src/`

### 3. 📊 当前状态
**正在等待** Worker `worker_code_mvp_v3_code_fix_20260514T094847` 完成 10 条 v3 测试（最后检查在第 6/10 条，预计数分钟内完成）。

Registry 状态：
- `mvp_baseline_001`: DONE, accuracy=74%, gate=PASS_FOLIO
- `mvp_pipeline_001`: DONE (negative), FOL crash 78%, C1/C4/C5 FAIL
- `mvp_pipeline_002`: RUNNING, v2 10 条结果已有（FOL crash 10%, Code crash 40%, C4/C5 PASS），v3 正在跑

三轮迭代进展：
- v1: FOL crash 78% → C1/C4/C5 全 FAIL
- v2: FOL crash 10% ✅, 但 Code crash 40%（thinking token 泄漏）→ C1/C2 FAIL
- v3: 修复 Code 侧（关闭 thinking mode + _strip_thinking 加固）→ 等待结果

### 4. 📋 待办
- Worker v3 回调到达 → 读取结果，核心关注 Code crash rate 和 effective_disagree_rate。如果 Code crash <20% 且 effective disagree >10% → 汇报 Director 并建议跑全量 204 条
- 如果 C1 仍 FAIL（disagree 不够）→ 分析原因（可能 FOL 太准导致双路一致），可能需要降低 FOL prompt 质量或换更弱的模型配置
- Director 批准全量后 → spawn Worker 跑 `pipeline.py --output results/results_v3_full.json`（预计 204×3min ≈ 10 小时）
- 全量完成 → analyze.py 出完整 C1-C5，更新 registry mvp_pipeline_002 为 DONE

### 5. 🎯 战略上下文
- EMNLP 2026 DDL: May 25（剩 11 天）
- 核心假设："双表征分歧提供诊断信号"。v1 数据中 effective disagree rate = 18%（2/11 双路都执行成功的样本），这是假设成立的关键证据。v3 需要更多双路成功样本来验证
- C4（targeted > blind）在 v2 已翻转为 +40pp，说明诊断信息有用。但这基于 exec_crash 的 single_error 样本，不是真正的 disagree。需要 Code 侧修好后看真实 disagree 上的 C4
- **易踩坑**：不要只改本地代码就说"已完成"——必须在服务器上 cat 验证。之前这个问题浪费了 8+ 小时
- **易踩坑**：Worker 轮询太频繁会耗尽上下文（第一个下载 Worker 就是这样死的）。ssh_execute 等待用 while+sleep 循环，不要 Worker 自己循环调 ssh


---
