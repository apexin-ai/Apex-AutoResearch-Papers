# ssh registry sync and gpu status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_registry_sync_and_gpu_status_20260521T174429_result.json`
- **Structured JSON:** [`78f4214fd17bf08c933a.json`](../../sessions/78/78f4214fd17bf08c933a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。汇总如下：

---

## Part 1: 实验指标汇总

| exp_id | dataset | greedy_f1 | oracle_f1 | mv_f1 | degen | n | file_size | lines | server | path |
|--------|---------|-----------|-----------|-------|-------|---|-----------|-------|--------|------|
| **scierc_n16_s456** | SciERC | 0.6641 | 0.8076 | 0.6643 | 0.070 | 529 | 35.7MB | 551 | 5090-c | `output/scierc_n16_s456/` |
| **e2_pretrained_conll_s42** | CoNLL | 0.5363 | 0.6299 | 0.6284 | 0.359 | 2756 | 111.1MB | 3453 | 5090-c | `output/e2_pretrained_conll_s42/` |
| **e2_pretrained_conll_s123_v2** | CoNLL | 0.5364 | 0.6257 | 0.6321 | 0.365 | 2756 | 111.2MB | 3453 | 5090-c | `output/e2_pretrained_conll_s123_v2/` |
| **e2_pretrained_scierc_s42_v2** | SciERC | 0.2434 | 0.3888 | 0.2618 | 0.009 | 529 | 38.1MB | 551 | 5090-c | `output/e2_pretrained_scierc_s42_v2/` |
| **scierc_n16_s42** | SciERC | 0.6631 | 0.8086 | 0.6607 | 0.070 | 529 | 35.6MB | 551 | 5090-c | `output/scierc_n16_s42/` |

关键观察：
- **e2_pretrained_scierc_s42_v2** 表现极差（greedy_f1=0.24, 46% samples F1=0），report 标记 FAIL + 警告建议用 T=0.7 重跑
- **e2_pretrained_conll** 两个 seed 的 degeneracy 很高（~0.36），说明 Qwen2.5-7B pretrained 在 CoNLL 上采样多样性不足
- **scierc_n16** 两个 seed（s42, s456）指标一致（greedy~0.664, oracle~0.808, degen=0.07），fine-tuned 模型质量稳定

---

## Part 2: GPU 状态

### autodl-5090-c — 全部空闲
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0-3 | RTX 5090 | 0% | 0/32607 MiB |

无 tmux session，无 Python 进程。

### autodl-5090 — 2 个 GPU 在跑
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX 5090 | 68% | 30152/32607 MiB |
| 1 | RTX 5090 | 0% | 空闲 |
| 2 | RTX 5090 | 0% | 空闲 |
| 3 | RTX 5090 | 48% | 29946/32607 MiB |

活跃进程：
- **GPU 0**: `fewnerd_n16_s456` — qwen3-8b-fewnerd-exp021-merged, N=16, seed=456
- **GPU 3**: `e2_pretrained_fewnerd_s456` — Qwen2.5-7B-Instruct pretrained, FewNERD, N=8, seed=456

GPU 1, 2 空闲可用。18 个 tmux session（多数为旧任务残留）。

---

## Part 3: FewNERD 训练配置

找到 3 个 FewNERD 训练配置：

### `train_config_fewnerd.yaml` — 原始 1-epoch smoke test
- base: Qwen3-8B, LoRA r=16 alpha=32, lr=2e-4, 1 epoch, batch=2×8

### `train_config_fewnerd_exp021.yaml` — 3-epoch（用于 exp021）
- base: Qwen3-8B, LoRA **r=32 alpha=64**, lr=2e-4, **3 epoch**, batch=2×8
- output: `output/exp_021_fewnerd_full`
- 已合并为 `checkpoints/qwen3-8b-fewnerd-exp021-merged/`

### `train_config_fewnerd_5epoch.yaml` — 5-epoch（已有）
- 与 3-epoch 完全一致，仅 `num_train_epochs: 5.0`
- output: `checkpoints/qwen3-8b-fewnerd-5epoch-lora`
- **checkpoint 已存在**，adapter_config 确认 r=32 alpha=64

5-epoch FewNERD 模型已经训练完成，checkpoint 在 `checkpoints/qwen3-8b-fewnerd-5epoch-lora/`。

---
