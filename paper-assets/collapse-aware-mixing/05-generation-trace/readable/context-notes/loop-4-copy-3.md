# reviewer / loop_4.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`5aa2895e53476ac5d890.json`](../../sessions/5a/5aa2895e53476ac5d890.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-13T23:37:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 `cuda:0`（RTX PRO 6000 96GB），服务器 `cqa1-38874` 只有一张卡
- AutoDL 实例，pip/HF 下载前必须 `source /etc/network_turbo` + 设 `REQUESTS_CA_BUNDLE` / `SSL_CERT_FILE` / `HF_HUB_DISABLE_XET=1`
- 数据盘 `/root/autodl-tmp/`，根分区 ~30GB 严禁存大文件
- 无 constraints.yaml，无显式 gpu_ids 白名单，但实际只有 1 卡所以只能是 cuda:0

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-38874`，工作目录 `/root/collapse-aware-mixing`
- Python：`/root/miniconda3/bin/python3`（conda base 环境，不是 venv）
- 模型：`EleutherAI/pythia-1b`，HF cache `/root/autodl-tmp/.hf_cache`
- 数据集：wikitext-103-raw-v1，checkpoint 输出 `/root/autodl-tmp/output_v7/`（G0/G1/G2 子目录，每代含 training/checkpoint-* + final_model/）
- 无 wandb 配置（`--no_wandb`）
- 活跃进程：`pivot_b_full_18ckpt`（PID 109597→子进程 109608，tmux session，cuda:0）—— 在全 18 checkpoint 上跑 generated eff_rank 分析，截至 handoff 时 1/18 完成，预计剩余 ~4.5h

### 3. 📊 当前状态
我刚完成两轮审查：
1. 确认 `pivot_b_full_18ckpt` 正常运行（GPU 29%/38GB，方向正确）
2. 发现两个 warning 已报 Director：(a) registry 状态仍为 QUEUED 应改 RUNNING；(b) `mvp_pilot_v8` + `v8_r2` 自 D014 pivot 后成孤儿，建议 CANCELLED

Registry 状态：
- `pivot_b_full_18ckpt`: QUEUED（实际 RUNNING），全 18 ckpt generated eff_rank 分析
- `mvp_pilot_v8` / `v8_r2`: PREPARING（孤儿，建议取消）
- `pivot_b_verification`: DONE (negative) — generated eff_rank 信号确认但 n-gram 更早
- `mvp_pilot_v7`: DONE (failed) — C1 假设被 falsified

无等待中的 cron 或 Director 决策。

### 4. 📋 待办
- `pivot_b_full_18ckpt` 完成 → **立即审查**全 18 checkpoint 的 generated eff_rank vs n-gram entropy 对比数据，这是 D013 核心问题的最终答案：
  - generated eff_rank 比 n-gram 更早下降 → Pivot B 完全成立，paper story 最强
  - generated eff_rank 更平滑/渐进（n-gram 是阶跃函数）→ Pivot B 成立，强调控制信号优势
  - generated eff_rank 无额外价值 → Pivot B 降级，按 D015 走 Q2 (negative result paper)
- 输出文件在 `/root/autodl-tmp/output_v7/pivot_b_analysis_full/`，预期有 `generated_vs_holdout_eff_rank.json`
- Agent 若提交新实验 → 检查是否更新了 v8/v8_r2 状态、是否清理了孤儿实验

### 5. 🎯 战略上下文
**决策链**：D001(MVP) → D003(wikitext) → D005(lr fix) → D007(降至20M) → D008(GO/NO-GO调整) → D011(G1 eff_rank上升，C1挑战) → D014(C1 definitively falsified) → D016(Pivot B GO，Direction C KILLED)

**核心结论**：holdout eff_rank 与 collapse 完全解耦（G0→G2 上升 +0.96% 而 generation 崩塌至 1 unique token）。Generated eff_rank 信号极强（63.89→3.87→1.06，-98.3%），但目前只有 3 个 final checkpoint 数据点，full_18ckpt 结果决定 Pivot B 能否回答 D013。

**易错点**：
- `pivot_b_verification` 的 `compare_verdict: PIVOT_B_LOSES` **不代表 Pivot B 失败**——D016 已判定该对比方法论无效（3 vs 18 checkpoints 不公平），full_18ckpt 才是公平对比
- 不要把 holdout eff_rank（~678，在 5000 holdout sequences 上算）和 generated eff_rank（~64→1，在 200 生成 samples 上算）混淆——两者量纲不同（前者 hidden states 维度高，后者是 token distribution 维度）
- DDL 2026-05-25，剩 12 天。算力不够的正确建议是"申请更多 GPU"，不是"降级 venue"


---
