import json
import requests
import os
import time
import copy
import PIL.Image
import base64
import random
from dataclasses import dataclass
from typing import List, Optional, Dict, Any, Union
from anthropic import Anthropic, AnthropicBedrock
from anthropic.types import TextBlock, ToolUseBlock, ThinkingBlock
import anthropic
from swarm.util import (Function, 
                  ChatCompletionMessageToolCall, 
                  CompletionUsage, 
                  ChatCompletion,
                  CompletionTokensDetails, 
                  PromptTokensDetails,
                  _generate_random_id,
                  Choice,
                  ChatCompletionMessage
)

from dotenv import load_dotenv
load_dotenv()

def convert_claude_to_openai_format(claude_response) -> ChatCompletion:
    """Convert Claude API response format to OpenAI ChatCompletion object."""
    
    choices = []
    
    # Handle both direct Claude response and OpenAI format
    if hasattr(claude_response, 'content'):
        # Direct Claude response
        content_blocks = claude_response.content
    else:
        # OpenAI format response
        content_blocks = claude_response.choices[0].message.content
    
    # Process each content block
    tool_calls = []
    text_content = None
    thinking_content = None
    thinking_signature = None
    
    if isinstance(content_blocks, list):
        # Handle list of content blocks
        for block in content_blocks:
            if block.type == 'text':
                text_content = block.text
            elif block.type == 'thinking':
                thinking_signature = block.signature
                thinking_content = block.thinking
            elif block.type == 'tool_use':
                tool_calls.append(
                    ChatCompletionMessageToolCall(
                        id=block.id,
                        type='function',
                        function=Function(
                            name=block.name,
                            arguments=json.dumps(block.input)
                        )
                    )
                )
    else:
        # Handle string content
        text_content = content_blocks
    
    # Create the message
    message = ChatCompletionMessage(
        role='assistant',
        content=text_content,
        thinking=thinking_content,
        thinking_signature=thinking_signature,
        tool_calls=tool_calls if tool_calls else None
    )
    
    # Create the choice
    choice = Choice(
        finish_reason='stop' if hasattr(claude_response, 'stop_reason') and claude_response.stop_reason == 'end_turn' 
                     else getattr(claude_response, 'stop_reason', 'stop'),
        index=0,
        logprobs=None,
        message=message
    )
    choices.append(choice)
    
    # Create usage details
    if hasattr(claude_response, 'usage'):
        # Handle both OpenAI and Claude usage formats
        usage_obj = claude_response.usage
        completion_tokens = getattr(usage_obj, 'output_tokens', 
                                  getattr(usage_obj, 'completion_tokens', 0))
        prompt_tokens = getattr(usage_obj, 'input_tokens',
                              getattr(usage_obj, 'prompt_tokens', 0))
        
        usage = CompletionUsage(
            completion_tokens=completion_tokens,
            prompt_tokens=prompt_tokens,
            total_tokens=completion_tokens + prompt_tokens,
            completion_tokens_details=CompletionTokensDetails(),
            prompt_tokens_details=PromptTokensDetails()
        )
    else:
        # Default usage if not available
        usage = CompletionUsage(
            completion_tokens=0,
            prompt_tokens=0,
            total_tokens=0,
            completion_tokens_details=CompletionTokensDetails(),
            prompt_tokens_details=PromptTokensDetails()
        )
    
    # Create the complete ChatCompletion object
    return ChatCompletion(
        id=f'chatcmpl-{_generate_random_id()}',
        choices=choices,
        created=int(time.time()),
        model=getattr(claude_response, 'model', 'claude-3'),
        object='chat.completion',
        system_fingerprint=f'fp_{_generate_random_id(8)}',
        usage=usage
    )

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def format_tool_input(tools):
    formatted_tools = []
    for idx, tool in enumerate(tools):
        function = tool["function"] if "function" in tool else tool
        formatted_tool = {
            "name": function["name"],
            "description": function["description"],
            "input_schema": function["parameters"],
        }
        # Use cache control for the last tool
        # if idx == len(tools) - 1:
        #     formatted_tool["cache_control"] = {"type": "ephemeral"}
        formatted_tools.append(formatted_tool)
    return formatted_tools

def claude_chat_completion_openai_format(
    model,
    messages,
    tools=None,
    n=1,
    max_tokens=1024,
    temperature=0.7,
    top_p=1.0,
    max_retries=20,
    api_key=[REDACTED]"ANTHROPIC_API_KEY"),
    stop=None,
    logprobs=False,
):
    assert n == 1
    client = Anthropic(api_key=[REDACTED]

    if "-thinking" in model:
        thinking_mode = True
        model = model.split("-thinking")[0].strip()
    else:
        thinking_mode = False

    message_list = []
    system_message = None
    # Format the messages in Claude's format
    for _message in messages:
        # avoid modifying the original message
        message = copy.deepcopy(_message)
        if isinstance(message, dict):
            if message["role"] == "system":
                system_message = [{"type": "text", "text": message["content"]}]
                continue
            elif message["role"] == "user":
                # only keep the role and content for user messages
                # avoid the additional field from assistant role
                message_list.append(
                    {
                        "role": "user",
                        "content": message["content"]
                    }
                ) 
            elif message["role"] == "assistant":
                if message.get("tool_calls", None):
                    assistant_messages = []
                    if "thinking" in message and "thinking_signature" in message:
                        if message.get("thinking_signature", None) and message.get("thinking_signature", None):
                            thinking_block = ThinkingBlock(thinking=message["thinking"], 
                                                           signature=message["thinking_signature"], 
                                                           type="thinking")
                            assistant_messages.append(thinking_block)
                    if message["content"]:
                        assistant_messages.append(TextBlock(text=message["content"], type="text"))
                    for tool_call in message["tool_calls"]:
                        assistant_messages.append(ToolUseBlock(
                            id=tool_call["id"], 
                            name=tool_call["function"]["name"], 
                            input=json.loads(tool_call["function"]["arguments"]),
                            type="tool_use"
                        ))
                    message_list.append({
                        "role": "assistant",
                        "content": assistant_messages
                    })
                elif message.get("content", None):
                    message_list.append({
                        "role": "assistant",
                        "content": message["content"]
                    })
                else:
                    # raise ValueError(f"Invalid assistant message: {message}")
                    pass
            elif message["role"] == "tool":
                message_list.append({
                    "role": "user",
                    "content": [{
                        "type": "tool_result",
                        "tool_use_id": message["tool_call_id"],
                        "content": str(message["content"]),
                    }]
                })
        # only the assistant message is not dict but ChatCompletionMessage
        elif isinstance(message, ChatCompletionMessage):
            assert message.role == "assistant"
            if message.tool_calls:
                assistant_messages = []
                if message.content:
                    assistant_messages.append(TextBlock(text=message.content, type="text"))
                for tool_call in message.tool_calls:
                    assistant_messages.append(ToolUseBlock(
                        id=tool_call.id, 
                        name=tool_call.function.name, 
                        input=json.loads(tool_call.function.arguments),
                        type="tool_use"
                    ))
                message_list.append({
                    "role": "assistant",
                    "content": assistant_messages
                })
            elif message.content:
                message_list.append({
                    "role": "assistant",
                    "content": message.content
                })
            else:
                raise ValueError(f"Invalid assistant message: {message}")
        else:
            raise ValueError(f"Invalid message type: {type(message)}")
            
    # Format tools for Claude
    formatted_tools = format_tool_input(tools) if tools else []
    
    # Change the model name to the Bedrock model name
    # bedrock_model_names = {
    #     "claude-3-5-haiku-20241022": "us.anthropic.claude-3-5-haiku-20241022-v1:0",
    #     "claude-3-5-sonnet-20240229": "us.anthropic.claude-3-5-sonnet-20240229-v1:0",
    #     "claude-3-5-sonnet-20241022": "us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    #     "claude-3-7-sonnet-20250219": "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    # }
    
    create_params = {
        "model": model,
        "max_tokens": max_tokens,
        "system": system_message,
        "messages": message_list,
        "tools": formatted_tools,
        "temperature": temperature,
        "top_p": top_p,
    }

    if thinking_mode:
        del create_params["top_p"]
        create_params["temperature"] = 1.0 # thinking mode only supports temperature 1.0
        budget_tokens = None if "-thinking" not in model else int(model.split("-thinking")[1].strip())
        budget_tokens = int(budget_tokens) if budget_tokens else 10000
        create_params["max_tokens"] = budget_tokens + max_tokens
        create_params["thinking"] = {"type": "enabled", "budget_tokens": budget_tokens}
    
    # Send the request to Claude
    for attempt in range(max_retries):
        try:
            completion = client.messages.create(
                **create_params
            )
            # Convert the Claude response to OpenAI format
            openai_completion = convert_claude_to_openai_format(completion)
            return openai_completion
        except anthropic.APIError as e:
            print(f"API Error (attempt {attempt + 1}/{max_retries}): {e}")
            if e.status_code == 429:  # Rate limit
                print("Rate limit exceeded, waiting longer...")
                time.sleep(5)
            else:
                time.sleep(1)
        except Exception as e:
            print(f"Unexpected Error (attempt {attempt + 1}/{max_retries}): {type(e).__name__}: {e}")
            time.sleep(1)
    
    print("Max retries exceeded")
    return None
    

if __name__ == "__main__":
    tools = [
    {
        "type": "function",
        "function": {
            "name": "get_delivery_date",
            "description": "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date.'",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "anyOf": [
                            {
                                "type": "string",
                                "description": "The customer's order ID.",
                            },
                            {
                                "type": "object",
                                "description": "The order person and name in the format of YYYY-MM-DD.",
                                "properties": {
                                    "order_person": {
                                        "type": "string",
                                        "description": "The order person.",
                                    },
                                    "order_name": {
                                        "type": "string",
                                        "description": "The name of the order.",
                                    }
                                },
                            }
                        ]
                    },
                },
                "required": ["order_id"],
            },
        }
        }
    ]

    messages = [
        {
            "role": "system",
            "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."
        },
        {
            "role": "user",
            "content": "Hi, can you tell me the delivery date for my order? The order person is John Doe and the order name is Dominos Pizza."
        },
        {
            "role": "assistant",
            "content": None,
            "tool_calls": [
                {
                    "id": "call_sNcq3LV89bWJCWgZvJpCac7I",
                    "function": {
                        "arguments": "{\"order_person\":\"John Doe\",\"order_name\":\"Dominos Pizza\"}",
                        "name": "get_delivery_date"
                    },
                    "type": "function"
                }
            ]
        },
        {
            "role": "tool",
            "tool_call_id": "call_sNcq3LV89bWJCWgZvJpCac7I",
            "tool_name": "get_delivery_date",
            "content": "2024-12-12"
        }
    ]
    
    content = claude_chat_completion_openai_format(model="claude-3-5-sonnet-20241022", messages=messages, tools=tools)
    print(content)