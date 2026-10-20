# infra mvp deploy v5 sandbox

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mvp_deploy_v5_sandbox_20260514T094356_result.json`
- **Structured JSON:** [`1307e38295f61d0f7502.json`](../../sessions/13/1307e38295f61d0f7502.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MVP 正常运行中，0 个 ERROR。

---

## 产出汇总

### 1. 文件验证结果

| 检查项 | 结果 |
|--------|------|
| `z3_sandbox.py` 存在 (12139 bytes) | **OK** |
| `autoformalize.py` 无 `import z3` | **OK** |
| `autoformalize.py` 使用 `get_sandbox()` | **OK** |
| `z3_checker.py` 使用 `get_sandbox()` (3处) | **OK** |
| 量词规则 `CRITICAL RULES` 存在 (两文件各1处) | **OK** |
| `test_z3_sandbox.py` 存在 | **OK** |

### 2. Crash test 完整输出

```
=== Test 1: Normal validation ===
  Z3 sandbox worker started (pid=36608)
  PASS: valid=True, err=None
  PASS: valid=True, err=None
  PASS: valid=True, err=None
  PASS: valid=False, err=Z3 subprocess error or crash

=== Test 2: IC check ===
  Consistent set: is_sat=True, ic_score=1.00, mcs=3
  Inconsistent set: is_sat=False, ic_score=0.50, mcs=1

=== Test 3: Crash test (os.abort in worker) ===
  PASS: Worker crashed, parent survived

=== Test 4: Post-crash validation ===
  Z3 sandbox worker started (pid=36628)
  PASS: valid=True, err=None (worker restarted)
  PASS: valid=True, err=None

=== Test 5: Entailment check ===
  Entailment: entails=True, status=entails

=== ALL TESTS PASSED ===
```

### 3. Dry-run mvp_report.json

```json
{
  "config": { "num_problems": 2, "num_chains": 2, "total_chains": 4 },
  "accuracy": { "svs": 0.5, "sc": 0.5, "delta": 0.0 },
  "formalization": { "total_claims": 93, "formalized_claims": 79, "rate": 0.8495 },
  "verdict": { "p1": "PASS", "p2": "PASS", "overall": "PASS" },
  "cost": { "total_calls": 153, "total_tokens": 116859, "estimated_cost_usd": 0.03271 }
}
```

### 4. 完整 MVP PID
- Python 进程 PID: **37622**
- 配置: 50 problems × 8 chains = 400 total chains

### 5. MVP 启动后日志（INFO 行）

```
17:51:19 [INFO] Loaded config from config_local.yaml
17:51:19 [INFO] MVP config: 50 problems × 8 chains = 400 total chains
17:51:19 [INFO] Loading 50 proofwriter depth-5 problems...
17:51:19 [INFO] Loaded 30220 problems from local cache
17:51:19 [INFO] Loaded 50 ProofWriter depth-5 problems
17:51:19 [INFO] Loaded 50 problems
17:51:19 [INFO] --- Problem 1/50: pw_20952 ---
17:51:32 [INFO] HTTP Request: POST http://localhost:8001/v1/chat/completions "HTTP/1.1 200 OK"
17:51:56 [INFO] HTTP Request: POST http://localhost:8001/v1/chat/completions "HTTP/1.1 200 OK"
```

### 6. 异常
- 首次启动 MVP 漏设 `HF_DATASETS_OFFLINE=1`，导致 HuggingFace 连接失败（Network is unreachable）。已 kill 并加上环境变量重启，现在正常运行，0 ERROR。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "config": {
      "num_problems": 2,
      "num_chains": 2,
      "total_chains": 4
    },
    "accuracy": {
      "svs": 0.5,
      "sc": 0.5,
      "delta": 0.0
    },
    "formalization": {
      "total_claims": 93,
      "formalized_claims": 79,
      "rate": 0.8495
    },
    "verdict": {
      "p1": "PASS",
      "p2": "PASS",
      "overall": "PASS"
    },
    "cost": {
      "total_calls": 153,
      "total_tokens": 116859,
      "estimated_cost_usd": 0.03271
    }
  }
}
```

</details>

---
