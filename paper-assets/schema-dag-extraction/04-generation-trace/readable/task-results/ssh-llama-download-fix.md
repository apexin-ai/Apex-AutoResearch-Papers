# ssh llama download fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama-download-fix_20260515T083106_result.json`
- **Structured JSON:** [`c1643b930a70ce2bd684.json`](../../sessions/c1/c1643b930a70ce2bd684.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。汇总：

**模型完整性验证**
- Model: `llama`, hidden_size=8192, num_layers=80
- Vocab: 128,000
- **Shards: 15/15** — 全部来自 nvidia/Llama-3.3-70B-Instruct-FP8
- Total size: **72.7GB**

**已完成操作**
1. 杀掉了所有冲突的下载进程（7+ 个）
2. 确认无 neuralmagic 污染 — 所有分片大小一致，符合 nvidia repo 模式
3. 从 hf-mirror.com 下载了缺失的 3 个分片（005, 007, 015），绕过 xet bridge
4. 清理了根分区（删除 `/tmp/plan_a_integration_test/` 等）腾出空间
5. transformers AutoConfig/AutoTokenizer 验证通过
6. 已 kill 残留的 wget 父进程

**磁盘空间**
| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/root/autodl-tmp/` (数据盘) | 250G | 210G | 41G | 84% |
| `/` (根分区) | 30G | 14G | 17G | 45% |

---
