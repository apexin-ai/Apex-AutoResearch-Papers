# fix graspune env and calibration

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_graspune-env-and-calibration_20260514T091406_result.json`
- **Structured JSON:** [`4b42249359b5b924e012.json`](../../sessions/4b/4b42249359b5b924e012.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。结果汇总：

## 任务 1: 依赖安全

**依赖状态**（全部已安装，无需额外操作）：

| 包 | requirements.txt | 已安装版本 | 动作 |
|---|---|---|---|
| torch | ==2.7.0 | 2.10.0+cu128 | **跳过**（不能降级） |
| transformers | ==4.51.0 | 5.8.0 | 已有（向后兼容） |
| datasets | ==2.16.1 | 4.8.4 | 已有 |
| accelerate | 无版本 | 1.13.0 | 已有 |
| sentencepiece | 无版本 | 0.2.1 | 已有 |
| tqdm | 无版本 | 4.67.3 | 已有 |
| safetensors | 无版本 | 0.7.0 | 已有 |
| numpy | 无版本 | 1.26.4 | 已有 |
| lm-eval | ==0.4.1 | 0.4.11 | 已有 |
| protobuf | 无版本 | 6.33.6 | 已有 |

**Import 验证**：所有 GRASPrune 核心模块（config, data, gates, pipeline, rebuild, evals）在 torch 2.10.0+cu128 下导入成功。

**警告注释**：已添加到 `run_graspune.sh` 第 2-3 行。

## 任务 2: 校准数据对齐

**前一个 Worker 已完成适配**：
- `data.py` 已有 `load_gsm8k_as_text()` 函数，将 GSM8K 的 question+answer 拼接为文本格式
- `load_text_dataset()` 已注册 `gsm8k` 分支
- `run_graspune.sh` 已配置 `--train-dataset gsm8k --num-samples 512 --max-len 512`

**Dry-run 验证结果**：
- GSM8K train split 前 512 样本加载成功（从 HF cache 读取）
- TokenBlockDataset 生成 **190 个 block**，block_size=512
- 输入格式正确：`Question: ... Answer: ...`
- tensor shape 正确：`input_ids=torch.Size([512])`, `attention_mask=torch.Size([512])`

两个任务均已完成，无需额外代码修改。

---
