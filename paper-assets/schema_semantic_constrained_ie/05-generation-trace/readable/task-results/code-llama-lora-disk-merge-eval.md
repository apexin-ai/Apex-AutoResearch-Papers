# code llama lora disk merge eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_lora_disk_merge_eval_20260515T171955_result.json`
- **Structured JSON:** [`e94c591aaae1d76fbff3.json`](../../sessions/e9/e94c591aaae1d76fbff3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部状态已掌握。汇报如下：

---

### 状态汇报

**1. GPU 状态**
- GPU 0: 17.2 GB used, 90% 利用率（eval 进程占用）
- GPU 1: 空闲

**2. 磁盘状态**
- 根分区: 12G/30G used, **19G 可用** — 无需额外清理
- 两个 merged checkpoint 已软链到数据盘 `/root/autodl-tmp/checkpoints/`

**3. 合并结果** — 已完成
- 4 shards: 4.98GB + 5.00GB + 4.92GB + 1.17GB ≈ **16GB**
- 路径: `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged/`
- 软链: `checkpoints/llama_lora_scierc_merged → /root/autodl-tmp/checkpoints/llama_lora_scierc_merged`

**4. 训练 Metrics**
| Metric | Value |
|--------|-------|
| eval_loss | 0.0595 |
| eval_token_accuracy | 98.17% |
| train_loss | 0.0501 |
| epochs | 3 |
| total_steps | 333 |
| train_runtime | 10:54 |

**5. Unconstrained Eval**
- PID: **287677**, 已运行 **5:30**
- 进度: **158/551 samples (~29%)**
- 输出: `outputs/w5_llama_lora_scierc_unconstrained.jsonl`
- 注意: registry 已被提前标记为 DONE（无法回退），实际进程仍在跑

**6. type_mask_processor.py**
- 399 行, 0 个 cf_fallback — **已是 clean 版本**，无需恢复

---

Registry 已更新完毕。`w5_llama_lora_scierc_constrained_eval` 仍为 PREPARING 状态，等 unconstrained eval 跑完后可提交。预计 eval 还需约 ~13 分钟完成。

---
