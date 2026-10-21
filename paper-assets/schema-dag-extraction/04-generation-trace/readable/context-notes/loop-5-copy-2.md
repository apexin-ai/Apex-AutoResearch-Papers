# agent / loop_5.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`41c0bf70d7ea852fd62d.json`](../../sessions/41/41c0bf70d7ea852fd62d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-15T22:52:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 cqa1-38874 的 cuda:0（单卡 RTX PRO 6000 Blackwell 98GB），无其他 GPU
- **C001**: 40-rel 子集来自 80-type pool 采样，论文必须写 "40-rel subsets sampled from the 80-relation pool"，不能暗示独立 pool
- **C002**: BCS amplification 3.4× 仅基于 16-type vs 80-type 两个 pool size，40-rel 的 BCS Δ 是 80-pool 内子集效应，不是第三个独立数据点
- Blackwell SM120 上 FP8 模型需要 flashinfer 0.6.11.post2 + nvidia-cuda-nvcc 13.2.78 + `CUDA_HOME=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13`，缺任何一个就 JIT 失败
- LLaMA-3.1-Instruct 必须用 `tokenizer.apply_chat_template()` 包装 prompt，裸文本调用零输出
- exp012_llama_8b_r2_exp2 (NER Channel 2 跨模型) 是 negative，**不写入论文主体**，至多 rebuttal 中诚实讨论

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874，工作目录 `/root/schema-dag-extraction`
- Python：`/root/miniconda3/bin/python`（conda base 环境，Python 3.12.3）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- Qwen3-32B-FP8：`/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/`
- LLaMA-3.1-8B-Instruct：`/root/autodl-tmp/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct`
- vLLM 0.20.2, torch 2.10.0+cu128, flashinfer 0.6.11.post2
- 活跃进程：**无**——全部实验完成，GPU 空闲，无 cron，无 Worker

### 3. 📊 当前状态
全部 31 个实验已完成（14 success / 5 negative / 10 failed / 2 killed）。Paper Agent Full Draft + exp012 patch 已完成，进入 Reviewer 对抗循环。GPU 当前空闲。无运行中的 Worker 或 Cron。

**核心证据链完整**：
- Claim 1（count→recall decline）：三任务（NER/ED/RE）+ 双模型（Qwen3/LLaMA）✓
- Claim 2（BCS→type confusion）：三任务 + 双模型 ✓，新发现 high-BCS floor 跨模型恒定 ≈51%
- Claim 3（SDGD）：正式放弃（D019），v1+v2 均 negative，作为 negative result + future work
- exp012 强复现（D031）：BCS Δ=-27.1pp/-23.9pp，达 Qwen3 的 75-87%

### 4. 📋 待办（条件触发式）
- Reviewer 对抗循环继续 → 派 Worker 做写作质量迭代，聚焦论文一致性和数字准确性
- AWQ 残留 ~36GB 在 `/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/` → 可派 Worker 清理释放磁盘
- Director 要求图表重生成/数字验证 → 用 cuda:0 跑可视化脚本
- ARR May 25 提交（距今 10 天）→ 最终 PDF 编译 + reference audit + 视觉审查

### 5. 🎯 战略上下文
**核心论文 story**：type confusability（用 BCS 量化）独立于 type count 驱动 training-free LLM IE 质量下降，形成 multi-channel degradation model（Channel 1: count→recall, Channel 2: confusability→type confusion）。

**决策链关键节点**：
- D031/D032：exp012 强复现成功，升级为 cross-family claim，不追加新模型，聚焦写作
- D019/D014：SDGD 正式放弃，negative result 写入 future work
- D026：exp006 交互效应不显著（p=0.505），不在论文主体引用

**易错点**：
- 不要把 40-rel BCS Δ 当作第三个独立数据点（C002）——它是 80-pool 的子集
- MAVEN per-type BCS 方向相反（正向），是 centrality confound，论文中作为 boundary condition 讨论，不要误用为支持证据
- Few-NERD pairwise r 用 0.112（bootstrap 校正后），不是早期的 0.156
- exp012_llama_8b_r2 的 exact/relaxed F1=0 不是 bug，是 LLaMA 缺少字符偏移量，text_match 是正确指标


---
