# director / loop_5.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`d4d0ef967dade71eea68.json`](../../sessions/d4/d4d0ef967dade71eea68.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-16T10:10:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3 on rtx5090-4x（4× RTX 5090 32GB）。不得使用其他 GPU。
- 所有 scope 扩展实验（plan_006/007/016）必须用 **bf16 LoRA**（无量化）。QLoRA 仅限专门验证 decoupling 的对照实验。违反会污染跨 scale 对比。
- D076 统一 eval 协议：batch_size=4, --no-quantize, --sft_adapter, max_new_tokens=1024, CUDA_VISIBLE_DEVICES 显式设置。所有论文数据必须在此协议下产出。
- C002 硬约束：所有训练/eval 命令必须设 CUDA_VISIBLE_DEVICES=X，禁止 device_map="auto"。
- 磁盘根分区禁止存大文件，所有模型/数据/checkpoint 在 `/root/autodl-tmp/`。
- CED vs flat-NLI 已确认统计不可区分（D078, p=0.22）——论文不能 claim CED > flat-NLI。

### 2. 🖥️ 基���设施快照
- 服务器：rtx5090-4x (connect.bjb2.seetacloud.com) + bjb2-12179，账号 root
- 工作目录：`/root/autodl-tmp/freige`
- 模型路径：
  - Qwen3-4B: `/root/autodl-tmp/models/Qwen/Qwen3-4B`
  - Qwen3-1.7B: `/root/autodl-tmp/models/Qwen/Qwen3-1.7B`（⚠️ 权重可能缺失，之前被清理过，需确认是否已重新下载）
  - Qwen3-8B: `/root/autodl-tmp/models/Qwen/Qwen3-8B`（完整，16GB）
  - LLaMA-3.1-8B: `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B/`（base 版，非 Instruct）
- 数据：Re-DocRED 已下载转换完成，与 DocREDProcessor 直接兼容
- SFT adapters: `/root/autodl-tmp/sft_output_*`（4B/1.7B/8B with-evidence + no-evidence variants）
- 磁盘：~49GB free（刚清理过 GRPO/DPO 旧输出 44GB）
- HF cache: `/root/autodl-tmp/.hf_cache`
- 无 W&B 配置，无 conda（用系统 Python）

### 3. 📊 当前状态
**刚做完**：
- D076 paired t-test 完成（D078）：CED vs flat-NLI Δ=-0.18pp, p=0.22，不显著
- plan_006 Qwen3-1.7B SFT bf16 训练完成（checkpoint-570）
- plan_006 Qwen3-8B SFT bf16 训练完成（checkpoint-570, eval_acc=0.8377）
- 磁盘清理释放 42GB
- LLaMA 代码兼容性修复中（apply_chat_template enable_thinking 参数）

**RUNNING**（4 GPU 满载）：
- cuda:0: 8B no-evidence SFT（bf16 LoRA），预计 ~10:33 UTC 完成
- cuda:1: plan_002 test eval（DocRED test set），预计 ~12:30 UTC
- cuda:2: 1.7B no-evidence eval，预计 ~11:10 UTC
- cuda:3: 8B SFT eval，预计 ~11:30 UTC

**Workers 运行中**：
- LLaMA template 兼容性修复（sft_trainer.py + inference.py + 其他文件）
- LLaMA dry run 准备

**意外发现**：1.7B SFT eval Ign-F1=0.4786，比 4B SFT baseline (0.4106) 高 6.8pp。待 1.7B no-evidence eval 完成后判断是否是 evidence tax 差异导致。

### 4. 📋 待办（条件触发式）
- 1.7B no-evidence eval 完成 → 计算 1.7B evidence tax（与 4B 的 7.47pp 对比），确认 tax 跨 scale 方向一致
- 8B SFT eval 完成 → 与 4B baseline 对比，建立 8B evidence tax baseline
- 8B no-evidence SFT 完成 → 提交 8B no-evidence eval（cuda:0 释放后）
- LLaMA 代码修复完成 → dry run 10 docs → 确认格式正确 → 提交 LLaMA SFT（cuda 释放后最先可用的卡）
- plan_002 test eval 完成 → 汇报 test set Ign-F1/Rel-F1，确认 dev-test degradation 程度
- 全部 scale eval 完成 → 更新 paper_framing.md 的 MVP Evidence Summary 加入多模型数据
- 1.7B/8B RSFT 需要先生成候选数据（N=8 per sample）→ 排在 eval 之后

### 5. 🎯 ��略上下文
**项目核心**：evidence-grounded DocRE 系统性研究。4 个 Claims：
- C1: Evidence generation tax ~7pp（已确认）
- C2: RL optimization pressure ∝ decoupling severity（GRPO QLoRA catastrophic → bf16 mild → DPO gradual → RSFT none）
- C3: CED vs flat-NLI 不显著，已降级（D056/D078）
- C4: EDCR 双层诊断（方法级 + per-relation）

**当前阶段**：D077 scope 扩展（用户明确指出模型/数据集不足）。目标：Qwen3-1.7B/4B/8B + LLaMA-3.1-8B + Re-DocRED。投稿目标 EMNLP 2026 ARR July。

**易踩的坑**：
1. LLaMA 用的是 base 模型（非 Instruct），需要手动设 chat_template（已决策方案 3）
2. 1.7B SFT eval 异常高（Ign-F1=0.4786 > 4B 的 0.4106）——不要急于下结论，4B baseline 是旧实验可能配置不同。等 D076 SFT baseline (0.3974) 作为真正对比基准。
3. 磁盘仍需关注：49GB free，LLaMA SFT checkpoint + RSFT 候选数据会占空间
4. Agent 队列经常堆积——发消息前检查 depth，避免冗余指令
5. RC12 (SAIS positioning) 是论文关键风险点：必须精准区分 discriminative evidence retrieval vs generative evidence production


---
