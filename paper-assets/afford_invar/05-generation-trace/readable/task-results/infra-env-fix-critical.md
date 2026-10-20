# infra env fix critical

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-fix-critical_20260519T163640_result.json`
- **Structured JSON:** [`b2e6acd3da6ef82351b5.json`](../../sessions/b2/b2e6acd3da6ef82351b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 CRITICAL 全部修复完成，最终验证通过。

## 结果

**CRITICAL 1** — transformers fork 安装成功：`transformers==4.40.1` from `moojink/transformers-openvla-oft`

**CRITICAL 2** — `import prismatic` 修复成功。修改了两个文件中的 `tensorflow_graphics` import：
- `/root/afford_invar/openvla-oft/prismatic/vla/datasets/rlds/oxe/utils/droid_utils.py` — 顶层 import 改为 try/except
- `/root/afford_invar/openvla-oft/prismatic/vla/datasets/rlds/oxe/transforms.py` — 3 处函数内 import 改为 try/except

**最终验证**：`import prismatic; from prismatic.models import load_vla` → `prismatic OK`

注意 stderr 中有 TensorFlow CUDA compute capability 12.0a 的 JIT 编译警告，不影响功能。

---
