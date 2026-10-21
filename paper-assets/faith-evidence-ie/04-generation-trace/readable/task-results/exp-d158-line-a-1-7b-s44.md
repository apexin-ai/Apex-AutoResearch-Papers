# exp d158 line a 1 7b s44

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_d158_line_a_1_7b_s44_20260524T083011_result.json`
- **Structured JSON:** [`5a226c1a71492627a8d9.json`](../../sessions/5a/5a226c1a71492627a8d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均已成功启动并注册。

## 提交结果

| 实验 | exp_id | GPU | PID | 显存占用 |
|------|--------|-----|-----|---------|
| **Line A**: 1.7B RSFT s44 候选生成 | `d158_1_7b_rsft_s44_generate` | cuda:0 | 302254 | 6.0 GB |
| **Line B**: 14B SFT s44 训练 | `d158_14b_sft_s44` | cuda:2 | 302391 | 44.7 GB |

**磁盘警告**：可用空间仅 65GB（< 100GB）。当前两个任务可正常运行，但后续 14B RSFT 生成 + 训练可能需要清理空间。可清理候选（不删除，仅列出）包括旧版 rsft_output_ced_s42_v2 (8G)、rsft_output_nli_large (8G)、rsft_output_4b_sft_s44_bf16 (7.5G)、sft_output_14b (7.3G) 等，总计可释放约 80GB+。

**注意**：`submit_training_job` 工具不可用，已用 `ssh_execute` + nohup 替代提交，cron 回调未自动注册，后续步骤需手动触发或另行设置监控。

---
