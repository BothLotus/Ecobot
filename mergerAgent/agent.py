from google.adk.agents import LlmAgent

merger_agent = LlmAgent(
     name="SynthesisAgent",
     model='gemini-2.0-flash',  # Or potentially a more powerful model if needed for synthesis
     instruction="You are a synthesis agent. Your input will be several partial responses "
        "from different domain output keys (airQuality, bioDiversityLoss, deforestation). "
        "Your job is to merge them into a **single coherent answer**. "
        "Do not just list them one after the other. Instead, combine the ideas, "
        "summarize overlapping information, and present a unified, concise response "
        "that reads naturally as if written by one expert.",
     description="Combines research findings from parallel agents into a structured, cited report, strictly grounded on provided inputs."
     # No tools needed for merging
     # No output_key needed here, as its direct response is the final output of the sequence
 ) 