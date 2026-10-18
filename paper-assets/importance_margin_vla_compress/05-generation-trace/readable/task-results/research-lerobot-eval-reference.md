# research lerobot eval reference

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lerobot_eval_reference_20260516T122703_result.json`
- **Structured JSON:** [`137229309a781aa2e6f9.json`](../../sessions/13/137229309a781aa2e6f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是核心结论：

---

## 调研结果

### 1. eval pipeline 没有遗漏关键步骤
逐项对比了我们的 `eval_success_rate.py` 和 LeRobot 官方实现：
- obs 图像处理、state 处理、language tokens、image key 映射——全部一致
- `adapt_to_pi_aloha=False`（SmolVLA base config），不需要 gripper 转换
- normalization：因为我们训练时直接调 `policy.forward()` 而不走 processor pipeline，训练和推理都在**原始空间**，不需要 normalize/unnormalize
- action chunk 执行方式：n_action_steps=50=chunk_size，我们的方式与官方等价

### 2. 0% success 的根因是 **LoRA fine-tuning 导致 flow matching mode collapse**
已在 `sim_rollout_diagnosis.md` 中有完整诊断。LoRA finetune 后模型 ODE 从任意噪声收敛到同一个固定点（近似 dataset mean action），完全忽略图像输入。Action std 从 pretrained 的 0.104 降至 0.006。

### 3. SmolVLA 在 aloha_sim_insertion 上 finetune 是已知难题
- GitHub issue [#2700](https://github.com/huggingface/lerobot/issues/2700) 报告了同样的训练不收敛问题
- SmolVLA 没有在 aloha sim 上的官方 benchmark 结果（只在 LIBERO 上验证了 87.3%）
- 预训练 SmolVLA base 在 insertion 上也是 0%（已验证，符合预期——它没在此任务上训练过）

### 4. Reference success rates
- ACT 在 aloha_sim_insertion 上：~20-50%
- SmolVLA 在 LIBERO 上：~87%（官方数据）
- SmolVLA 在 aloha_sim_insertion 上：无官方数据，社区报告训练不收敛

完整报告已写入 `eval_results/lerobot_eval_investigation.md`。

---
