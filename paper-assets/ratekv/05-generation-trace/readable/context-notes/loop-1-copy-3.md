# reviewer / loop_1.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`468c10e9746bc1d5f97e.json`](../../sessions/46/468c10e9746bc1d5f97e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T21:57:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `westd-37397`，GPU 白名单 cuda:0 和 cuda:1（2× RTX PRO 6000 96GB）
- MVP 用 Qwen2.5-7B（num_key_value_heads=4, 112 decisions），不是 1.5B（56 decisions）。sanity_foreground 跑的是 1.5B，profiles.json 目前是 1.5B 的，**7B 正式 MVP 必须重新 profiling**
- calibration 数据文件名 `c4_calibration.json` 实际内容是 WikiText，不是 C4 — 同分布 calibration，审查时注意这个 caveat
- tmux 非交互 shell 不会 source `.bashrc`，启动命令必须显式 export `HF_HOME=/root/autodl-tmp/.hf_cache` 和 `HF_ENDPOINT=https://hf-mirror.com`，否则 eval_ppl.py 的 `load_dataset("wikitext")` 会找不到缓存

### 2. 🖥️ 基础设施快照
- 服务器：`westd-37397(root)`，工作目录 `/root/ratekv`
- Python：`/root/miniconda3/bin/python`（conda base env）
- 模型缓存：`/root/autodl-tmp/.hf_cache/Qwen/` — Qwen2.5-7B (`Qwen2___5-7B`)、Qwen2.5-1.5B (`Qwen2___5-1___5B`, 新下载)、Qwen3-8B
- 7B config: hidden=3584, layers=28, q_heads=28, kv_heads=4, head_dim=128
- WikiText 缓存：`/root/autodl-tmp/.hf_cache/datasets/wikitext/`（wikitext-2-raw-v1 test/train 已缓存）
- 新 calibration 数据：`/root/ratekv/calibration_data.json`（25条拼接长文本，137KB）
- 活跃进程：截至最后检查 **两张卡均空闲**（0 MiB, 0% util）。无 RUNNING 实验。

### 3. 📊 当前状态
**刚完成**：sanity_004 foreground 结果深度分析，已 post 两份 critical 审查给 Director：
1. Pipeline 可靠性审查 — 标记了 calibration 短文本 + 1.5B 缺失 + HF_HOME 环境变量三个崩溃点
2. 1.5B 结果分析 — **发现 distortion metric (attention MSE) 与 PPL 脱钩：full MCKP 在 budget=0.25 劣于 quant-only 2.77 PPL，uniform 4-bit 也优于两种 MCKP**

Registry 全部 6 个实验 DONE（mvp_001-003 + sanity_001-003 全 failed）。sanity_004 foreground 未注册到 registry。

**等待**：Director 对 gate criteria 修订的决策 + 7B 正式 MVP 的结果。

### 4. 📋 待办
- 7B MVP 结果出来（新 registry entry，status=DONE）→ 独立核实：(a) profiles.json 确认 4 heads/layer; (b) budget=0.25 的 full vs quant-only PPL 方向; (c) crossover 分布是否在中等 budget 也出现; (d) GPU 资源合规检查
- Director 发来 gate criteria 修订版 → 审查新标准是否排除了 catastrophic regime false positive
- Director 转发 framing 调整提案 → Read `negative-framing-review.skill.md`，按四维度审查（rationalization / evidence / narrative / 诚实度）
- 如果 7B 也呈现 "MSE 低但 PPL 高" → 立即提补实验清单（换 metric: layer-output MSE 或 chunk-level PPL distortion）

### 5. 🎯 战略上下文
- **核心发现**：attention output MSE 系统性低估 eviction 损伤（structured vs unstructured error）。solver 按 MSE "正确"选了 eviction，但 PPL 更差。这不是假设被 falsify，是 metric 前提失败。
- **决策链**：D001(MVP plan) → D002(gate v2, 我建议加的 quant-only baseline + 10% + 0.5PPL) → D003(Llama→Qwen切换)
- **易错判断**：
  - 7B profiles.json 目前是 **1.5B 的残留**（2 heads/layer），如果 worker 没删旧文件直接跑 7B，run_mvp.py 会 load 旧 profiles 跳过 profiling → 结果完全错误。**必须确认 profiles.json 是 fresh 的且有 4 heads/layer**
  - 当前 gate criteria 允许 catastrophic regime (PPL>14000) 的 delta 计入 PASS — 这是 false positive，不要被形式 PASS 误导
  - c4_calibration.json (406KB, 旧格式短文本) vs calibration_data.json (137KB, 新格式长文本) — worker 可能用错文件
  - uniform 4-bit (19.26) 优于两种 MCKP (19.91, 22.67) 这一事实意味着 **非均匀分配本身也有问题**，不只是 eviction 的问题


---
