# agent / loop_2.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`6be7070fc9cb0309321b.json`](../../sessions/6b/6be7070fc9cb0309321b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-14T14:50:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：gpu_ids=[0,1,2,3]，rtx5090-4x 和 gpu-5090-4x-1 是**同一台物理机**（4x RTX 5090 32GB），两个 SSH endpoint 共享同一组 GPU
- GRPO 训练必须用 `submit_training_job`，不能 nohup
- submit 命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（conda 环境，不是 venv）
- AutoDL 实例：pip/git 前必须 `source /etc/network_turbo`；HF 下载设 `HF_HUB_DISABLE_XET=1` + SSL 证书环境变量
- MVP-2 三路 GRPO 对比是串行的（4 GPU 全占），但 mvp2_sft_eval 可以独立先跑

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x（= gpu-5090-4x-1），account=root
- 工作目录：`/root/autodl-tmp`（代码在 `/root/autodl-tmp/freige/`）
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 模型：`/root/autodl-tmp/models/Qwen3-4B`
- SFT checkpoint：`/root/autodl-tmp/sft_output`
- 数据：`/root/autodl-tmp/data/docred`（train 3027, dev 985）
- NLI cache：`/root/autodl-tmp/nli_cache/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- accelerate 配置：`freige/configs/accelerate_4gpu.yaml`（ZeRO-2 + QLoRA + bf16）
- 活跃进程：**无**（全部 GPU 空闲）
- 活跃 cron：**无**（reconcile 返回 0）

### 3. 📊 当前状态
**刚发生**：mvp2_grpo_ced_r2 以 EXIT_CODE=137 (OOM/SIGKILL) 失败。已派 Worker `worker_diagnose_mvp2_grpo_ced_r2_20260514T112754` 去读日志诊断，**尚未回调**。已向 Director 汇报失败 + 初步判断。

**Registry 概览**：
| exp_id | status | conclusion | 摘要 |
|--------|--------|------------|------|
| mvp1_ced_signal | DONE | success | CED 信号验证 PASS (margin 0.48, acc 81.5%) |
| smoke_test_grpo | DONE | success | ZeRO-2 + QLoRA 功能验证 |
| mvp2_sft_warmup | DONE | success | SFT 基线 (eval_loss 0.72, acc 83.5%) |
| precompute_nli_train | DONE | success | NLI cache 已部署 |
| mvp2_grpo_ced | DONE | failed | 代码 bug (None tail)，已修 |
| mvp2_grpo_ced_r1 | DONE | killed | Mode collapse (F1→0)，修复了 checkpoint/reward weighting/clip |
| mvp2_grpo_ced_r2 | DONE | failed | **OOM (137)**，诊断 Worker 进行中 |
| mvp2_sft_eval | PREPARING | — | SFT baseline eval，可独立先跑 |
| mvp2_grpo_extract | PREPARING | — | extraction-only reward baseline |
| mvp2_grpo_flatnli | PREPARING | — | flat-NLI reward baseline |

**等待中**：
- Worker 回调：`worker_diagnose_mvp2_grpo_ced_r2_20260514T112754`（OOM 诊断）
- Director 决策：无（已汇报，等诊断结果后再发详细修复方案）

### 4. 📋 待办（条件触发式）
- 诊断 Worker 回调 → 读诊断报告，update_registry 写 notes，向 Director 汇报具体 OOM 原因 + 修复方案（大概率：减 num_generations 4→2 或减 max_completion_length 或回退 num_iterations=1 + 大 kl_coef）
- Director 批准修复方案 → spawn Worker 改代码/配置 → 提交 mvp2_grpo_ced_r3
- 任何时刻 GPU 空闲 → 可先提交 mvp2_sft_eval（不依赖 GRPO），利用空闲 GPU 跑 SFT baseline eval
- CED GRPO 成功 → 按 ROADMAP 串行跑 mvp2_grpo_flatnli → mvp2_grpo_extract → MVP-2 结果分析
- CED GRPO 连续 3 次失败 → 考虑向 Director 提 pivot：先跑 flat-NLI 和 extraction-only 收集 baseline 数据，CED 降低显存后并行补跑

### 5. 🎯 战略上下文
- **核心假设**：CED (Contrastive Evidence Discrimination) 奖励能提升 Evi-F1。MVP-1 已验证信号存在 (margin 0.48, acc 81.5%)，MVP-2 验证端到端训练效果
- **决策链**：D001(两阶段 MVP) → D002(MVP-1 PASS) → D003(smoke test PASS) → D004(发现 2 server = 1 machine) → D005(r1 collapse) → D006(kill r1, 准备 r2)
- **MVP-2 pass criteria**：CED GRPO Evi-F1 > SFT Evi-F1 ≥ 2pp；F1 > 45；F1 退化 ≤ 5pp
- **CED 三连失败是当前最大风险**：r0 代码 bug、r1 mode collapse、r2 OOM——三次失败原因各不相同，说明 GRPO+CED 配置空间还没稳定。num_iterations=2（为防 collapse 加的）很可能是 OOM 元凶，需要找到 collapse 和 OOM 之间的平衡点
- **易踩的坑**：(1) 不要假设 .venv 存在，这台机器用 conda base；(2) rtx5090-4x 和 gpu-5090-4x-1 是同一台机器，不能同时各跑 4 卡实验；(3) r1 的修复（reward weighting、save_steps、kl_coef）已合入代码，r3 只需调显存相关参数


---
