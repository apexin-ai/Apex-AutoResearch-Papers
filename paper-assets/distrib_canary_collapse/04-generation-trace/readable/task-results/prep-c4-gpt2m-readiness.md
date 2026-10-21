# prep c4 gpt2m readiness

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_c4_gpt2m_readiness_20260515T113213_result.json`
- **Structured JSON:** [`e2258ca02af4a7ea07a5.json`](../../sessions/e2/e2258ca02af4a7ea07a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/prep_c4_gpt2m_readiness.md`。

**核心发现**：

| 检查项 | 状态 |
|--------|------|
| GPT-2-medium 模型缓存 | ❌ 文件已下载（1.5GB）但在错误路径（`hub/` 外），需 mv 到 `hub/` 内 |
| C4 数据集 (`data/c4_5k/`) | ✅ train 4500 / eval 500 / prompts ≤500，格式匹配 |
| 训练脚本适配 | ✅ `--model_name gpt2-medium` + `--data_dir` + `--batch_size 32` 均支持，无需改动 |
| 命令草拟 | ✅ 已生成 a100_s42 和 a025_s42 两条命令 |

**提交前唯一 blocker**：执行 `mv /root/autodl-tmp/.hf_cache/models--gpt2-medium/ /root/autodl-tmp/.hf_cache/hub/models--gpt2-medium/`（先删除 hub 下的空壳目录），否则 `from_pretrained('gpt2-medium')` 找不到本地缓存会重新下载。

---
