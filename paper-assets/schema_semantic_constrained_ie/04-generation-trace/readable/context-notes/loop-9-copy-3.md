# reviewer / loop_9.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`993d5ddafac1718ad892.json`](../../sessions/99/993d5ddafac1718ad892.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T18:17:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: westd-16980 上 cuda:0 + cuda:1，两卡都可用
- **⚠️ CUDA_VISIBLE_DEVICES 命令覆盖 bug**: submit_training_job 的 `gpu` 字段设 cuda:1，但 spec.command 里硬编码了 `CUDA_VISIBLE_DEVICES=0`，导致内层覆盖外层。当前 w5_qwen_docred_lora_training 实际跑在 GPU 0（nvidia-smi 确认: GPU0=88326/97887MiB@99%, GPU1=0MiB@0%），registry 声称 cuda:1 是错的
- **⚠️ 孤儿进程未清**: PID 294946 (02:04 UTC, 非 tmux) 和 PID 295339 (02:05 UTC, tmux=w5_qwen_docred_lora_training) 两个 `train_lora_docred.py` 同时跑在 GPU 0。Agent 声称 "清理重复进程后重新提交" 但旧进程仍在。训练暂未 OOM（88GB/94GB），但风险高
- **Llama DocRED 训练 (PID 297434) 刚提交到 cuda:0**——如果启动，三个进程抢一张卡，必 OOM。需先 kill 孤儿进程 + 修正 Qwen 训练到 cuda:1 后再启动 Llama
- **W&B 未配置**: 本项目 `WANDB_MODE=disabled`，不检查 wandb 指标
- **数据路径易错**: SciERC 在 `data/processed_data/test.json`（不是 `data/scierc/`），constraints 在项目根 `ontology_constraints.json`

### 2. 🖥️ 基础设施快照
- **服务器**: westd-16980 (root)，工作目录 `/root/schema_semantic_constrained_ie`
- **Python**: `/root/miniconda3/bin/python3` (conda base)，torch 2.10.0+cu128，transformers 4.57.6
- **GPU**: 2× NVIDIA RTX PRO 6000 Blackwell (94GB each)，CUDA 12.8
- **模型路径**:
  - Qwen3-8B: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`
  - Llama-3.1-8B: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
  - Qwen LoRA merged (SciERC): `/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged`
  - Llama LoRA merged (SciERC): `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged`
- **Checkpoints 数据盘**: `/root/autodl-tmp/checkpoints/`（根分区仅 30G）
- **活跃进程**: PID 294946 + PID 295339 (两个 train_lora_docred.py, 都在 GPU 0)，tmux=`w5_qwen_docred_lora_training`
- **Cron**: 无

### 3. 📊 当前状态
**刚完成**: Llama SciERC 2×2 composability matrix (D028)，两模型 SciERC 全部验证完毕。

**RUNNING**:
- `w5_qwen_docred_lora_training`: Qwen DocRED LoRA 训练，36/573 steps (~20s/step)，ETA ~3h。但存在上述双进程 + GPU 错位问题。

**PREPARING**:
- `w5_llama_docred_lora_training`: 刚提交 (PID 297434)，cuda:0。尚未确认是否实际启动。
- `w5_llama_docred_sft_data_gen`: 数据生成已完成 (train=3053, dev=998)，状态未更新为 DONE。
- `w1_cf_fallback_llama_docred` / `w1_cf_fallback_llama_scierc`: 已 killed (D020 analytical finding)。

**Issue Tracker**: 15/16 resolved, W1 in_progress (analytical finding + Paper Agent 写作中)。

**我本轮未发出任何审查报告**——刚收集完状态即触发 handoff。上述 GPU 双进程 + CUDA_VISIBLE_DEVICES 覆盖 bug 是本轮发现的新问题，尚未通过 `reviewer_post_to_director` 上报。

### 4. 📋 待办（条件触发式）
- **立即**: 将 GPU 双进程 + CUDA_VISIBLE_DEVICES 命令覆盖 bug 通过 `reviewer_post_to_director` 上报 Director（severity: critical——两个进程挤 GPU0 且 Llama 训练即将加入，三进程共享一卡必 OOM；GPU1 完全空转）
- Qwen DocRED LoRA 训练完成 → 核实 checkpoint 存在 + loss 收敛 → 等 Agent 跑 unconstrained + constrained eval → 审查 2×2 matrix 数据一致性
- Llama DocRED LoRA 训练完成 → 同上审查
- 全部 4 个 DocRED FT cell 完成 → 审查完整 composability matrix 跨模型一致性 + paper 数字更新
- Paper Agent 提交章节写作审查 → 按 §5 模板审查（注意 composability 数字是否更新到 DocRED FT 结果）
- **DDL 监控**: May 19 内部稿，May 25 EMNLP ARR。剩余 GPU-hours: Qwen DocRED LoRA ~3h + eval ~2h + Llama DocRED LoRA ~3h + eval ~2h ≈ 10h 串行 / 可并行到 ~5h。算力充足，无 deadline 风险。

### 5. 🎯 战略上下文
- **项目核心**: OntoCoDec 两层约束解码（grammar + semantic），编译 IE ontology 为 token-level constraints
- **决策链**: D001(EMNLP) → D003(MVP GO) → D006(SciERC核心结果) → D014(tightness×RV双因素) → D020(CF analytical) → D025/D028(composability confirmed)
- **Composability 覆盖**: SciERC 2×2 两模型✅，DocRED 2×2 两模型 FT 行 pending——这是最后的实验数据
- **下一个"我"最容易判断错的事**:
  1. Registry 声称 GPU 分配 ≠ 实际 GPU 使用。必须 ssh nvidia-smi 独立核实，不信 registry.spec.gpu 字段
  2. Agent 说"清理了重复进程"但 ps aux 可能仍有孤儿——kill_job 不杀子进程是已知问题
  3. CF violation 是 known limitation (D020 analytical finding)，不是未解决 bug——不要作为 critical 打回
  4. ET 计数口径已改（D011，每 entity 只计 1 次），旧数字（DocRED ET=8.18%）已废弃，新口径 ET=2.48%
  5. W&B 不可用（WANDB_MODE=disabled），指标交叉验证只能靠 log 文件 + registry


---
