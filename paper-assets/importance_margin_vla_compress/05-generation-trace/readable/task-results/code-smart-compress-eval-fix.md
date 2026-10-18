# code smart compress eval fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_smart_compress_eval_fix_20260518T005347_result.json`
- **Structured JSON:** [`53553b1eec769416fa6e.json`](../../sessions/53/53553b1eec769416fa6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在正常运行。

## 产出汇总

1. **旧进程**: 已 kill，无残留进程
2. **Checkpoint 确认**:
   - M=32: `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m32/checkpoint.pt` (1.5GB), 训练完成 (eval loss=0.052)
   - M=64: `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/smart_compress_m64/checkpoint.pt` (1.5GB), 训练完成 (eval loss=0.062)
3. **新 eval 脚本**: `/root/autodl-tmp/importance_margin_vla_compress/eval_smart_compress_libero.py`
   - 正确实例化 SmartCompressWrapper(policy, compress_config={"num_queries": M})
   - load_state_dict 加载完整 wrapper 权重（含 compressor + policy）
   - 推理走 `wrapper.forward_inference(batch)`，vision tokens 经过 cross-attention compression
4. **Dry-run 结果**: M=32 加载成功，无 missing/unexpected keys，Task 0 Ep 1 SUCCESS (140 steps)，action 输出正常
5. **正式 eval PID**:
   - M=32 on GPU 0: PID **420909**
   - M=64 on GPU 1: PID **426524**
   - 两者都在正常产出 episode 结果（M=32 已跑到 ~8 eps，M=64 已跑到 ~2 eps）

---
