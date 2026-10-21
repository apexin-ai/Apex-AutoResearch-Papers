# reviewer / loop_9.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`49f665aa62a5d89f86da.json`](../../sessions/49/49f665aa62a5d89f86da.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-17T07:51:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- cqa1-38874 只能用 GPU 0（`execution.gpu_ids=[0]`）。之前 D051 全程合规，但 LLaMA 70B 跑在 westd-24295 用 2 卡（TP=2），westd 的 GPU 分配需确认。
- 论文文件在**本地** workspace（`projects/schema-dag-extraction/docs/paper/`），训练代码/数据在**远程** cqa1-38874（`/root/schema-dag-extraction/`）。两边同名文件（如 plot scripts）本地是 production 版本。
- Oracle gap 数字刚被标 warning：introduction 写 +29.8pp，sdgd_negative 写 +22pp。Director 应已收到修复建议，但下一个"你"审查时需确认是否已统一。

### 2. 🖥️ 基础设施快照
- **主服务器**: cqa1-38874 (root), 工作目录 `/root/schema-dag-extraction/`, Python `/root/miniconda3/bin/python3.12`
- **新服务器**: westd-24295（LLaMA 70B 用），env-setup worker 失败过一次（API timeout），需重试
- **模型**: Qwen3-32B-FP8 (cqa1, vLLM), LLaMA 3.1 70B-Instruct-FP8 `neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8` (westd, 待部署)
- **活跃进程**: prompt_sensitivity 刚完成（EXIT_CODE=0）；D051 全部完成（3 seeds × 2 datasets）；cqa1 GPU 0 当前空闲
- **LLaMA 脚本已就绪**: `/root/schema-dag-extraction/scripts/run_d051_count_curves_llama70b.py`, `run_bcs_controlled_llama70b.py`, `run_llama70b_cross_model.sh`

### 3. 📊 当前状态
刚完成 Round 10 Action Matrix 审查并提交。核心审查意见：
- SYSTEMIC_ISSUE A（因果语言）修复方向正确但不应过度矫正 — BCS-controlled 是操纵实验，可用比纯 correlation 更强的语言
- 遗漏 prompt sensitivity 结果整合（PS row 已建议补入）
- TOST 解读同意 R2 reading（primary passed, factorial is sensitivity check）

**Registry RUNNING**: `exp_d051_count_curves_25`（实际已全部完成，registry metrics 滞后）
**等待中**: Director 批准 Action Matrix 后 Agent 开始执行 text modifications（预计 4-6h）；westd env-setup 重试；LLaMA 70B 实验启动

### 4. 📋 待办
- Agent 开始执行 Round 10 Action Matrix → 逐条审查 text modifications（重点：C1 因果语言是否过度矫正、C2 R² 叙事重构、W1 页数是否 ≤8）
- westd-24295 env-setup 成功 → 验证 GPU 分配合规 + 确认 LLaMA 脚本可执行
- LLaMA 70B count curves 完成 → 交叉验证：monotone RE decline 是否复现、NER U-shape 是否复现、BCS correlation 方向+量级 vs Qwen3
- Agent 提交修改后章节审查 → 按 §5.1-5.2 维度审（Claim 可信度、叙事逻辑、审稿人攻击面），用 §5.3 评分模板（如 paper_agent_request_review 触发）
- prompt sensitivity 数据写入论文 → 验证数字与 worker 报告一致（count_32: v2 r=-0.648, minimal r=-0.771, 4/4 negative）

### 5. 🎯 战略上下文
- **论文核心结论**: schema-guided LLM IE 的性能退化可分解为两个正交维度（count→recall, confusability→type confusion），pairwise SCS 是跨任务稳健的 confusion predictor，SDGD decomposition 因 merge amplification + routing failure 而失败
- **目标**: EMNLP 2026 ARR May 25 cycle（还剩 ~8 天）
- **最大 claim 强度**: "robust architecture-independent phenomenon" — 不是 "empirical law"（缺 tight functional form + broad replication）
- **易错点 1**: 本地 vs 远程文件。论文在本地，代码在远程。plot 脚本两边都有但本地是 production 版。审 "worker 是否修改了 X" 前必须确认 X 的 ground truth 在哪一边
- **易错点 2**: NER U-shape 最低点位置。3-seed mean 确认 count_22 为 minimum（0.268），但 seed=123 最低点在 count_44（差异仅 0.5pp）。论文已改为 "plateau at ~0.27 across counts 22-44"
- **易错点 3**: Oracle gap 两个数字（+29.8pp vs +22pp）来自不同实验配置，已报 warning 待修复
- **决策链关键节点**: D012 story spine 修订 → D019 drop SDGD as positive contribution → D051 3-seed 25-batch upgrade → Round 10 SYSTEMIC "predictive framework" pivot


---
