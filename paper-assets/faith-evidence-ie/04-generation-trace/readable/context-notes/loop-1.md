# director / loop_1.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`dd2d7e6b72389342cd62.json`](../../sessions/dd/dd2d7e6b72389342cd62.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-14T08:44:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- rtx5090-4x 和 gpu-5090-4x-1 是**同一台机器**（D004），只有 4 张 RTX 5090 32GB，不是 8 张。不要尝试在两个"服务器"上并行跑训练
- GPU 白名单：cuda:0-3 on rtx5090-4x。不存在第二台独立服务器
- AutoDL 磁盘：大文件必须放 `/root/autodl-tmp/`，根分区只有 30G
- 模型下载必须用 ModelScope（HF 在 AutoDL 上反复 timeout），已踩过坑
- flash_attn 未装，用 SDPA（attn_implementation="sdpa"）
- QLoRA + ZeRO-3 不兼容（dtype mismatch），只能用 ZeRO-2 + QLoRA
- 用户明确要求 MVP 之后必须 Dream（`dream_simulate(review_mode="full")`），不可跳过

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (connect.bjb2.seetacloud.com:12179)，SSH 密钥认证（~/.ssh/id_ed25519）
- 工作目录：`/root/autodl-tmp/freige/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型：Qwen3-4B → `/root/autodl-tmp/models/Qwen3-4B`（ModelScope 下载）
- SFT checkpoint：`/root/autodl-tmp/sft_output/`（adapter 264MB，eval loss 0.72，token acc 83.5%）
- DeBERTa NLI：`/root/autodl-tmp/.hf_cache/` 下 microsoft/deberta-v3-base
- DocRED 数据：`/root/autodl-tmp/data/docred/`（train 3027 docs, dev 985 docs）
- NLI 预计算 cache：`/root/autodl-tmp/data/docred/train_nli_cache.json`（38180 samples）
- 活跃进程：mvp2_grpo_ced_r1（PID 24122，tmux 运行，cuda:0-3，~step 16/189，ETA ~UTC 16:00）
- Cron 监控：已注册 300s 间隔监控 CED r1
- TRL 版本：1.1.0；vLLM 0.18.1（超出 TRL 支持范围，当前不用 vLLM 所以无影响）

### 3. 📊 当前状态
**MVP-2 GRPO 三路对比进行中**，CED 是第一路。

Registry 状态：
- `mvp1_ced_signal`: DONE/success — margin 0.4827, accuracy 81.5%, r=0.34
- `mvp2_sft_warmup`: DONE/success — eval loss 0.72, token acc 83.5%
- `smoke_test_grpo`: DONE/success — ZeRO-2+QLoRA 功能性通过
- `precompute_nli_train`: DONE/success — 38180 samples, 68.8s
- `mvp2_grpo_ced` (r0): DONE/failed — None 值 bug 崩溃（已修复）
- `mvp2_grpo_ced_r1`: **RUNNING** — step ~16/189, CED reward 0.085→0.427 (5x)，F1 0.008→0.043，format 0.85+，趋势积极
- `mvp2_grpo_flatnli`: PREPARING — 等 CED 完成后串行启动
- `mvp2_grpo_extract`: PREPARING — 等 flat-NLI 完成后启动
- `mvp2_sft_eval`: PREPARING — 等 CED 完成后在间隙执行

已就绪等待部署：
- `eval/inference.py` 440 行，已部署+验证，dry-run 通过
- `run_mvp2_chain.sh` 链式启动脚本正在编写中（Agent Worker）
- flat-NLI 和 extraction-only 的启动命令已验证

### 4. 📋 待办（条件触发式）
- CED r1 完成（cron 回调）→ 立即跑 SFT eval（inference.py, 单卡推理 ~30min）→ 启动 GRPO flat-NLI（4 卡，stage 2）
- flat-NLI 完成 → eval → 启动 GRPO extraction-only（stage 1）
- extraction-only 完成 → eval → 汇总三路对比结果
- 三路对比结果出齐 → 判定 MVP-2 pass criteria：CED Evi-F1 > SFT Evi-F1 ≥ 2pp; F1 > 45; F1 退化 ≤ 5pp
- MVP-2 PASS → `complete_mvp()` → 写 `paper_framing.md` → 写 `experiment_plan.yaml` → `dream_simulate(review_mode="full")` → 更新 ROADMAP（用户明确要求不可跳过 Dream）
- MVP-2 FAIL → 分析原因（截断率？F1 过低？CED 无增益？），决定调参重跑或 pivot
- CED r1 step 30 时 F1 < 0.05 且截断率 > 20% → 考虑停止训练，max_completion_length 提高到 2048 重跑

### 5. 🎯 战略上下文
- 决策链：D001(MVP 设计) → D002(MVP-1 PASS) → D003(smoke test PASS, ZeRO-2+QLoRA) → D004(双 endpoint = 同一机器, 改串行)
- CED r1 训练趋势积极：step 15 CED reward 从 0.085 跳到 0.427，format 85%+，F1 在上升但绝对值仍低(0.043)——F1 是否能涨到可接受水平是 MVP-2 最大不确定性
- 33.4% gold evidence p_pos < τ=0.5（获得 0 CED reward），44.4% 样本无 hard negatives（CED 退化为 flat NLI）——Research 阶段可能需要调 τ 或改进 hard negative 挖掘
- 目标 EMNLP 2026 ARR (May 25) / AAAI 2027 (Aug 1)。串行三路 GRPO ~19.5h，MVP-2 今天内完成是紧凑但可行的
- Human Review 5 条优化建议已记录在 ROADMAP，全部留到 Research 阶段处理
- 易错点：不要再把 gpu-5090-4x-1 当独立服务器派训练任务；grpo_trainer.py 的 `.get()` 已修复但 run_eval.py 已被 inference.py 取代，后续评测统一用 inference.py


---
