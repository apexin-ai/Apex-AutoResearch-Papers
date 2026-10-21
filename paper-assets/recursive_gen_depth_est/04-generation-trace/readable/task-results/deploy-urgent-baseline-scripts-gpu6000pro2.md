# deploy urgent baseline scripts gpu6000pro2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_urgent-baseline-scripts-gpu6000pro2_20260519T142327_result.json`
- **Structured JSON:** [`931ff10c6a1c67a2c898.json`](../../sessions/93/931ff10c6a1c67a2c898.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**结果汇总：**

| 脚本 | 远程路径 | 编译 | 行数 |
|------|---------|------|------|
| detectgpt_baseline_v2.py | `scripts/detectgpt_baseline_v2.py` | OK | 418 |
| mink_prob_baseline.py | `scripts/mink_prob_baseline.py` | OK | 336 |
| binoculars_ordinal_eval.py | `scripts/binoculars_ordinal_eval.py` | OK | 550 |

**路径修正记录：**

| 脚本 | 位置 | 修改内容 |
|------|------|---------|
| detectgpt_baseline_v2.py | L14 (新增) | `os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")` |
| detectgpt_baseline_v2.py | L62 | `SCORING_MODEL_NAME`: `"openai-community/gpt2-large"` → `"/root/autodl-tmp/models/gpt2-xl"` |
| binoculars_ordinal_eval.py | L428 | `--observer_model` default: `"EleutherAI/pythia-1.4b"` → `"/root/autodl-tmp/models/pythia-1.4b"` |

**注意事项：**
- detectgpt 的 T5-large 扰动模型（`google-t5/t5-large`）服务器上没有本地缓存，首次运行会从 hf-mirror 下载（~3GB）
- binoculars 的 performer 模型（`EleutherAI/pythia-410m`）同理，首次运行需下载（~820MB）
- 依赖全部就绪：torch 2.10+cu128, transformers 5.8.1, sklearn 1.8.0, scipy 1.17.1, numpy 2.2.6

---
