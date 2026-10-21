# code 340m eval

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_340m_eval_20260518T142903_result.json`
- **Structured JSON:** [`213d629768e85c2f593f.json`](../../sessions/21/213d629768e85c2f593f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是完整结果报告。

---

## 340M 模型评测结果（6 models × 6 tasks）

**服务器**: westb-48145 (root), GPU: RTX PRO 6000, batch_size=16  
**评测脚本**: `/root/entrainment_gated_ft/run_lmeval_clean.py`  
**输出目录**: `/root/entrainment_gated_ft/lm_eval_clean/340m/`

### 1. 模型清单（6个）

| # | 模型 | 类型 |
|---|------|------|
| 1 | transformer_340M_baseline | Transformer (tie=True) |
| 2 | 340M-20B-GatedDeltaNet-pure-baseline | GDN pure |
| 3 | 340M-20B-GatedDeltaNet-hybrid-3-1 | GDN hybrid 3:1 |
| 4 | 340M-20B-GatedDeltaNet-hybrid-6-1 | GDN hybrid 6:1 |
| 5 | 340M-20B-GatedDeltaNet-hybrid-12-1 | GDN hybrid 12:1 |
| 6 | 340M-20B-GatedDeltaNet-New-hybrid-24-1 | GDN hybrid 24:1 |

### 2. Transformer 验证

Transformer 340M (tie_word_embeddings=True) 已验证 tying 正确：lambada ppl=26.23（正常范围），无 tying bug。

### 3. 完整评测结果

| Model | LambadaOAI acc/ppl | HellaSwag acc_norm | WinoGrande acc | ARC-Easy acc_norm | ARC-Chall acc_norm | MMLU acc |
|-------|------|------|------|------|------|------|
| **Transformer** | **0.3745** / **26.23** | **0.4304** | **0.5422** | **0.5316** | 0.3003 | **0.2501** |
| GDN pure | 0.3753 / 34.81 | 0.4147 | 0.5083 | 0.4823 | 0.2790 | 0.2477 |
| GDN hybrid-3:1 | 0.3268 / 47.96 | 0.4093 | 0.5067 | 0.4870 | **0.3055** | 0.2323 |
| GDN hybrid-6:1 | 0.3513 / 39.10 | 0.4111 | 0.5399 | 0.4739 | 0.2841 | 0.2394 |
| GDN hybrid-12:1 | 0.3252 / 42.98 | 0.4179 | 0.5122 | 0.4710 | 0.2773 | 0.2339 |
| GDN New-hybrid-24:1 | 0.3507 / 38.43 | 0.3764 | 0.5193 | 0.4802 | 0.2696 | 0.2331 |

**加粗** = 该列最优值。

### 4. 关键发现

- Transformer 在大多数 benchmark 上领先 GDN 变体（HellaSwag、ARC-Easy、MMLU、lambada ppl）
- GDN pure 在 lambada acc (0.3753) 上微略超过 Transformer (0.3745)，但 ppl 差距较大（34.81 vs 26.23）
- GDN hybrid-3:1 在 ARC-Challenge 上最优（0.3055），超过 Transformer（0.3003）
- GDN hybrid-6:1 在 WinoGrande 上接近 Transformer（0.5399 vs 0.5422）
- New-hybrid-24:1 的 HellaSwag acc_norm 明显偏低（0.3764）

### 5. 问题与解决

- **网络超时**: 服务器无外网，dataset 加载时重试延迟。通过设置 `HF_DATASETS_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1` 解决
- **SSH 超时**: eval 命令超过 30s ssh 限制。通过 `nohup` 后台运行 + log 轮询解决
- 所有 6 个 JSON 结果文件已保存在 `/root/entrainment_gated_ft/lm_eval_clean/340m/`

---
