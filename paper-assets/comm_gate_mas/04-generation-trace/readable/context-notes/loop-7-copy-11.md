# director / loop_7.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`a1e6c895ac4aaac5e3f5.json`](../../sessions/a1/a1e6c895ac4aaac5e3f5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-04-27T12:04:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- **只能用 cuda:1**。cuda:0/2/3 属于其他项目，D184/D187 两次越界事故后已建立硬性规则。启动脚本必须验证 `CUDA_VISIBLE_DEVICES=1`
- vLLM 在 cuda:1 上预分配 ~86GB KV cache 是正常行为（96GB Blackwell 卡），不要当作异常去杀进程
- P2 oracle_online_llama 有 48h 硬限：4/29 00:00 UTC 截止，超时执行 fallback plan (D175)
- DeepSeek oracle κ=0.0 不可用（D181），oracle 替代方案走 D191 决策树

### 2. 🖥️ 基础设施快照
- 服务器：westb-4x6000-a (connect.westb.seetacloud.com)，SSH host = `comm_gate`
- 工作目录：`/root/autodl-tmp/comm_gate_mas`
- GPU：4× RTX PRO 6000 Blackwell (96GB)，本项目仅 cuda:1
- 活跃进程：P0 seeds 123+456 在 tmux `p0_seeds_123_456`（cuda:1，vLLM PID 646624）
- e2e_llama_gsm8k_n300_clean 实验 RUNNING，cron 120s 监控

### 3. 📊 当前状态
- **刚完成**：R12 文本修改（C1 72B wording + M6 backbone count），Reviewer 全部 PASS
- **RUNNING**：e2e_llama_gsm8k_n300_clean — P0 heuristic length<30 pruning on Llama/GSM8K N=300，seeds 123+456 串行运行中（~2-4h 预估）
- **PENDING**：qwen_length_only_gsm8k, oracle_online_llama_gsm8k_v2, e2e_qwen3_8b_gsm8k 等 5 个
- **等待中**：刚给 Agent 发了 P0+P1 状态检查指令（om_x100b51c1491c2cb0c14a190fd59a5fd），Agent 回复应在队列中

### 4. 📋 待办
- Agent 回复 P0+P1 状态 → 评估进度，P1 若仍 429 阻塞则决策走 D191 替代路线（Claude oracle κ>0.8 → 用；否则 heuristic-only narrative）
- P0 seeds 123+456 完成 → 3-seed 聚合统计 → 启动 P5 e2e_qwen3_8b_gsm8k 跨代验证（cuda:1）
- P1 Mac 端 oracle precompute 完成 → 启动 P2 oracle_online_llama（硬限 4/29 00:00 UTC）
- P5 完成后 → P3 llama_length_only 补种子（cuda:1）
- Review 团队回传审稿报告 → 按 review-report-action skill 处理（先 Holistic Pass 再逐条 Action Matrix）

### 5. 🎯 战略上下文
- **核心叙事**："Perturbation sensitivity ≠ pruning safety: ack 消息扰动敏感但可安全剪枝，且该 dissociation 在 7B→72B scale-stable"
- 双 backbone 10-seed 非劣效已成立（Llama Δ=+2.1±2.4pp, Qwen Δ=+0.40±1.02pp）。72B oracle N=265 零翻转。当前补的是 **heuristic e2e 证据线**（不依赖 oracle API）
- **P1 阻塞是关键风险**：OpenAI 429 限流导致 GPT-4o oracle precompute 受阻（D190）。如果 4/28 前 P1 无法完成，P2 oracle_online 将走 fallback（heuristic-only narrative，放弃 oracle 在线对比）
- **NeurIPS 2026**：abstract 5/3-4, paper 5/5-6。时间紧但核心结果已足够，剩余实验是加固
- 易错点：不要混淆 heuristic mode（length<30 纯本地）和 oracle mode（需 API）；seed 123 旧数据已标记为脏（D186 vLLM 崩溃），只用重跑后的数据


---
