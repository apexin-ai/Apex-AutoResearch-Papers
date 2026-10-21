# reviewer / loop_1.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`2ce76234ea8c9e8ceb7d.json`](../../sessions/2c/2ce76234ea8c9e8ceb7d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T08:49:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0,1,2,3（4 张 RTX 5090 32GB）。rtx5090-4x 和 gpu-5090-4x-1 是**同一台机器**（hostname autodl-container-c6024f958a-75d16efa），不能当两台用，不能并行跑两个 GRPO
- GRPO 三路对比必须串行：CED → chain script（SFT eval → CED eval → flat-NLI train+eval → extract-only train+eval）
- NLI 模型 `cross-encoder/nli-deberta-v3-base` 跑在 CPU 上，不占 GPU 显存——这是设计如此，不是 bug
- AutoDL 网络：HF 下载经常超时（日志已出现多次 ReadTimeoutError），模型文件应已缓存本地，新下载需 `source /etc/network_turbo`

### 2. 🖥️ 基础设施快照
- 服务器: rtx5090-4x (root)，工作目录 `/root/autodl-tmp/freige`
- Python: `/root/miniconda3/bin/python`（conda base 环境）
- 模型: Qwen3-4B base 未确认具体路径；SFT adapter `/root/autodl-tmp/sft_output/`；GRPO CED 输出 `/root/autodl-tmp/grpo_s3`
- 数据: `/root/autodl-tmp/data/docred/`；NLI cache `/root/autodl-tmp/data/docred/train_nli_cache.json`（38180 entries, 14MB）
- Chain script: `/root/autodl-tmp/run_mvp2_chain.sh`（6 phases，CED 完成后启动）
- Eval 脚本: `/root/autodl-tmp/freige/eval/inference.py`（440 行，替代旧 run_eval.py）
- 训练日志: `~/runs/faith-evidence-ie/mvp2_grpo_ced_r1.log`
- DeepSpeed config: `/root/autodl-tmp/freige/configs/deepspeed_zero2.json`（ZeRO-2 + CPU offload）
- Accelerate config: `accelerate_4gpu.yaml`（具体路径未确认，在 freige/ 下）

### 3. 📊 当前状态
mvp2_grpo_ced_r1 正在训练，step 18/189（~42 min elapsed，预计还需 ~7h）。4 GPU 全活跃（100%/69%/68%/74%）。

训练趋势（step 5→10→15）：
- format_reward: 0.554 → 0.886 → 0.853（稳定 ~85%+）
- ced_reward: 0.085 → 0.048 → 0.427（step 15 跳升，关注是否持续）
- f1_reward: 0.008 → 0.012 → 0.043（缓慢上升）
- clipped_ratio: 18.1% → 6.9% → 13.8%
- frac_zero_std: 12.5% → 32.5% → 5.0%（step 15 最佳）
- step_time: ~120s → ~155s（step 11+ 变慢，可能因生成长度增加）

Registry:
- RUNNING: mvp2_grpo_ced_r1
- PREPARING: mvp2_sft_eval, mvp2_grpo_flatnli, mvp2_grpo_extract
- DONE: mvp2_sft_warmup(success), mvp2_grpo_ced(failed—None bug), precompute_nli_train(success), smoke_test_grpo(success), mvp1_ced_signal(success)

### 4. 📋 待办
- mvp2_grpo_ced_r1 完成通知 → 核实：(1) checkpoint 存到 /root/autodl-tmp/grpo_s3 (2) 最终 loss/reward 曲线无异常 (3) GPU 合规 (4) registry 更新正确
- run_mvp2_chain.sh 启动 → 核实 Phase 1 SFT eval 配置正确，CUDA_VISIBLE_DEVICES=0
- mvp2_sft_eval 结果出来 → 记录 baseline F1/Evi-F1，这是 MVP-2 gate 的分母
- mvp2_grpo_ced eval (chain Phase 2) 结果 → 与 SFT eval 对比，检查 CED Evi-F1 > SFT Evi-F1 ≥ 2pp 且 F1 > 45
- flat-NLI / extract-only 训练+eval 完成 → 三路对比，确认 CED 优势是否显著
- 任何实验 F1 < 45 或 Evi-F1 退化 → 立即 severity:warning 报 Director

### 5. 🎯 战略上下文
- 核心假设：CED reward 比 flat-NLI reward 更能抗 distractor 句（实体共现干扰），从而产生更好的 evidence grounding
- MVP-1 已 PASS：CED margin 0.48, acc 81.5%，证明 CED 信号存在但有局限（44.4% 样本无 hard negatives → CED 退化为 flat NLI；33.4% gold evidence p_pos < τ=0.5）
- MVP-2 是关键验证：CED GRPO 是否真的在下游 Evi-F1 上超过 SFT baseline ≥ 2pp
- 已修复的关键 bug：grpo_trainer.py 的 None→`.lower()` crash（6 处 .get() 调用），run_eval.py 的 "output"→"raw_text" key mismatch
- 易错点：(1) step_time 从 ~120s 涨到 ~155s 是正常的（生成长度增加），不要误报 (2) HF ReadTimeoutError 是 AutoDL 网络问题，模型已缓存不影响训练 (3) ced_reward step 10 暂降到 0.048 是因为 tau 调度 + 样本方差，step 15 回到 0.427 才是趋势 (4) frac_zero_std=32.5% 在 step 10 偏高但 step 15 恢复到 5%——关注是否稳定
- 发表门槛: Evi-F1 > 57.34 AND F1 > 53——这是最终目标，MVP-2 gate 较宽松（F1 > 45, Evi-F1 差 ≥ 2pp）


---
