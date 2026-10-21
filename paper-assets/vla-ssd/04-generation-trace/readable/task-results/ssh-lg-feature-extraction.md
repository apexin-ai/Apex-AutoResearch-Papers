# ssh lg feature extraction

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_lg-feature-extraction_20260515T164416_result.json`
- **Structured JSON:** [`066b3e8bfac0e40601ae.json`](../../sessions/06/066b3e8bfac0e40601ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 job 已提交成功：

| Job | exp_id | GPU | PID | Log |
|-----|--------|-----|-----|-----|
| Trained VLA on LIBERO-Goal | `lg_extract_trained` | cuda:0 | 627251 | `~/runs/vla-ssd/lg_extract_trained.log` |
| Untrained VLA on LIBERO-Goal | `lg_extract_untrained` | cuda:1 | 627330 | `~/runs/vla-ssd/lg_extract_untrained.log` |

- Trained: `openvla-7b` checkpoint → `features/trained_libero_goal/`
- Untrained: `openvla-7b-untrained` checkpoint → `features/untrained_libero_goal/`

---
