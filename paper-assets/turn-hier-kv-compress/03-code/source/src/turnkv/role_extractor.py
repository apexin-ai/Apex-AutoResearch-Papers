# Protocol marker role extractor — identifies segment boundaries and semantic roles
# from tokenized multi-turn chat input.

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List, Optional, Union

if TYPE_CHECKING:
    pass

from .eass import Segment

__all__ = ["RoleExtractor", "Segment", "TemplateConfig", "LLAMA3_CONFIG", "TEMPLATE_REGISTRY"]


# ---------------------------------------------------------------------------
# Template configuration
# ---------------------------------------------------------------------------

@dataclass
class TemplateConfig:
    """Marker configuration for a specific chat template."""

    name: str
    header_start_token_id: int
    header_end_token_id: int
    eot_token_id: int
    bos_token_id: int
    role_mapping: Dict[str, str]
    tool_call_token_id: Optional[int] = None
    thinking_start_text: str = "<think>"
    thinking_end_text: str = "</think>"


LLAMA3_CONFIG = TemplateConfig(
    name="llama3",
    header_start_token_id=128006,
    header_end_token_id=128007,
    eot_token_id=128009,
    bos_token_id=128000,
    role_mapping={
        "system": "SYSTEM_PROMPT",
        "user": "USER_MESSAGE",
        "assistant": "ASSISTANT_MESSAGE",
        "ipython": "TOOL_RESULT",
    },
    tool_call_token_id=128255,  # <|python_tag|>
    thinking_start_text="<think>",
    thinking_end_text="</think>",
)

TEMPLATE_REGISTRY: Dict[str, TemplateConfig] = {
    "llama3": LLAMA3_CONFIG,
}


# ---------------------------------------------------------------------------
# RoleExtractor
# ---------------------------------------------------------------------------

class RoleExtractor:
    """Extract segment boundaries and semantic roles from tokenized chat input.

    Works in two modes:
    - With a real HuggingFace tokenizer (used to decode header role text).
    - With ``tokenizer=None`` for testing — header role text is resolved via
      a ``token_to_text`` lookup table passed at construction time.
    """

    def __init__(
        self,
        tokenizer=None,
        template_name: str = "llama3",
        *,
        token_to_text: Optional[Dict[int, str]] = None,
    ):
        """
        Args:
            tokenizer: HuggingFace tokenizer (optional — can be None for tests).
            template_name: chat template identifier.
            token_to_text: mapping from token id → text, used when tokenizer is
                None to decode header content and detect thinking markers.
        """
        if template_name not in TEMPLATE_REGISTRY:
            raise ValueError(
                f"Unknown template {template_name!r}. "
                f"Available: {list(TEMPLATE_REGISTRY)}"
            )
        self.tokenizer = tokenizer
        self.config = TEMPLATE_REGISTRY[template_name]
        self._token_to_text = token_to_text or {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def extract(self, input_ids: Union[List[int], "torch.Tensor"]) -> List[Segment]:
        """Extract ordered segments from a tokenized chat sequence."""
        ids = self._to_list(input_ids)
        if not ids:
            return []

        cfg = self.config
        raw_blocks = self._split_into_raw_blocks(ids, cfg)
        segments = self._assign_roles_and_splits(raw_blocks, ids, cfg)
        return segments

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _to_list(input_ids) -> List[int]:
        if hasattr(input_ids, "tolist"):
            return input_ids.tolist()
        return list(input_ids)

    def _decode_tokens(self, token_ids: List[int]) -> str:
        """Decode a short span of token ids to text."""
        if self.tokenizer is not None:
            return self.tokenizer.decode(token_ids, skip_special_tokens=False)
        return "".join(self._token_to_text.get(t, "") for t in token_ids)

    # ------------------------------------------------------------------

    def _split_into_raw_blocks(
        self, ids: List[int], cfg: TemplateConfig
    ) -> List[dict]:
        """Identify raw blocks delimited by header markers.

        Returns a list of dicts:
            {
                "header_start": int,   # index of <|start_header_id|>
                "content_start": int,  # index right after <|end_header_id|> + newlines
                "block_end": int,      # index after <|eot_id|> (or end of sequence)
                "role_text": str,      # decoded role string ("system", "user", …)
            }
        """
        blocks: List[dict] = []
        n = len(ids)
        i = 0

        while i < n:
            if ids[i] != cfg.header_start_token_id:
                i += 1
                continue

            header_start = i
            i += 1  # skip <|start_header_id|>

            # Collect tokens until <|end_header_id|>
            role_token_ids: List[int] = []
            while i < n and ids[i] != cfg.header_end_token_id:
                role_token_ids.append(ids[i])
                i += 1

            if i < n:
                i += 1  # skip <|end_header_id|>

            role_text = self._decode_tokens(role_token_ids).strip()

            # Skip the two newlines that follow <|end_header_id|> in llama3
            while i < n and ids[i] not in (
                cfg.header_start_token_id,
                cfg.eot_token_id,
            ):
                # peek — the content starts here; break out
                break

            content_start = i

            # Find end of block: next <|eot_id|> or next <|start_header_id|>
            # (whichever comes first — last assistant block may lack eot)
            block_end = n
            j = content_start
            while j < n:
                if ids[j] == cfg.eot_token_id:
                    block_end = j + 1  # include the eot token in the block
                    break
                if j > content_start and ids[j] == cfg.header_start_token_id:
                    block_end = j
                    break
                j += 1

            blocks.append(
                {
                    "header_start": header_start,
                    "content_start": content_start,
                    "block_end": block_end,
                    "role_text": role_text,
                }
            )
            i = block_end

        return blocks

    # ------------------------------------------------------------------

    def _assign_roles_and_splits(
        self, raw_blocks: List[dict], ids: List[int], cfg: TemplateConfig
    ) -> List[Segment]:
        """Convert raw blocks into final Segment list with turn indices."""

        segments: List[Segment] = []
        turn_index = 0
        seen_first_user = False

        # If the sequence starts with BOS before the first header, fold it
        # into the first block's start.
        first_block_start = raw_blocks[0]["header_start"] if raw_blocks else 0

        for block_idx, block in enumerate(raw_blocks):
            role_text = block["role_text"]
            base_role = cfg.role_mapping.get(role_text, "UNKNOWN")

            # Determine effective start — include BOS for the very first block.
            seg_start = block["header_start"]
            if block_idx == 0 and first_block_start > 0:
                seg_start = 0  # absorb leading BOS

            seg_end = block["block_end"]
            content_start = block["content_start"]

            # --- Turn index logic ---
            if role_text == "system":
                cur_turn = 0
            elif role_text == "user":
                if seen_first_user:
                    turn_index += 1
                else:
                    seen_first_user = True
                cur_turn = turn_index
            else:
                cur_turn = turn_index

            # --- Sub-segment splitting for assistant messages ---
            if base_role == "ASSISTANT_MESSAGE":
                sub_segs = self._split_assistant_block(
                    ids, seg_start, content_start, seg_end, cur_turn, cfg
                )
                segments.extend(sub_segs)
            else:
                segments.append(
                    Segment(
                        role=base_role,
                        start_idx=seg_start,
                        end_idx=seg_end,
                        turn_index=cur_turn,
                    )
                )

        return segments

    # ------------------------------------------------------------------

    def _split_assistant_block(
        self,
        ids: List[int],
        seg_start: int,
        content_start: int,
        seg_end: int,
        turn_index: int,
        cfg: TemplateConfig,
    ) -> List[Segment]:
        """Split an assistant block into ASSISTANT_MESSAGE / TOOL_CALL / THINKING_TRACE."""

        # Check for <|python_tag|> → TOOL_CALL
        if cfg.tool_call_token_id is not None:
            for k in range(content_start, seg_end):
                if ids[k] == cfg.tool_call_token_id:
                    return [
                        Segment(
                            role="TOOL_CALL",
                            start_idx=seg_start,
                            end_idx=seg_end,
                            turn_index=turn_index,
                        )
                    ]

        # Check for <think>…</think> in the content text
        content_ids = ids[content_start:seg_end]
        content_text = self._decode_tokens(content_ids)

        think_start_tag = cfg.thinking_start_text
        think_end_tag = cfg.thinking_end_text

        if content_text.lstrip().startswith(think_start_tag):
            # Find where <think> starts in the token stream
            think_start_pos = content_text.find(think_start_tag)
            think_end_pos = content_text.find(think_end_tag, think_start_pos)

            if think_end_pos >= 0:
                # We need to map text positions back to token indices.
                think_end_text_end = think_end_pos + len(think_end_tag)

                # Walk tokens to find the split point
                split_token_idx = self._text_offset_to_token_idx(
                    content_ids, think_end_text_end
                )
                abs_split = content_start + split_token_idx

                segments: List[Segment] = []
                # Thinking segment (header + think content)
                segments.append(
                    Segment(
                        role="THINKING_TRACE",
                        start_idx=seg_start,
                        end_idx=abs_split,
                        turn_index=turn_index,
                    )
                )
                # Remaining assistant content (if any non-trivial tokens remain)
                if abs_split < seg_end:
                    # Check if remaining content is non-empty (not just eot)
                    remaining = ids[abs_split:seg_end]
                    non_special = [
                        t for t in remaining if t != cfg.eot_token_id
                    ]
                    if non_special:
                        segments.append(
                            Segment(
                                role="ASSISTANT_MESSAGE",
                                start_idx=abs_split,
                                end_idx=seg_end,
                                turn_index=turn_index,
                            )
                        )
                    else:
                        # Extend thinking to cover trailing eot
                        segments[-1] = Segment(
                            role="THINKING_TRACE",
                            start_idx=seg_start,
                            end_idx=seg_end,
                            turn_index=turn_index,
                        )
                return segments
            else:
                # <think> without closing </think> — treat entire block as thinking
                return [
                    Segment(
                        role="THINKING_TRACE",
                        start_idx=seg_start,
                        end_idx=seg_end,
                        turn_index=turn_index,
                    )
                ]

        # Plain assistant message
        return [
            Segment(
                role="ASSISTANT_MESSAGE",
                start_idx=seg_start,
                end_idx=seg_end,
                turn_index=turn_index,
            )
        ]

    def _text_offset_to_token_idx(
        self, token_ids: List[int], text_offset: int
    ) -> int:
        """Map a character offset in decoded text to the corresponding token boundary."""
        cumulative = 0
        for i, tid in enumerate(token_ids):
            tok_text = self._decode_tokens([tid])
            cumulative += len(tok_text)
            if cumulative >= text_offset:
                return i + 1
        return len(token_ids)
