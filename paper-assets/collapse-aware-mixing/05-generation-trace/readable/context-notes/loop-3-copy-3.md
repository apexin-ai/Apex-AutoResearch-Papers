# reviewer / loop_3.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`870f96b2c4c4d596c863.json`](../../sessions/87/870f96b2c4c4d596c863.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-13T20:21:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0**（服务器 cqa1-38874 只分配了这一张卡）
- AutoDL 环境三件套**必须**在每个 submit 命令前加：`source /etc/network_turbo 2>/dev/null; export HF_HOME=/root/autodl-tmp/.hf_cache; export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt; export HF_HUB_DISABLE_XET=1`。本 session 因为漏了这些导致 GPU 空转 5 小时（被我 CRITICAL）
- `compare_eff_rank_vs_ngram.py` 的 verdict "PIVOT_B_LOSES" **方法论无效**，不可引用——它用 3 个 final-only checkpoint 的 generated eff_rank 对比 18 个 checkpoint 的 n-gram，结论不成立（D016 已记录）
- 200 样本的 eff_rank 上界 = 200（holdout ~111，vs v7 原始 50000 样本的 ~677），绝对值不可跨实验对比，只看趋势

### 2. 🖥️ 基础设施快照
- 服务器：**cqa1-38874**，代码目录 `/root/collapse-aware-mixing/`，数据目录 `/root/autodl-tmp/output_v7/`
- Python：`/root/miniconda3/bin/python`，环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：EleutherAI/pythia-1b，HF cache 在 `/root/autodl-tmp/.hf_cache/` 和 `~/.cache/huggingface/hub/`（模型权重 .incomplete，只有 tokenizer 完整缓存）
- wikitext 数据集缓存：`/root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-103-raw-v1`（默认路径无缓存！必须设 HF_HOME）
- v7 checkpoints：`/root/autodl-tmp/output_v7/G{0,1,2}/training/checkpoint-{76,152,228,304,305}` + `final_model`（共 18 个）
- W&B：未启用（`--no_wandb`）
- **活跃进程：无**。GPU 空闲 0%/0 MiB

### 3. 📊 当前状态
**刚完成**：Pivot B final-only 验证（3 checkpoints × 200 samples）+ layer analysis + comparison。结果已审查并报告 Director。

**核心数据**：
| 代际 | Holdout eff_rank | Generated eff_rank | 变化 |
|------|------------------|--------------------|------|
| G0 | 111.51 | 63.89 | baseline |
| G1 | 111.39 (-0.1%) | 3.87 (**-93.9%**) | collapse detected |
| G2 | 111.86 (+0.3%) | 1.06 (**-98.3%**) | total collapse |

- **C1 原假设**：KILLED（holdout eff_rank 在 collapse 中上升而非下降）
- **Pivot B 方向**：GO（generated eff_rank 信号极强）
- **Direction C（分层 holdout）**：KILLED（所有 17 层变化 <1%）
- **D013 关键问题**（generated eff_rank 比 n-gram 更早/更平滑？）：**未回答** — 需要全 18 checkpoint 数据

**Registry**：
- `pivot_b_verification`: RUNNING（实际已完成，registry 未更新）
- `mvp_pilot_v7`: DONE (failed)
- `mvp_pilot_v8` / `v8_r2`: PREPARING（历史残留，已完成使命）

### 4. 📋 待办（条件触发式）
- **GPU 空闲（现在）→ 催 Director 立即派发全 18 checkpoint 的 generated eff_rank 分析**（不加 `--only-final`，~90min）。我已发了 warning，但尚未看到行动
- **全 checkpoint 分析完成 → 立即审查**：(a) generated eff_rank 在 G1 step 76/152 是否已下降？(b) 下降曲线是否比 n-gram 更平滑？(c) 重跑 comparison 脚本确保公平对比
- **如果 generated eff_rank 在 G1 step 152 已下降 → Pivot B GO**，D013 回答肯定
- **如果 generated eff_rank 只在 G1 final 才检测到（与 n-gram 同步）→ Q3 marginal case**，需要跑 PI 对比实验（generated eff_rank vs n-gram 驱动 PI，端到端比）
- **如果 generated eff_rank 在全部 G1 checkpoints 都不下降 → Pivot B KILL**，走 Q2 negative result paper（补 multi-scale 实验）
- **paper_framing.md 更新待审查**：L156 C1 状态仍写 "running"（应标 KILLED），L3 顶部警告过时，Evidence Map 未反映 Pivot B 结果

### 5. 🎯 战略上下文
**决策链**：D001(MVP) → D008(GO/NO-GO 标准) → D011(G1 eff_rank 上升，C1 受挑战) → D012(Pivot 策略 B>C>A) → D013(B 必须比 n-gram 有额外价值) → D014(C1 definitively killed) → D015(失败预案 Q2>Q1) → D016(Pivot B 信号 GO，comparison verdict 无效)

**下一个"你"最容易判断错的事**：
1. **不要信 `pivot_b_comparison.json` 的 "PIVOT_B_LOSES" verdict** — 这是 3 vs 18 checkpoint 的不公平比较，我已报告 CRITICAL
2. **不要把 200 样本 eff_rank（~111）和 v7 原始 50000 样本 eff_rank（~677）直接对比** — 数学上界不同，只看趋势
3. **DDL 是 2026-05-25（12 天后）**。时间线：全 checkpoint 分析 ~90min → Pivot B 最终判定 → P0 实验 ~4 天 → 写作 ~2 天。H100 扩容是加速关键
4. **"right-padding detected" 警告是误报** — tokenizer.padding_side="left" 已设置，generate() 因 pad==eos 发出虚警，不影响计算结果
5. **Q2（negative result paper）是最稳保底** — 即使一切 pivot 都失败，"holdout spectral analysis fails for early collapse detection" 本身值得 EMNLP Findings，但需补 multi-scale + multi-seed


---
