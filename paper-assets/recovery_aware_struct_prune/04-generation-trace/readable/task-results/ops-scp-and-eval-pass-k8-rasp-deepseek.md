# ops scp and eval pass k8 rasp deepseek

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp-and-eval-pass-k8-rasp-deepseek_20260516T232326_result.json`
- **Structured JSON:** [`8c22efae3700a4f46831.json`](../../sessions/8c/8c22efae3700a4f46831.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**总结：**

1. **传输完成：** RASP checkpoint (`grpo_stage2_rasp_20_v9`) 已成功传输到 westd-11672（12G model + tokenizer + config，排除了不必要的 checkpoint-10 中的 optimizer）
2. **Standard 传输：** `grpo_stage2_standard_20_v8` 正在后台传输中（PID 653962）
3. **pass@k eval 已启动：** westd-11672 cuda:0 上运行，PID 60022
   - 模型已加载（GPU 0 占用 12,497 MiB）
   - 参数：`--voting --num_samples_per_question 8 --voting_temperature 0.7 --max_samples 200 --seed 42 --max_new_tokens 512`
   - 输出：`/root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_deepseek.json`
   - 日志：`/root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_deepseek.log`
4. **Registry 已更新：** exp_id `eval_pass_k8_rasp_20_grpo_deepseek` 状态 RUNNING

**限制说明：** westb 和 westd 无法直接互通（不同 seetacloud 区域），通过生成临时 SSH 密钥建立了 westb→westd 的 rsync 通道。

---
