# Ecobot
Overview 
The purpose of this website is to use googles ADK agents to provide scientific facst about the ecological lives on our planet in quick succession. 

To set up your environment:

python -m venv .venv            ### To create your virtual environment
.venv\Scripts\activate.bat      ### To activate your virtual environment
pip install google-adk          ### To install the google adk libraries within your virtual environment
pip show google-adk             ### To verify google adk libs install

To run the website:
Within the main directory of the repo run 
python webserver.py             ### Starts the fastapi webserver along with starting Agent session

The website is located in the url http://localhost:80/frontend/index.html

