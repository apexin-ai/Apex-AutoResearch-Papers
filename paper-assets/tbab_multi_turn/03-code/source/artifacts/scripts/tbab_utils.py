"""
Utility functions for TBAB multi-turn training.

Core functions:
- find_turn_boundaries: detect Mistral [INST]/[/INST] turn boundaries
- build_position_ids: construct per-turn or continuous position IDs
- build_4d_causal_mask: construct [batch, 1, seq_len, seq_len] causal mask
- insert_bridge_tokens: insert bridge tokens between turns

Input: tokenized input_ids from Mistral chat template
Output: modified input_ids, position_ids, attention_mask, labels
"""

import torch
from typing import List, Tuple


def find_turn_boundaries(
    input_ids: List[int],
    eos_token_id: int,
    inst_token_ids: List[int],
) -> List[Tuple[int, int]]:
    """Find turn boundaries in Mistral chat-templated input_ids.

    A turn boundary is defined by each [INST]...[/INST]...EOS block.
    Returns list of (turn_start, turn_end) where:
    - Turn 0 starts at position 0 (includes BOS)
    - Turn N>0 starts at the [INST] token after previous EOS
    - Each turn ends at the EOS token (inclusive)

    Args:
        input_ids: flat list of token IDs from apply_chat_template
        eos_token_id: EOS token ID (</s>)
        inst_token_ids: token IDs for "[INST]" (encoded without special tokens)

    Returns:
        List of (start_idx, end_idx) tuples, end_idx inclusive.
    """
    eos_positions = [i for i, t in enumerate(input_ids) if t == eos_token_id]

    boundaries = []
    turn_start = 0
    for eos_pos in eos_positions:
        boundaries.append((turn_start, eos_pos))
        turn_start = eos_pos + 1

    return boundaries


def insert_bridge_tokens(
    input_ids: List[int],
    labels: List[int],
    turn_boundaries: List[Tuple[int, int]],
    bridge_token_ids: List[int],
) -> Tuple[List[int], List[int], List[Tuple[int, int]]]:
    """Insert bridge tokens between turns (bridge belongs to the next turn).

    Bridge tokens are inserted AFTER turn N's EOS and BEFORE turn N+1's [INST].
    No bridge before the first turn.

    Args:
        input_ids: original token IDs
        labels: original labels (-100 for non-loss positions)
        turn_boundaries: from find_turn_boundaries
        bridge_token_ids: list of K bridge token IDs

    Returns:
        (new_input_ids, new_labels, new_turn_boundaries)
        New boundaries account for inserted bridge tokens.
    """
    if len(turn_boundaries) <= 1:
        return input_ids, labels, turn_boundaries

    k = len(bridge_token_ids)
    new_input_ids = []
    new_labels = []
    new_boundaries = []

    for turn_idx, (start, end) in enumerate(turn_boundaries):
        if turn_idx > 0:
            bridge_start = len(new_input_ids)
            new_input_ids.extend(bridge_token_ids)
            new_labels.extend([-100] * k)

        turn_start_new = len(new_input_ids)
        new_input_ids.extend(input_ids[start:end + 1])
        new_labels.extend(labels[start:end + 1])
        turn_end_new = len(new_input_ids) - 1

        if turn_idx > 0:
            new_boundaries.append((bridge_start, turn_end_new))
        else:
            new_boundaries.append((turn_start_new, turn_end_new))

    return new_input_ids, new_labels, new_boundaries


def build_position_ids(
    seq_len: int,
    turn_boundaries: List[Tuple[int, int]],
    use_reset: bool,
    num_bridge: int = 0,
) -> List[int]:
    """Build position IDs for the sequence.

    Without reset: standard [0, 1, 2, ..., seq_len-1].
    With reset (and bridge): each turn's bridge starts at 0, content continues from K.
    With reset (no bridge): each turn starts at 0.

    For turns with bridge (turn_idx > 0 when bridge is used):
        bridge positions: [0, 1, ..., K-1]
        content positions: [K, K+1, ..., K+content_len-1]

    Args:
        seq_len: total sequence length
        turn_boundaries: (start, end) tuples. When bridge is used, turn_idx>0
            boundaries include the bridge prefix.
        use_reset: whether to reset positions per turn
        num_bridge: number of bridge tokens (0 if no bridge)
    """
    if not use_reset:
        return list(range(seq_len))

    position_ids = [0] * seq_len

    for turn_idx, (start, end) in enumerate(turn_boundaries):
        has_bridge = (turn_idx > 0 and num_bridge > 0)
        if has_bridge:
            for i in range(num_bridge):
                position_ids[start + i] = i
            content_start = start + num_bridge
            for i, pos in enumerate(range(content_start, end + 1)):
                position_ids[pos] = num_bridge + i
        else:
            for i, pos in enumerate(range(start, end + 1)):
                position_ids[pos] = i

    return position_ids


def build_4d_causal_mask(
    seq_len: int,
    dtype: torch.dtype = torch.bfloat16,
) -> torch.Tensor:
    """Build a standard causal 4D attention mask [1, 1, seq_len, seq_len].

    This bypasses transformers' internal packed-sequence detection that would
    block cross-turn attention when position_ids are non-monotonic.

    Returns:
        Tensor of shape [1, 1, seq_len, seq_len] with 0.0 for allowed
        positions and -inf (via finfo.min) for masked positions.
    """
    mask = torch.full((seq_len, seq_len), torch.finfo(dtype).min, dtype=dtype)
    mask = torch.triu(mask, diagonal=1)
    return mask.unsqueeze(0).unsqueeze(0)


def build_labels(
    input_ids: List[int],
    turn_boundaries: List[Tuple[int, int]],
    end_inst_token_ids: List[int],
    num_bridge: int = 0,
) -> List[int]:
    """Build labels: only assistant content has loss, everything else is -100.

    For each turn, find [/INST] and set labels for tokens after it until turn end.
    Bridge tokens (if present at turn start for turn_idx > 0) are always -100.

    Args:
        input_ids: token IDs (possibly with bridge tokens inserted)
        turn_boundaries: (start, end) tuples
        end_inst_token_ids: token IDs for "[/INST]"
        num_bridge: number of bridge tokens per turn boundary
    """
    labels = [-100] * len(input_ids)
    end_inst_len = len(end_inst_token_ids)

    for turn_idx, (start, end) in enumerate(turn_boundaries):
        has_bridge = (turn_idx > 0 and num_bridge > 0)
        search_start = start + num_bridge if has_bridge else start

        end_inst_pos = None
        for i in range(search_start, end + 1 - end_inst_len + 1):
            if input_ids[i:i + end_inst_len] == end_inst_token_ids:
                end_inst_pos = i
                break

        if end_inst_pos is not None:
            assistant_start = end_inst_pos + end_inst_len
            for i in range(assistant_start, end + 1):
                labels[i] = input_ids[i]

    return labels
