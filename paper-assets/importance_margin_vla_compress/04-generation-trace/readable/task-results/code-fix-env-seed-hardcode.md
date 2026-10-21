# code fix env seed hardcode

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-env-seed-hardcode_20260521T022741_result.json`
- **Structured JSON:** [`06a96f272ae23ce33e16.json`](../../sessions/06/06a96f272ae23ce33e16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**修改结果：**

| 服务器 | eval_openvla_libero.py | eval_openvla_l2norm_libero.py |
|--------|----------------------|------------------------------|
| westd-41074 | `env.seed(args.seed)` ✅ | 文件不存在 |
| westd-38929 | `env.seed(args.seed)` ✅ | `env.seed(args.seed)` ✅ |
| westd-27271 | `env.seed(args.seed)` ✅ | `env.seed(args.seed)` ✅ |
| cqa1-33015 | 文件不存在 | 文件不存在 |

---
