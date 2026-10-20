# diagnose eval math500 sft cka only 20 fixed

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_cka_only_20_fixed_20260523T150554_result.json`
- **Structured JSON:** [`a38eff128f4d1dc805a6.json`](../../sessions/a3/a38eff128f4d1dc805a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**失败原因：模型目录不存在。**

`/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/` 在 westd-32935 上不存在。Tokenizer 加载时立即报 `OSError`，进程退出。

日志中的关键错误：
```
OSError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': 
'/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20'
```
这是 transformers 在本地路径找不到 `config.json` 后、尝试当作 HF repo id 解析失败的报错（加上 `HF_HUB_OFFLINE=1` 禁止了远程下载）。

**该服务器上存在的 `sft_cka_only_*` 模型：**
- `sft_cka_only_15`
- `sft_cka_only_20_floor_0.3`
- `sft_cka_only_20_floor_0.5`
- `sft_cka_only_20_floor_0.6`
- `sft_cka_only_25`

没有不带 floor 后缀的 `sft_cka_only_20`。

**修复方案：**
1. 如果目标是评估某个 floor 变体，改用已有路径，例如 `sft_cka_only_20_floor_0.5`
2. 如果确实需要 `sft_cka_only_20`（无 floor），需先运行对应的 SFT 恢复训练生成该 checkpoint

---
