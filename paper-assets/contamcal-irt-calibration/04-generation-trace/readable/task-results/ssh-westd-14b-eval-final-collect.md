# ssh westd 14b eval final collect

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-14b-eval-final-collect_20260519T031059_result.json`
- **Structured JSON:** [`548d565e3f7a34d185a4.json`](../../sessions/54/548d565e3f7a34d185a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 14B eval 结果已收集完毕。

## 服务器验证
4× NVIDIA RTX PRO 6000 Blackwell, 各 97887 MiB — 确认正确。

## 14B Eval 结果（全部完成）

| Adapter | MMLU Acc | ARC-Challenge Acc |
|---------|----------|-------------------|
| d000_s42 (base) | 0.7459 (10474/14042) | 0.9352 (1096/1172) |
| d005_s42 | 0.7542 (10591/14042) | 0.9309 (1091/1172) |
| d025_s42 | 0.7577 (10640/14042) | 0.9283 (1088/1172) |
| d050_s42 | 0.7687 (10794/14042) | 0.9283 (1088/1172) |
| d100_s42 | 0.7651 (10744/14042) | 0.9309 (1091/1172) |

## cuda:0 状态
**空闲** — 0MiB 占用，0% 利用率。GPU 1/2/3 各有一个 python 进程在跑。

## Eval 进程
无 eval 相关进程，无 eval_14b tmux session。全部 eval 已完成。

## OLMo-2-1124-7B 模型
**已下载就绪** — config.json 存在，模型文件（6 个 safetensors shards）在 `/root/autodl-tmp/models/OLMo-2-1124-7B/`。

---
