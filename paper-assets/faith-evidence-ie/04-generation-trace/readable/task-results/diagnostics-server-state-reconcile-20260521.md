# diagnostics server state reconcile 20260521

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostics_server_state_reconcile_20260521_20260521T231942_result.json`
- **Structured JSON:** [`f70d809199ffad290046.json`](../../sessions/f7/f70d809199ffad290046.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 服务器状态报告 (rtx5090-4x, 2026-05-22 ~07:20 UTC)

### 1. GPU 占用表

| GPU | 显存占用 | 利用率 | PID | 实验 |
|-----|---------|--------|-----|------|
| 0 | 6,071 / 97,887 MiB (6%) | 51% | 140534 | test_eval_1_7b_sft_s42 |
| 1 | 32,503 / 97,887 MiB (33%) | 91% | 125323 | test_eval_14b_sft_s42 |
| 2 | 94,451 / 97,887 MiB (97%) | 99% | 142872 | rsft_trainer rsft-ced-s42-v2 |
| 3 | 32,503 / 97,887 MiB (33%) | 91% | 143166 | test_eval_14b_sft_s42_no_evi |

### 2. PID 存活表

**Registry 标记 RUNNING 的 PID（全部已死）：**

| PID | 实验 | 状态 |
|-----|------|------|
| 97434 | test_eval_14b_rsft_s42 | DEAD — 实验已完成 |
| 95606 | eval_llama_rsft_s42_no_evi_2048 | DEAD — 实验已完成 |
| 93402 | d140_4b_sft_s42_with_evi_2048 | DEAD — 实验已完成 |
| 87302 | d140_8b_sft_s42_no_evi_2048_fix | DEAD — 实验已完成 |
| 87382 | d140_1_7b_sft_s42_no_evi_2048_fix | DEAD — 实验已完成 |
| 88987 | d140_4b_sft_s42_no_evi_2048_fix | DEAD — 实验已完成 |

**Cron 追踪的 PID：**

| PID | 实验 | 状态 |
|-----|------|------|
| 125321 | test_eval_14b_sft_s42 (bash wrapper) | ALIVE, 已运行 4h47m |
| 140534 | test_eval_1_7b_sft_s42 | ALIVE, 已运行 30m |

**不在 registry 中的新进程：**

| PID | 实验 | 启动时间 | GPU |
|-----|------|---------|-----|
| 142872 | rsft_trainer rsft-ced-s42-v2 | 07:14 | cuda:2 |
| 143166 | test_eval_14b_sft_s42_no_evi | 07:14 | cuda:3 |

### 3. 已完成实验（registry 未更新）

**Dev set 实验：**

| 实验 | 模型 | no_evi | ign_F1 | F1 | evi_f1_joint | 完成时间 |
|------|------|--------|--------|-----|-------------|---------|
| d140_1_7b_sft_s42_no_evi_2048_fix | Qwen3-1.7B | yes | 0.4233 | 0.4436 | — | May 21 17:31 |
| d140_4b_sft_s42_no_evi_2048_fix | Qwen3-4B | yes | 0.4016 | 0.4095 | — | May 21 17:50 |
| d140_8b_sft_s42_no_evi_2048_fix | Qwen3-8B | yes | 0.5019 | 0.5227 | — | May 21 18:29 |
| d140_4b_sft_s42_with_evi_2048 | Qwen3-4B | no | 0.3946 | 0.4033 | 0.3129 | May 21 19:32 |
| eval_llama_rsft_s42_no_evi_2048 | Llama-3.1-8B RSFT | yes | 0.5559 | 0.5703 | — | May 21 22:01 |

**Test set 实验：**

| 实验 | 模型 | F1 | ign_F1 | evi_f1_joint | 完成时间 |
|------|------|-----|--------|-------------|---------|
| test_eval_14b_rsft_s42 | Qwen3-14B RSFT | 0.3849 | 0.3849 | 0.2688 | May 21 23:26 |
| test_eval_4b_sft_s42 | Qwen3-4B SFT | 0.2232 | 0.2232 | 0.1640 | May 22 06:46 |
| test_eval_8b_sft_s42 | Qwen3-8B SFT | 0.3106 | 0.3106 | 0.2279 | May 22 07:02 |
| test_eval_llama_sft_s42 | Llama-3.1-8B SFT | 0.3420 | 0.3420 | 0.2409 | May 22 07:09 |

### 4. 正在运行实验

| 实验 | PID | GPU | 进度 | 速度 | 预计完成 |
|------|-----|-----|------|------|---------|
| test_eval_14b_sft_s42 | 125323 | cuda:1 | 421/500 (84%) | ~45s/it | **~08:20** |
| test_eval_1_7b_sft_s42 | 140534 | cuda:0 | 73/500 (15%) | ~26s/it | **~10:20** |
| test_eval_14b_sft_s42_no_evi | 143166 | cuda:3 | 9/500 (2%) | ~35s/it | **~12:00** |
| rsft_trainer rsft-ced-s42-v2 | 142872 | cuda:2 | 81/510 (16%) | ~4.6s/step | **~07:53** |

### 5. 异常发现

1. **Registry 严重过期**：6 个标记为 RUNNING 的 PID 全部已死，对应实验早已完成（最早 May 21 17:31），需批量更新为 COMPLETED
2. **2 个新进程未注册**：PID 142872 (rsft-ced-s42-v2) 和 PID 143166 (test_eval_14b_sft_s42_no_evi) 在运行但可能不在 registry 中
3. **no-evidence dev 实验的 field_compliance_rate 全为 0%**：1.7B 和 4B no_evi 模型输出完全没有 evidence 字段（符合预期，因为 no_evidence=true），但 8B 的 field_compliance 为 0.8%（8/985 个文档意外输出了 evidence）
4. **test set F1 普遍大幅低于 dev set**：4B SFT 从 dev 0.41 降到 test 0.22，8B SFT 从 0.52 降到 0.31，14B RSFT 从较高 dev 降到 0.38。这个差距异常大，可能与 test_revised split 的评估方式不同（test set 没有 ign_f1 校正，precision=ign_precision）有关
5. **rsft-ced-s42-v2 训练占用 94GB 显存**（cuda:2 几乎满载）——4B 模型训练占这么多 VRAM 不太正常，需检查是否有显存泄漏或 batch_size 过大

---
