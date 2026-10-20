# agent / loop_3.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`42dc75be7729f9814d87.json`](../../sessions/42/42dc75be7729f9814d87.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-15T04:56:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **westd-11235 的 cuda:0 和 cuda:1**（2× RTX PRO 6000 Blackwell 98GB）
- `--gpu 0` 对应 cuda:0，`--gpu 1` 对应 cuda:1，不要搞反
- VOTA v5 准确率以 `eval_results.json` 为准是 **0.9916**，不是 0.9941（旧残留文件）
- no_trace baseline 当前用的是 v4（75.13%），**v5 还未补跑**——引用数字时必须标注 "(v4)"
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不存在 .venv
- 数据格式化 token budget 必须扣除 chat template overhead（31 tokens），否则 TRL 右截断切掉 label——这是 v2 collapse 的根因，已修复但不要回退

### 2. 🖥️ 基础设施快照
- **服务器**: westd-11235，工作目录 `/root/trace-verdict-study`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- **模型**: `/root/autodl-tmp/.hf_cache` 下的 Qwen2.5-Coder-7B-Instruct（通过 ModelScope CDN 下载）
- **数据**: `/root/autodl-tmp/trace-verdict-study-data/`（vota_train.jsonl, full_trace_train.jsonl, vota_no_ae_train.jsonl 各 4720 条）
- **Checkpoints**: `/root/autodl-tmp/trace-verdict-study-checkpoints/{condition}/final/`
- **W&B project**: `trace-verdict-study`
- **活跃进程**:
  - `full_trace_label_only_seed42`: PID 955296, tmux session, cuda:0, cron 监控中
  - `vota_no_ae_seed42`: PID 953133, tmux session, cuda:1, cron 监控中
- **所有 Worker 已完成**，无 running Worker

### 3. 📊 当前状态
两个 ablation 实验同时在跑，都是本轮核心实验：

| exp_id | GPU | Plan | 假设 | 预计完成 |
|--------|-----|------|------|---------|
| `vota_no_ae_seed42` | cuda:1 | plan_001 (P0) | 去除 actual/expected 后 VOTA 是否仍有效 → 决定 Claim 1 强度 | ~06:17 UTC |
| `full_trace_label_only_seed42` | cuda:0 | plan_002 (P1) | label-only loss 能否提升 full_trace 81.8% → 探索 gradient dilution 假说 | ~07:00 UTC |

**已完成的关键实验链**（v5 代码版本）:
- no_trace_v4: 75.13% (baseline，v5 未补跑)
- full_trace_v5: 81.8% (+6.7pp)
- VOTA v5: 99.16% (+24.0pp)
- full_trace_v2: 28.4% (killed, 根因=chat template bug, D006 已关)

**等待**: 两个 cron 回调（实验完成时自动触发）。无 pending Director 决策。

### 4. 📋 待办（条件触发式）
- **plan_001 cron 回调到达** → spawn Worker 跑 eval + bootstrap compare → 根据结果分叉：
  - accuracy >80% → Claim 1 用 "genuine behavioral understanding" framing，向 Director 汇报 positive
  - accuracy ~75% → Claim 1 改为 "assertion-point state comparison" framing，产出 Framing 调整提案
- **plan_002 cron 回调到达** → spawn Worker 跑 eval → 对比 full_trace_v5(81.8%)：
  - 有提升 → gradient dilution 假说得证，写入 paper 作为 ablation 证据
  - 无提升 → gradient dilution 不是 gap 主因，full_trace-VOTA gap 归因于信息密度
- **两个 ablation 都完成后** → cuda:1 补跑 `no_trace_v5`（~20min，统一 v5 代码版本）
- **no_trace_v5 完成后** → 启动 plan_003（VOTA component ablation，4 conditions，P0，~8h，需要两张卡）
- **plan_001 + plan_003 都完成后** → 决定是否启动 plan_004（DeepSeek-Coder 复现）或 plan_005（第二 verdict task）

### 5. 🎯 战略上下文
- **投稿目标**: EMNLP 2026 ARR，deadline **May 25**（剩 10 天），480 GPU-h 可用（充裕）
- **核心发现**: verdict task 的 trace SFT 存在清晰的粒度梯度 no_trace < full_trace < VOTA，信息密度比信息量更重要
- **决策链**: D001(pass阈值) → D002(Round1作废) → D003(MVP PASS) → D004(chat template bug定位) → D005(full_trace v5确认81.8%) → D006(三条件层次确立)
- **最容易判断错的事**:
  1. **不要把 plan_001 negative（vota_no_ae 降到 ~75%）当作项目 negative**——即使 VOTA 效果来自 string comparison，"verdict task 需要 assertion-point state 而非 full trace" 仍然是 publishable finding，只是 framing 不同（见 paper_framing.md contingency）
  2. **full_trace_v2 的 28.4% 不是 gradient dilution，是 chat template bug**——memory.md 已经纠正了这个误解，不要把 "gradient dilution" 当作已验证事实引用
  3. **no_trace baseline 是 v4 不是 v5**——最终论文数字需要 v5 补跑后统一，在此之前所有跨条件对比都要标注版本差异
  4. **registry 中大量 killed/queued 的旧实验**（v1-v3）是历史遗留，不要理会


---
