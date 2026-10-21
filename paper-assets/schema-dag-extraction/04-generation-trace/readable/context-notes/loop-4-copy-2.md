# agent / loop_4.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`f0ec81b8bd94682b41ac.json`](../../sessions/f0/f0ec81b8bd94682b41ac.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-15T19:45:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- 只能用 **cqa1-38874** 服务器，**cuda:0**（唯一 GPU：RTX PRO 6000 Blackwell 98GB）
- LLaMA-3.1-8B-Instruct **必须用 chat template**（`tokenizer.apply_chat_template`），裸文本 prompt 输出空 JSON。参考 `run_extraction.py` L220-279 的修复
- Blackwell SM120 跑 FP8 需要 flashinfer 0.6.11.post2 + nvidia-cuda-nvcc 13.2.78，脚本必须设 `export CUDA_HOME=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13`
- `VLLM_ATTENTION_BACKEND` env var 在 vLLM 0.20.2 已废弃，**不要设置**
- 磁盘 248/250GB 接近满，70B AWQ 残留占 ~36GB 待清理
- `gpu_memory_utilization` 用 0.80（不是 0.90），防止 VRAM 冲突

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-38874, 工作目录 `/root/schema-dag-extraction`
- **Python**: `/root/miniconda3/bin/python`（conda base, Python 3.12.3）
- **环境激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**:
  - Qwen3-32B-FP8: `/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/`
  - LLaMA-3.1-8B-Instruct: `/root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct`
  - 70B AWQ 残留: 待清理释放 ~36GB
- **数据**: Few-NERD `/root/schema-dag-extraction/data/parquet/test.parquet`, FewRel `/root/schema-dag-extraction/data/fewrel_parquet/`, MAVEN `/root/schema-dag-extraction/data/maven_parquet/`
- **活跃进程**: exp012_llama_8b_r2 (PID 315801) **已死亡**，cron 检测 miss 3/5，pending escalation。无活跃 Worker。
- **关键软件**: vLLM 0.20.2, torch 2.10.0+cu128, flashinfer 0.6.11.post2

### 3. 📊 当前状态
**exp012_llama_8b_r2（RUNNING but process dead）** — LLaMA-3.1-8B chat template 修复版，验证 confusability effect 跨模型泛化。PID 315801 已消失（cron miss 3/5），需要立即诊断：读日志 `~/runs/schema-dag-extraction/exp012_llama_8b_r2.log` 判断是正常完成还是 crash。如果有结果文件则分析入 registry；如果 crash 则需要 r3。

**exp006_interaction_2x2（DONE/negative）** — 交互效应不显著 (p=0.505)，D026 决策已记录。不入论文主体。

**Paper Agent Full Draft** — writing_plan.yaml 已审批（D020/D024），但没有活跃 Worker 在写。距 ARR May 25 还有 **10 天**。

**Registry 总计**: 28 实验，11 success / 4 negative / 10 failed / 3 killed。Worker 池 = 0（违反 L1 #4）。

### 4. 📋 待办（条件触发式）
- **立即** → spawn Worker 读 exp012_llama_8b_r2 日志，判断完成/crash。完成则分析结果 + update_registry；crash 则诊断 + 准备 r3
- exp012_llama_8b_r2 成功 → 录入 metrics + patch 进论文 multi-model validation section + 向 Director 汇报
- exp012_llama_8b_r2 失败 → 清理后重跑 r3（这已是第 8+ 次尝试，考虑向 Director 报告 risk）
- AWQ 残留清理 → spawn Worker 删除 70B 模型释放 ~36GB 磁盘
- GPU 空闲 + 40-rel 未完成 → 考虑是否再试（已 3 次 failed，memory.md 记录"放弃"决策，**不要再跑**）
- Paper Agent Full Draft → spawn Writer Worker 继续写作（D024 单模型版本可先行，8B 结果后 patch）
- **资源饱和**: Worker 池 = 0 严重违规。至少应同时有：1) exp012 诊断 Worker  2) Paper writing Worker  3) AWQ 清理 Worker

### 5. 🎯 战略上下文
**核心结论**: Type confusability（BCS）独立于 type count 驱动 training-free LLM IE 质量下降。Multi-channel degradation model: count→recall decline, confusability→type confusion。

**证据强度**: Claim 1+2 三任务验证完成（Few-NERD ✓ FewRel 80-rel ✓ MAVEN ✓），bootstrap CI 全部 exclude null。Claim 3 (SDGD) 正式放弃 (D019)，转 negative result + future work。

**最易判断错的事**:
- exp012_llama_8b_r2 是 chat template 修复后的版本（之前 7+ 次失败），**不要回退到旧的 prompt 方式**
- 40-rel 中间点已决定放弃（memory.md），**不要再尝试**
- MAVEN per-type BCS 正方向是 centrality confound（不是 bug），论文作为 boundary condition 讨论
- Few-NERD pairwise r 用 0.112（不是旧值 0.156），confusion ratio 用 21.2x（不是 9.9x）——见 Bootstrap 校正
- D024: 多模型验证硬截止 May 18，Paper Agent 应立即启动 Full Draft（单模型版本先行）
- 目标 **EMNLP 2026, ARR May 25**（距今 10 天），时间极紧


---
