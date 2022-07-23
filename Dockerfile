FROM python:3.9 
# Or any preferred Python version.
ADD main.py /
# install dotenv n shits
RUN pip install requests beautifulsoup4 python-dotenv
# install fastapi and uvicorn
RUN pip install fastapi uvicorn
#CMD [ "python", "./main.py" ]
# Or enter the name of your unique directory and parameter set.