# diagnose smollm3 3b wiki a100 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_smollm3_3b_wiki_a100_s43_fp32_20260519T232818_result.json`
- **Structured JSON:** [`01afe4baf11d1ec2a8a6.json`](../../sessions/01/01afe4baf11d1ec2a8a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根因：磁盘满** — `/root/autodl-tmp` 250G 已 100% 占满，仅剩 3.5MB。

### 失败细节
- **gen_0**: 完成 (6.4M，仅 metrics/config)
- **gen_1**: 完成 (12G，含 checkpoint)
- **gen_2**: 训练 5000/5000 步跑完，但 `model.save_pretrained()` 写 safetensors 时磁盘满报错。checkpoint 目录残留 5G 损坏文件
- 错误位置：`iterative_train.py:318` → `safetensors_rust.SafetensorError: I/O error: No space left on device`

### 磁盘占用大户
| 目录 | 大小 | 状态 |
|------|------|------|
| `pythia14b_wiki_a100_s43/` | **53G** | 已完成 (gen_0-10 + all_metrics.json) |
| `smollm3_3b_wiki_a100_s42_fp32_v3/` | **24G** | 已完成 (gen_0-10 + all_metrics.json) |
| `smollm3_3b_wiki_a100_s43/` | 17G | 当前失败实验 |
| `gpt2m_wiki_a100_s42/` | 14G | — |
| `models/` | 17G | 预训练模型 |

### 修复方案

重跑 gen_2 到 gen_9 还需约 **50-80G** 空间。需要清理：

1. **必须**：删 `gen_2/checkpoint/` 残留 (5G)
2. **建议**：清理已完成实验中不再需要的中间 checkpoint：
   - `pythia14b_wiki_a100_s43/` 各 gen 的 checkpoint（保留 all_metrics.json 和 analysis 即可）→ 预计释放 ~45G
   - `smollm3_3b_wiki_a100_s42_fp32_v3/` — 如果 s42 (12G) 已有完整结果，v3 可能可以删 → 释放 24G

注意 registry 已有 note：**"19828 磁盘满导致失败。转移到 17855:cuda:3 重跑。"** — 看起来已经计划在另一台服务器重跑。如果 17855 空间充足，可以直接在那边跑，无需在 19828 清理。

---
