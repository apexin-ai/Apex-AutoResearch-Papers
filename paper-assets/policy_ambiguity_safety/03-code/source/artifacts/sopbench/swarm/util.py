import inspect
import json
from datetime import datetime
import random
from dataclasses import dataclass
from typing import List, Optional, Dict, Any, Union
from openai import ChatCompletion
import time

@dataclass
class Function:
    arguments: str
    name: str
    
    def to_dict(self):
        return {
            "arguments": self.arguments,
            "name": self.name
        }

@dataclass
class ChatCompletionMessageToolCall:
    id: str
    function: Function
    type: str
    
    def to_dict(self):
        return {
            "id": self.id,
            "function": self.function.to_dict(),
            "type": self.type
        }

@dataclass
class ChatCompletionMessage:
    role: str
    content: Optional[str]
    thinking: Optional[str] = None
    thinking_signature: Optional[str] = None
    tool_calls: Optional[List[ChatCompletionMessageToolCall]] = None
    function_call: Optional[Any] = None
    refusal: Optional[Any] = None
    audio: Optional[Any] = None
    response_id: Optional[str] = None
    
    def to_dict(self):
        tool_calls_dict = [tool_call.to_dict() for tool_call in self.tool_calls] if self.tool_calls else None
        return {
            "content": self.content,
            "thinking": self.thinking,
            "thinking_signature": self.thinking_signature,
            "role": self.role,
            "tool_calls": tool_calls_dict,
            "function_call": self.function_call,
            "refusal": self.refusal,
            "audio": self.audio,
            "response_id": self.response_id
        }


@dataclass
class Choice:
    finish_reason: str
    index: int
    logprobs: Optional[dict]
    message: ChatCompletionMessage

@dataclass
class CompletionTokensDetails:
    accepted_prediction_tokens: int = 0
    audio_tokens: int = 0
    reasoning_tokens: int = 0
    rejected_prediction_tokens: int = 0

@dataclass
class PromptTokensDetails:
    audio_tokens: int = 0
    cached_tokens: int = 0

@dataclass
class CompletionUsage:
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int
    completion_tokens_details: CompletionTokensDetails
    prompt_tokens_details: PromptTokensDetails

@dataclass
class ChatCompletion:
    id: str
    choices: List[Choice]
    created: int
    model: str
    object: str
    system_fingerprint: str
    usage: CompletionUsage
    service_tier: Optional[Any] = None

def _generate_random_id(length: int = 24) -> str:
    """Generate a random ID string."""
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def ChatCompletionMessage_to_dict(msg) -> Dict[str, Any]:
    """Convert ChatCompletionMessage to a dict."""
    try:
        msg_dict = msg.to_dict()
        return msg_dict
    except Exception as e:
        # Convert ChatCompletionMessage to dict and print
        msg_dict = {
            "role": msg.role,
            "content": msg.content,
        }
        
        # Add tool_calls if present
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            tool_calls = []
            for tool_call in msg.tool_calls:
                tool_call_dict = {
                    "id": tool_call.id,
                    "type": tool_call.type,
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    }
                }
                tool_calls.append(tool_call_dict)
            msg_dict["tool_calls"] = tool_calls
        return msg_dict
    

def construct_chatcompletion(role: str, 
                   content: str, 
                   tool_calls: Optional[List[ChatCompletionMessageToolCall]] = None
                   ) -> ChatCompletion:
    
    choices = [Choice(
        finish_reason="stop",
        index=0,
        logprobs=None,
        message=ChatCompletionMessage(
            content=content,
            role=role,
            tool_calls=tool_calls,
            function_call=None,
            refusal=None,
            audio=None
        )
    )]
    return ChatCompletion(
        id=f'chatcmpl-{_generate_random_id()}',
        choices=choices,
        created=int(time.time()),
        model="None",
        object='chat.completion',
        system_fingerprint=f'fp_{_generate_random_id(8)}',
        usage=CompletionUsage(
            completion_tokens=0,
            prompt_tokens=0,
            total_tokens=0,
            completion_tokens_details=CompletionTokensDetails(),
            prompt_tokens_details=PromptTokensDetails()
        )
    )


def model_dump_json(message):
    message_raw = {
                    'content': message.content,
                    'thinking': message.thinking,
                    'thinking_signature': message.thinking_signature,
                    'role': message.role,
                    'tool_calls': [
                        {
                            'function': {
                                'name': tool.function.name,
                                'arguments': tool.function.arguments
                            },
                            'id': tool.id,
                            'type': tool.type
                        } for tool in (message.tool_calls or [])
                    ]
                }
    return json.dumps(message_raw)


def debug_print(debug: bool, *args: str) -> None:
    if not debug:
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = " ".join(map(str, args))
    print(f"\033[97m[\033[90m{timestamp}\033[97m]\033[90m {message}\033[0m")
    _ = input("Press Enter to continue...")


def merge_fields(target, source):
    for key, value in source.items():
        if isinstance(value, str):
            target[key] += value
        elif value is not None and isinstance(value, dict):
            merge_fields(target[key], value)


def merge_chunk(final_response: dict, delta: dict) -> None:
    delta.pop("role", None)
    merge_fields(final_response, delta)

    tool_calls = delta.get("tool_calls")
    if tool_calls and len(tool_calls) > 0:
        index = tool_calls[0].pop("index")
        merge_fields(final_response["tool_calls"][index], tool_calls[0])


def function_to_json(func) -> dict:
    """
    Converts a Python function into a JSON-serializable dictionary
    that describes the function's signature, including its name,
    description, and parameters.

    Args:
        func: The function to be converted.

    Returns:
        A dictionary representing the function's signature in JSON format.
    """
    type_map = {
        str: "string",
        int: "integer",
        float: "number",
        bool: "boolean",
        list: "array",
        dict: "object",
        type(None): "null",
    }

    try:
        signature = inspect.signature(func)
    except ValueError as e:
        raise ValueError(
            f"Failed to get signature for function {func.__name__}: {str(e)}"
        )

    parameters = {}
    for param in signature.parameters.values():
        try:
            param_type = type_map.get(param.annotation, "string")
        except KeyError as e:
            raise KeyError(
                f"Unknown type annotation {param.annotation} for parameter {param.name}: {str(e)}"
            )
        parameters[param.name] = {"type": param_type}

    required = [
        param.name
        for param in signature.parameters.values()
        if param.default == inspect._empty
    ]

    return {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": func.__doc__ or "",
            "parameters": {
                "type": "object",
                "properties": parameters,
                "required": required,
            },
        },
    }
    
    
def display_messages(messages: List[Union[Dict[str, Any], ChatCompletionMessage]]) -> None:
    """Display messages in a formatted way.
    
    Args:
        messages: List of messages, each can be either a dict or ChatCompletionMessage
    """
    for msg in messages:
        if isinstance(msg, dict):
            print(json.dumps(msg, indent=4))
        else:
            # Convert ChatCompletionMessage to dict and print
            msg_dict = {
                "role": msg.role,
                "content": msg.content,
            }
            
            # Add tool_calls if present
            if hasattr(msg, 'tool_calls') and msg.tool_calls:
                tool_calls = []
                for tool_call in msg.tool_calls:
                    tool_call_dict = {
                        "id": tool_call.id,
                        "type": tool_call.type,
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        }
                    }
                    tool_calls.append(tool_call_dict)
                msg_dict["tool_calls"] = tool_calls
                
            print(json.dumps(msg_dict, indent=4))
        print("---")  # Add separator between messages 

