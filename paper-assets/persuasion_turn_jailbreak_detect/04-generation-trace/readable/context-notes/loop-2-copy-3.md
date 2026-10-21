# reviewer / loop_2.md

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`4b78f2b4322debae4d19.json`](../../sessions/4b/4b78f2b4322debae4d19.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-17T16:52:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0-3 on westd-33183，越界即 critical（C001）
- TF-IDF ≤0.65 是 sanity gate，必须通过后才能训练 Phase B。当前 TF-IDF=1.0，数据不合格
- Pilot (pilot_phase_b) 结果不可引用为 evidence（n=3 benign in test, TF-IDF=1.0）
- Phase B full 结果同样不可引用（TF-IDF=1.0 = 词汇快捷方式，treatment 性能无法归因于 persuasion strategy）
- Benign persuasion_strategy 全部 hardcoded=7，这是 spurious feature，treatment 可能在利用它

### 2. 🖥️ 基础设施快照
- 服务器: westd-33183 (root)，4× RTX PRO 6000 Blackwell 96GB
- 工作目录: /root/persuasion_turn_jailbreak_detect
- 模型缓存: /root/autodl-tmp/hf_cache/Qwen/Qwen3-8B, Qwen2.5-7B-Instruct
- DeBERTa: microsoft/deberta-v3-base (HF 在线)
- 数据: data/generated/crescendo_all.jsonl (250条), benign_v4c_full_gpu0.jsonl (115条), benign_v4c_full_gpu2.jsonl (115条)
- 训练数据: data/final/{train,val,test}.jsonl (336/72/72)
- Checkpoints: checkpoints/phase_b_deberta/best/model.pt (735MB), checkpoints/phase_b_gru/{baseline,treatment}
- 磁盘: 30GB 总量, ~6.5GB 可用 (79% used)
- 活跃进程: 无 Python 进程，4 GPU 全部空闲
- wildchat_benign_226.jsonl 已存在于 data/ (733KB)，尚未被使用或评估

### 3. 📊 当前状态
我刚完成 Phase B full 结果审查，发送了 [severity: critical] 报告给 Director。核心结论：TF-IDF=1.0 在所有 K 值完美分类，benign 数据的 register mismatch 问题从 v4b(0.924) 到 v4c(1.0) 恶化。Treatment F1=0.987@K=2 低于 TF-IDF=1.0，方法无增量价值。

Registry: pilot_phase_b (DONE, conclusion=success — 但我已标注为不可信)。Phase B full 未注册 registry。

等待: Director 对 critical 报告的响应 — 是否 pivot 数据策略。

### 4. 📋 待办
- Director 决定 pivot 数据策略 → 审查新方案是否能解决 register mismatch（三个方向: WildChat 真实对话 / formal register 混入 / adversarial filtering）
- 新 benign 数据生成完成 → 独立跑 TF-IDF sanity check 核实 ≤0.65
- sanity PASS + 新 Phase B 启动 → 核实 GPU 合规 + 实验注册 registry
- 任何 Worker 完成通知 → 标准审查流程（数据一致性/实验设计/结论可靠性）
- Agent 注册新实验 → 检查 spec 完整性（命令/服务器/数据路径/模型版本/seed/checkpoint）

### 5. 🎯 战略上下文
- 项目: DisPeD — 用 persuasion strategy sequences 检测多轮 jailbreak，目标 EMNLP 2026 ARR DDL 2026-05-25（~7天）
- D001: 接受 DeBERTa F1=0.789 作为 baseline，停止 TF-IDF 数据迭代，reframe 为 early detection
- **核心瓶颈是数据不是模型**: benign 生成数据（v4b/v4c）与 jailbreak 有系统性 register 差异（casual vs formal/hypothetical），TF-IDF 一眼看穿。模型再好也没用，必须先修数据
- wildchat_benign_226.jsonl 是潜在突破口 — 真实对话可能有更自然的 register 分布，但尚未评估
- 易错判断: treatment F1 数字很漂亮（0.987-1.0），容易被误认为 MVP PASS。必须看 TF-IDF sanity — TF-IDF > 0.65 时任何 treatment 结果都不可信
- Register mismatch 是这个项目从头到尾的核心 blocker，已迭代 v1→v4c 六轮未解决


---
