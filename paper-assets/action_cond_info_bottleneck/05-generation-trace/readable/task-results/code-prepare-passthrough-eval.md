# code prepare passthrough eval

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-passthrough-eval_20260516T194703_result.json`
- **Structured JSON:** [`5ffe2e3b0daef74d122a.json`](../../sessions/5f/5ffe2e3b0daef74d122a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修改文件：** `/root/acib/scripts/eval_acib.py`

**实现方式：** 利用已有的 `ACIBPolicy.toggle_acib(enabled)` 机制。当 `acib_enabled=False` 时，`_connector_hook` 直接 return 原始 output，不经过 scorer reweighting。无需 monkey-patch scorer forward，零额外代码侵入。

**改动点：**
- L58-59: 添加 `--disable_scoring` argparse flag
- L86: `patch_make_policy` 签名加 `disable_scoring=False`
- L138-139: `toggle_acib(not disable_scoring)` + 提示 print
- L218: 启动日志打印 disable_scoring 状态
- L229: run_info.json 记录该参数
- L233: main() 传参

**新建文件：** `/root/acib/scripts/run_passthrough_eval.sh`（已 chmod +x）

**dry-run 验证：** `--help` 成功��示 `--disable_scoring` 参数，argparse 正常工作。

---
