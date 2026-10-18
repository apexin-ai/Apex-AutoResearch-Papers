# fix openvla script suite guard

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_openvla_script_suite_guard_20260526T040002_result.json`
- **Structured JSON:** [`80324008c1c9efb379b7.json`](../../sessions/80/80324008c1c9efb379b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改汇总：

| 服务器 | 路径 | Patch | 语法 |
|--------|------|-------|------|
| westd-27271 | `/root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py` | ✅ | ✅ |
| westd-41074 | 同上 | ✅ | ✅ |
| westd-38929 | 同上 | ✅ | ✅ |
| cqa1-33015 | 同上 | ✅ | ✅ |

修改内容：
1. `--model_path` 和 `--unnorm_key` 默认值从硬编码 object 改为 `None`
2. `main()` 中 `parse_args()` 后插入 `SUITE_MODEL_MAP` 校验：未传 `--model_path` 时按 suite 自动映射正确模型；显式传了但与 suite 不匹配时抛 `ValueError` 拒绝执行

---
