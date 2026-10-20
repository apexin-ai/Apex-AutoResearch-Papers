# infra env setup and submit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-setup-and-submit_20260514T050853_result.json`
- **Structured JSON:** [`b18b9cb86c2391f84bed.json`](../../sessions/b1/b18b9cb86c2391f84bed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。执行汇总：

**环境**
- 服务器：4x RTX 5090 32GB，Python 3.12.3，conda base
- 所有依赖已预装（torch 2.10.0+cu128, transformers 4.57.6, trl 1.1.0, peft 0.19.0 等），无需额外安装

**数据与模型**
- DocRED（train 12.4MB, dev 4.1MB, test 3.5MB）→ `/root/autodl-tmp/data/docred/`
- DeBERTa NLI 模型已缓存 → `/root/autodl-tmp/.hf_cache/`

**代码部署**
- 16 个源文件 + 3 个配置文件 → `/root/autodl-tmp/freige/`
- 导入验证通过：dev split 12275 samples, 6830 with hard negatives

**实验提交**
| 实验 | tmux session | GPU | 状态 |
|------|-------------|-----|------|
| `mvp1_ced_signal` | mvp1_ced_signal | cuda:0 (CPU推理) | 运行中，正在处理 6830 样本 |
| `smoke_test_grpo` | smoke_test_grpo | cuda:1,2,3 | 运行中，正在加载模型 |

---
