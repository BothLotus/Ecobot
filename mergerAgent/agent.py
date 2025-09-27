from google.adk.agents import LlmAgent

merger_agent = LlmAgent(
     name="SynthesisAgent",
     model='gemini-2.0-flash',  # Or potentially a more powerful model if needed for synthesis
     instruction="You are an AI Assistant responsible for structing information in a clean and organized fashion",
     description="Combines research findings from parallel agents into a structured, cited report, strictly grounded on provided inputs."
     # No tools needed for merging
     # No output_key needed here, as its direct response is the final output of the sequence
 ) 