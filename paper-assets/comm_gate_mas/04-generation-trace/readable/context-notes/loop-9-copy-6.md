# reviewer / loop_9.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`d15017540de47483e2eb.json`](../../sessions/d1/d15017540de47483e2eb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-04-28T12:10:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:1**（gpu_ids=[1]），cuda:0 被其他项目占用（PID 154166, 4563 MiB）。发现越界进程立即 CRITICAL
- vLLM model name 必须与 config 中 `model.name` 匹配——已连续 4 次因 model name mismatch 导致实验失败（v1 全 404, v2/v3 hang）。pre-flight check 必须校验 model name，不能只检 server alive
- AutoDL 脚本必须 `source /etc/network_turbo` 或设 `HF_DATASETS_OFFLINE=1`，否则 HuggingFace 连接失败（Errno 101 Network is unreachable）
- `pruning_validation.py` 的 httpx 调用必须有 per-call timeout（v4 已修复，L137/L236/L1281/L1319），回退该修复会重现 task 7-13 挂死 bug

### 2. 🖥️ 基础设施快照
- 服务器：**westb-4x6000-a**（comm_gate 账号），4× NVIDIA RTX PRO 6000 Blackwell (97GB each)
- 工作目录：`/root/autodl-tmp/comm_gate_mas`
- Python：`/root/miniconda3/bin/python3`（conda base 环境，不用 venv）
- 模型路径：`/root/autodl-tmp/models/Llama-3.1-8B-Instruct`（vLLM serve on port 8001, PID 32700, cuda:1, 83GB VRAM）
- HF cache：`/root/.cache/huggingface/datasets/gsm8k/`（已缓存）+ `/root/autodl-tmp/.hf_cache/`
- 活跃进程：`llama_heuristic_3seed_v4`（tmux session, PID 166264 wrapper → 166292 python3, cuda:1）
- 无 W&B 配置（此项目不检查 W&B）

### 3. 📊 当前状态
我刚审完 `llama_heuristic_3seed` v1→v4 的连续 4 轮修复：
- **v1**: 全部 200 tasks 404（model name mismatch）→ CRITICAL
- **v2**: 修复 model name，hung at task 7/200 → CRITICAL
- **v3**: 加 timeout/PYTHONUNBUFFERED，hung at task 9-13/200 → CRITICAL
- **v4**: 修复 pruning_validation.py per-call httpx timeout，**正在运行**（刚启动 ~5 min，6/200 tasks 完成，尚未通过 hang 点）

Registry RUNNING/PREPARING:
- `llama_heuristic_3seed_v4` — RUNNING，Llama heuristic 3-seed，预计 ~2.2h 完成
- `llama_length_only_gsm8k_5seed_v2` — RUNNING（但 conclusion=success，metrics 已填，可能只是 status 未更新）

等待：v4 是否通过 task 13+ 的 hang 点——如果 15-20 分钟后 task 数 >20 则大概率修复成功

### 4. 📋 待办
- v4 task 数 >20 且持续增长 → 发 `[severity: info] PASS` 确认修复有效
- v4 再次 hang（task 数停滞 >10 min）→ `[severity: critical]` 要求排查具体 task（gsm8k_000X）是否触发 vLLM 异常长推理
- v4 全部 3 seeds 完成 → 审查 metrics：Δ 是否在 [-5pp, +5pp] 范围内、suppression rate 是否与 Llama 其他实验一致（~75%）、3 seed 间方差是否合理
- `llama_length_only_gsm8k_5seed_v2` 如果 status 仍 RUNNING → 检查进程是否已结束，提醒 Director 更新 registry

### 5. 🎯 战略上下文
- 项目核心：LLM 多智能体通信中 acknowledgment 消息可安全剪枝（oracle/heuristic 两条路线）
- **Qwen 侧数据充分**：10-seed oracle (Δ=+0.4±1.02pp, TOST p=0.048)、10-seed stochastic t=0.7 (Δ=+0.3±1.8pp)、length-only ablation (Δ=+0.5±1.5pp)
- **Llama 侧是短板**：heuristic 3-seed 是论文 Table 1 最后一个关键数据点，之前只有 `e2e_llama_gsm8k_n300_clean`（heuristic 3-seed, Δ=+2.44±1.71pp, suppression 75.7%）但那个用的是 N=300 的旧配置
- **易错点**：Llama heuristic suppression rate ~75% 远高于 Qwen ~40%，因为 Llama 回复更短触发 char<30 阈值。这不是 bug——两个模型通信模式不同，但论文必须解释这个差异
- **易错点**：不要把 `llama_length_only_gsm8k` 的 suppress ~0.8% 和 heuristic 的 ~75% 混淆——length_only 只看字符长度，heuristic 包含 keyword+pattern 规则


---
