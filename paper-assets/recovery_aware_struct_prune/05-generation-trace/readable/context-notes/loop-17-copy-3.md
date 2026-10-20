# reviewer / loop_17.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`2123e9ade80c47be8bed.json`](../../sessions/21/2123e9ade80c47be8bed.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-21T19:19:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C005：westd cuda:0-3，westb cuda:0-1。越界即 CRITICAL + kill
- westd 数据盘 `/root/autodl-tmp` 反复爆满（619G），训练任务必须加 `save_total_limit=1`，提交前 `df -h` 确认空间
- `eval_math500.py` 的 `--output_path` 必须是文件路径不是目录，否则 IsADirectoryError（line 230 已修但旧调用可能残留）
- `train_sft_warmup.py` 的 TRL 版本不支持 `max_seq_length`（已修为兼容写法），pipeline 脚本 `run_alpha4_pipeline.sh` 的 SFT 步骤可能仍用旧参数
- MATH-500 评估统一用 `--max_new_tokens 2048`（D097），不是默认 4096

### 2. 🖥️ 基础设施快照
- **westd-29022** (root)：工作目录 `/root/recovery_aware_struct_prune`，数据盘 `/root/autodl-tmp`（清理后 ~345G/619G, 275G 可用）
  - Python: `/root/miniconda3/bin/python`，conda base 环境
  - 模型存储: `/root/autodl-tmp/recovery_aware_struct_prune/`（sft_*, grpo_*, pruned_*）
  - 日志: `/root/runs/recovery_aware_struct_prune/`（根分区，25G 空余）
- **westb-23072** (root)：同结构，数据盘未爆
- W&B: 项目级配置（未在本 session 验证 entity/project）
- HF cache: westd `/root/.cache/huggingface/`（根分区）

### 3. 📊 当前状态

**RUNNING 实验**（registry）：
| 实验 | 服务器 | GPU | 进度 | 备注 |
|------|--------|-----|------|------|
| eval_math500_grpo_random_20_v2 | westd | 1 | ~35% (176/500) | ETA ~6h from 18:00 UTC |
| eval_math500_sft_random_20 | westd | 3 | ~28% (140/500) | ETA ~9h from 18:00 UTC |
| eval_math500_grpo_standard_25_v2 | westb | 0 | ~44% (222/500) | ETA ~4.7h from 18:00 UTC |
| eval_math500_sft_standard_25 | westb | 1 | ~27% (135/500) | ETA ~7h from 18:00 UTC |
| grpo_alpha4_20 | westd | 2 | 刚提交 | GRPO v5 config 已核对一致 |

**刚完成**：
- sft_alpha4_20_v2 成功（2 epochs, 936 steps, 模型存 `/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20/`）
- eval_math500_grpo_cka_only_25_v2: 18.4%（92/500）✅ 入 registry
- eval_math500_sft_cka_only_25_v2: 19.2%（96/500）✅ 入 registry

**westd GPU 0 空闲**，无任务分配。

### 4. 📋 待办（条件触发式）
- grpo_alpha4_20 完成 → 验证 GRPO v5 config 一致性 + GSM8K/MATH-500 eval 提交 + 检查 RASP α=4.0 是否 collapse（reward=0.008 级别 = passive failure）
- eval_math500_grpo_standard_25_v2 完成（最快到的）→ 核对 C1 decoupling：Δ(GRPO-SFT) 应在 ±2pp 内（SFT=13.0% v1 采用）
- eval_math500_sft_random_20 + grpo_random_20_v2 都完成 → 构建 Random 20% MATH-500 行，验证 C1 + CKA>Standard>Random 排序
- 4 个 MATH-500 全部完成 → 汇总完整 MATH-500 @2048 表格，与 GSM8K 交叉验证排序一致性
- Director 回复 Round 5 Action Matrix audit → 跟踪 Paper Agent 执行（特别是 Q5 Dense GRPO MATH-500 = -4.6pp 的处理）

### 5. 🎯 战略上下文
- **C1 Decoupling 是核心结论**：GRPO reward-accuracy decoupling 普遍成立，recovery capacity 在剪枝时锁定、SFT 固化、GRPO 无法改变。所有已完成数据点 Δ(GRPO-SFT) 在 ±2pp 内
- **但 C1 有裂缝**：Dense GRPO 在 MATH-500 上 -4.6pp（69.0% vs 73.6% SFT），意味着 Dense 模型 GRPO 也可能"退化"——这不是"剪枝锁定"独有现象。Round 5 审稿 Q5 攻击面，需要在论文中 qualify
- **15% 是 CKA lead example 但单 seed**：15% CKA GRPO GSM8K = 72.25%（超越 dense SFT 71.71%），是最强 claim 支撑，但只有 1 个 seed。已提 warning 给 Director
- **α=4.0 是 RASP collapse 诊断实验**：如果 α=4.0 RASP 仍 collapse（reward ≈ 0），说明 RASP 在高 sparsity 下系统性失败；如果恢复了，说明 α=2.0 是超参问题。对论文 narrative 影响大
- **易错点**：
  - registry 中 `eval_math500_sft_standard_25` 状态是 RUNNING 但实际用的 v1 数据（13.0%，Director 批准采用），westb GPU 1 上跑的是新的 v2 rerun
  - 不要把 `/root/runs/` 下的日志目录当文件读——有些 eval 的日志在子目录里（如 `eval_math500_grpo_random_20_v2/eval_math500_grpo_random_20_v2.log`），有些直接是 `.log` 文件
  - westd 磁盘随时可能再爆，每次训练任务前必须检查


---
