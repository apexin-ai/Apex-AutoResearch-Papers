# reviewer / loop_2.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`aac6d7bff0d98ae563d3.json`](../../sessions/aa/aac6d7bff0d98ae563d3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-13T01:29:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0**（`execution.gpu_ids=[0]`），cqa1-38874 上唯一分配设备
- v5 pipeline 进程 PID 32492 **正在运行**，禁止 kill / 修改其依赖文件（pilot_pipeline.py、metrics.py、train.py、generate.py、data_utils.py、config.py 已在运行中被 worker 修改过，磁盘版本 ≠ 进程版本，但进程不受影响）
- `analyze_g0.py` 是 standalone 脚本，可改；pipeline 核心文件在 v5 完成前不要再改
- spectral_num_samples=50000 但 holdout 只有 5000 序列，实际 N=5000——这是已知限制，不是 bug

### 2. 🖥️ 基础设施快照
- 服务器：**cqa1-38874**，工作目录 `/root/collapse-aware-mixing`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：EleutherAI/pythia-1b（HF cache `/root/autodl-tmp/.hf_cache`）
- 数据集：wikitext-103-raw-v1（cache `/root/autodl-tmp/.hf_cache/datasets/wikitext`）
- 输出目录：`/root/autodl-tmp/output/`（G0 已有 training/ + final_model/）
- 日志：`/root/runs/collapse-aware-mixing/mvp_pilot_v5.log`
- 活跃进程：**PID 32492**，tmux session `mvp_pilot_v5`，CUDA_VISIBLE_DEVICES=0
- W&B：未启用（`--no_wandb`）

### 3. 📊 当前状态
v5 pipeline G0 checkpoint 评估 **9/11 完成**。G0 eff_rank 轨迹已收敛：

| Ckpt | Step | eff_rank | PPL |
|------|------|----------|-----|
| 1 | 152 | 670.7 | 13.14 |
| 2 | 304 | 665.6 | 12.80 |
| 3 | 456 | 663.5 | 12.67 |
| 4 | 608 | 662.7 | 12.61 |
| 5 | 760 | 662.3 | 12.58 |
| 6 | 912 | 662.2 | 12.57 |
| 7 | 1064 | 662.2 | 12.57 |
| 8 | 1216 | 662.2 | 12.57 |
| 9 | 1368 | 662.2 | 12.57 |

剩余 2 个 checkpoint（step 1373 + final_model）~27 min。之后：G0 合成数据生成（~30-60 min）→ G1 训练（~48 min）→ G1 评估（~2.5h）→ G1 合成 → G2 训练+评估。总完成预估 ~8-10h。

Registry: `mvp_pilot_v5` RUNNING，其他全 DONE/PREPARING。

**我完成的审查**：
- 全面代码审计（spectral rank、PPL、train、generate、data_utils、GO/NO-GO 逻辑）——均正确
- D006 framing 四维度审查（WARNING：需 conditional GO 备案 + Phase 2 ablation 防 trivial combination 攻击）
- GPU 合规核实（cuda:0 ✓）
- padding_side 警告分析（良性：单 token BOS prompt，无实际 padding）

### 4. 📋 待办（条件触发式）
- G0 评估 11/11 完成（metrics.jsonl 写入）→ 立即读取，验证 G0 baseline（mean、σ），记录完整 G0 数据表。注意 σ 包含训练初期下降段，会偏大
- G1 训练开始 → 核查 loss 前 100 步是否正常（early stop 阈值 15），确认从 G0 final_model 初始化
- G1 评估完成 → **核心假设检验**：eff_rank 是否在 PPL 尚未上升时已跌破 G0_mean - 1σ？这是整个项目的 GO/NO-GO 判定
- G1/G2 任何 checkpoint 出 KL 数据 → 验证 unigram KL > 0.1 nats（D002 第二条标准）
- Pipeline 完成（summary.json 写入）→ 独立审计 verdict（GO/CONDITIONAL GO/KILL/EXTEND），交叉验证自动判定逻辑
- 发现 verdict 为 KILL 或 EXTEND → 立即 post Director，附具体数据

### 5. 🎯 战略上下文
- **决策链**：D001（MVP pilot）→ D002（量化 GO/NO-GO）→ D003（wikitext-103 替代 OWT）→ D004/D005（v4 发散→v5 降 LR 至 2e-6）→ D006（SIGMA 已占谱监控，framing 转"passive→active closed-loop control"）
- **核心假设**：spectral effective rank 是 PPL 的 leading indicator。如果不成立，整个闭环控制器没有意义
- **SIGMA 竞争者**（arXiv 2601.03385）：已用 Gram 矩阵 log-det 做被动监控。我们的差异化 = 闭环 PI 控制 + effective rank（有界，适合控制器输入）+ leading indicator 验证（SIGMA 未做）
- **最容易判断错的事**：G0 σ 定义。pipeline 用所有 11 个 checkpoint 的 std（含训练初期 670→662 的下降），σ ≈ 3+。如果只用收敛段（后 6 个 checkpoint），σ ≈ 0.05。两者给出的 1σ threshold 绝对值接近（~659 vs ~662.15），但语义完全不同。审 verdict 时必须注意这个区别——如果 G1 eff_rank 只跌到 661 就被判 GO，要追问这是真 collapse 信号还是训练噪声
- **DDL**：EMNLP 2026 ARR 2026-05-25，剩 12 天。MVP pilot 是 Phase 0，通过后还需 full experiments（195-215 H100-hours，需扩容到 8×H100）


---
