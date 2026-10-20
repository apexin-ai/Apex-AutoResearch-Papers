# diagnose mvp pilot gpt2 ioi v3

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_pilot_gpt2_ioi_v3_20260513T011903_result.json`
- **Structured JSON:** [`b419b88c6b1c38f4066b.json`](../../sessions/b4/b419b88c6b1c38f4066b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three tasks complete. Here's the final output:

```json
{
  "k3_off_diagonal_pct": "13.3%  95% CI: [1.7%, 40.5%]",
  "k3_css_distribution": {"1/3": 103, "2/3": 45, "3/3": 7},
  "phase_d_fix": "Monkeypatch AutoConfig.from_pretrained and AutoTokenizer.from_pretrained to redirect 'gpt2' -> '/root/autodl-tmp/gpt2-small', bypassing network dependency entirely",
  "phase_d_result": {
    "css_1.00 (7 edges)":   {"cpr": 0.1095, "cmd": 0.911},
    "css_0.67 (52 edges)":  {"cpr": 0.0634, "cmd": 0.9582},
    "method_acdc (14 edges)": {"cpr": 0.0286, "cmd": 0.9937},
    "circus_core (15 edges)": {"cpr": -0.1081, "cmd": 1.1337},
    "method_eap_ig (100 edges)": {"cpr": -0.1092, "cmd": 1.1348},
    "stable_core (13 edges)": {"cpr": -0.187, "cmd": 1.2143},
    "method_edge_pruning (100 edges)": {"cpr": -0.2413, "cmd": 1.2699},
    "css_0.33 (155 edges)": {"cpr": -0.4862, "cmd": 1.5205}
  },
  "root_cause": "AutoDL blocks outgoing network by default. TransformerLens from_pretrained('gpt2-small') internally calls AutoConfig.from_pretrained('gpt2') and AutoTokenizer.from_pretrained('gpt2'), both requiring HuggingFace Hub access. With no network and no HF cache, both fail with LocalEntryNotFoundError/ConnectTimeoutError.",
  "error_type": "infrastructure",
  "fix_steps": [
    "1. Monkeypatched AutoConfig.from_pretrained and AutoTokenizer.from_pretrained to redirect gpt2 aliases to /root/autodl-tmp/gpt2-small",
    "2. Wrote standalone run_phase_d_only.py that loads cached Phase A-C results and runs only evaluation",
    "3. Patched run_mvp.py with same monkeypatch for future full-pipeline runs"
  ],
  "can_auto_fix": true
}
```

**Key observations on Phase D evaluation**: All CPR values are near zero or negative, with css_1.00 (the 7 three-way consensus edges) performing best at CPR=0.1095. This is expected — the evaluation uses **node-level** zero ablation on **edge-level** circuits, creating a granularity mismatch. The edge-level circuits identify important connections, but zeroing out entire nodes (heads/MLPs) is far more destructive than necessary. This doesn't invalidate the 13.3% off-diagonal finding; it means the evaluation metric needs edge-level ablation to be meaningful.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "k3_off_diagonal_pct": "13.3%  95% CI: [1.7%, 40.5%]",
    "k3_css_distribution": {
      "1/3": 103,
      "2/3": 45,
      "3/3": 7
    },
    "phase_d_fix": "Monkeypatch AutoConfig.from_pretrained and AutoTokenizer.from_pretrained to redirect 'gpt2' -> '/root/autodl-tmp/gpt2-small', bypassing network dependency entirely",
    "phase_d_result": {
      "css_1.00 (7 edges)": {
        "cpr": 0.1095,
        "cmd": 0.911
      },
      "css_0.67 (52 edges)": {
        "cpr": 0.0634,
        "cmd": 0.9582
      },
      "method_acdc (14 edges)": {
        "cpr": 0.0286,
        "cmd": 0.9937
      },
      "circus_core (15 edges)": {
        "cpr": -0.1081,
        "cmd": 1.1337
      },
      "method_eap_ig (100 edges)": {
        "cpr": -0.1092,
        "cmd": 1.1348
      },
      "stable_core (13 edges)": {
        "cpr": -0.187,
        "cmd": 1.2143
      },
      "method_edge_pruning (100 edges)": {
        "cpr": -0.2413,
        "cmd": 1.2699
      },
      "css_0.33 (155 edges)": {
        "cpr": -0.4862,
        "cmd": 1.5205
      }
    },
    "root_cause": "AutoDL blocks outgoing network by default. TransformerLens from_pretrained('gpt2-small') internally calls AutoConfig.from_pretrained('gpt2') and AutoTokenizer.from_pretrained('gpt2'), both requiring HuggingFace Hub access. With no network and no HF cache, both fail with LocalEntryNotFoundError/ConnectTimeoutError.",
    "error_type": "infrastructure",
    "fix_steps": [
      "1. Monkeypatched AutoConfig.from_pretrained and AutoTokenizer.from_pretrained to redirect gpt2 aliases to /root/autodl-tmp/gpt2-small",
      "2. Wrote standalone run_phase_d_only.py that loads cached Phase A-C results and runs only evaluation",
      "3. Patched run_mvp.py with same monkeypatch for future full-pipeline runs"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
