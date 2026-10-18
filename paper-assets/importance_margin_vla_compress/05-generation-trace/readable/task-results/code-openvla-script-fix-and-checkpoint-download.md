# code openvla script fix and checkpoint download

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla-script-fix-and-checkpoint-download_20260520T231347_result.json`
- **Structured JSON:** [`ff9e6eb21bdb1d6b7244.json`](../../sessions/ff/ff9e6eb21bdb1d6b7244.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: eval_openvla_libero.py 修改

语法验证: **SYNTAX OK** / Import check: **parseable**

Diff 摘要（16 处修改）:

| 变更 | 旧 | 新 |
|------|-----|-----|
| 删除全局常量 | `CHECKPOINT_PATH = "/root/autodl-tmp/openvla-libero-object"`&lt;br>`UNNORM_KEY = "libero_object"` | *(移除)* |
| argparse 新增参数 | *(无)* | `--model_path`, 默认 `"/root/autodl-tmp/openvla-libero-object"` |
| `load_model()` | 无参数，用全局 `CHECKPOINT_PATH` | `load_model(model_path)`，参数化所有路径引用 |
| unnorm_key 推断 | 硬编码 `"libero_object"` | `next(iter(vla.norm_stats.keys()))` 自动推断 |
| `load_model` 返回值 | `return vla, processor` | `return vla, processor, unnorm_key` |
| `get_action()` | 签名无 unnorm_key，用全局 `UNNORM_KEY` | 新增 `unnorm_key: str` 参数 |
| `count_vision_tokens()` | 签名无 unnorm_key，用全局 `UNNORM_KEY` | 新增 `unnorm_key` 参数 |
| `main()` 调用 | `vla, processor = load_model()` | `vla, processor, unnorm_key = load_model(args.model_path)` |
| results dict | `"model": "openvla-7b-libero-object"` | `"model": args.model_path` |

### Part 2: Checkpoint 下载

| 指标 | 值 |
|------|-----|
| 磁盘总量 | 250GB |
| 已用 | 187GB |
| **可用** | **64GB** |
| 已有 checkpoint | `openvla-libero-object` (15GB) |
| 下载目标 | `openvla-7b-finetuned-libero-spatial`, `libero-goal`, `libero-10` (各 ~15GB) |
| 下载 PID | **673289** (运行中) |
| 初始状态 | `libero-spatial` 开始下载，1/16 files fetched |

64GB 可用、3 个 checkpoint 共 ~45GB，空间够用。下载在后台进行，可通过 `cat /tmp/checkpoint_download.log` 和 `ps -p 673289` 追踪进度。

---
