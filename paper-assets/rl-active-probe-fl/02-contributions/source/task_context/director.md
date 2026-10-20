---
loop: 1
reason: max_messages
updated: '2026-05-14T08:24:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C001：仅允许 gpu-6000pro-1 的 cuda:0 和 cuda:1（RTX PRO 6000 Blackwell 94GB × 2）
- `rtx6000-diagprobe` 和 `gpu-6000pro-1` 是同一台物理服务器，SSH 连接用 gpu-6000pro-1
- 大文件必须放 `/root/autodl-tmp/`，根分区只有 30GB
- pip/git 前必须 `source /etc/network_turbo`
- Qwen3-8B 必须禁用 thinking 模式（三重保险：prompt `/no_think` + `enable_thinking=False` + template patch），否则 completion 被 `<think>` 吃掉，reward=0
- API 用 OpenRouter 兼容格式（openai 库 + base_url `http://47.94.22.126/v1`），key_id: `openrouter_api_key`，模型名 `anthropic/claude-opus-4.7-fast`。用户要求控制 API 费用，全量阶段用本地 Qwen3-30B-A3B 替代

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-1, SSH `ssh -p 18314 root@connect.westd.seetacloud.com`，密码 secret `ssh_password_rtx6000`
- 工作目录：`/root/autodl-tmp/diagprobe/`
- Python：`/root/miniconda3/bin/python`（conda base，不是 venv）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3-8B/`（注意 Qwen/ 子目录）
- Qwen3-30B-A3B：后台下载中（~15GB/60GB），目标 `/root/autodl-tmp/models/`
- 数据：`/root/autodl-tmp/diagprobe/data/`（probes_train.jsonl 294 条, eval.jsonl 202 条, train.jsonl 294 条）
- W&B：offline 模式（无 API key），日志在 `/root/autodl-tmp/diagprobe/wandb/`
- 软件栈：torch 2.10+cu128, TRL 1.1.0, PEFT 0.19.0, vLLM 0.18.1
- 活跃进程：eval-sft-v1 (GPU 0) + eval-base-v2 (GPU 1)，预计 30-90min 完成

### 3. 📊 当前状态
刚修复 Qwen3-8B thinking 模式问题（D006），dry-run 5/5 通过（无 think + 有 probe 格式）。双卡正在跑评估：
- eval-sft-v1 (GPU 0, RUNNING)：验证 SFT checkpoint 在 no-think 下能否生成 probe
- eval-base-v2 (GPU 1, RUNNING)：no-think 下的 base model baseline
- grpo-mvp-v1: FAILED（reward=0，thinking 吃掉 tokens）
- sft-mvp-v1: DONE（loss 2.13→1.55, 可复用 checkpoint）

等待：两个 eval Worker 回调。

### 4. 📋 待办
- eval-sft-v1 完成 → 如果 probe_generation_rate > 50% → SFT checkpoint 有效，立即启动 grpo-mvp-v2（no-think, GPU 0）
- eval-sft-v1 完成 → 如果 probe_generation_rate < 50% → 重训 SFT（no-think template, ~3min）再跑 GRPO
- eval-base-v2 完成 → 记录 baseline metrics
- grpo-mvp-v2 完成 → 启动 eval-grpo（双卡并行 eval-sft + eval-grpo 或单独跑）
- 全部 eval 完成 → 汇总 MVP pass/fail 判断（3pp threshold + bootstrap CI + probe exec ≥80% + probe-dep ≥20%）
- MVP pass → `complete_mvp()` → post-mvp-kickoff skill → paper_framing + experiment_plan + dream_simulate
- Qwen3-30B-A3B 下载完成 → 验证 vLLM 推理可用，后续 API 调用切本地

### 5. 🎯 战略上下文
- 目标：EMNLP 2026 ARR DDL 5/25（剩 11 天，今天是 Day 1）
- 核心假设：GRPO + fix-based reward 训练的诊断探针 > SFT-only（debugging accuracy ≥3pp）
- 决策链：D001（eval 样本 200）→ D002（test gen via solution+API, single-bug only）→ D003（MVP 必须有 fix-based reward）→ D004（496 样本够用）→ D005（Qwen3-30B-A3B 替代 API）→ D006（禁用 thinking 重跑）
- 易错点 1：Qwen3-8B 所有生成路径都必须禁用 thinking，漏一个就 reward=0。已有三重保险但新增脚本要检查
- 易错点 2：TRL 1.1.0 的 API 与旧版不兼容（已踩过 max_seq_length→max_length, max_prompt_length 移除, completion 格式 list[dict] 非 str），新增 TRL 调用要查文档
- 易错点 3：SFT checkpoint 是 LoRA adapter（不是完整模型），GRPO 和 eval 加载时需检测 adapter_config.json + merge_and_unload
- eval-base-v1 结果无效（thinking 模式下跑的），不可引用；eval-base-v2 才是真正的 baseline
