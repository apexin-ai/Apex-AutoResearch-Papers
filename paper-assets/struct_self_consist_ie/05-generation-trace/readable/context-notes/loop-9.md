# director / loop_9.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`ee5a4a62f0c394d57d33.json`](../../sessions/ee/ee5a4a62f0c394d57d33.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-21T01:41:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：5090 cuda:0-3, 5090-b cuda:0-3, 5090-c cuda:0-3（共 12 张，不可跨项目用别人的卡）
- API 余额已耗尽（`http://47.94.22.126/v1` 返回 402）——Frontier SC / Spider SQL remaining / HumanEval 全部阻塞，等用户充值或提供 OpenRouter 直连 key（`sk-or-*` 格式）
- 存储的 `openrouter_api_key` 实际是 TUM proxy key，不是 OpenRouter 直连 key——不要尝试用它调 `https://openrouter.ai/api/v1`
- 14B inference 进程（PID 252310）不要标 failed——Agent 已 5 次误判 vLLM 长初始化进程（M021/M037/M038/M047/M049），必须 ps + nvidia-smi 双信号确认
- 论文统一用 micro_f1（D204），不混用 mean_f1
- Frontier SC API 阻塞已向 Reviewer 澄清——不要再标记为"不受 API 影响"

### 2. 🖥️ 基础设施快照
- **autodl-5090** (4×RTX 5090): `/root/autodl-tmp/struct_self_consist_ie`。32B merged model at `checkpoints/qwen25-32b-fewnerd-merged/`。merge script: `scripts/merge_32b_lora.py`
- **autodl-5090-b** (4×RTX 5090): `/root/autodl-tmp/struct_self_consist_ie`。Models: Qwen2.5-7B, Qwen3-8B, LLaMA-3.1-8B, 16 LoRA checkpoints. vLLM 0.18.1. 32B base model downloaded via ModelScope.
- **autodl-5090-c** (4×RTX 5090): `/root/autodl-tmp/struct_self_consist_ie`。14B merged at `checkpoints/qwen25-14b-fewnerd-merged-final/`
- **活跃进程**: 32B inference PID 978386 (5090, TP=4, ~8.8%); 14B N=8 PID 252310 (5090-c:cuda:0); FewNERD T-ablation s123 PID 296744/296880/297143 + s456 PID 297409 (5090-b:cuda:0-3); CoNLL s456 (5090-c:cuda:1-3)
- **Cron**: 14B PID 252310 监控已注册（5min）; 32B cron 已删除（训练完成）

### 3. 📊 当前状态
**刚完成**：D208 战略跃迁——3 件 P0 全部 dispatch（Mechanistic Probe → Agent; Impossibility Reframe → Paper Agent 已在执行 Worker 1 Abstract; Multi-Model Correlation → Agent）。32B 训练 DONE，merge DONE，inference RUNNING。

**RUNNING 实验（8 个）**：
- exp_32b_inference_fewnerd (5090:0-3, ~8.8%, ETA 2-3h)
- exp_14b_inference_fewnerd N=8 (5090-c:0, ETA 6-10h)
- FewNERD T-ablation s123 T=0.5/0.8/1.2 (5090-b:0-2)
- FewNERD T=0.8 s456 (5090-b:3)
- CoNLL T-ablation s456 T=0.5/0.8/1.2 (5090-c:1-3)

**等待中**：
- Agent 执行 P0-1 hidden state probe（需确认 LSC hidden states 可用性）
- Agent 执行 P0-3 multi-model error correlation（CPU-only）
- Paper Agent 执行 Reframe（Abstract → Intro → Framework → Mechanistic → Related Work → Conclusion）
- 用户回复 API 充值/OpenRouter key
- 各 T-ablation/CoNLL worker 完成回调

### 4. 📋 待办（条件触发式）
- 32B inference 完成 → 立即跑 multi-model ensemble analysis（7B+LLaMA+14B+32B on FewNERD same instances）
- 14B N=8 完成 → 收集结果 + 加入 multi-model correlation matrix + kill_after_n8 自动触发
- P0-1 probe AUROC ≈ 0.87 → 论文 §3 写实（mechanistic introspection limit confirmed）; probe AUROC ≈ 0.51 → §3 改为"信息也不存在于 representation"（同样有价值）
- API 充值/key 到达 → 立即启动 Frontier SC（代码已修好，3 bugs fixed: entity_set + JSON 容错 + URL）
- FewNERD/CoNLL T-ablation s123/s456 全部完成 → 统一 T-ablation 分析（3 datasets × 4 temps × 3 seeds）
- Paper Agent 完成 Reframe 初稿 → 审查 page count（必须 ≤8 页 main text）
- 空闲 GPU 释放 → CoNLL T=1.0 seed=123 baseline（尚未覆盖）

### 5. 🎯 战略上下文
- **D208 核心转向**：论文从 "Triple Contribution (QE+Diagnostic+Prescriptive)" 转为 "Capability Ceiling / Impossibility Result"。7 个 method negative = universal phenomenon 的证据。Mechanistic probe 是关键杠杆。
- **Reviewer 警告**：Round 10 曾用 IB formal theorem 尝试 impossibility 被打回（trivial/tautological）。现在必须走 empirical exhaustion + mechanistic evidence 路径，不要 formal proof。
- **Scope 精确性**：Impossibility 是 "entity-level unsupervised agreement signals can't bridge correlation-selection gap"，不是 "SC doesn't work"。LP selection (+1.36pp)、entity construction (+1.02-1.53pp)、cross-model (+0.42pp) 是 escape routes。
- **最容易判断错的事**：(1) 认为 Frontier SC 可以启动（不行，API 全阻塞）；(2) 14B 进程没输出就标 failed（vLLM 初始化慢，必须 ps+nvidia-smi 双确认）；(3) Spider SQL 196/200 数据是 bugfix 后收集的（已确认可用于论文）
- **决策链关键节点**：D203(4.5 mandate) → D206(RE reframe as capability floor) → D207(API 阻塞优先级调整) → D208(Impossibility reframe + mech probe + multi-model)


---
