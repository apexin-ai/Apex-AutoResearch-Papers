# code gpt2 new task prep

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpt2-new-task-prep_20260513T081635_result.json`
- **Structured JSON:** [`959c87f30b5b17147227.json`](../../sessions/95/959c87f30b5b17147227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

**选择任务：Factual Recall（国家首都）**

选择理由：
- GPT-2 上有已知电路研究（Meng et al. 2022 ROME/MEMIT），方便文献对比
- 电路结构与已有任务互补——测试 MLP 知识提取路径（IOI 测 name movers，SVA 测 agreement heads，GT 测 year comparison）
- 22 个国家-首都对全部单 token，logit difference 信号强（delta +3.95 ~ +17.62）

**Dry-run 验证结果：**
- 数据生成：462 prompts（22×21 对），格式正确
- 模型加载：GPT-2 Small 12L/12H，cuda:1 正常
- Metric：clean logit diff = +5.03, corrupt = -3.39, delta = +8.42（信号强）
- EAP-IG：32,491 edges scored，top edges 包含 `input→m0`, `a9.h8→logits`（符合知识提取电路预期）

**代码位置：** `/root/min_necessary_circuit_css/run_factual_recall.py`

**运行方法：**
```bash
cd /root/min_necessary_circuit_css && python run_factual_recall.py
```
- 使用 cuda:1，三方法 EAP-IG + Edge Pruning + ACDC，top-100 binarization
- 结果写入 `factual_recall_results.json`
- 中间 cache 文件：`cache_eap_ig_fr.json`, `cache_ep_fr.json`, `cache_acdc_fr.json`

等 Director 确认后可直接运行完整实验。

---
