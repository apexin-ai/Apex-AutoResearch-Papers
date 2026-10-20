# reviewer / loop_4.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`baa73c8d139ad0c29b3a.json`](../../sessions/ba/baa73c8d139ad0c29b3a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-15T19:06:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-11235 上仅 `cuda:0` 和 `cuda:1`，越界立即 critical
- 数据盘：大文件必须放 `/root/autodl-tmp/`，根分区 ~30GB
- 网络：pip/git 前 `source /etc/network_turbo`；HF 下载设 `HF_HUB_DISABLE_XET=1` + SSL 证书环境变量
- DeepSeek full_trace v3 训练：**必须确认 `to_chat_text()` label-preserving truncation 已生效后才能提交**，之前 v1/v2 都因 label truncation 失败

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235(root)，代码根目录 `/root/trace-verdict-study`
- 数据：`/root/autodl-tmp/trace-verdict-study-data/`（{condition}_train.jsonl / _test.jsonl）
- Checkpoints：`/root/autodl-tmp/trace-verdict-study-checkpoints/{exp_name}/`
- 模型：`/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct`，DeepSeek 在 `/root/trace-verdict-study/models/deepseek-coder-6.7b-instruct`
- 训练日志：`/root/runs/trace-verdict-study/{exp}.log`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/`
- 活跃进程（截至 handoff 前 ~30min）：
  - PID 144517 cuda:0 — deepseek_exception_only_seed123，step ~130/444（~29%），ETA ~20:10 UTC
  - PID 146592 cuda:1 — vota_seed456_v2，step ~54/444（~12%），ETA ~20:40 UTC

### 3. 📊 当前状态
**刚完成**：Paper Agent Step 5 Round 1 全文审查，已通过 `reviewer_post_to_director` 发送。评分 Overall=4/10，3 个 critical（method.tex gradient_accumulation 错误、truncation 策略错误、wang2025dcsh 占位符引用），8 个 warning。

**Registry 活跃实验**：
- `deepseek_exception_only_seed123` — RUNNING，cross-model seed robustness
- `vota_seed456_v2` — RUNNING，VOTA seed robustness（低优先级）
- `deepseek_full_trace_seed42_v3` — PREPARING，等 GPU 释放 + code fix 确认（`to_chat_text()` 已修复，我已发 info 确认）

**已审查的 worker**：
- bootstrap_pvalues：4 个 Qwen 比较均 p<0.0001 显著。DeepSeek 缺 predictions.jsonl 无法比较
- per_class_and_ci_verify：CI 验证确认 exception_only 下界=99.58（非论文的 99.50），per-class LaTeX 表已生成
- full_trace_data_integrity：数据完好，label 均完整，truncation 问题仅在训练时

### 4. 📋 待办（条件触发式）
- deepseek_exception_only_seed123 完成 → 审查：accuracy 是否接近 99.33%（seed42 final）或 99.83%（seed42 epoch1）？与 Qwen 3-seed 完美一致性对比
- vota_seed456_v2 完成 → 审查：accuracy 是否接近 99.41%（seed42），确认 VOTA seed robustness
- deepseek_full_trace_v3 提交训练 → **立即检查**：(1) 使用的 train_sft.py 是否含 label-preserving truncation，(2) GPU 是否在白名单内
- Paper Agent Round 2 提交 → 重点验证：method.tex 3 个 critical 是否修复，per-class 表是否加入，CI 99.50→99.58 是否修正
- 任何新训练提交 → 例行 `nvidia-smi` GPU 越界检查

### 5. 🎯 战略上下文
**核心结论**：exception_only 是 verdict prediction 的 model-agnostic sufficient signal（99.83% Qwen / 99.33% DeepSeek，gap=0.50pp）。VOTA 跨模型退化 14.96pp。信息密度分解：26% gradient dilution + 74% information overload。

**论文状态**：EMNLP 2026 ARR May 25 deadline（10 天后）。全文初稿已完成但有 3 个 critical 需修。参考文献仅 7 篇（需 30+）。

**易错点**：
1. **不要信 method.tex 的超参描述**——gradient_accumulation=8（非 4），无 cosine decay（是 linear），有 warmup_ratio=0.1 和 weight_decay=0.01
2. **DeepSeek exception_only 有 epoch1/final 分歧**：epoch1=99.83%（=Qwen），final=99.33%。best-checkpoint gap=0pp 是强 claim，但论文仅在脚注提及，Discussion 缺分析
3. **calibration 倍数比不要用四舍五入后的值算**：精确 Brier 比=150x（非 framing 写的 197x），ECE 比=63x（非 57x）
4. **vota_no_ae 精度**：registry 存 0.994（99.4%），论文写 99.41%——可能是 registry 四舍五入，但需确认
5. **ae_only 异常高**（99.92%）：bootstrap worker 也标记了这个。不一定是 bug，但值得关注数据/评估是否有泄漏


---
