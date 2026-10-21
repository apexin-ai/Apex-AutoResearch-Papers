# agent / loop_6.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`2e293a4c3926e34dd277.json`](../../sessions/2e/2e293a4c3926e34dd277.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-16T20:04:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- 只能用 westd-32608 cuda:0（唯一 GPU，gpu_ids=["cuda:0"]）
- DeepSeek 模型已从 R1-Distill-Qwen-7B 改为 R1-Distill-**LLaMA**-8B（Director D021修正，Qwen底座被审稿人攻击）
- P0 实验自动串链不请示（Director 2026-05-16 授权），偏离 plan 或遇问题时才汇报
- submit_training_job command 用 bash 脚本调用时不需要 `bash -c` 包装（直接 `bash /path/script.sh`）
- vLLM 端口分配：14B=8000, Mistral=8001, LLaMA=8002, DeepSeek-R1=8003

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608, root@, 工作目录 /root/symb_invariant_consensus
- Python：/root/miniconda3/bin/python（conda base 环境）
- GPU：1× NVIDIA RTX PRO 6000 Blackwell 98GB
- 模型路径（/root/autodl-tmp/models/）：
  - Qwen2.5-14B-Instruct（主力，exp-001/002 用）
  - DeepSeek-R1-Distill-Llama-8B/（已下载验证，15GB，LlamaForCausalLM）
  - Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct/（ModelScope下载，进行中 PID 186855，~43%）
  - Mistral-7B-Instruct-v0.3（ModelScope 3次截断，正在换 HF 直接下载）
- vLLM：PID 174298 serving Qwen2.5-14B-Instruct on port 8000
- 活跃 GPU 实验：sica_k_sensitivity_14b (PID 237939, tmux=sica_k_sensitivity_14b, K-ablation 60题 6个K值, ETA ~May 17 02:00 UTC)
- ⚠️ 可能有冲突进程 PID 235733 (tmux=exp002, 804题错误版本)——已派 worker kill，但未确认完成

### 3. 📊 当前状态
刚完成：
- exp-001 (sica_expanded_14b) DONE/success，分析报告已产出（+0.25pp, p=0.74, D012 +3.3pp 是噪声）
- exp-002 (sica_k_sensitivity_14b) 已提交 RUNNING

等待回调的 Worker：
- worker_fix_kill-wrong-k-ablation_20260516T200324（kill PID 235733）
- worker_download_mistral-7b-hf-fix_20260516T194106（Mistral HF 下载）
- worker_prep_exp-013-data-extract_20260516T194125（从 exp-001 提取 constraint cache）
- worker_code_analyze-expanded_20260516T080105（analyze_expanded.py 脚本）
- worker_code_gsm8k-pilot-script_20260516T080120（GSM8K pilot 脚本）

Registry RUNNING：sica_k_sensitivity_14b
Registry QUEUED：无

### 4. 📋 待办（条件触发式）
- exp-002 cron 回调(DONE) → 分析 K=11 gap（核心：0 则仅 tiebreak）→ 立即启动 exp-012 (GSM8K 30题 pilot, 脚本已备)
- exp-013 constraint cache Worker 完成 → 确认三种方法产生不同结果 → 汇报 Director 审批后启动
- Mistral 下载 Worker 完成 → 若成功记录路径+验证；若 401 则报告放弃用 LLaMA 替代
- LLaMA-3.1-8B 下载完成（PID 186855）→ 验证 tokenizer → 确认 start_vllm_llama_8b.sh 路径正确
- kill-wrong-k-ablation Worker 完成 → 确认 PID 237939 仍在跑
- exp-012 完成 → 启动 exp-010 (Mistral-7B) 或 exp-011 (LLaMA-8B)，按 ROADMAP 排期

### 5. 🎯 战略上下文
- **D025 pivot 已确认**：SICA≈SC (+0.25pp, N=804)。论文 narrative 从"accuracy improvement"转向"principled tiebreaking + C0 as diagnostic"
- **K=11 是关键**：odd-K 无 tie，若 gap=0 → 证明 SICA 仅靠 tiebreak 生效。这决定了 Claim 1 的 framing
- **Claim 2 (跨模型 C0)**：需要 3 个非 Qwen 模型数据点（Mistral/LLaMA/DeepSeek-R1-LLaMA）。DeepSeek 已就绪，LLaMA 下载中，Mistral 有风险
- **May 19 checkpoint**：全部 GPU 实验完成 → 数据充分性判定 → 冲 EMNLP May 25 ARR 或切 AAAI Aug 1
- **易错点**：
  - ModelScope 下载路径有嵌套（如 `LLM-Research/Meta-Llama-3___1-8B-Instruct/`），vLLM 启动脚本的 MODEL_PATH 必须指向含 config.json 的那层
  - 不要重启 exp-002——PID 237939 是正确的 60 题版本，不是 235733 的 804 题版本
  - FOLIO sub-claim 已 dead (0pp)，不要再在 FOLIO-only 上投入 GPU


---
