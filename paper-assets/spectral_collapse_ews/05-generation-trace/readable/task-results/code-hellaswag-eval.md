# code hellaswag eval

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hellaswag_eval_20260516T090120_result.json`
- **Structured JSON:** [`37407a28e385dc33b107.json`](../../sessions/37/37407a28e385dc33b107.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇报

| 指标 | 值 |
|------|------|
| **acc_norm** | **0.4130** |
| acc | 0.3450 |
| acc_norm_stderr | 0.0049 |
| acc_stderr | 0.0047 |

- **模型路径**: `/root/spectral_collapse_ews/checkpoints/gen_0`
- **评估耗时**: 94.4 秒（含模型加载）
- **结果文件**: `/root/spectral_collapse_ews/results/hellaswag_gen0/results.json`
- **批量脚本**: `/root/spectral_collapse_ews/eval_hellaswag.sh`（用法: `bash eval_hellaswag.sh 0 10 cuda:1`）

注：Pythia-410M-deduped 的 HellaSwag acc_norm ~0.413 与公开基准一致。数据集因 AutoDL 网络限制需通过代理获取 HF 重定向 URL 后直连 xet CDN 下载，已缓存到 `/root/.cache/huggingface/hellaswag_manual/`，批量脚本可离线复用。

---
