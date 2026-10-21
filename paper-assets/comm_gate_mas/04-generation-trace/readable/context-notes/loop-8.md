# agent / loop_8.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`3bfe19a667eb47b66e02.json`](../../sessions/3b/3bfe19a667eb47b66e02.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-04-29T02:46:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- **只能用 cuda:1**（gpu_ids=[1]），cuda:0/2/3 分配给其他项目，禁止使用
- 服务器 westb-4x6000-a 必须用 conda base 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（系统 Python 无 pyyaml）
- vLLM pre-flight check 必须校验 model name（`curl /v1/models` 比对），仅 HTTP 200 不够（D217 事故：错误模型导致全量 404）
- 禁止对部分有效数据使用 `--force` 重跑——只补跑缺失 seeds，不覆盖已验证数据
- 72B oracle 实验用 Qwen2.5-72B-Instruct-AWQ，需 vLLM 服务端跑在 cuda:1 上，orchestrator 跑在本地 Mac

### 2. 🖥️ 基础设施快照
- 服务器：**westb-4x6000-a**，SSH account=`comm_gate`，工作目录 `/root/autodl-tmp/comm_gate_mas`
- Python：`/root/miniconda3/bin/python`（conda base），激活命令见上
- 模型路径：Qwen2.5-7B/72B-AWQ、Llama-3.1-8B 通过 vLLM 加载（HF cache 在服务器默认位置）
- W&B：未使用（本项目用 JSON 输出 + registry 追踪）
- 活跃进程：`llama_heuristic_stratqa_3seed` PID=521912, cuda:1, 3-seed sequential（seed 0 ~task 22/200）
- Cron：reconcile 返回 0 活跃——llama_heuristic_stratqa_3seed 的 cron 可能已清理（之前有 false positive 回调，retry_count=2）
- 无活跃 Worker（均已完成/销毁）

### 3. 📊 当前状态
**刚完成**：cross-task robustness 实验批次——StrategyQA (Llama/Qwen) + ARC (Llama/Qwen)。StrategyQA 两个都 success（Llama +6.5pp, Qwen -0.5pp non-inf）。ARC 两个 invalid（answer extraction bug，D226 标记作废，不入论文）。P0+P1+P2 论文修改全部完成。

**正在跑**：
- `llama_heuristic_stratqa_3seed` (RUNNING) — StrategyQA 3-seed 复现，验证 +6.5pp 鲁棒性，cuda:1, pid=521912，预计 ~2-3 小时完成全部 3 seeds

**PREPARING（大多数是历史残留，非活跃）**：
- `oracle_qwen72b_seed123` — 72B 第二 seed，等 cuda:1 空出后启动
- `vllm_llama_8192` / `vllm_llama_8192_v2` — 旧 vLLM 服务条目，可忽略
- `p1_oracle_precompute_*` / `oracle_qwen_gsm8k` / `5run_pruned_rerun` — 已脱离 critical path

**等待中**：无 Worker 回调、无活跃 Cron。llama_heuristic_stratqa_3seed 完成后需要人工检查或重新注册 cron 监控。

### 4. 📋 待办（条件触发式）
- `llama_heuristic_stratqa_3seed` 3-seed 完成 → 分析结果：CI 是否排除 0 → 若是则升级 StrategyQA claim 为 "robust"，写入论文 cross-task 表格
- 3-seed 完成且 cuda:1 空出 → 启动 `oracle_qwen72b_seed123`（72B seed 2），命令已在 registry spec 中
- 72B seed 2 完成 → 0 discordant flips → 更新 results.tex L93 "preliminary single-seed" 措辞；有 discordant → 停止，不再补 seed 3
- ARC 实验 invalid (D226) → 如果 Director 要求修复 answer extraction bug 并重跑，需要修改 `src/pruning_validation.py` 中 ARC 选项格式化逻辑（commit 543603b 已部分修复）
- DDL 逼近（abstract 5/3, paper 5/5-6）→ PDF 编译验证 + Reviewer 复审应在 5/1-2 完成

### 5. 🎯 战略上下文
**核心发现**：Dissociation——ack 消息扰动敏感性最高，但聚合剪枝安全。双 backbone (Qwen/Llama) 10-seed oracle + heuristic 均通过 non-inferiority。72B 单 seed 零翻转。

**决策链关键节点**：
- D222/D223: Reviewer 反审后确认 reframe 策略——"empirical finding paper"定位，不 overclaim 理论贡献
- D221: GPU 冻结令——cuda:1 不释放给其他项目，留给阈值实验 → 72B seed 2
- D220: Llama heuristic 5-seed beneficial (+2.20pp)，但主 claim 仍保守用 non-inferiority
- D226: ARC 实验因 answer extraction bug 全部 invalid，cross-task 表格只报 StrategyQA + GSM8K

**易错点**：
- Llama +2.1pp 和 Qwen +0.4pp 效果差 5×，不要 claim "consistently improves"——主 claim 是 non-inferiority (safety)，improvement 只是 Llama 的 secondary finding
- 72B 是 AWQ 量化版，suppress rate 66.8% 但只有单 seed——措辞必须用 "preliminary"
- Gemma κ=0.35 标注质量差，论文中降级为 "exploratory"，不计入主 backbone 数
- Heuristic (char<30) 跨任务迁移差（StrategyQA F1=0.213），定位为 proof-of-concept 不是 deployment-ready
- Cron 监控可能不活跃——接手后先确认 llama_heuristic_stratqa_3seed 是否仍在跑（`ps -p 521912`），必要时重新注册 cron


---
