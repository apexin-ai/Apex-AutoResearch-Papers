# exp plan 021 instruct model

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_021_instruct_model_20260517T153626_result.json`
- **Structured JSON:** [`9ae1b4c6b6c7823e61ad.json`](../../sessions/9a/9ae1b4c6b6c7823e61ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

446/5000 d0 samples 完成，GPU 1 稳定运行 (4187 MiB, 47%)。

总结执行情况：

**Plan_021 Qwen2.5-1.5B-Instruct 验证实验 - 已启动运行**

完成的操作：
1. **清理**：杀掉 2 个孤立的重复 pipeline 进程，保留 tmux session `qwen25-1p5b-instruct-001`
2. **修复 pipeline**：
   - `generate_d0` 和 `generate_next_depth` 从 BOS-seeded 改为 **chat template** 生成 (`apply_chat_template` + "Write a passage about a random topic.")
   - 添加 `repetition_penalty=1.0, top_k=0` 覆盖 Qwen 默认的 generation_config，确保与 base model 实验一致 (仅用 nucleus p=0.95, temp=1.0)
3. **模型下载**：aria2c 下载完成 (Qwen2.5-1.5B-Instruct, 2.9GB)
4. **Pipeline 运行中**：PID 795692, cuda:1, 当前 d0 生成 ~446/5000

**预计总时长**：~4-5 小时（d0-d3 生成 + 3x LoRA finetune + feature extraction + classification）

**关键配置**：
- exp_id: `qwen25-1p5b-instruct-001`
- tmux session: `qwen25-1p5b-instruct-001`
- GPU: cuda:1 (RTX PRO 6000 Blackwell, 98GB VRAM)
- 结果路径: `/root/autodl-tmp/recursive_gen_depth_est/results/qwen25_1.5b_instruct/summary.json`

---
