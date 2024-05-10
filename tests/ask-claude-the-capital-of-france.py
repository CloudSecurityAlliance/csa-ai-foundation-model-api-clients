#!/usr/bin/env python3

# This is a local test for dev

from foundation_model_api_clients import FoundationModelAPIClient

def main():
    model_name = 'claude'
    
    client = FoundationModelAPIClient(model_name)

    system_prompt = "You are a helpful assistant."
    user_prompt = "What is the capital of France?"
    user_data = None
    output_file = 'claude-response.json'

    response = client.generate_response(
        system_prompt,
        user_prompt,
        user_data,
        temperature=0.7,
        max_tokens=100,
        output_file=output_file
    )

if __name__ == '__main__':
    main()
