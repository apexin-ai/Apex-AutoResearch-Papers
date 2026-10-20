# director / loop_6.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`85ad1e62d6fd24357841.json`](../../sessions/85/85ad1e62d6fd24357841.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-16T12:33:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3 on rtx5090-4x（4× RTX 5090 32GB）。不得使用其他 GPU。
- scope 扩展实验（plan_006/007/016）必须用 **bf16 LoRA**（无量化）。QLoRA 仅限 decoupling 对照。
- D076 统一 eval 协议：batch_size=4, --no-quantize, --sft_adapter, max_new_tokens=1024, CUDA_VISIBLE_DEVICES 显式设置。
- C002：所有训练/eval 命令必须设 CUDA_VISIBLE_DEVICES=X，禁止 device_map="auto"。
- **C005**：no-evidence 模型 eval 必须传 `--no_evidence` 参数（之前因漏传导致 1.7B/8B 结果全部无效）。
- SSH 命令必须用 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ..."` 包��（tmux 用 /bin/sh，裸命令 python: command not found）。
- CED vs flat-NLI 统计不可区分（D078, p=0.22）——论文不能 claim CED > flat-NLI。
- cwd 必须是 `cd /root/autodl-tmp`，不是 `cd /root/autodl-tmp/freige`。

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (connect.bjb2.seetacloud.com) + bjb2-12179，root
- 工作目录：`/root/autodl-tmp/freige`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：Qwen3-4B `/root/autodl-tmp/models/Qwen/Qwen3-4B`、1.7B `.../Qwen3-1.7B`、8B `.../Qwen3-8B`、LLaMA-3.1-8B `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B/`
- SFT adapters：`/root/autodl-tmp/sft_output_qwen3_4b`、`sft_output_qwen3_1_7b_no_evidence`、`sft_output_qwen3_8b`、`sft_output_qwen3_8b_no_evidence`、`sft_output_llama_3_1_8b`、`sft_output_llama_3_1_8b_no_evidence`
- 数据：DocRED `/root/autodl-tmp/data/docred`、Re-DocRED `/root/autodl-tmp/data/re-docred`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 无 W&B，无 venv（conda base）
- 活跃进程（最后确认时）：
  - cuda:0: plan_007_redocred_4b_sft_eval (PID 342069)
  - cuda:1: 1.7B no-evi eval v3 (PID 337844) + LLaMA with-evi eval (PID 340116)
  - cuda:2: 8B no-evi eval v2 (PID 335357)
  - cuda:3: LLaMA no-evi eval (PID 339692)

### 3. 📊 当前状态
**刚���完**：
- D076 paired t-test 完成：CED vs flat-NLI p=0.22，统计不可区分（4 seeds each）
- LLaMA-3.1-8B SFT with-evidence 训练完成（train_loss=0.5246, token_acc=0.8361）
- LLaMA-3.1-8B no-evidence SFT 训练完成（train_loss=0.456, token_acc=0.815）
- 8B no-evidence SFT 训练完成（train_loss=0.6509）
- 8B SFT eval 完成：Ign-F1=0.5051
- test set eval 完成（plan_002）：无本地 F1（需 CodaLab），截断率 62.6%
- ��复 --no_evidence 漏传 bug（C005 约束已添加），1.7B/8B no-evi eval 重跑��

**RUNNING（4 GPU 满载）**：
- cuda:0: Re-DocRED 4B SFT eval (plan_007)，~15-20min
- cuda:1: 1.7B no-evidence eval v3 + LLaMA with-evidence eval（共享 GPU）
- cuda:2: 8B no-evidence eval v2（含 --no_evidence）
- cuda:3: LLaMA no-evidence eval（含 --no_evidence）

**等���**：上述 eval 全部完成后可计算完整 multi-scale + cross-family evidence tax。

### 4. 📋 待办（条件触发式）
- 1.7B no-evi eval v3 完成 → 提取 Ign-F1 → 计算 1.7B evidence tax = 0.4786 - X
- 8B no-evi eval v2 完成 → 提取 Ign-F1 → 计算 8B evidence tax = 0.5051 - X
- LLaMA with-evi eval 完成 → 提取 Ign-F1（LLaMA baseline）
- LLaMA no-evi eval 完成 → 提取 Ign-F1 → 计算 LLaMA evidence tax
- Re-DocRED eval 完成 → Ign-F1 确认跨数据集泛化（plan_007）
- 全部 eval 收齐 → 更新 paper_framing.md MVP Evidence Summary 加入 multi-scale + cross-family 数据
- 全部 eval 收齐 → 用户问过 CodaLab 账号（test set 提交），待用户回复
- GPU 释放后 → 下一阶段：RSFT 候选生成（N=8 per sample）for 1.7B/8B/LLaMA → RSFT 训练

### 5. 🎯 战略上下文
**项目核心**：FREIGE — evidence-grounded DocRE 系统性研究。4 Claims：
- C1: Evidence generation tax（4B 确认 ~7.5pp；1.7B/8B/LLaMA 数据即将到位）
- C2: RL optimization pressure ∝ decoupling severity（QLoRA catastrophic / bf16 mild / DPO gradual / RSFT none）
- C3: CED vs flat-NLI 不显著，已降级（D078 确认）
- C4: EDCR 双层诊断（方法级 + per-relation）

**阶段**：D077 scope 扩展（用户指出模型/数据集不足）。投稿 EMNLP 2026 ARR July。

**Dream median 评分 4（borderline reject）**，主要弱点：方法学新颖性有限(W1)、任务定义是 straightforward extension(W2)、RSFT 提升modest(W3)、LLaMA 验证不完整(W4)、缺 encoder-based 对比(W5)、related work 太薄(W6)。当前实验正在修复 W4（LLaMA 全流程）和部分 W3（multi-scale）。

**易踩���坑**：
1. 1.7B SFT eval Ign-F1=0.4786 > 4B baseline 0.3974——看似反常但 4B baseline 是 D076 协议下的数字（比早期实验低）。不要用旧 4B 数字做对比。
2. Agent 队列容易堆积 cron ���调——发消息前检查 depth，必要时 replace_agent_queue
3. no-evidence eval 必须有 --no_evidence 参数（C005），已经因此浪费 >2h GPU 时间
4. SSH 命令必须 bash -c + conda activate 包裹，否则 EXIT_CODE=127
5. 无 W&B + 无 sentinel → cron 经常误判成功实验为 failed，收到 failed 回调先 tail 日志确认


---
