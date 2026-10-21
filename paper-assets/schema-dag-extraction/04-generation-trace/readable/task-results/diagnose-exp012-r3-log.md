# diagnose exp012 r3 log

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp012_r3_log_20260515T155436_result.json`
- **Structured JSON:** [`e8d55f767d6c0c57aef6.json`](../../sessions/e8/e8d55f767d6c0c57aef6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**Conclusion: failed**

**失败原因**: vLLM 初始化阶段，FlashInfer 0.6.11.post2 JIT 编译报错：

```
CUDA compiler and CUDA toolkit headers are incompatible, please check your include paths
```

`ninja: build stopped: subcommand failed` → vLLM `LLM()` 构造抛出 `RuntimeError: Engine core initialization failed`。

**关键事实**:
- 实验从未进入推理阶段，无任何 metrics 产出
- 无 W&B 数据（符合预期——连 init 都没过）
- 无输出文件（`/root/autodl-tmp/exp012*` 不存在）
- 日志文件 `/tmp/exp012_r3.log`（425KB），主要内容是 FlashInfer 编译错误的 include chain

**根因**: 服务器上 flashinfer 版本与 CUDA toolkit 版本不兼容。重跑前需要升级/降级 flashinfer 或 CUDA toolkit 使之匹配。

**已完成操作**:
- Registry 更新为 `DONE / failed`，含 notes
- Cron 监控已删除

---
