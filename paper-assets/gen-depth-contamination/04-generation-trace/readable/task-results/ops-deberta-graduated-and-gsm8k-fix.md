# ops deberta graduated and gsm8k fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deberta_graduated_and_gsm8k_fix_20260520T192259_result.json`
- **Structured JSON:** [`1dbbdc1031d068467fbd.json`](../../sessions/1d/1dbbdc1031d068467fbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务状态总结：

## 修复 1：deberta_graduated

已成功提交到 cqa1 cuda:1（PID 359411）。训练进行中：373/825 steps (45%)，约 2.5 it/s，预计 ~8 分钟后完成训练+eval。

注意修正了两个原始命令中的问题：
- `--gpu 1` → `--device cuda:0`（脚本只接受 `--strategy`/`--device`/`--seed`/`--skip_eval`）
- 因为 `submit_training_job` 设置 `CUDA_VISIBLE_DEVICES=1`，物理 GPU 1 映射为 cuda:0

## 修复 2：GSM8K 401 问题

**根因**：lm_eval 下载 `openai/gsm8k` 时走了 xethub 后端（`cas-server.xethub.hf.co`），返回 401 Unauthorized。3 次重试均失败，所有 eval JSON 中 gsm8k 记为 null。

**已完成**：
- GSM8K 数据已用 `HF_HUB_DISABLE_XET=1` + `HF_ENDPOINT=https://hf-mirror.com` 预下载缓存（1319 test examples）
- Arrow 缓存已复制到 HF_HOME 路径下

**GSM8K 补跑方案**（当前实验完成后执行）：
1. 当前 expanded_downstream_eval 仍在运行（已完成 6/10 模型，GPU 0），进程内未设 `HF_HUB_DISABLE_XET=1`，剩余模型的 GSM8K 仍会失败
2. 等当前实验跑完后，删除所有 `*_eval.json`
3. 用 `HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com` 重跑
4. 预计耗时 ~30-40 分钟（10 个模型重新训练+全 benchmark eval）

---
