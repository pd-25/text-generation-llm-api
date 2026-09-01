def generate_response(client, query):
     # First API call with reasoning
      response = client.chat.completions.create(
        # model="google/gemma-4-26b-a4b-it:free",
        model="nvidia/nemotron-3.5-lightning:free",
        stream=True,
        messages=[
                {
                  "role": "user",
                  "content": query
                }
              ],
        # extra_body={"reasoning": {"enabled": True}}
      )
    
      # Extract the assistant message with reasoning_details
      for chunk in response:
         content = chunk.choices[0].delta.content
         if content:
             print(content, end="", flush=True)
             yield content