# code apply v2 full fixes

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_apply_v2_full_fixes_20260518T112437_result.json`
- **Structured JSON:** [`f4afc650c3f8067038ee.json`](../../sessions/f4/f4afc650c3f8067038ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**3 项修复已应用（远程 + 本地同步）：**
1. `config.py`: GAR_EPSILON 0.001 → 0.002
2. `train_phase2.py`: --lambda-gar default 0.5 → 5.0；新增 --init-bias 参数 (default=2.0)，传入模型构造
3. `threadgate.py`: ThreadGatedModel.__init__ 和 create_model 的 init_bias 5.0 → 2.0

**Dry-run 5 步指标：**

| Step | L_NTP | L_GAR | Loss | Gate | Mem |
|------|-------|-------|------|------|-----|
| 0 | 1.9796 | 0.1226 | 2.5927 | 0.8743 | 42.3GB |
| 1 | 1.3270 | 0.1226 | 1.9399 | 0.8744 | 42.3GB |
| 2 | 1.5047 | 0.0792 | 1.9009 | 0.8747 | 46.7GB |
| 3 | 1.6303 | 0.0851 | 2.0558 | 0.8757 | 46.7GB |
| 4 | 1.8503 | 0.0508 | 2.1044 | 0.8764 | 46.7GB |

- L_GAR 非零 ✓ (0.05~0.12)
- GAR 贡献占总 loss 15-30% ✓
- Gate ≈ 0.874 ≈ sigmoid(2.0) ✓
- 无 OOM/NaN ✓
- 峰值 46.7GB / 102GB ✓
- Gate 梯度已接收 ✓

---
