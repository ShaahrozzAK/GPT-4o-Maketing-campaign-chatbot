import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from fpdf import FPDF

def main(): 
    try: 
        # Get configuration settings 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        
        # Initialize the Azure OpenAI client
        client = AzureOpenAI(
            azure_endpoint=azure_oai_endpoint,
            api_key=azure_oai_key,
            api_version="2024-02-15-preview"
        )

        # Create a system message 
        system_message = """ You are an expert in the marketing area and you have 30 years creating successful marketing campaigns for users. You also have extensive experience in content creation.

Your main objective is to help the user create a marketing campaign that contains a well-defined strategy and a pdf calendar that already contains the content of the posts, images, text, promotions, advertising times, suggested budget and everything else. that you think is necessary for the proposal. 
        """
        messages_array = [{"role": 'system', "content": system_message}]
        chat_history = "System: " + system_message + "\n"

        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            print("\nSending request for summary to Azure OpenAI endpoint...\n\n")
            
            # Send request to Azure OpenAI model
            messages_array.append({"role": "user", "content": input_text})
            chat_history += "User: " + input_text + "\n"

            response = client.chat.completions.create(
                model=azure_oai_deployment,
                temperature=0.7,
                max_tokens=1200,
                messages=messages_array
            )

            generated_text = response.choices[0].message.content
            messages_array.append({"role": "assistant", "content": generated_text})
            chat_history += "Assistant: " + generated_text + "\n"

            # Print generated text
            print("response:" + generated_text + "\n")

        # Create PDF of the chat
        pdf = FPDF()
        pdf.add_page()
        
        # Add Unicode font (DejaVuSans)
        pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
        pdf.set_font("DejaVu", size=12)
        
        # Split chat history into lines and add them to the PDF
        for line in chat_history.split('\n'):
            pdf.multi_cell(0, 10, line)

        # Save the PDF
        pdf_output_path = "chat_history.pdf"
        pdf.output(pdf_output_path)
        print(f"Chat history saved to {pdf_output_path}")

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()
