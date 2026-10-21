# ssh 7b zs inference 5090c

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_7b-zs-inference-5090c_20260520T064018_result.json`
- **Structured JSON:** [`cd101452e498c7b79058.json`](../../sessions/cd/cd101452e498c7b79058.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**关键发现：GPU 2,3 无法释放。**

PID 155544 (vLLM) 已经不存在了（kill 之前就已经退出）。当前占用所有 4 块 GPU 的是 **Qwen2.5-32B FewNERD seed42 训练**（LlamaFactory 分布式，PID 804665-804668），配置文件 `train_config_qwen25_32b_fewnerd_s42.yaml`。

现状汇总：

| 项目 | 状态 |
|------|------|
| vLLM PID 155544 | 早已退出，不是 GPU 占用原因 |
| GPU 0-3 | 全部被 Qwen2.5-32B FewNERD 训练占满（每卡 ~30GB） |
| Qwen2.5-7B base 模型 | 不存在，需下载（/root/autodl-tmp/models/ 只有 Qwen3-4B） |
| 推理脚本 | `code/run_mvp_pilot.py`，支持 `--model_path`/`--dataset fewnerd`/`--n_samples 8`/`--seed`/`--use_train_format false`（ZS 应关闭 train format） |

**无法启动 7B ZS inference**——没有空闲 GPU。需要你决定：

1. **等 32B 训练完成**后再跑 7B ZS（训练还需多久可以查 wandb/log）
2. **Kill 32B 训练**腾出 GPU 2,3（但会丢失训练进度）
3. 先只做模型下载，推理等 GPU 空闲后再启动

要我查一下 32B 训练的进度/预计完成时间吗？

---
