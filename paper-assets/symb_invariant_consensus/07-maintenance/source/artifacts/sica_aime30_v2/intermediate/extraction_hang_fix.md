## Extraction Hang Bug Fix (2026-05-15)

### Root Cause
HTTP requests to vLLM had no timeout. When vLLM closed connections (CLOSE_WAIT), Python client waited indefinitely.

### Fixes Applied to constraint_extractor.py
1. **HTTP timeout**: `OpenAI(timeout=120.0)` on both VLLMBackend and APIBasedLLM
2. **Future timeout**: `future.result(timeout=180)` + `as_completed(timeout=600)`
3. **Concurrency limit**: `Semaphore(6)` + `max_workers=6` (was 12)
4. **Health check**: `check_vllm_health()` before each batch

### Smoke Test (k=4, max_tokens=2048)
- Extraction completed in 26s (no hang)
- 4/4 traces processed (2 with constraints, 2 empty due to truncation)
- Pipeline end-to-end: 121.7s