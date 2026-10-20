# analysis gradient cka westd34685 — Part 2 of 2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-gradient-cka-westd34685.md) · [Structured JSON](../../../sessions/89/891bd07936e9db1d758e.json)

## Before a recorded user message

### Tool result

_source line 194 · 2026-05-23T03:16:31.887Z_

<details><summary>↩ Tool result · `toolu_01Xka7XmT2QrjfsGX3sq3esC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"431:    def _process_action_masks(self, labels):\\n432:        \\\"\\\"\\\"Helper to get action masks from labels\\\"\\\"\\\"\\n433:        current_action_mask = get_current_action_mask(labels)\\n434:        next_actions_mask = get_next_actions_mask(labels)\\n489:    def _build_multimodal_labels(self, labels, projected_patch_embeddings):\\n490:        \\\"\\\"\\\"Build multimodal labels with IGNORE_INDEX for patch embeddings\\\"\\\"\\\"\\n491:        if labels is not None:\\n492:            projected_patch_labels = torch.full(\\n495:                dtype=labels.dtype,\\n496:                device=labels.device,\\n498:            return torch.cat([labels[:, :1], projected_patch_labels, labels[:, 1:]], dim=1)\\n507:        labels: Optional[torch.LongTensor] = None,\\n540:            assert labels is None, \\\"Unexpected key `labels` provided during cached generation!\\\"\\n548:                labels=None,\\n566:                labels=labels,\\n581:            all_actions_mask = self._process_action_masks(labels)\\n606:                all_actions_mask = self._process_action_masks(labels)\\n631:            # Build labels for multimodal sequence if needed\\n632:            multimodal_labels = self._build_multimodal_labels(labels, projected_patch_embeddings)\\n641:                labels=multimodal_labels,\\n658:                f\\\"=> `labels` = {labels is not None}\\\\n\\\"\\n760:    def _prepare_labels_for_action_prediction(self, labels, input_ids):\\n761:        \\\"\\\"\\\"Creates labels tensor for action prediction if not provided\\\"\\\"\\\"\\n762:        # Extend labels tensor with fake action labels\\n764:        labels_extension = (\\n765:            torch.ones((labels.shape[0], input_ids.shape[-1] - labels.shape[-1])).to(labels.device).to(labels.dtype)\\n768:        labels = torch.cat([labels, labels_extension], dim=-1)\\n771:        labels[:, -1] = STOP_INDEX\\n773:        return labels\\n803:        labels,\\n818:            timesteps = torch.Tensor([t]).to(labels.device)\\n856:                labels=None,\\n886:        labels,\\n908:            labels=None,\\n983:        # Create fake labels tensor (needed for action mask)\\n984:        labels = input_ids.clone()\\n985:        labels[:] = IGNORE_INDEX\\n993:        # Update labels tensor for action mask computation later\\n994:        labels = self._prepare_labels_for_action_prediction(labels, input_ids)\\n998:        all_actions_mask = self._process_action_masks(labels)\\n1039:                labels,\\n1052:                labels,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77059271-bd5d-4e51-ae63-bc00d74282ce",
  "uuid": "daa195c8-9c9c-420a-816b-b228e3da145c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"431:    def _process_action_masks(self, labels):\\\\n432:        \\\\\\\"\\\\\\\"\\\\\\\"Helper to get action masks from labels\\\\\\\"\\\\\\\"\\\\\\\"\\\\n433:        current_action_mask = get_current_action_mask(labels)\\\\n434:        next_actions_mask = get_next_actions_mask(labels)\\\\n489:    def _build_multimodal_labels(self, labels, projected_patch_embeddings):\\\\n490:        \\\\\\\"\\\\\\\"\\\\\\\"Build multimodal labels with IGNORE_INDEX for patch embeddings\\\\\\\"\\\\\\\"\\\\\\\"\\\\n491:        if labels is not None:\\\\n492:            projected_patch_labels = torch.full(\\\\n495:                dtype=labels.dtype,\\\\n496:                device=labels.device,\\\\n498:            return torch.cat([labels[:, :1], projected_patch_labels, labels[:, 1:]], dim=1)\\\\n507:        labels: Optional[torch.LongTensor] = None,\\\\n540:            assert labels is None, \\\\\\\"Unexpected key `labels` provided during cached generation!\\\\\\\"\\\\n548:                labels=None,\\\\n566:                labels=labels,\\\\n581:            all_actions_mask = self._process_action_masks(labels)\\\\n606:                all_actions_mask = self._process_action_masks(labels)\\\\n631:            # Build labels for multimodal sequence if needed\\\\n632:            multimodal_labels = self._build_multimodal_labels(labels, projected_patch_embeddings)\\\\n641:                labels=multimodal_labels,\\\\n658:                f\\\\\\\"=> `labels` = {labels is not None}\\\\\\\\n\\\\\\\"\\\\n760:    def _prepare_labels_for_action_prediction(self, labels, input_ids):\\\\n761:        \\\\\\\"\\\\\\\"\\\\\\\"Creates labels tensor for action prediction if not provided\\\\\\\"\\\\\\\"\\\\\\\"\\\\n762:        # Extend labels tensor with fake action labels\\\\n764:        labels_extension = (\\\\n765:            torch.ones((labels.shape[0], input_ids.shape[-1] - labels.shape[-1])).to(labels.device).to(labels.dtype)\\\\n768:        labels = torch.cat([labels, labels_extension], dim=-1)\\\\n771:        labels[:, -1] = STOP_INDEX\\\\n773:        return labels\\\\n803:        labels,\\\\n818:            timesteps = torch.Tensor([t]).to(labels.device)\\\\n856:                labels=None,\\\\n886:        labels,\\\\n908:            labels=None,\\\\n983:        # Create fake labels tensor (needed for action mask)\\\\n984:        labels = input_ids.clone()\\\\n985:        labels[:] = IGNORE_INDEX\\\\n993:        # Update labels tensor for action mask computation later\\\\n994:        labels = self._prepare_labels_for_action_prediction(labels, input_ids)\\\\n998:        all_actions_mask = self._process_action_masks(labels)\\\\n1039:                labels,\\\\n1052:                labels,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"431:    def _process_action_masks(self, labels):\\n432:        \\\"\\\"\\\"Helper to get action masks from labels\\\"\\\"\\\"\\n433:        current_action_mask = get_current_action_mask(labels)\\n434:        next_actions_mask = get_next_actions_mask(labels)\\n489:    def _build_multimodal_labels(self, labels, projected_patch_embeddings):\\n490:        \\\"\\\"\\\"Build multimodal labels with IGNORE_INDEX for patch embeddings\\\"\\\"\\\"\\n491:        if labels is not None:\\n492:            projected_patch_labels = torch.full(\\n495:                dtype=labels.dtype,\\n496:                device=labels.device,\\n498:            return torch.cat([labels[:, :1], projected_patch_labels, labels[:, 1:]], dim=1)\\n507:        labels: Optional[torch.LongTensor] = None,\\n540:            assert labels is None, \\\"Unexpected key `labels` provided during cached generation!\\\"\\n548:                labels=None,\\n566:                labels=labels,\\n581:            all_actions_mask = self._process_action_masks(labels)\\n606:                all_actions_mask = self._process_action_masks(labels)\\n631:            # Build labels for multimodal sequence if needed\\n632:            multimodal_labels = self._build_multimodal_labels(labels, projected_patch_embeddings)\\n641:                labels=multimodal_labels,\\n658:                f\\\"=> `labels` = {labels is not None}\\\\n\\\"\\n760:    def _prepare_labels_for_action_prediction(self, labels, input_ids):\\n761:        \\\"\\\"\\\"Creates labels tensor for action prediction if not provided\\\"\\\"\\\"\\n762:        # Extend labels tensor with fake action labels\\n764:        labels_extension = (\\n765:            torch.ones((labels.shape[0], input_ids.shape[-1] - labels.shape[-1])).to(labels.device).to(labels.dtype)\\n768:        labels = torch.cat([labels, labels_extension], dim=-1)\\n771:        labels[:, -1] = STOP_INDEX\\n773:        return labels\\n803:        labels,\\n818:            timesteps = torch.Tensor([t]).to(labels.device)\\n856:                labels=None,\\n886:        labels,\\n908:            labels=None,\\n983:        # Create fake labels tensor (needed for action mask)\\n984:        labels = input_ids.clone()\\n985:        labels[:] = IGNORE_INDEX\\n993:        # Update labels tensor for action mask computation later\\n994:        labels = self._prepare_labels_for_action_prediction(labels, input_ids)\\n998:        all_actions_mask = self._process_action_masks(labels)\\n1039:                labels,\\n1052:                labels,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 195_

<details><summary>Logged reasoning block</summary>

````text
Now I see the key piece:

```python
def _build_multimodal_labels(self, labels, projected_patch_embeddings):
    """Build multimodal labels with IGNORE_INDEX for patch embeddings"""
    if labels is not None:
        projected_patch_labels = torch.full(
            ...
            dtype=labels.dtype,
            device=labels.device,
        )
        return torch.cat([labels[:, :1], projected_patch_labels, labels[:, 1:]], dim=1)
```

So labels ARE extended to include IGNORE_INDEX for vision patches! The structure is:


- `labels[:, :1]` → first token (BOS?)
- `projected_patch_labels` → IGNORE_INDEX for all vision patches
- `labels[:, 1:]` → rest of text labels

So the extended labels (multimodal_labels) has shape (B, text_seq_len + num_patches, D). But wait, the first token is split out and then the patches are inserted after it. So:
- multimodal_labels = [first_text_token, patch_labels(num_patches), rest_text_tokens(text_seq_len-1)]
- Total length = 1 + num_patches + (text_seq_len - 1) = num_patches + text_seq_len

So the multimodal labels end up with the vision patches interleaved right after the first token, padding the sequence to match the extended embeddings length.

Now in `run_forward_pass`, the action mask is computed from the original text labels (B, text_seq_len), but the text hidden states are extracted as (B, text_seq_len - 1, D) after removing the patches and the first token. This creates a dimension mismatch between the mask and the actual text representations I'm working with.

Looking at how the multimodal labels are constructed, the sequence becomes [BOS] [PATCH_0..PATCH_255] [TEXT_1..TEXT_n-1], so I need to carefully track whether text_seq_len includes the BOS token and how that affects the slicing when extracting text hidden states.

The text_hidden_states slice from position num_patches to -1 gives me T - 1 tokens, but the mask from get_current_action_mask has length T, so there's a dimension mismatch I need to resolve. I've been overthinking the dimension mismatch—the actual code probably handles the slicing internally. Rather than keep analyzing, I should just write the script and test it against the actual model, since the forward pass clearly works in the existing training code. My approach will be to replicate the exact forward pass from the training loop, separate out the gradients for action_loss and occ_loss, and use hooks on the ViT blocks to trace where the gradients flow.

Writing both scripts now...
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77059271-bd5d-4e51-ae63-bc00d74282ce",
  "uuid": "fc2d4c12-5691-4135-8b8e-4b5a4f26b311",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013aQbzKt9VU4hAXfXgMYHKw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3918,
      "cache_read_input_tokens": 130049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3918
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 196_

I now have complete understanding of the architecture. Let me write both scripts. The key findings:

- `_build_multimodal_labels` extends labels with IGNORE_INDEX for vision patches
- Vision backbone: DINOv2 (`featurizer`, 24 blocks) + SigLIP (`fused_featurizer`, 27 blocks)
- Fused features → `_cached_patch_features` (before projection)
- OCC head directly uses patch_features; action loss flows through projector → LLM → action_head

Now writing and uploading both scripts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77059271-bd5d-4e51-ae63-bc00d74282ce",
  "uuid": "6b80ed07-3966-47e1-8799-b6885359b1ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013aQbzKt9VU4hAXfXgMYHKw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3918,
      "cache_read_input_tokens": 130049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3918
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 197_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01L25m7uD61GqDHGs7R4bh8x`</summary>

```json
{
  "server": "westd-34685",
  "command": "mkdir -p /root/occsafe_vla/artifacts",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "77059271-bd5d-4e51-ae63-bc00d74282ce",
  "uuid": "4796aa8c-f428-47f6-8a55-1fc1be8e20c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013aQbzKt9VU4hAXfXgMYHKw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3918,
      "cache_read_input_tokens": 130049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3918
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 198 · 2026-05-23T03:17:14.610Z_

<details><summary>↩ Tool result · `toolu_01L25m7uD61GqDHGs7R4bh8x`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "77059271-bd5d-4e51-ae63-bc00d74282ce",
  "uuid": "6ce6f01d-3cf3-4350-9ee7-414e254e4600",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---
