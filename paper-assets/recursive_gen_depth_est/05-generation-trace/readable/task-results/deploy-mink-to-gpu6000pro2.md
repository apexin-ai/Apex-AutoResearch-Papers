# deploy mink to gpu6000pro2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_mink-to-gpu6000pro2_20260519T140015_result.json`
- **Structured JSON:** [`fed4125b32b59d514a82.json`](../../sessions/fe/fed4125b32b59d514a82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**修改汇总：**

| 行号 | 原内容 | 新内容 |
|------|--------|--------|
| L25 | `os.environ["CUDA_VISIBLE_DEVICES"] = "1"` | `# CUDA_VISIBLE_DEVICES controlled externally` |
| L264 | `print("Loading GPT-2 Large...")` | `print("Loading GPT-2 XL...")` |
| L265 | `GPT2TokenizerFast.from_pretrained("gpt2-large")` | `GPT2TokenizerFast.from_pretrained("/root/autodl-tmp/models/gpt2-xl")` |
| L267 | `GPT2LMHeadModel.from_pretrained("gpt2-large")` | `GPT2LMHeadModel.from_pretrained("/root/autodl-tmp/models/gpt2-xl")` |

**服务器路径：** `/root/autodl-tmp/recursive_gen_depth_est/scripts/mink_prob_baseline.py`
**语法验证：** SYNTAX OK

---
