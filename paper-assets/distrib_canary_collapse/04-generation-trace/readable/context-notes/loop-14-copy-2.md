# agent / loop_14.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`7183a52d3895eccf2ffb.json`](../../sessions/71/7183a52d3895eccf2ffb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-19T07:13:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855:cuda:0-5 + westd-19828:cuda:0-1，共 8 张，**不得用白名单外 GPU**
- D079：≤3B 模型一律 fp32（不传 --bf16）。>3B（如 Pythia-6.9B）允许 bf16 但仅作补充证据
- D080：`torch_dtype` 参数对 Qwen3.5 无效，**必须** `.to(dtype=target_dtype)` 强制转换。iterative_train.py 已修复（md5: `5b37837e7a6378f42bcb740f8f5e4773`，两台服务器一致）
- D091+D092：dose-response 主轴 + step function **必须纯 fp32**。bf16/fp32 PermG 反转已确认
- D093：padding_side right-padding bug 已确认影响所有实验的 generation 质量——后续需关注此 bug 的处置决策
- 提交命令必须包含完整 conda 激活 + HF 三变量（HF_HOME/HF_HUB_DISABLE_XET/HF_ENDPOINT），否则 127 或下载失败

### 2. 🖥️ 基础设施快照
- **westd-17855**: 6× RTX PRO 6000 Blackwell (98GB)，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- **westd-19828**: 2× 同款，同路径
- Python: `/root/miniconda3/bin/python`（conda activate base）
- 模型本地路径: `/root/autodl-tmp/models/{SmolLM3-3B-Base, Qwen3.5-0.8B-Base}/`；Pythia/GPT-2 走 HF cache
- HF cache: `/root/autodl-tmp/.hf_cache`，HF_ENDPOINT=`https://hf-mirror.com`
- 活跃进程（8/8 GPU 满载）:
  - 17855:cuda:0 — scale_69b_a100_s42 (PID 29028, bf16, 6.9B scale验证, gen 9/10 接近完成)
  - 17855:cuda:1 — qwen35_08b_wiki_a100_s42_v2 (PID 74455, fp32, Table 7)
  - 17855:cuda:2 — a050_s42_fp32 (PID 96513, 05:31提交, ~10:30完成)
  - 17855:cuda:3 — a050_s43_fp32 (PID 96593, 同上)
  - 17855:cuda:4 — a050_s44_fp32 (PID 96734, 同上)
  - 17855:cuda:5 — a010_s42_fp32 (PID 95313, 05:20提交, ~10:20完成)
  - 19828:cuda:0 — gen_gpt2m_a100_s43_fp32 (PID 407859, GPT-2m Table 7)
  - 19828:cuda:1 — smollm3_3b_wiki_a100_s42_v3 (PID 408261, 00:24提交, ~14:24完成)
- Cron 监控: scale_69b + gen_gpt2m 确认活跃（reconcile 通过）

### 3. 📊 当前状态
8/8 GPU 满载，0 Worker 活跃，43 success / 1 negative / 8 failed / 74 total。

**刚完成的关键实验**（D080 fp32 修复批次，均 success）:
- interv_pred_a075_s42_fp32_v4：predictive intervention α=0.75 fp32
- alpha_sweep_a060_s42_fp32_v3：dose-response transitional α=0.60 fp32
- alpha_sweep_a005_s42_v3：盲区延伸 α=0.05 fp32

**正在等待的回调**: 8 个 RUNNING 实验的 cron 完成回调。最先完成的应是 scale_69b（gen 9/10，约 1h 内）。

**Paper 进度**: Intro ✅ + patches, Method/RW 写作中。Lag sensitivity + intervention 5-method + dual-track figure 已通过 Reviewer。

### 4. 📋 待办（条件触发式）
- scale_69b 完成 → 检查 padding_side 影响 + 6.9B scale claim 决策（bf16 数据，补充证据）
- a050 fp32 × 3 seeds 完成（~10:30 UTC）→ 计算纯 fp32 PermG step function 转折点 + MMCT batch 重算 → 更新 dose-response map 的 α=0.50 行
- a010_s42_fp32 完成（~10:20 UTC）→ 与 s43 fp32 汇合做双 seed 盲区确认 → D075 claim 最终锁定
- qwen35_v2 / gpt2m_s43_fp32 / smollm3_v3 各自完成 → Table 7 新行（跨架构泛化证据）
- 所有 fp32 dose-response 完成后 → α=0.25 仍是 fp16（需决策是否重跑 fp32 或标注 provenance）
- α=0.00 同为 fp16 → 同上决策

### 5. 🎯 战略上下文
- **Target**: EMNLP 2026 ARR June cycle, DDL ~June 15（~27 天）
- **核心贡献**: D067 升级为 method paper——MMCT 方法 (FPR=0) + regime map (8-point dose-response) + 跨架构泛化 (目标 7/7 架构族)
- **决策链**: D079(fp32规则) → D080(dtype bug) → D085(ppl失效) → D086(FDR校正) → D087(双轨叙事) → D088(Claim4 prevention paradox) → D090(Claim4 scope α≥0.75) → D091(fp32 mandatory) → D092(bf16/fp32反转) → D093(padding_side bug)
- **易错点**:
  - 不要把 bf16 和 fp32 数据混在 dose-response 主轴表里——D091/D092 明确要求纯 fp32
  - α=0.00/0.25 数据仍是 fp16 provenance，dose-response 表写入时必须标注或决策重跑
  - scale_69b 是 bf16 实验，结论放 Table 7 补充列但不进 dose-response 主轴
  - SmolLM3 是 3B，按 D079 必须 fp32（已正确提交）
  - D093 padding_side bug 影响范围待 Director 决策，可能需要全局重审 generation 质量


---
