# agent / loop_13.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`ffe72667d9b2abff0532.json`](../../sessions/ff/ffe72667d9b2abff0532.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-16T10:30:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 = cuda:0,1,2,3（rtx5090-4x），提交前 nvidia-smi 确认目标卡显存 < 2GB
- cwd 必须 `cd /root/autodl-tmp`，不是 `/root/autodl-tmp/freige`
- RSFT checkpoint 路径极易搞错：CED s42=`rsft_output/`（无 `_ced`），s44=`rsft_output_s44/`（无 `_ced`）；flat-NLI 全系列 ckpt=507 不是 510。以 memory.md 映射表为准
- 训练脚本可能无 W&B/sentinel → cron 会误判 failed。收到 failed 回调先 tail 日志确认是否正常完成
- 提交重试前先检查磁盘是否已有有效输出（之前冗余重跑过 eval_flat_nli_s44 和 1.7B no-evidence SFT）

### 2. 🖥️ 基础设施快照
- **服务器**: rtx5090-4x（主力，4× RTX 5090 32GB）| bjb2-12179（备用）
- **工作目录**: `/root/autodl-tmp/`（代码 `freige/`，数据 `data/docred/`，模型 `models/`）
- **Python**: `/root/miniconda3/bin/python`（conda base，不用 venv）
- **环境激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **模型路径**: `models/Qwen/Qwen3-4B`, `models/Qwen/Qwen3-1.7B`, `models/Qwen/Qwen3-8B`
- **活跃进程**:
  - PID 319632: plan_002_test_eval_s44_r2 (cuda:1, test set eval)
  - PID 322966: plan_006_qwen3_8b_sft_eval (cuda:3)
  - PID 324679: plan_006_qwen3_1_7b_no_evidence_eval (cuda:2)
  - PID 325491: plan_006_qwen3_8b_no_evidence_sft (cuda:0, training)
- **Cron**: 4 个活跃 cron 监控上述 4 个实验

### 3. 📊 当前状态
4 GPU 全满负荷跑 D077 scope 扩展实验：
- **cuda:0**: Qwen3-8B no-evidence SFT 训练（plan_006 ablation，估计 ~3-4h）
- **cuda:1**: DocRED test set eval（plan_002，RSFT CED s44 最终数字）
- **cuda:2**: Qwen3-1.7B no-evidence eval（plan_006 对照组）
- **cuda:3**: Qwen3-8B evidence-SFT eval（plan_006 实验组）

**等待中**:
- 4 个 cron 回调（实验完成时触发）
- seed_comparison_prep (PREPARING) — 已有 pre-analysis，4-seed paired t-test 已完成确认 CED≈flat-NLI
- Worker 池 = 0（当前无活跃 Worker，cron 回调到后需立即 spawn）

**下一波（GPU 释放后）**:
- plan_006 Qwen3-8B no-evidence eval（等 cuda:0 训练完）
- plan_016 LLaMA-3.1-8B cross-family（模型可能还在下载，需确认）
- plan_007 Re-DocRED 跨数据集验证

### 4. 📋 待办（条件触发式）
- plan_002_test_eval_s44_r2 完成 → 记录 test set 最终数字到 registry，report Director（这是论文 main table 的最终 row）
- plan_006_qwen3_8b_sft_eval 完成 → 与 plan_006_qwen3_8b_no_evidence_sft 的 eval 配对计算 8B evidence tax
- plan_006_qwen3_1_7b_no_evidence_eval 完成 → 与已有 1.7B evidence-SFT eval 对比，计算 1.7B evidence tax
- plan_006_qwen3_8b_no_evidence_sft 训练完成 → 立即提交 eval（cuda:0 释放后原地跑）
- 所有 plan_006 eval 收齐 → 汇总 evidence tax vs model size 表（1.7B / 4B / 8B），向 Director 汇报 C1 跨 scale 结论
- LLaMA-3.1-8B 模型就绪 → 启动 plan_016 SFT（需先确认 prompt template 适配）
- Re-DocRED 数据就绪 → 启动 plan_007 eval

### 5. 🎯 战略上下文
- **核心 story**: FREIGE 三大贡献——(1) evidence tax 量化 ~8pp，(2) QLoRA-specific decoupling（bf16 仅 mild），(3) CED reranker 恢复 97%
- **C3 已降级**: CED vs flat-NLI 统计不可区分 (D056/D078)，不再作为独立 claim，改为 robustness evidence
- **D077 scope 扩展是当前主线**: 从 Qwen3-4B 单模型扩到 1.7B/8B/LLaMA，从 DocRED 扩到 Re-DocRED。目的是让 reviewer 不能说 "only tested on one model/dataset"
- **投稿 EMNLP 2026 Main (ARR July, ~7/15-25)**，时间充裕（~2 个月）
- **易错点**: (1) 不要混淆 `rsft_output_r2b/` (旧实验) 和 CED s42 `rsft_output/`；(2) plan_006 8B 需要两个 eval（evidence + no-evidence）才能算 tax；(3) LLaMA 可能需要不同 prompt template，不要直接套 Qwen 配置
- **决策链核心**: D077 scope 扩展 → D076 统一协议 → D072 EDCR 双层诊断 → D069 decoupling spectrum 修正


---
