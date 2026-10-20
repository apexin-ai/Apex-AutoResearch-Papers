# ops urgent temp cleanup

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_temp_cleanup_20260519T072526_result.json`
- **Structured JSON:** [`e8852d7642d3085859aa.json`](../../sessions/e8/e8852d7642d3085859aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。报告：

### 结果

| 项目 | 删除前 | 删除后 |
|------|--------|--------|
| 磁盘已用 | 30G (99%) | 16G (51%) |
| 可用空间 | 515M | **15G** |

### 删除内容
1. **杀掉了 PID 45803** — 一个正在运行的 `snapshot_download('LLM-Research/Meta-Llama-3.1-8B-Instruct')` 进程，正在实时吞噬磁盘（这是空间骤降到 515M 的原因）
2. `/root/.cache/modelscope/hub/models/._____temp/` — 8.1G（Llama 旧下载残留）
3. `/root/.cache/modelscope/hub/models/LLM-Research/` — 1.1G（Llama 部分下载）
4. `/root/.cache/huggingface/datasets/HuggingFaceH4___ultrachat_200k/` — 2.9G（训练用的是 `data/ultrachat_8k` 本地副本，此缓存冗余）

### 剩余缓存
- `modelscope/Qwen/Qwen2.5-7B-Instruct` — 15G（LoRA 训练的 base model，**不可删**）
- `pip` — 92M
- HF hub — 12K（空）

### 可用空间：15G >= 17G？
**否，15G < 17G。** 差 2G。若需达到 17G，可选清理 pip 缓存（92M，杯水车薪）或 miniconda 中的无用包（`conda clean --all` 可能释放数百 MB）。但 15G 对 LoRA-only 训练已充裕。

### LoRA 训练状态
正常运行中：`phase2_lora_only_s42`，GPU 利用率 99%，显存 88.9 GiB。

---
