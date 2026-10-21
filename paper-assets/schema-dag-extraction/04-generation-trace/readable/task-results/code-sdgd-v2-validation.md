# code sdgd v2 validation

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sdgd-v2-validation_20260515T133921_result.json`
- **Structured JSON:** [`9872f5dafa42c519a48e.json`](../../sessions/98/9872f5dafa42c519a48e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。**SDGD v2 代码就绪，无 bug。**

审查结果摘要：

| 检查项 | 状态 |
|--------|------|
| 脚本存在且可执行 | ✅ |
| Python imports 正确 | ✅ |
| vLLM 参数 (enforce_eager, max_model_len=4096, gpu_mem=0.95) | ✅ |
| 模型路径 | ✅ |
| 数据路径 (test.parquet, 4.8MB) | ✅ |
| sim_matrix.pt | ✅ |
| min_batch_size 逻辑 | ✅ 8 batches [18,12,11,7,7,5,3,3] → 4 batches [19,18,15,14] |
| Confidence merge (logprobs=1, cumulative_logprob/n_tokens, threshold=-1.0) | ✅ |
| `cumulative_logprob` 属性兼容 vLLM 0.20.2 | ✅ 确认在 CompletionOutput 中 |
| 冲突解决：同 span 不同 type → 保留最高 confidence | ✅ 有意设计，抑制 FP |
| Stage 1 decomposition 已完成 | ✅ 4 个 JSON 已生成 |
| 输出写入 artifacts/exp008_v2/ | ✅ |
| Logging 充分 | ✅ |

**预估运行时间**：~4 小时（single_pass 30min + sdgd_zero 45min + random_batch 45min + per_type 2h）

**提交命令**：
```bash
cd /root/schema-dag-extraction && nohup bash scripts/run_sdgd_v2_fewnerd.sh > artifacts/exp008_v2_run.log 2>&1 &
```

验证报告已写入 `artifacts/sdgd_v2_validation.json`。

---
