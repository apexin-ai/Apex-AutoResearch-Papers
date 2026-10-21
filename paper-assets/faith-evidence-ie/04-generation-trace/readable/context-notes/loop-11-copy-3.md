# reviewer / loop_11.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`a98983ac9b565ea56b43.json`](../../sessions/a9/a98983ac9b565ea56b43.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-16T10:11:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3（rtx5090-4x，4× RTX 5090 32GB）。越界立即 critical。
- 所有 D077 scale 实验必须使用 bf16 LoRA（--no-quantize），不得用 QLoRA。原因：Paper Claim 2 论证 QLoRA 放大 decoupling，scale 对比如果混入 QLoRA 则 confounded。
- D076 统一 eval 协议：batch_size=4, --no-quantize, --sft_adapter, max_new_tokens=1024, 正确 seed。违反者结果无效。
- 磁盘操作：大文件只存 `/root/autodl-tmp/`，根分区 30GB 禁存模型。
- LLaMA cross-family 实验：代码已修复 `enable_thinking` 兼容（7 个文件），但尚未实际跑过 LLaMA SFT/eval，首次提交需 dry-run 验证。

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (root) + bjb2-12179 (root)
- 工作目录：`/root/autodl-tmp/freige`（代码）、`/root/autodl-tmp/`（模型/数据/输出）
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型路径：`/root/autodl-tmp/models/Qwen/Qwen3-1.7B`���`Qwen3-4B`、`Qwen3-8B`、`Meta-Llama-3.1-8B`
- 数据集：`/root/autodl-tmp/data/docred/`（dev.json 998 docs）
- SFT 输出：`sft_output_qwen3_1_7b_bf16`、`sft_output_qwen3_8b_bf16`、`sft_output_qwen3_1_7b_no_evidence`
- 磁盘：清理后 49GB 可用 / 250GB（81%）
- W&B project：freige-sft
- 活跃进程（截至 handoff）：
  - cuda:0: 8B no_evidence SFT (PID 325491, ~85/570 步, ETA ~48min)
  - cuda:1: 已释放（1.7B SFT eval 完成）
  - cuda:2: 1.7B no_evidence eval (PID 324679, 29/247 batches, ETA ~1.5h)
  - cuda:3: 8B SFT eval（running）

### 3. 📊 当前状态
刚完成：
- Review #17：LLaMA 模板兼容阻塞（已被 Agent 修复，7 个文件统一）、cuda:2 进程健康确认、GPU 全卡利用率核查
- 1.7B SFT eval 完成：ign_f1=0.4786（bf16 LoRA, seed=42）
- D076 paired t-test 定论：CED vs flat-NLI p=0.22, 不显著
- 磁盘清理完成：释放 42GB（删除旧 GRPO/DPO 输出）
- LLaMA template 修复：sft_trainer/inference/grpo_trainer/rsft_trainer/rsft_generate/dpo_trainer/smoke_test 全部兼容

等待中：
- cuda:0: 8B no_evidence SFT 训练完成 → 需要 eval
- cuda:2: 1.7B no_evidence eval 完成 → 计算 1.7B evidence tax
- cuda:3: 8B SFT eval 完成 → 获取 8B with-evidence baseline
- plan_002_test_eval (cuda:1 已释放，可能已完成或需重查)

### 4. 📋 待办（条件触发式）
- 1.7B no_evidence eval 完成 → 计算 1.7B evidence tax = (no_evi ign_f1) - 0.4786，对比 4B 的 7.47pp
- 8B SFT eval 完成 → 记录 8B with-evidence baseline ign_f1
- 8B no_evidence SFT 完成 → 提交 8B no_evidence eval（cuda 空出时）
- 8B no_evidence eval 完成 → 计算 8B evidence tax，三点趋势（1.7B/4B/8B）
- 三组 evidence tax 数据齐全 → 审查 D077 multi-scale claim 是否成立（tax 随 scale 变化趋势）
- LLaMA SFT 首次提交 → 要求 dry-run 验证模板兼容修复有效
- Agent 提 registry 修正（8B SFT 从 failed→success）→ 核实修正合理性

### 5. 🎯 战略上下文
- **核心结论链**：D056 确认 CED≈flat-NLI（p=0.22）→ D077 扩展 multi-scale + cross-family 验证 evidence tax 普遍性
- **Paper 三大 Claim**：(1) Evidence tax 存在且显著，(2) QLoRA 放大 decoupling，(3) RSFT 部分恢复 evidence 质量
- **1.7B bf16 SFT ign_f1=0.4786 远超 4B QLoRA baseline 0.3974** — 这不是 bug，是 bf16 vs QLoRA 的差距（支持 Claim 2）。不要误判为"1.7B 比 4B 强"——它们训练方式不同。公平对比必须同 regime（bf16 vs bf16 或 QLoRA vs QLoRA）。
- **易错点**：(1) 不要拿 bf16 LoRA 模型和 QLoRA 模型直接比绝对值得出"小模型更强"；(2) worker_ops 报告有时 PID/elapsed 信息错误（本轮已发现两次），始终独立 ssh 验证；(3) eval 输出目录为空是正常的（完成后才写），不要误判为卡死。


---
