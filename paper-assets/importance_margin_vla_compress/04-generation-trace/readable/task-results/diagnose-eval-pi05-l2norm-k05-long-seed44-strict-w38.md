# diagnose eval pi05 l2norm k05 long seed44 strict w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_l2norm_k05_long_seed44_strict_w38_20260527T220420_result.json`
- **Structured JSON:** [`9e71ae976fede5a9e474.json`](../../sessions/9e/9e71ae976fede5a9e474.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验实际已成功完成，无需重跑。**

- EXIT_CODE=129 (SIGHUP) 出现在实验打印最终结果并保存 JSON **之后**，是 wrapper/session 清理信号，不影响数据
- 全部 10 tasks × 50 episodes 跑完，总 SR = **52.6%** (263/500)
- 结果文件 `pi05_l2norm_k0.50_libero_10_seed44.json` 已验证完整
- 运行时长 ~170 min，服务器 GPU 状态正常

---
