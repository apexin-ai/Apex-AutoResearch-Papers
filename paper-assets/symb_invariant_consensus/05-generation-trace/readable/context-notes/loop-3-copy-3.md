# reviewer / loop_3.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`4f4586cab9d0867c53f7.json`](../../sessions/4f/4f4586cab9d0867c53f7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-16T01:19:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0（westd-32608 单卡服务器，无其他 GPU）
- vLLM max_model_len=16384，实验 max_tokens 必须 ≤12288（16384 会 400 全灭，proofwriter30 v1 已验证）
- sica_folio30 registry spec.command 仍写着 `--max-tokens 16384`，**启动前必须改为 12288**。我已报 critical + warning 给 Director，但截至 handoff 时 spec.command 未修正
- 模型固定 QwQ-32B，不可替换（D003）

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608(root)，工作目录 `/root/symb_invariant_consensus`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- vLLM：PID 129131（EngineCore PID 129399），端口 8000，模型 `/root/autodl-tmp/models/QwQ-32B/Qwen/QwQ-32B`，max_model_len=16384，gpu_mem_util=0.90
- 数据：`data/proofwriter_subset.json`（30题 T:10/F:10/U:10），`data/folio_subset.json`（30题 T:10/F:10/U:10）
- 活跃进程：sica_proofwriter30_v2（PID 155077，tmux=sica_proofwriter30_v2，cuda:0）
- GPU：NVIDIA RTX PRO 6000 Blackwell 98GB，约 89GB 已用，100% util
- 无 W&B 配置

### 3. 📊 当前状态
sica_proofwriter30_v2 正在运行，P2/30（约 06:30 UTC 进入 traces 5-8/12）。预估总运行 ~2.5-3h。P1 完成结果：SICA=SC=True，SC 12/12 unanimous（单候选），8/12 traces 提取失败（No JSON），390s。

Registry 状态：
- sica_proofwriter30_v2: RUNNING — 逻辑域 ProofWriter 30题，max_tokens=12288 修复版
- sica_folio30: QUEUED — 等 proofwriter 完成后启动，**command 中 max_tokens 仍为 16384 需修**

已发给 Director 的未关闭 issue：
1. [critical→已确认] folio30 max_tokens=16384 回退 bug，Worker 只在 notes 备注未改 command
2. [warning] proofwriter30_v2 P1 单候选 + 高提取失败率（仅 1 题数据，待跟踪）
3. [info] D012 逻辑域 MVP 标准审查通过

### 4. 📋 待办（条件触发式）
- sica_proofwriter30_v2 完成（cron on_complete 或 worker_done）→ 全量审查：C0 多候选率、C1 提取率、SC vote diversity 分布、GPU 合规、结果与 log 一致性。特别关注：逻辑域是否真的产生多候选（整个 pivot 的核心假设）
- sica_folio30 启动前 → 验证实际启动命令是否用了 12288（不要信 spec.command，看 tmux/ps 实际参数）
- sica_folio30 完成 → 同上全量审查 + 合并 60 题按 D012 标准判定 PASS/INCONCLUSIVE/FAIL
- 如果 proofwriter30_v2 的多候选率 = 0%（同 AIME/MATH）→ 立即报 critical 给 Director，逻辑域 pivot 假设不成立，C0 FAIL 确定

### 5. 🎯 战略上下文
**决策链**：D001(MVP) → D002(拒CRD) → D003(标准v2) → D006(kill MATH) → D010(AIME 0pp结构性) → D011(逻辑域pivot) → D012(逻辑域MVP标准)

**核心结论**：QwQ-32B 在数学域（AIME 22题 + MATH 10题 + temp_diversity 5题）答案一致性是模型级特征，所有题目零多候选，SICA≡SC 是结构性的。逻辑域 True/False/Unknown 3-way 答案是最后希望。

**最容易判断错的事**：
1. P1 单候选（12/12 True）可能让你急于下"逻辑域也失败"的结论——但 P1 是 gold=True 的简单推理链题，QwQ-32B 做对了且 unanimous 是正常的。关键看 gold=Unknown 的题（模型不确定性最高）和模型做错的题。等至少 10 题数据再评估 C0。
2. "No JSON found" 的 8/12 提取失败不等于约束提取率低——这是 constraint extraction 阶段的 JSON parse 失败，不是 answer extraction。SC votes 12/12 说明 answer 提取是好的。C1 要看的是 constraint 提取率，但定义上需要看 D012 怎么算。
3. folio30 的 live_test_passed=true 不代表 16384 安全——live test 很可能用了脚本默认值 12288，不是 spec 中的命令行参数。


---
