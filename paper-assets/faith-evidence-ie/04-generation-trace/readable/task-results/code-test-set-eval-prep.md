# code test set eval prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_test-set-eval-prep_20260520T153719_result.json`
- **Structured JSON:** [`1b9c7fd6b04310f81625.json`](../../sessions/1b/1b9c7fd6b04310f81625.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本已创建。汇报如下：

---

## 汇报

### 1. 代码支持情况

`inference.py` 原生支持 `--split test`：
- 使用 `prepare_test_data()` 构建推理输入（无需 gold labels）
- 自动生成 `codalab_submission.json`（CodaLab 提交格式）
- 不计算 metrics（test set 无 gold labels）
- 另有独立的 `test_inference.py`，功能类似但更早期

### 2. 脚本已创建

| 脚本 | 模型 | Dev ign_f1 | SFT Adapter |
|------|------|-----------|-------------|
| `test_8b_rsft_best.sh` | RSFT k=1 s43 | 0.5471 | `sft_output_qwen3_8b_bf16` |
| `test_8b_sft_best.sh` | SFT s43 | 0.5324 | `sft_output_qwen3_8b_s43` |
| `test_8b_sft_no_evidence_best.sh` | SFT no-evidence | 0.5079 | `sft_output_qwen3_8b_no_evidence` |

路径：`/root/autodl-tmp/freige/scripts/test_eval/`

运行方式：`GPU=0 bash scripts/test_eval/test_8b_rsft_best.sh`

### 3. 🚨 关键阻塞：所有 Qwen3-8B SFT adapter 目录为空

以下 4 个目录均只有 `.` 和 `..`（May 20 15:52 创建的空目录）：
- `/root/autodl-tmp/sft_output_qwen3_8b_bf16/`
- `/root/autodl-tmp/sft_output_qwen3_8b_s43/`
- `/root/autodl-tmp/sft_output_qwen3_8b_s44/`
- `/root/autodl-tmp/sft_output_qwen3_8b_no_evidence/`

**影响**：全部 3 个 test eval 都无法运行——RSFT eval 需要先 merge SFT adapter 再加载 RSFT adapter，SFT eval 直接依赖 SFT adapter。需要恢复或重新训练 8B SFT adapters。

RSFT adapter 本身（`rsft_output_qwen3_8b_k1_s43/`，698MB）完好。

### 4. 8B SFT best seed 确认

| Seed | ign_f1 |
|------|--------|
| s42 (default) | 0.5051 |
| **s43** | **0.5324** |
| s44 | 0.4681 |

Best seed = s43。

### 5. CodaLab 提交

test set eval 产出 `codalab_submission.json`，需手动提交到 DocRED CodaLab 获取分数。

---
