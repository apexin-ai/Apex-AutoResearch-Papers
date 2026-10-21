# ops emergency disk cleanup

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency_disk_cleanup_20260517T080329_result.json`
- **Structured JSON:** [`890506f4346b0eff4ed9.json`](../../sessions/89/890506f4346b0eff4ed9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理前
磁盘: 250G/250G used (1.2M 可用)

## 已清理
| 目录 | 大小 |
|------|------|
| grpo_ced_lr5e6/ | 6.8G |
| grpo_ced_kl001/ | 7.8G |
| merged_sft_rsft_ced_s43/ | 7.6G |
| .hf_cache/ | 2.2G |
| 8个空目录 | 0 |
| **总计** | **24.4G** |

## 清理后
磁盘: 226G/250G used, **25G 可用** (91%)

dpo_output / dpo_output_1ep / dpo_data 在服务器上不存在，跳过。

两个正在运行的 eval（rsft_s44_dev_eval_preds 97%、1.7B eval 74%）现在有足够空间写出 predictions.json。

## 仍需 Director 审批的大目录

如果后续还需更多空间，以下目录值得考虑：

| 目录 | 大小 | 说明 |
|------|------|------|
| rsft_topk3_output/ | 8.0G | 旧 topk3 实验 |
| rsft_output_s43/ | 8.0G | 旧 seed 43（ced_s43 已单独保留） |
| rsft_output_flat_nli_s45/ | 8.0G | flat_nli 系列 |
| rsft_output_flat_nli_s44/ | 8.0G | flat_nli 系列 |
| rsft_output_flat_nli_s43/ | 8.0G | flat_nli 系列 |
| rsft_output_flat_nli/ | 8.0G | flat_nli 系列 |
| rsft_output/ | 8.0G | 最早的 RSFT |
| rsft_output_r2a/, r2b/ | 13.0G | round 2 variants |

---
