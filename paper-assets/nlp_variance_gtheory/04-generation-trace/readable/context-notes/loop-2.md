# director / loop_2.md

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`62ea7043318b84f8a47f.json`](../../sessions/62/62ea7043318b84f8a47f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-21T19:34:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-32570:cuda:0-3 + westd-19912:cuda:0-3，共 8 张。westd-15695 已释放，westd-13176 永远连不上已废弃
- westd-19912 上 run_experiment.py 已 patch 加了 benchmark 列过滤（M019），但老版 design_matrix 文件（未按 benchmark 拆分的）仍在服务器上——新任务必须用 shard 文件或确认代码过滤生效
- 占位文件风险：westd-32570 上 `internlm_math.jsonl` 和 `deepseek_math.jsonl` 可能是 57,600 行 `{"_placeholder": true}` 占位文件，symlink watcher 应该已替换为真实数据，但启动任何分析前必须验证无 `_placeholder` 行
- OLMo MMLU/ARC/HellaSwag 原始 288K 行文件备份在 `.bak_unfiltered`，当前 57,600 行文件是过滤后的正确版本

### 2. 🖥️ 基础设施快照
- **westd-32570**: connect.westd.seetacloud.com:13176, /root/nlp_variance_gtheory, 4× RTX PRO 6000 96GB
- **westd-19912**: connect.westd.seetacloud.com:19912, /root/nlp_variance_gtheory, 4× RTX PRO 6000 96GB
- 模型缓存：`/root/autodl-tmp/.hf_cache/` (两台都有)
- 推理引擎：vLLM, bfloat16, enforce_eager
- 8 模型：Llama-3.1-8B, Mistral-7B-v0.3, Qwen3-8B, Gemma-2-9B, InternLM2.5-7B, DeepSeek-7B, OLMo-2-7B, Yi-1.5-9B
- 输出文件：`/root/nlp_variance_gtheory/results/{model}_{benchmark}.jsonl`，每个 57,600 行
- 活跃进程：chain_single_gpu.sh (各 GPU 串行推理链) + watcher 脚本 (symlink + accelerator)，具体 PID 需重新 SSH 检查（session 重置后状态可能变化）

### 3. 📊 当前状态
**推理进度（最后确认 ~02:30 CST）**：
- westd-32570: 27/30 runs done (90%)。Llama/Mistral/Qwen 5/5 ✅, Gemma MATH 97%, InternLM MATH ✅ + GSM8K 26%, DeepSeek GSM8K 13% + MATH 待 GPU 2 accelerator
- westd-19912: OLMo MMLU/ARC/HellaSwag ✅ (已清洗), GSM8K 13.5% + MATH 6.6% 重跑中; Yi MMLU ✅ ARC ✅ HellaSwag 71% + GSM8K 6.6%
- Agent 预估全局 ETA ~05:30 CST (8×5 全部就绪)

**刚做完**：RESET_BOTH 已批准，给新 Agent 派了综合指令（GPU 盘点 + R1-W4/W5 分析任务 + 两台服务器状态检查）。给 Paper Agent 派了 Step 3→4 推进指令。

**等待中**：新 Agent session 启动后处理综合指令；Paper Agent 处理 fig2 修复确认 + Step 4 初稿；推理完成后的 worker 回调。

### 4. 📋 待办（条件触发式）
- Agent 回复 GPU 盘点 → 确认推理正常，空闲卡立即排任务
- 8×5 推理全部完成 → 启动 exp-004 综合分析（前提：验证所有 .jsonl 无 placeholder）
- exp-004 分析完成 → 更新 paper_framing.md 数字 → 派 Paper Agent patch 8-model 数据到初稿
- R1-W4 分析完成 → 如果 GSM8K ordering 是 no-op，Paper Agent 在论文中 disclose 并从 free-form design 移除 ordering facet
- R1-W5 分析完成 → 结果写入 robustness package，Paper Agent 纳入 Experiments 章节
- Paper Agent Step 4 初稿完成 → 提交 Reviewer 对抗循环
- 初稿 + 8-model 数据都就绪 → re-dream (review_mode="full") 评估完整论文
- re-dream 通过 → submit_paper_to_review 提交 Group C 正式审稿

### 5. 🎯 战略上下文
- **核心 narrative (D010)**：Format-conditional variance dichotomy — MC benchmarks item-dominated (42-49%), free-form methodology-dominated。这是从 D003 "gradient" 到 D010 "dichotomy" 的 pivot，更 robust
- **目标**：保 3.5 争 4.0 (AAAI 2027, abstract Jul 21, paper Jul 28)
- **最大风险**：8-model 数据是否 confirm dichotomy pattern（如果新模型打破 MC vs free-form 的清晰分界线，claim 需要再次调整）
- **Zhou 2026 (PSN-IRT, AAAI Oral)** 是最强 direct competitor——区分要点：IRT 优化 "which items"，G-theory 优化 "how many conditions across facets"，互补不竞争
- **易踩的坑**：(1) 占位文件未替换就跑分析 → 垃圾数据不报错；(2) westd-19912 旧 design_matrix 未过滤 → 5× 膨胀 (M019)；(3) chain 脚本文件名冲突导致重复运行（已有 placeholder+symlink 机制但需验证）
- **错题本重点**：M017 (OLMo 用错 items 文件), M018 (GPU 冲突), M019 (design_matrix 未过滤)——都是跨服务器部署时脚本验证不足
- **审稿 13 个 issues**：3 critical (R1-N1 binary data, R1-N2 model count, R2-N1 scope) + 10 warning，详见 artifacts/review_issues.yaml


---
