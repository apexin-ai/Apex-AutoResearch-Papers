# ops check llama rsft test result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_llama_rsft_test_result_20260517T183717_result.json`
- **Structured JSON:** [`8ac2f4932bf185f06af6.json`](../../sessions/8a/8ac2f4932bf185f06af6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**LLaMA RSFT test predictions 完成。**

| 项目 | 值 |
|---|---|
| 状态 | 成功 |
| 文档数 | 1000 |
| 预测数 | 27,918 |
| CodaLab 条目 | 25,773 |
| 格式正确率 | 99.8% (998/1000) |
| 截断率 | 792/1000 |
| 推理耗时 | 2h58m (10.73s/doc) |
| predictions 文件 | `/root/autodl-tmp/eval_results/plan_006_llama_rsft_test/predictions.json` (8.0MB) |
| CodaLab 提交文件 | `/root/autodl-tmp/eval_results/plan_006_llama_rsft_test/codalab_submission.json` (2.2MB) |

CodaLab 提交文件已就绪，可直接上传评测。截断率 79.2% 较高，与 dev 评估一致（max_new_tokens=1024 对长文档不够）。

---
