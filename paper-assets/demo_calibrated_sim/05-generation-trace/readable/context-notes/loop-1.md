# agent / loop_1.md

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`58bb0680c54236738b30.json`](../../sessions/58/58bb0680c54236738b30.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T16:13:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:2 和 cuda:3（gpu_ids=[2,3]），即使 Director 指定白名单外的卡也必须 push back
- vLLM 启动必须三件套：`enforce_eager=True` + `TORCHDYNAMO_DISABLE=1` + `VLLM_USE_V1=0`，缺一个就 defunct
- 单卡 4090D 24GB 无法 bf16 跑 Qwen 7B + DPO ref model，必须 QLoRA 4-bit
- flash_attention_2 不可用，只能用 sdpa
- 部署文件必须同一 ssh 会话内写入 + ssh_read_only 验证，Worker 自报的验证结果不可信（mvp-002/003 教训）
- **24h 死线**：ARR 5/25，DPO 必须出 H-gate 结果。DPO 也 FAIL → MVP KILL

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977（AutoDL），工作目录 /root/democalib/
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，pip/python 在 /root/miniconda3/bin/
- 基础模型：/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct（符号链接，含 `___`）
- DPO 数据：/root/democalib/data/dpo_pairs.jsonl（1434 pairs）
- DPO v2 数据构建脚本：/root/democalib/build_dpo_pairs_v2.py（chat-template 版，备用）
- DPO checkpoint 输出：/root/democalib/results/dpo_checkpoint/
- 活跃进程：dpo-001 训练 PID 170853, tmux=dpo_train, cuda:3, cron 已注册
- cuda:2：vLLM PID 110596 待清理（kill worker 已派但未收到回调）
- HF cache：/root/autodl-tmp/.hf_cache

### 3. 📊 当前状态
刚完成：mvp-004 全 6 variant 数据收集 → registry DONE(negative) + memory.md D004 完整数据表。aave-corpus-gen 标记 killed。dpo-001 注册 RUNNING + cron。tokenizer-fix v2 脚本已就绪。

Registry RUNNING：
- **dpo-001**: QLoRA DPO 训练，cuda:3，1077 steps，上次检查 331/1077 (31%)，loss 0.67-0.70，预计 ~UTC 16:30 完成

等待回调：
- Worker `kill-vllm-cuda2`（清理 cuda:2 残留 vLLM）
- Worker `prepare-hgate-eval`（H-gate 评估脚本准备）
- Cron dpo-001（训练完成检测）

### 4. 📋 待办
- dpo-001 cron 回调（训练完成）→ 检查 rewards/accuracies：>0.6 有效，≤0.55 需用 v2 数据重训
- rewards/accuracies > 0.6 → 用 eval_dpo_model.sh 在 cuda:2 启动 H-gate 评估（合并 LoRA 或 vLLM --enable-lora → 跑 20 tasks → 对比 baseline）
- rewards/accuracies ≤ 0.55 → 用 build_dpo_pairs_v2.py 重建数据（chat-template 格式）→ 重训 DPO
- H-gate 评估完成 → 判定 H2（politeness gap ≥30% reduction）+ H3（completion ≥29.6%）→ 汇报 Director
- H-gate PASS → 进入论文写作阶段
- H-gate FAIL → MVP KILL，汇报 Director 终止项目

### 5. 🎯 战略上下文
- 决策链：D001(MVP 三阶段) → D002(politeness 主维度) → D003(BCP 全线 FAIL, pivot DPO) → D004(BCP 6 variant 完整数据)
- BCP 失败已充分诊断（三个机制：全局抑制/跨维度干扰/过校正反弹），6/6 variants 一致，可作为论文 Section 4.1 negative result
- DPO 是 MVP 最后一条路。核心风险：48% tokenizer mismatch 可能导致训练无效（accuracy ≤0.55），v2 脚本已备好
- 易错点1：vLLM 加载 QLoRA LoRA adapter 可能不支持（需验证 vLLM 0.18.1 兼容性），保险路线是先 merge_lora.py 合并再加载 full model
- 易错点2：H-gate baseline 数据已有（n=19），DPO 评估只需跑校准版，不要重跑 baseline 浪费 GPU 时间
- 易错点3：completion baseline 是 36.8%（不是 37%），H3 阈值是 29.6%（80% × 36.8% = 29.44%，向上取整）


---
