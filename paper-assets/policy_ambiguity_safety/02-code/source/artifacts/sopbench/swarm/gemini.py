import random
import time
import re
import json
import copy
import requests
import os
import traceback
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
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

def _extract_function_call(candidate: Dict) -> Optional[List[ChatCompletionMessageToolCall]]:
    """Extract function call information from the candidate if present."""
    if isinstance(candidate.get('content', {}).get('parts', [{}])[0], dict) and \
       'functionCall' in candidate.get('content', {}).get('parts', [{}])[0]:
        function_call = candidate['content']['parts'][0]['functionCall']
        return [
            ChatCompletionMessageToolCall(
                id=f'call_{_generate_random_id()}',
                type='function',
                function=Function(
                    arguments=json.dumps(function_call['args']),
                    name=function_call['name']
                )
            )
        ]
    return None

def _create_message(candidate: Dict, tool_calls: Optional[List[ChatCompletionMessageToolCall]]) -> ChatCompletionMessage:
    """Create a ChatCompletionMessage from the candidate."""
    return ChatCompletionMessage(
        content=None if tool_calls else candidate['content']['parts'][0]['text'],
        role='assistant',
        tool_calls=tool_calls,
        function_call=None,
        refusal=None,
        audio=None
    )

def _create_usage(gemini_metadata: Dict) -> CompletionUsage:
    """Create CompletionUsage from Gemini metadata."""
    return CompletionUsage(
        completion_tokens=gemini_metadata.get('candidatesTokenCount', 0),
        prompt_tokens=gemini_metadata.get('promptTokenCount', 0),
        total_tokens=gemini_metadata.get('totalTokenCount', 0),
        completion_tokens_details=CompletionTokensDetails(),
        prompt_tokens_details=PromptTokensDetails()
    )

def format_function_input(function: Dict) -> Dict:
    """Clean a function to remove unsupported properties in Gemini.
    Unsupport properties: additionalProperties, anyOf"""
    
    # Create a deep copy of the function to avoid modifying the original
    function = copy.deepcopy(function)
    
    if "additionalProperties" in function["parameters"]:
        del function["parameters"]["additionalProperties"]
        
    properties = function["parameters"]["properties"]    
    if not properties:
        del function["parameters"]
        return function

    # Transform anyOf parameters to multiple properties
    new_properties = {}
    for key, property in properties.items():
        if "anyOf" in property:
            for any_of_idx, any_of in enumerate(property["anyOf"]):
                new_any_of = copy.deepcopy(any_of)
                if "additionalProperties" in new_any_of:
                    del new_any_of["additionalProperties"]
                new_key = f"{key}_{any_of_idx}"
                new_properties[new_key] = new_any_of
            # remove the original key from required
            if key in function["parameters"]["required"]:
                function["parameters"]["required"].remove(key)
        else:
            new_property = copy.deepcopy(property)
            if "additionalProperties" in new_property:
                del new_property["additionalProperties"]
            if "items" in new_property:
                if "additionalProperties" in new_property["items"]:
                    del new_property["items"]["additionalProperties"]
            new_properties[key] = new_property
            
    function["parameters"]["properties"] = new_properties
    return function

def format_function_output(completion: ChatCompletion) -> Dict:
    """Clean the output of a function call to deal with **anyOf** parameters."""
    for choice in completion.choices:
        if choice.message.tool_calls:
            for tool_call in choice.message.tool_calls:
                # identification_1 -> identification (identification is a anyOf parameter)
                new_arguments = {}
                for key, value in json.loads(tool_call.function.arguments).items():
                    new_arguments[re.sub(r'_\d+$', '', key)] = value
                tool_call.function.arguments = json.dumps(new_arguments)
    return completion

def convert_gemini_to_openai_format(gemini_response: Dict) -> ChatCompletion:
    """
    Convert Gemini API response format to OpenAI ChatCompletion object.
    
    Args:
        gemini_response: Dictionary containing Gemini API response
        
    Returns:
        ChatCompletion object in OpenAI format
    """

    # Process all candidates
    choices = []
    for idx, candidate in enumerate(gemini_response['candidates']):
        # Create tool calls if present
        tool_calls = _extract_function_call(candidate)
        
        # Create the message
        message = _create_message(candidate, tool_calls)
        
        # Create the choice
        choice = Choice(
            finish_reason='tool_calls' if tool_calls else candidate['finishReason'].lower(),
            index=idx,
            logprobs=None,
            message=message
        )
        choices.append(choice)
    
    # Create usage details
    usage = _create_usage(gemini_response['usageMetadata'])
    
    # Create the complete ChatCompletion object
    return ChatCompletion(
        id=f'chatcmpl-{_generate_random_id()}',
        choices=choices,
        created=int(time.time()),
        model=gemini_response['modelVersion'],
        object='chat.completion',
        system_fingerprint=f'fp_{_generate_random_id(8)}',
        usage=usage
    )

def gemini_chat_completion_openai_format(
        model: str,
        messages: List[Dict[str, str]],
        tools: List[Dict[str, Any]] = None,
        n=1,
        max_tokens=1024,
        temperature=0.7,
        top_p=1.0,
        max_retries=10,
        stop=None,
        logprobs=False,
    ) -> List[str]:
        """
        Generate chat completions using Gemini API.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            tools: List of tool dictionaries as in OpenAI's tool calling format
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            top_p: Top-p sampling parameter
            n: Number of completions to generate
            
        Returns:
            List of completion strings
        """
        
        # Get the API key
        api_key = [REDACTED]"GEMINI_API_KEY")
        
        # Construct the payload
        
        # Safety settings
        gemini_safety_settings = [
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        # Generation config
        gemini_generation_config = {
                "maxOutputTokens": max_tokens,
                "temperature": temperature,
                "topP": top_p,
                "candidateCount": int(n),
            }
        
        # Convert messages from OpenAI format to Gemini format
        gemini_messages = []
        used_tools = {}
        sys_prompt = ""
        for msg_idx, message in enumerate(messages):
            role = message["role"]
            if role == "system":
                sys_prompt = message["content"]
            elif role == "user":
                parts = [{"text": message["content"]}]
                gemini_messages.append({"role": "user", "parts": parts})
            elif role in ["assistant", "model"]:
                if message.get("tool_calls", None):
                    function_calls = []
                    for tool_call in message["tool_calls"]:
                        function_calls.append({"functionCall": {"name": tool_call.get("function").get("name"), 
                                                                "args": json.loads(tool_call.get("function").get("arguments"))}})
                        used_tools[tool_call.get("id")] = tool_call.get("function").get("name")
                    gemini_messages.append(
                        {"role": "model", "parts": function_calls}
                    )
                else:
                    gemini_messages.append(
                        {"role": "model", "parts": [{"text": message["content"]}]}
                    )
            elif role == "tool":
                gemini_messages.append(
                    {"role": "user", "parts": [{
                        "functionResponse": {
                            "name": used_tools[message["tool_call_id"]],
                            "response": {
                                "name": used_tools[message["tool_call_id"]],
                                "content": message["content"]
                            }
                        }
                    }]}
                )
    
        # System instruction (optional)
        if sys_prompt:
            gemini_system_instruction = {
                "parts": [{"text": sys_prompt}]
            }
        else:
            gemini_system_instruction = None
            
        # Tools (optional)
        if tools:
            func_declarations = []
            for tool in tools:
                function = tool["function"]
                # Gemini does not support additionalProperties
                function = format_function_input(function)
                function_declaration = {
                        "name": function["name"],
                        "description": function["description"],
                    }
                # Gemini does not support empty parameters
                if "parameters" in function:
                    function_declaration["parameters"] = function["parameters"]
                func_declarations.append(function_declaration)
            gemini_tools = [{"function_declarations": func_declarations}]
        else:
            gemini_tools = None
            
        # Construct the payload according to the version
        payload = {
            "contents": gemini_messages,
            "safetySettings": gemini_safety_settings,
            "generationConfig": gemini_generation_config,
        }
        if gemini_system_instruction:
            payload["system_instruction"] = gemini_system_instruction
        if gemini_tools:
            payload["tools"] = gemini_tools
        # GDM url
        headers = {"Content-Type": "application/json"}
        beta = "v1alpha" if "thinking" in model else "v1beta"
        url = f"https://generativelanguage.googleapis.com/{beta}/models/{model}:generateContent?key={api_key}"
            
        # Make API request
        # Retry up to 10 times if there is an error
        retry = 0
        while retry < max_retries:
            try:
                response = requests.post(url, headers=headers, json=payload)
                # response.raise_for_status()
                completion = response.json()
                completion = convert_gemini_to_openai_format(completion)
                # clean the output of the function call
                completion = format_function_output(completion)
                return completion
            except requests.exceptions.RequestException as e:
                print(f"Request failed (attempt {retry + 1}/{max_retries}): {str(e)}")
                time.sleep(2 * min((1.25**retry), 5))
                retry += 1
            except Exception as e:
                # print full traceback
                traceback.print_exc()
                print(f"Error: {str(e)}")
                time.sleep(2 * min((1.5**retry), 5))
                retry += 1
        return None
    
# Test function
if __name__ == "__main__":
    # test_response = {
    #     'idx': 0,
    #     'completion': {
    #         'candidates': [{
    #             'content': {
    #                 'parts': [{
    #                     'functionCall': {
    #                         'name': 'get_delivery_date',
    #                         'args': {'order_id': 'XA2315'}
    #                     }
    #                 }],
    #                 'role': 'model'
    #             },
    #             'finishReason': 'STOP',
    #             'safetyRatings': [
    #                 {'category': 'HARM_CATEGORY_HATE_SPEECH', 'probability': 'NEGLIGIBLE'},
    #                 {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'probability': 'NEGLIGIBLE'},
    #                 {'category': 'HARM_CATEGORY_HARASSMENT', 'probability': 'NEGLIGIBLE'},
    #                 {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'probability': 'NEGLIGIBLE'}
    #             ]
    #         }],
    #         'usageMetadata': {
    #             'promptTokenCount': 117,
    #             'candidatesTokenCount': 13,
    #             'totalTokenCount': 130
    #         },
    #         'modelVersion': 'gemini-1.5-flash-002'
    #     }
    # }
    
    # print(convert_gemini_to_openai_format(test_response))
    
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
    
    content = gemini_chat_completion_openai_format(model="gemini-2.5-pro-exp-03-25", messages=messages, tools=tools)
    """
    Target Output: ChatCompletion(id='chatcmpl-AckLkaZwrVVBWdSAez5lJTzke9YK0', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='The delivery date for your order (Dominos Pizza) is December 12, 2024.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None)), Choice(finish_reason='stop', index=1, logprobs=None, message=ChatCompletionMessage(content='The delivery date for your order (Dominos Pizza) is December 12, 2024.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1733797996, model='gpt-4o-mini-2024-07-18', object='chat.completion', service_tier=None, system_fingerprint='fp_bba3c8e70b', usage=CompletionUsage(completion_tokens=42, prompt_tokens=188, total_tokens=230, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
    """
    print(content)