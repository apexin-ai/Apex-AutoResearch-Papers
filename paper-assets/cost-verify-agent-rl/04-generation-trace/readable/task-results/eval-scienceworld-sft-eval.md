# eval scienceworld sft eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_scienceworld_sft_eval_20260519T175037_result.json`
- **Structured JSON:** [`18beb2851855b596d2b6.json`](../../sessions/18/18beb2851855b596d2b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

每个 episode 约 63s，第 2 个正在进行中。1796 episodes x 63s = ~31 小时。这是一个很长的 eval。

当前状态总结：

**已完成**：
- Checkpoint 传输：westd → bjb1 完成，所有 13 个文件大小完全一致
- Eval 已启动：PID=183712，bjb1 上运行中

**Eval 详情**：
- 模型：Qwen3ForCausalLM（config 显示 hidden_size=2048, 28 layers）
- 设置：dev split, 1796 episodes, 30 task types, T=0.4, TP=2, max_model_len=32768
- 第 1 个 episode：FAIL(score=3), valid=1%, fmt=61%, 100 steps, 63.4s
- 预计运行时间：~31 小时（每 episode ~63s）

**注意事项**：
- valid=1% 和 fmt=61% 比较低，说明模型生成的动作大多不在有效动作列表中。需要更多 episodes 才能判断整体表现
- tokenizer 有个 Mistral regex 警告，但不影响 Qwen3 模型
- 建议后续用 `tail -20 /tmp/eval_scienceworld.log` 查看进度
- 结果 JSON 将保存在 `/root/autodl-tmp/checkpoints/scienceworld_sft/eval_results_dev.json`

要继续监控还是等运行完毕后再查看结果？

---
