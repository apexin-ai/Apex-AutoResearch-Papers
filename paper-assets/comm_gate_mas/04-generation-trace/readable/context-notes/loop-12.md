# director / loop_12.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`6a279d62c4e34b487369.json`](../../sessions/6a/6a279d62c4e34b487369.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-04-30T03:12:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westb-4x6000-a 只用 cuda:1 (account: comm_gate); bjb2-4x5090-b 用 cuda:0 + cuda:1 (account: root)
- gpu_ids config 已更新为 `["cuda:0", "cuda:1"]`，D247 刚恢复分配，之前 D241/D244 全部释放过
- 2026-04-24 事故教训: 严禁在 gpu_ids 白名单外启动实验，别人的卡有别人的项目
- NeurIPS D&B deadline: abstract 5/3-4, paper 5/5-6，补充实验必须 5/2 前完成

### 2. 🖥️ 基础设施快照
- westb-4x6000-a: connect.westb.seetacloud.com, account=comm_gate, 4×RTX 6000 Pro 96GB
- bjb2-4x5090-b: connect.bjb2.seetacloud.com, account=root, 4×RTX 5090
- 代码路径: /root/autodl-tmp/comm_gate_mas (两台服务器相同)
- DistilBERT 模型: 应在 data/classifier/ 下（Agent 未完成探测就 reset 了）
- HF cache: /root/autodl-tmp/.hf_cache (AutoDL 标准)
- 活跃进程: 无。无 RUNNING 实验，无 Worker，无 cron

### 3. 📊 当前状态
我刚规划了 3 组并行补充实验（D247），更新了 ROADMAP 和 GPU config。Agent reset 前正在处理第一条指令（环境探测），但排队的 GPU 解锁消息可能未被处理。

Registry: 0 RUNNING, 6 stale PREPARING (oracle_qwen_gsm8k, p1_oracle_precompute_llama_gpt4omini 等，均为历史残留可忽略)。130 实验已完成 (91 success / 11 negative / 15 failed)。

等待中: R2/R3 二审报告（Review Director 侧）; P0 匿名仓库上传（需用户手动操作）。

### 4. 📋 待办
- Agent 新 session 启动 → 重发 3 组实验指令（环境探测 + EXP-A/B/C），之前的消息随 reset 丢失
- EXP-A/B/C 审批请求到达 → 审批 + allocate GPU（westb cuda:1 / bjb2 cuda:0 / bjb2 cuda:1）
- 实验完成 → 结果写入论文，更新 provenance
- R2/R3 二审报告到达 → 按 review-report-action skill 处理（Holistic Pass + Action Matrix）
- Manager 上线 → 可通知释放不需要的服务器（当前实验结束后）

### 5. 🎯 战略上下文
论文核心: perturbation sensitivity ≠ pruning safety (dissociation)，双 backbone (Qwen/Llama) × 双任务 (GSM8K/StratQA) 已 2×PASS。

D247 补充实验目标（用户明确要求"继续补实验"）:
- EXP-A: DistilBERT online E2E — 填 oracle→deployment 断层，D&B track 最关心的实用性
- EXP-B: 第三模型家族 (Mistral > DeepSeek > Phi) — 从 2 家族→3 家族泛化
- EXP-C: 3-agent 拓扑 oracle — 从 2-agent→3-agent 泛化

易错点:
- Agent 的新 session 不知道 D247 计划，必须重新发完整指令（不能假设它记得）
- bjb2 的 5090 是 32GB VRAM，7B 模型够用，14B+ 不行
- 之前 Agent 报 GPU 阻塞是因为 gpu_ids 为空，已修复，但要确认 Agent 读到了新 config
- 6 个 stale PREPARING 实验是历史残留，不要试图恢复它们


---
